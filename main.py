import time
from plyer import notification
from notifyme.messages_dict import dict_message
import random

if __name__ == "__main__":
    message_choice = random.randint(0, 17)
    while True:
        notification.notify(
            app_name="Water-Notifier",
            title="Please drink Water",
            message=dict_message[message_choice],
            timeout=10
        )
        time.sleep(60*60)
