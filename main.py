from plyer import notification
from notifyme.messages_dict import dict_message
import random

if __name__ == "__main__":
    # We are creating a dictionary to store the different messages of the notification


    # To chose a random item we will create a random number and print the message in the dictionary at that index point
    choices = random.randint(0, 17)

    # START    notification code starts here

    # Uncomment the below and the last line to run this code on a interval of 1hr
    # while True:

    # Using this function the notification will pop up
    notification.notify(

        # This is the name of the App
        app_name="Water-Notifier",

        # This is the title of the notification
        title="Please drink Water",

        # This is the random message in the notification
        message=dict_message[choices],

        # This is how much time the pop-up should last
        timeout=10

    )

# Uncomment this to make the program wait for 1hr before the next pop-up
# time.sleep(60*60)
