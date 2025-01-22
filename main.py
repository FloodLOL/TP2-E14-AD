from scraper import scrape_items
from notifier import send_notification

if __name__ == "__main__":
    items = scrape_items()
    if items:
        summary_message = f"No d'items trouvés {len(items)}"
        send_notification(summary_message)
    else:
         print("Aucun item trouvé")
