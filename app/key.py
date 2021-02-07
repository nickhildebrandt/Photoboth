#!/usr/bin/env python3
# ------------------------------------------------------------------
# [Nick Hildebrandt] MacAndMore
#          (C)2020
# ------------------------------------------------------------------

import time
import RPi.GPIO as GPIO
BUTTON_GPIO = 16
if __name__ == '__main__':
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	pressed = False
	while True:
# button is pressed when pin is LOW
		if not GPIO.input(BUTTON_GPIO):
			if not pressed:
				import subprocess
				rc = subprocess.call("$HOME/photoboth/app/press.sh", shell=True)
# button not pressed (or released)
	else:
		pressed = False
	time.sleep(0.1)
