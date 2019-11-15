
#from gpiozero import LED
from bluedot import BlueDot
from signal import pause

def dpad(pos):
	if pos.top:
		print ("up")
	elif pos.left:
		print ("left")
	elif pos.right:
		print ("right")
	elif pos.bottom:
		print ("down")
	elif pos.middle:
		print("fire")

bd = BlueDot()
bd.when_pressed = dpad

pause()
