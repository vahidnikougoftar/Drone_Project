from network_utils import connect_to_drone_wifi
from config import DRONE_WIFI_SSID
import cv2
import numpy as np
from djitellopy import Tello
import time
import pyttsx3
import sys

# Connect to Tello's Wi-Fi network
if not connect_to_drone_wifi(DRONE_WIFI_SSID):
    sys.exit(1)

class FaceDetectionDrone:
    def __init__(self):
        # Initialize TTS engine
        self.engine = pyttsx3.init()
        
        # Connect to Tello drone
        self.tello = Tello()
        self.tello.connect()
        
        # Enter SDK mode
        self.tello.send_command_without_return("command")
        
        # Start video stream
        self.tello.streamon()
        
        # Initialize battery warning flag
        self.low_battery_warning_given = False

    def run(self):
        while True:
            # Get the image from the drone
            frame = self.tello.get_frame_read().frame

            # ... existing face detection code ...

            # Check battery status
            self.check_battery()

            # ... existing display code ...

            key = cv2.waitKey(1) & 0xff
            if key == 27:  # ESC
                break
            elif key == ord('t'):
                self.tello.takeoff()
            elif key == ord('l'):
                self.tello.land()

        self.tello.land()
        self.tello.streamoff()
        cv2.destroyAllWindows()

    def check_battery(self):
        battery = self.tello.get_battery()
        if battery <= 20 and not self.low_battery_warning_given:
            self.engine.say(f"Warning: Battery level is {battery} percent")
            self.engine.runAndWait()
            self.low_battery_warning_given = True
        elif battery > 20:
            self.low_battery_warning_given = False
