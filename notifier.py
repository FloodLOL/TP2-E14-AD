from plyer import notification

from scraper import scraped_items

item = scraped_items.item

def send_notification(message):
    notification.notify(
        title=(f'item {item} trouvé'),
        message=message,
        app_icon='None',
        app_name='TP2 E14',
        timeout=10
    )