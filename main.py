# IMPORTS
import time  # We are importing the time module to get the time
from plyer import notification
import random
if __name__ == "__main__":
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
	
	"Water helps in mataining a regularity in digetion",

	"Water improves your Concentration Level",

	"Water is more essential than fool",

	"Water will give us everything that we need",

	"Water is the house of life and it is good for us",

	"Water is precious so dont waste it"
	
	]

	choices = random.randint(0, 17)

	# while True:
	notification.notify(
		title = "Please drink Water",
		message = dictMessage[choices],
		timeout = 10
	)
		# time.sleep(60*60)
