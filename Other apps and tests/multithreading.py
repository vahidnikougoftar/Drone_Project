#!/usr/bin/env python3
__author__ = 'Anton Vanhoucke'

# import evdev
# import ev3dev.auto as ev3
import threading
import pygame
from pygame.locals import KEYDOWN , K_LEFT , K_RIGHT
# from time import sleep 
# from ev3dev2.sound import Sound
# from ev3dev2.motor import MediumMotor, OUTPUT_B , OUTPUT_D

## Some helpers ##
def scale(val, src, dst):
    """
    Scale the given value from the scale of src to the scale of dst.

    val: float or int
    src: tuple
    dst: tuple

    example: print(scale(99, (0.0, 99.0), (-1.0, +1.0)))
    """
    return (float(val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]

def scale_stick(value):
    return scale(value,(0,255),(-100,100))

def clamp(value, floor=-100, ceil=100):
    """
    Clamp the value within the floor and ceiling values.
    """
    return max(min(value, ceil), floor)

## Initializing ##
print("Finding ps3 controller...")
# devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
# for device in devices:
#     if device.name == 'PLAYSTATION(R)3 Controller':
#         ps3dev = device.fn

# gamepad = evdev.InputDevice(ps3dev)

# Initialize globals
speed = 0
turn = 0
running = True
# s = Sound()

# Within this thread all the motor magic happens
class MotorThread(threading.Thread):
    def __init__(self):
        # Add more sensors and motors here if you need them
        # self.steering = ev3.MediumMotor(ev3.OUTPUT_B)
        engine = clamp(speed)
        self.engine = engine #ev3.LargeMotor(ev3.OUTPUT_D)
        threading.Thread.__init__(self)

    def run(self):
        # print("\n\nEngine running!")
        # s.beep()
        # Change this function to suit your robot. 
        # The code below is for driving a simple tank.
        while running:
            engine_speed = clamp(speed)* 2.0 # to speed up the engine ! 
            # left_dc = clamp(speed+turn)
            self.engine = engine_speed #.run_direct(duty_cycle_sp=-engine_speed)
            # self.steering.run_direct(duty_cycle_sp=left_dc)

        self.motor.stop()

class SteeringThread(threading.Thread):
    def __init__(self):
        # Add more sensors and motors here if you need them
        steering = clamp(turn)* 2.0 # to speed up the engine ! 
            
        self.steering = steering #ev3.MediumMotor(ev3.OUTPUT_B)
        threading.Thread.__init__(self)

    def steer(self):
        # print("\n\nEngine running!")
        # s.beep()
        # Change this function to suit your robot. 
        # The code below is for driving a simple tank.
        while running:
            # right_dc = clamp(speed-turn)
            steering_angle = clamp(turn)
            self.steering = steering_angle # .run_direct(duty_cycle_sp=steering_angle)
            print(steering_angle)
            # self.steering.on_to_position(speed=15, position = steering_angle , brake=True)

        # self.motor.stop()

# Multithreading magics
motor_thread = MotorThread()
motor_thread.setDaemon(True)
motor_thread.start()

steering_thread = SteeringThread()
steering_thread.setDaemon(True)
steering_thread.start()


for event in pygame.event.get():   #this loops infinitely
    if event.type == KEYDOWN :
        if event.key == K_LEFT:
            print('left')
        if event.key == K_RIGHT:
            print('right')

