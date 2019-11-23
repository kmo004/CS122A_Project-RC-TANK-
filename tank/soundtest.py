from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from signal import pause
from time import sleep
b = TonalBuzzer(25)

b.play(Tone(220))
sleep(.1)
b.play(Tone(500))
sleep(.1)

