#!/usr/bin/env python
# -*- coding: utf-8 -*-

import picamera
import os
import time
import json
from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO

with open("config.json") as file:
	data = json.load(file)

overlay_renderer = None

font_size	= data["font"]["size"]
font_art	= data["font"]["art"]
sleep_time	= data["text"]["sleep_time"]
three		= data["text"]["3"]
two			= data["text"]["2"]
one			= data["text"]["1"]
fps			= data["foto"]["fps"]
pic			= data["foto"]["pic"]

def main():

	def W():
		W			= data["resolution"]["W"]
		return(W)
	
	def H():
		H			= data["resolution"]["H"]
		return(H)

	W = float(W())
	H = float(H())
	
	BUTTON_GPIO = 16
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	pressed = False

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

	with picamera.PiCamera() as camera:
		camera.resolution = (W, H), framerate=fps
		camera.crop       = (0.0, 0.0, 1.0, 1.0)
		camera.start_preview()

		overlay_renderer = None

		while True:
			text(text = "Mache ein Foto mit dem Knopf")
			if not GPIO.input(BUTTON_GPIO):
				if not pressed:
					text(text = three)
					time.sleep(sleep_time)
					text(text = two)
					time.sleep(sleep_time)
					text(text = one)
					time.sleep(sleep_time)
					date = ("data/" + (time.strftime("%Y%m%d-%H%M%S")) + (pic))
					text(text = " ")
					camera.shutter_speed = camera.exposure_speed
					camera.exposure_mode = 'off'
					g = camera.awb_gains
					camera.awb_mode = 'off'
					camera.awb_gains = g
					camera.capture((date), use_video_port=False)
					time.sleep(3)


		else:
			pressed = False
		time.sleep(0.1)


if __name__ == '__main__':
	import sys
	main()