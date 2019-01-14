import time
import board
import pulseio
import digitalio
from adafruit_motor import servo

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.D1)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.  
my_servo = servo.Servo(pwm)

while True:
	my_servo.angle = 0
	led.value = True
	while button.value:
		time.sleep(0.01)
	for i in range(30):
		time.sleep(0.01)
		my_servo.angle = i
	my_servo.angle = 100
	led.value = False
	while not button.value:
		time.sleep(0.01)

