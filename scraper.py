from enum import unique
import requests
from bs4 import BeautifulSoup

URL = 'https://hobbysag.com/collections/nouveautes/pokemon'

def scrape_items():
    response = requests.get(URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        items = soup.find_all('a', href=lambda href: href and '/products/' in href)

        unique_items = set(item.text.strip() for item in items if "Prismatic Evolutions" in item.text)

        stripped_items = [item.replace("Prismatic Evolutions","").strip() for item in unique_items]

        return stripped_items
    else:
        print(f"Incapable d'accéder à la page {URL} : {response.status_code}")
        return []

# products = scrape_items()
# print(products)
