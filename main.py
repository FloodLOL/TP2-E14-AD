from scraper import scraped_items
from notifier import send_notification

if __name__ == "__main__":
    items = scraped_items()
    if items:
        send_notification(f"Item trouvé {items}")
    else:
         print("Aucun item trouvé")

