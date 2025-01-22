from scraper import scrape_items
from notifier import send_notification

if __name__ == "__main__":
    items = scrape_items()
    if items:
        summary_message = f"Items\n" + "\n".join([f"Product: {item[0]}, Price: {item[1]}" for item in items])
        send_notification(summary_message)
    else:
         print("Aucun item Prismatic Evolutions trouvé")
