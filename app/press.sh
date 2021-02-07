#!/bin/bash
# ------------------------------------------------------------------
# [Nick Hildebrandt] MacAndMore
#          (C)2020
# ------------------------------------------------------------------

clear
cat $HOME/photoboth/app/3.counter
sleep 1
clear
cat $HOME/photoboth/app/2.counter
sleep 1
clear
cat $HOME/photoboth/app/1.counter
sleep 1
clear
sudo service picam stop
raspistill -p 0,0,1920,1080 -f -w 1920 -h 1080 --timeout 1300 -o $HOME/photoboth/data/`date +"%Y-%m-%d_%H-%M"`.png
sudo service picam start
cat $HOME/photoboth/app/danke.print
sleep 2
bash $HOME/photoboth/app/interface.sh && exit
