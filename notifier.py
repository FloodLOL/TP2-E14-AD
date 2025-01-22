from plyer import notification

def send_notification(message):
    try:
        notification.notify(
            title="Item trouvé",
            message=message,
            app_icon=None, 
            app_name="TP2 E14",
            timeout=10
        )
        print(f"{message}")
    except Exception as e:
        print(f"Erreur lors de l'envoi de la notification : {e}")
