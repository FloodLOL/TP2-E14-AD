import requests
from bs4 import BeautifulSoup

URL = 'https://hobbysag.com/collections/nouveautes/pokemon'


def scrape_items():
    response = requests.get(URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        product_cards = soup.find_all('div', class_='card__content')

        product_details = []
        
        seen_products = set()

        for card in product_cards:

            name = card.find('h3', class_='card__heading')
            if name:
                product_name = name.text.strip()
            else:
                product_name = "Unknown Product"

            regular_price_tag = card.find_next('span', class_='price-item--regular')

            sale_price_tag = card.find_next('span', class_='price-item--sale')

            if sale_price_tag:
                price = sale_price_tag.text.strip()
            elif regular_price_tag:
                price = regular_price_tag.text.strip()
            else:
                price = "Price not found"

            if "Prismatic Evolutions" in product_name and product_name not in seen_products:
                product_details.append((product_name, price))
                seen_products.add(product_name)

        return product_details
    else:
        print(f"Incapable d'accéder à la page {URL} : {response.status_code}")
        return []
# Example usage
products = scrape_items()
for product in products:
    print(f'Product: {product[0]}, Price: {product[1]}')