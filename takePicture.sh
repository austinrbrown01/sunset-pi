#!/bin/bash

DATE=$(date +"%y-%m-%d_%H_%M_%S")
fswebcam -r 1920x1080 -S 30 --fps 15 -D 2 --no-banner /home/pi/Desktop/SunsetProject/camImages/$DATE.jpg
