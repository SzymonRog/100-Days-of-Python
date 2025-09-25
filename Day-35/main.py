import requests

API_KEY  = "fea46c6b80d9670e1b730622c1c9db4b"
LON = 17.038538
LAT = 52.405374

parmas = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "units": "metric"
}
response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast", params=parmas)
response.raise_for_status()
data = response.json()
print(data)