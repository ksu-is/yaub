import time
import random

from gpiozero import Servo
from time import sleep
count = 0
servo = Servo(25)

#Table of behaviors 1
while count < 5:
	number = int(random.randint(1,3))
	if number == 1:
		#gentle switch
		servo.max()
		sleep(1)
		servo.min()
	elif number == 2:
		#fakeout behavior
		servo.mid()
		servo.min()
		servo.max()
		servo.min()
	else:
		#double check behavior
		servo.max()
		sleep(.5)
		servo.mid()
		servo.max()
		servo.min()
