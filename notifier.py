from plyer import notification

def send_notification(message):
    max_length = 256
    message_parts = [message[i:i+max_length] for i in range(0, len(message), max_length)]

    try:
        for part in message_parts:
            notification.notify(
                title="Item trouvé",
                message=part,
                app_icon=None, 
                app_name="TP2 E14",
                timeout=10
            )
            print(f"{part}")
    except Exception as e:
        print(f"Erreur lors de l'envoi de la notification : {e}")
