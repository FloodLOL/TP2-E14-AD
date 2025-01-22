from plyer import notification

def send_notification(message):
    max_length = 256
    truncate_message = message[:max_length]
    try:
        notification.notify(
            title="Item trouvé",
            message=truncate_message,
            app_icon=None, 
            app_name="TP2 E14",
            timeout=10
        )
        print(f"Notification sent: {truncate_message}")  
    except Exception as e:
        print(f"Erreur lors de l'envoi de la notification : {e}")
