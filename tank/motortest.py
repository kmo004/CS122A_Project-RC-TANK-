
from bluedot import BlueDot
from signal import pause
from time import sleep
from gpiozero import Robot


def dpad(pos):
	if pos.top:
		print ("up")
		robot.forward()
	elif pos.left:
		print ("left")
		robot.left()
	elif pos.right:
		print ("right")
		robot.right()
	elif pos.bottom:
		print ("down")
		robot.backward()
	elif pos.middle:
		print("fire")
		#robot.stop()

def stop():
	robot.stop()


robot = Robot(left=(4,14), right=(17,18))
bd = BlueDot()
bd.border = True
bd.when_pressed = dpad
bd.when_move = dpad
bd.when_released = stop

#robot = Robot(left=(left=(4,14), right(17,18))
pause()
