import html
import re
import requests
from bs4 import BeautifulSoup


class ZillowScraper:

    def __init__(self, url):
        self.url = url
        self.soup = self.get_soup()

    def get_soup(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")

    def get_properties(self):
        properties = {}

        cards = self.soup.find_all(
            "article",
            attrs={"data-test": "property-card"}
        )

        for index, card in enumerate(cards):

            # Price
            price_element = card.find(
                "span",
                class_="PropertyCardWrapper__StyledPriceLine"
            )

            price = re.search(
                r'\$[\d,]+',
                html.unescape(price_element.get_text())
            ).group()

            # Address
            address = html.unescape(card.find(
                "address",
                attrs={"data-test": "property-card-addr"}
            ).get_text(strip=True))

            # URL
            url = card.find(
                "a",
                attrs={"data-test": "property-card-link"}
            )["href"]

            properties[index] = {
                "price": price,
                "address": address,
                "url": url
            }

        return properties