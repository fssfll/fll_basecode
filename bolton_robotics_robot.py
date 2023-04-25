##########################################################
# Pybrcks Micropython Base Code For Lego Mindstorm EV3 
# Created in Partnership: FLL Team 18300 & Bolton Robotics
#
# This code is free for all to use and modify in the spirit 
# of co-opertition.  Please consider giving a shout-out to
# Bolton Robotics and FLL Team 18300 if you find it helpful.
#
##########################################################
# bolton_robotics_robot.py
##########################################################
#
# Modify this file if Ev3 wiring differs from the the following
# default configuration:
#
# --- MOTOR WIRING ---
# Port A: attachment motor
# Port B: left drive motor
# Port C: right drive motor
# Port D: not connected
#
# --- SENSOR WIRING ---
# Port 1: Color Sensor
# Port 2: not connected
# Port 3: not connected
# Port 4: not connected
#
# --- ROBOT WHEEL SIZE AND SPACING---
# wheel_diameter: 56mm
# axle_track: 115mm (distance between wheels)
#
##########################################################

# Import the necessary libraries
import sys
import math
import time
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.iodevices import *
from pybricks.tools import wait, StopWatch
from pybricks.hubs import EV3Brick
from pybricks.media.ev3dev import Font

################################
# Define custom_robot Class
################################
class bolton_robotics_robot:

    def __init__(self):
        
        '''
        This is the construtor for our robot class. 
        This function gets called when a robot object is made from the robot class.
        '''

        # Initialize the brick, motors, sensors
        # Use "try" so there can be an exception if there is an initialization error
        try:
            self.ev3 = EV3Brick()
        except:
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"EV3 FAIL")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.left_attachment_motor = Motor(Port.A)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT A")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.left_drive_motor = Motor(Port.B)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT B")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.right_drive_motor = Motor(Port.C)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT C")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.right_attachment_motor = Motor(Port.D)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT D")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.left_color_sensor = ColorSensor(Port.S1)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT 1")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.right_color_sensor = ColorSensor(Port.S4)
        except: 
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"CHECK PORT 4")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()
        try:
            self.robot = DriveBase(self.left_drive_motor, self.right_drive_motor, wheel_diameter=56.9, axle_track=89)
            self.robot.settings(straight_speed=600, straight_acceleration=500, turn_rate=200, turn_acceleration=123)
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.GREEN)
            self.watch = StopWatch()
            self.ev3.screen.draw_text(10,40,"STARTUP GOOD!")
            self.ev3.screen.set_font(Font(size=30, bold=True))
            wait(1000)
            self.ev3.screen.clear()    
        except:
            self.ev3.screen.clear()
            self.ev3.light.off()
            self.ev3.light.on(Color.RED)
            self.ev3.screen.draw_text(0,40,"STARTUP ERROR")
            self.ev3.screen.draw_text(0,80,"NOT WIRING")
            self.ev3.speaker.beep(frequency=2000, duration=1000)
            wait(4000)
            self.ev3.screen.clear()
            sys.exit()

################################
# Define functions as needed
################################
    
    # Reset The Gyro

    # Gyro tank turn

    # Line follow
 

