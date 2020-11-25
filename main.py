# IMPORTS
import time  # We are importing the time module to get the time

from plyer import notification  # We are importing the plyer module to show the notification

import random  # We are using Random to show a random message about water in our program



if __name__ == "__main__": 
	
	# We are creating a dictionary to store the different messages of the notification
	dictMessage =[

	"Water lubricates the body joints",

	"Water is the basis of life of all human-beings, animals and plants",

	"Water is essential for our bodies to function properly",

	"Water forms saliva and mucus",

	"Water boosts skin health and beauty",

	"Water help in the cushioning of the brain, spinal cord, and other sensitive tissues.",

	"Water regulates our body temperature",

	"Water will avoid any Kidney diseases from you",

	"Plants make their food with the help of water, and without water the plants cannot survive",

	"Water flushes away our body waste",

	"Water helps maintain our blood pressure level",

	"Water will also help in control of calories",
	
	"Water helps in maintaining a regularity in digestion",

	"Water improves your Concentration Level",

	"Water is more essential than fool",

	"Water will give us everything that we need",

	"Water is the house of life and it is good for us",

	"Water is precious so don't waste it"
	
	]

	# To chose a random item we will create a random number and print the message in the dictionary at that index point
	choices = random.randint(0, 17)


	# START    notification code starts here

	# Uncomment the below and the last line to run this code on a interval of 1hr
	# while True:

	# Using this function the notification will pop up
	notification.notify(

		# This is the name of the App
		app_name = "Water-Notifier",

		# This is the title of the notification
		title = "Please drink Water",

		# This is the random message in the notification
		message = dictMessage[choices],

		# This is how much time the pop-up should last
		timeout = 10

	)

		# Uncomment this to make the program wait for 1hr before the next pop-up
		# time.sleep(60*60)
