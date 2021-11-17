import time
import random

from gpiozero import Servo
from time import sleep
count = 0
#servo = Servo(25)

#Table of behaviors 1
#while count < 5:
	#gentle switch
#	servo.max()
#	sleep(1)
#	servo.min()

number = int(random.randint(1,5))
print(number)