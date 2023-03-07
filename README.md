# COMP 603 Project 1 ROS HelloWorld

**Author**: Li Chen, lchen0@umass.edu

**Last Edited**: 2023.03.07

---

## 1. Preparation

### 1.1 Required Files and Packages

    Files:
    boundary.csv
    env_setup.sh
    run_drawer.sh

    Packages:
    turtlesim_cleaner/
    rospy
    geometry.msg

### 1.2 Compilation
Before running the drawer application, you need to create your own ROS workspace `workspace`. Then create a directory `workspace/src`.

Move all files to `workspace/`. Move package `turtlesim_cleaner` to `workspace/src`

Before compiling, you need to make `env_setup.sh` and `run_drawer.sh` script files executable. Open a terminal under `workspace/`, run

    $ chmod +x env_setup.sh
    $ chmod +x run_drawer.sh

Then, do compilation. Run under `workspace/`

    $ catkin_make
    $ source devel/setup.bash 
    or
    $ source devel/setup.zsh

## 2.Usage
To run the program, you need to run `roscore` first. Under `workspace/`, run

    $ ./env_setup.sh

Then, open a turtlesim node. Open another terminal under `workspace/`, run

    $ rosrun turtlesim turtlesim_node

Then, open another new terminal under `workspace/`, run

    $ ./run_drawer.sh

Now you should see a window of turtlesim node, a turtle is running to draw the boundary. 

## 3. Extra
The boundary points generation program `boundary_list.py` is also provided. You can import own image into `workspace`, modify `boundary_list.py` and get a `*.csv` file of the image boundary.