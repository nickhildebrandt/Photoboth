#!/usr/bin/env python
# -*- coding: utf-8 -*-

import picamera
import os
import time
from PIL import Image, ImageDraw, ImageFont

def main():
    """
    Displayes preview on PiTFT with PiCamera.add_overlay(). Displayed animation
    is composed of two layers; One continuously displays the input from camera
    while another continuously gets refreshed every time a calculation is done.
    It worls faster because the layers are divided and the original preview
    layer does not get affected by another layer that requires some calculation
    and image creation.
    It, however, has a weak point. This outputs to default display device,
    /dev/fb0. To display the same output to PiTFT, /dev/fb1, you need to use
    rpi-fbcp and let it copy the /dev/fb0 output to /dev/fb1.
    """

    # prep picamera
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.rotation   = 180
        camera.crop       = (0.0, 0.0, 1.0, 1.0)

        # display preview
        camera.start_preview()

        # continuously updates the overlayed layer and display stats
        overlay_renderer = None
        while True:
            text = time.strftime('%H:%M:%S', time.gmtime())
            img = Image.new("RGB", (1024, 768))
            draw = ImageDraw.Draw(img)
            draw.font = ImageFont.truetype(
                            "/usr/share/fonts/truetype/freefont/FreeSerif.ttf",
                            50)
            draw.text((10,10), text, (255, 255, 255))

            if not overlay_renderer:
                """
                If overlay layer is not created yet, get a new one. Layer
                parameter must have 3 or higher number because the original
                preview layer has a # of 2 and a layer with smaller number will
                be obscured.
                """
                overlay_renderer = camera.add_overlay(img.tostring(),
                                                      layer=3,
                                                      size=img.size,
                                                      alpha=128);
            else:
                overlay_renderer.update(img.tostring())

if __name__ == '__main__':
    import sys
    try:
        main()
    except:
        print 'Unexpected error : ', sys.exc_info()[0], sys.exc_info()[1]