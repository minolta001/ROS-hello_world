#!/usr/bin/zsh
killall -9 roscore
killall -9 rosmaster
catkin_make
roscore