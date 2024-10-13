from djitellopy import Tello 
import cv2 

###########################################################
width = 320 # width of the image
height = 240 # height of the image
startCounter = 1 # 0 if flying, 1 if testing
###########################################################

#### Connect to Tello's Wifi network
import os  
drone_wifi =  'TELLO-9A5430' # input('Input Name/SSID of the Wi-Fi network we would like to connect: ')  
# connecting to the provided Wi-Fi network  
os.system(f"networksetup -setairportnetwork en0 {drone_wifi}")  

# connect to Tello (make sure Drone is turned on, and connect to its wifi)
drone = Tello()
drone.connect()

drone.for_back_velocity = 0 
drone.left_right_velocity = 0 
drone.up_down_velocity = 0 
drone.yaw_velocity = 0 
drone.speed = 0 

print(f" battery level : {drone.get_battery()}")

drone.streamoff()
drone.streamon()


while True :

    # Get the image from Tello
    frame_read = drone.get_frame_read()
    myframe = frame_read.frame
    img = cv2.resize(myframe,(width,height))

    # to Takeoff in the beggining 
    # if startCounter == 0 :
    #     drone.takeoff()
    #     # drone.move_right(5)
    #     # drone.rotate_clockwise(90)
    #     startCounter == 1 

    ### ! There is a 2nd way of moving the drone, and that's using Velocity ! 
    ### ! TRY THIS !
    # if drone.send_rc_control:
    #     drone.send_rc_control(drone.left_right_velocity,drone.for_back_velocity,drone.up_down_velocity,drone.yaw_velocity)

    ## Display Image
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow("my Drone Capture",img)

    # rotate indefinitely until Q is pressed 
    # import time 
    # if startCounter == 1 :
    #     drone.rotate_clockwise(45)
    #     time.sleep(1)        


    # Wait for "Q" button to STOP and land
    key = cv2.waitKey(1) & 0xff
    if key == ord('q'):
        drone.land()
        frame_read.stop()
        drone.streamoff()
        exit(0)
        break
