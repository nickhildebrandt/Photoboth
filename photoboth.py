#!/usr/bin/env python3
# ------------------------------------------------------------------
# [Nick Hildebrandt] MacAndMore
#          (C)2021
# ------------------------------------------------------------------

import time
import RPi.GPIO as GPIO
import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gdk
from gi.repository import Notify

APP_NAME = 'Photoboth'

class Main:
    def __init__(self):
        gladeFile       = "photoboth.glade"
        self.builder    = Gtk.Builder()
        self.builder.add_from_file(gladeFile)

        window          = self.builder.get_object("Main")
        window.connect("delete-event", Gtk.main_quit)
        window.show()


BUTTON_GPIO = 16
if __name__ == '__main__':
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	pressed = False
	while True:
# button is pressed when pin is LOW
		if not GPIO.input(BUTTON_GPIO):
			if not pressed:
				capture()
# button not pressed (or released)
	else:
		pressed = False
	time.sleep(0.1)

#def capture():
