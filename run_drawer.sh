#!/usr/bin/zsh
###
 # @Author: Li Chen lchen0@umass.edu
 # @Date: 2023-03-07 15:13:48
 # @LastEditors: Li Chen lchen0@umass.edu
 # @LastEditTime: 2023-03-07 16:03:04
 # @FilePath: /undefined/home/lichen_ubuntu_t480/OneDrive_minolta001@gmail.com/UmassAmherst/2023_Spring/COMP_603/P1/P1D2/ros-helloworld/env_setup.sh
 # @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
### 
chmod u+x src/turtlesim_cleaner/src/umass_drawer.py
source devel/setup.zsh
rosrun turtlesim_cleaner umass_drawer.py