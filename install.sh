#!/bin/bash
# ------------------------------------------------------------------
# [Nick Hildebrandt] MacAndMore
#          (C)2020
# ------------------------------------------------------------------
# /dev/sda1 /home/pi/photoboth/data auto user,umask=000,utf8, 0 0
cat $HOME/photoboth/logo.asa
# Update System and install deb
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install python3 python3-dev python3-rpi.gpio python3-picamera python3-pil ttf-mscorefonts-installer
sudo dpkg-reconfigure locales tzdata keyboard-configuration
# Create Interface on Startup
cp $HOME/photoboth/config/.bash_login $HOME
# Enable Auto Login
sudo cp $HOME/photoboth/config/logind.conf /etc/systemd/
sudo cp $HOME/photoboth/config/override.conf /etc/systemd/system/getty@tty1.service.d/
sudo reboot
