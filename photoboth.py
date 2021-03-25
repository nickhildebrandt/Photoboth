#!/usr/bin/env python3
# ------------------------------------------------------------------
# [Nick Hildebrandt] MacAndMore
#          (C)2021
# Photoboth for PI
# ------------------------------------------------------------------

from __future__ import absolute_import, division, print_function, unicode_literals

import time
import RPi.GPIO as GPIO
import picamera
import time
import pi3d

W, H = 800, 600

with picamera.PiCamera() as camera:

    camera.resolution = (W, H)
    camera.framerate = 30
    camera.start_preview()

    #NB layer argument below, fps as slow as needed for whatever's changing
    DISPLAY = pi3d.Display.create(w=W, h=H, layer=4, frames_per_second=10)
    DISPLAY.set_background(0.0, 0.0, 0.0, 0.0) # transparent
    shader = pi3d.Shader("uv_flat")
    CAMERA = pi3d.Camera(is_3d=False)
    font = pi3d.Font("/usr/share/fonts/truetype/freefont/FreeSerif.ttf",
                          (128, 255, 128, 255)) # blue green 1.0 alpha
    keybd = pi3d.Keyboard()
    tx = -DISPLAY.width / 2 + 150 # incr right, zero in middle
    ty = DISPLAY.height / 2 - 50 # incr upwards

    while DISPLAY.loop_running():
      text = pi3d.String(font=font, string=time.strftime('%H:%M:%S', time.gmtime()),
                      camera=CAMERA, x=tx, y=ty, z=1.0, is_3d=False)
      text.set_shader(shader)
      text.draw()
      time.sleep(0.1)
      if keybd.read() == 27:
        DISPLAY.destroy()
        break