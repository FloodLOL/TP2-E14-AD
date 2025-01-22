from scraper import scrape_items
from notifier import send_notification

if __name__ == "__main__":
    items = scrape_items()
    if items:
        send_notification(f"Item trouvé {items}")
    else:
         print("Aucun item trouvé")

