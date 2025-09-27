import requests
from datetime import datetime, timedelta
from twilio.rest import Client
import dotenv
import os

# ----------- Konfiguracja -------------
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
CHANGE_THRESHOLD = 5  # % zmiany, powyżej którego wysyłamy wiadomość

dotenv.load_dotenv()

CLIENT_NUMBER = os.getenv("CLIENT_PHONE")
USER_NUMBER = os.getenv("USER_PHONE")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

client = Client(ACCOUNT_SID, AUTH_TOKEN)

# ----------- Pobranie danych giełdowych -------------
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": ALPHAVANTAGE_API_KEY,
}

response = requests.get(url="https://www.alphavantage.co/query", params=params)
response.raise_for_status()
data = response.json()

# ----------- Pobranie danych dla dwóch ostatnich dni giełdowych -------------
current_date = datetime.now().date()
formatted_data = []

# Pobieramy wczoraj i przedwczoraj (uwzględniając weekendy/święta)
i = 1
while len(formatted_data) < 2:
    day = current_date - timedelta(days=i)
    day_str = day.strftime("%Y-%m-%d")
    if day_str in data["Time Series (Daily)"]:
        formatted_data.append(data["Time Series (Daily)"][day_str])
    i += 1


# ----------- Obliczenie procentowej zmiany -------------
def calculate_percentage_change(prev_close, yesterday_close):
    change = (yesterday_close - prev_close) / prev_close * 100
    return round(change, 2)


change_percentage = calculate_percentage_change(
    float(formatted_data[1]["4. close"]),  # przedwczoraj
    float(formatted_data[0]["4. close"])  # wczoraj
)


# ----------- Pobranie wiadomości z NewsAPI -------------
def get_news(since_date):
    params = {
        "qInTitle": COMPANY_NAME,
        "from": since_date,
        "language": "en",
        "sortBy": "relevancy",
        "pageSize": 3,
        "apiKey": NEWS_API_KEY
    }
    response = requests.get(url="https://newsapi.org/v2/everything", params=params)
    response.raise_for_status()
    return response.json()


# ----------- Formatowanie wiadomości -------------
def format_message(news, change_percentage):
    up = "↑"
    down = "↓"
    symbol = up if change_percentage > 0 else down

    if not news["articles"]:
        return f"{STOCK} {symbol} {change_percentage}%\nNo relevant news found."

    article = news["articles"][0]
    return (
        f"{STOCK} {symbol} {change_percentage}%\n"
        f"Headline: {article.get('title', 'N/A')}\n"
        f"Brief: {article.get('description', 'N/A')}"
    )


# ----------- Wysyłanie wiadomości jeśli zmiana > threshold -------------
if abs(change_percentage) >= CHANGE_THRESHOLD:
    # Data wczoraj do NewsAPI
    news_since = (current_date - timedelta(days=1)).strftime("%Y-%m-%d")
    news = get_news(news_since)
    message = format_message(news, change_percentage)

    response_message = client.messages.create(
        to=USER_NUMBER,
        from_=CLIENT_NUMBER,
        body=message,
    )
    print("Message sent:")
    print(message)
else:
    print(f"No significant change ({change_percentage}%), no message sent.")
