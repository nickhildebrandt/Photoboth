#!/bin/bash
# ------------------------------------------------------------------
# [Nick Hildebrandt] MacAndMore
#          (C)2020
# ------------------------------------------------------------------

cat $HOME/photoboth/app/logo.asa
# Update System and install deb
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install python3 python3-dev python3-rpi.gpio python3-picamera
sudo dpkg-reconfigure locales tzdata keyboard-configuration
# Create picam Service
sudo cp $HOME/photoboth/config/picam.service /etc/systemd/system/
sudo systemctl enable picam.service
# Create Interface on Startup
touch $HOME/.bash_login
echo "bash $HOME/photoboth/app/interface.sh" >> $HOME/.bash_login
chmod u+rx $HOME/photoboth/app/press.sh
chmod +x $HOME/photoboth/app/press.sh
# Enable Auto Login
sudo cp $HOME/photoboth/config/logind.conf /etc/systemd/
sudo cp $HOME/photoboth/config/override.conf /etc/systemd/system/getty@tty1.service.d/
sudo reboot
