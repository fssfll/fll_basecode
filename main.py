#!/usr/bin/env pybricks-micropython

##########################################################
# Pybrcks Micropython Base Code For Lego Mindstorm EV3 
# Created in Partnership: FLL Team 18300 & Bolton Robotics
#
# This code is free for all to use and modify in the spirit 
# of co-opertition.  Please consider giving a shout-out to
# Bolton Robotics and FLL Team 18300 if you find it helpful.
#
# Description:
# Intended to be used for First Lego League style competitions
# where multiple missions are run in a timed competitive match.
# This code allows for selection of up to 8 missions using the
# EV3 up, down, left and right buttons along with the center button
# to switch from missions 1-4 and missions 5-8.
#
# To get started, modify the bolton_robotics_robot.py file such
# that your robot's wiring and construction matches that described 
# in the bolton_robotics_robot class.
#
# After making any needed changes to the bolton_robotics_robot
# class to reflect your robot's construction add your mission
# code to one or more of the eight mission python files.
#
# After downloading, run the main.py python file on the EV3 which
# will initialize the robot, check for wiring issues and display 
# the program select menu.
# 
##########################################################

# Import the necessary libraries
import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick
from bolton_robotics_robot import bolton_robotics_robot
from menu import menu

###########
# Startup
###########
# Instantiate the Robot
r = bolton_robotics_robot()

# Additional initialization routines
# like calibrating the gyro could go here

# Program select menu
menu(r)
