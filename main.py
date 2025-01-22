from scraper import scrape_items
from notifier import send_notification

if __name__ == "__main__":
    items = scrape_items()
    if items:
        #summary_message = f"No d'items Prismatic Evolution trouvés : {len(items)}"
        summary_message = f"Items\n"+"\n".join(items)
        send_notification(summary_message)
    else:
         print("Aucun item Prismatic Evolutions trouvé")
