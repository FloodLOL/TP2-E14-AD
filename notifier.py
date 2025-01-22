from plyer import notification


def send_notification(message):
    try:
        notification.notify(
            title=(f'item trouvé'),
            message=message,
            app_icon=None,
            app_name='TP2 E14',
            timeout=10
        )
    except Exception as e:
        print(f"Erreur lors de l'envoi de la notification : {e}")

send_notification("web scraping avec python reussi!")