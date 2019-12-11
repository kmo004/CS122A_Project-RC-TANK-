import os
from bluedot import BlueDot
from signal import pause
from time import sleep
from gpiozero import Robot
from gpiozero import LED
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from gpiozero import AngularServo
count = 0
turretAngle = 0
#servo.angle = turretAngle

def dpad(pos):
#controls are backwards because a lot of German tanks had frontal Engines but i found out the TigerII has backend engines later on after i already put the board in.

	if pos.top:
		#print ("up")
		robot.backward()
	elif pos.left:
		#print ("left")
		robot.right()
	elif pos.right:
		#print ("right")
		robot.left()
	elif pos.bottom:
		#print ("down")
		robot.forward()
	elif pos.middle:
		#print("fire")
		led.on()
		fire.play(Tone(500))
		sleep(.1)
		fire.play(Tone(220))
		sleep(.1)
		fire.stop()
		led.off()

def stop():
	robot.stop()

def rotated(rotation):
	robot.stop()
	#servo = AngularServo(21,min_angle= -90, max_angle = 90, max_pulse_width = .0024, min_pulse_width = .00015)
	global count
	global turretAngle
	curr = count
	count = count+ rotation.value
	#print("{} {} {}".format(count, rotation.clockwise, rotation.anti_clockwise))
	#print if the turret is turning and in what direction(inc = clockwise and dec = counter clockwise)

	if curr < count:
		if turretAngle > -90:
			turretAngle = turretAngle - 10
	elif curr > count:
		if turretAngle < 90:
			turretAngle = turretAngle + 10
	servo.angle = turretAngle

	
robot = Robot(right=(4,14), left=(17,18))
bd = BlueDot()
led = LED(22)
fire = TonalBuzzer(25)
servo = AngularServo(21,min_angle= -90, max_angle = 90, max_pulse_width = .0024, min_pulse_width = .00015,frame_width = .25)

bd.border = True
bd.when_rotated = rotated
bd.when_pressed = dpad
bd.when_move = dpad
bd.when_released = stop


pause()
