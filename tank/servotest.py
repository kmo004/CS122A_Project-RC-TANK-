from gpiozero import Servo
from time import sleep

#servo = Servo(21)
servo = Servo(21,.0024,.00015)

while True:
	servo.min()
	sleep(2)
	servo.mid()
	sleep(2)
	servo.max()
	sleep(2)
