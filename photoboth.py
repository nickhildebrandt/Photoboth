#!/usr/bin/env python3
# ------------------------------------------------------------------
# [Nick Hildebrandt] MacAndMore
#          (C)2021
# ------------------------------------------------------------------

import time
import RPi.GPIO as GPIO
import gi
import picamera

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
from gi.repository import GLib
from gi.repository import GObject
from gi.repository import Gdk

APP_NAME = 'Photoboth'

class Main:
    def __init__(self):
        gladeFile       = "photoboth.glade"
        self.builder    = Gtk.Builder()
        self.builder.add_from_file(gladeFile)

        window          = self.builder.get_object("Main")
        window.connect("delete-event", Gtk.main_quit)
        window.show()

	try:
    	camera.start_preview()
    	time.sleep(10)
    	camera.stop_preview()
	finally:
    	camera.close()

if __name__ == '__main__':
    main = Main()
    Gtk.main()


#def capture():
