from bs4 import BeautifulSoup
import requests


class DataScraper:
    def __init__(self):
        self.offers = {}


    def get_offers(self):
        response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
        response.raise_for_status()

        content = response.text

        soup = BeautifulSoup(content, "html.parser")

        prices_tag = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
        prices = [price.text.split('/')[0].strip("+") for price in prices_tag]

        address_tag = soup.find_all(name="address")
        list_address = [address.text.strip().split(",")[1:3] for address in address_tag]
        address = [str(address[0] + "," + address[1]) for address in list_address]

        links_tag = soup.find_all(name="a", class_='property-card-link')
        links = [link['href'] for link in links_tag]

        self.offers = {
            i: {
                'address': address[i],
                'price': prices[i],
                'link': links[i],
            }
            for i in range(len(prices))
        }
        print(self.offers)
        return self.offers
