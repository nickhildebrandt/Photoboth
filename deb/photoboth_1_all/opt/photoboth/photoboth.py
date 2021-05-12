#!/usr/bin/env python
# -*- coding: utf-8 -*-

from picamera import PiCamera
import os
import time
import json
from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO

with open("config.json") as file:
	data = json.load(file)

overlay_renderer = None

W			= data["resolution"]["W"]
H			= data["resolution"]["H"]
font_size	        = data["font"]["size"]
font_art	        = data["font"]["art"]
satz		        = data["text"]["satz"]
sleep_time	        = data["text"]["sleep_time"]
three		        = data["text"]["3"]
two			= data["text"]["2"]
one			= data["text"]["1"]
light		        = data["foto"]["light"]
fps			= data["foto"]["fps"]
pic			= data["foto"]["pic"]
path                    = data["foto"]["path"]

def main():

	BUTTON_GPIO = 16
	LAMPE_GPIO = 18
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(LAMPE_GPIO, GPIO.OUT)
	pressed = False

	if light == "ON":
		GPIO.output(LAMPE_GPIO, False)

	def text(text):
		global overlay_renderer
		img = Image.new("RGBA", (W, H), (255, 0, 0, 0))
		draw = ImageDraw.Draw(img)
		draw.font = ImageFont.truetype(font_art, font_size)
		w, h = draw.textsize(text)
		draw.text(((W-w)/2,(H-h)/2), text, (255, 255, 255))

		if not overlay_renderer:
			overlay_renderer = camera.add_overlay(img.tobytes(),
												  layer=3,
												  size=img.size,
												  alpha=128);
		else:
			overlay_renderer.update(img.tobytes())

	camera = PiCamera(resolution=(W, H), framerate=fps)
	camera.crop       = (0.0, 0.0, 1.0, 1.0)
	camera.start_preview()

	overlay_renderer = None
	try:
		while True:
			text(text = satz)
			if not GPIO.input(BUTTON_GPIO):
				if not pressed:
					if light == "ON":
						GPIO.output(LAMPE_GPIO, True)
					text(text = three)
					time.sleep(sleep_time)
					text(text = two)
					time.sleep(sleep_time)
					text(text = one)
					time.sleep(sleep_time)
					date = ((path) + (time.strftime("%Y%m%d-%H%M%S")) + (pic))
					text(text = " ")
					camera.capture((date), use_video_port=False)
					time.sleep(sleep_time)
					if light == "ON":
						GPIO.output(LAMPE_GPIO, False)
			else:
				pressed = False
				time.sleep(0.1)
	finally:
		GPIO.cleanup()


if __name__ == '__main__':
	import sys
	main()
