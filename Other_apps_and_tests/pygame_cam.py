# import libraries 
import pygame 
import pygame.camera
from time import sleep

# initialize
pygame.init()
pygame.camera.init()

screen = pygame.display.set_mode((1280,720))
# get a lisf of connected cameras : 
camlist = pygame.camera.list_cameras()
print(camlist)

# take a picture from each camera and display 
if camlist:
    for cam in camlist:
        
        c = pygame.camera.Camera(cam,(640,480))
        c.start()
        img = c.get_image()
        print(type(img),img)
        screen.blit(img,(50,50))
        pygame.display.flip()
        sleep(1.5)

        
