import requests
from bs4 import BeautifulSoup


from bs4 import BeautifulSoup

URL = 'https://hobbysag.com/collections/nouveautes/pokemon'

def scrape_items():
        response = requests.get(URL)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            items = soup.find_all('a', href_='/products/')
            return [items.text.strip() for item in items]
        else:
            print(f"Incapable d'accéder à la page {URL} : {response.status_code}")
            return []