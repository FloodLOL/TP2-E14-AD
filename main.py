from scraper import scrape_items
from notifier import send_notification

def split_message_into_parts(items, max_length=256):
    message_parts = []
    current_message = ""
    
    for item in items:
        item_message = f"Product: {item[0]}, Prix: {item[1]}"
        
     
        if len(current_message) + len(item_message) + 1 <= max_length:
            
            if current_message:
                current_message += "\n" + item_message
            else:
                current_message += item_message  
        else:
            message_parts.append(current_message)
            current_message = item_message  

    if current_message:
        message_parts.append(current_message)
    
    return message_parts


if __name__ == "__main__":
    items = scrape_items()
    if items:

        message_parts = split_message_into_parts(items)

        for part in message_parts:
            send_notification(part)
    else:
        print("Aucun item Prismatic Evolutions trouvé")
