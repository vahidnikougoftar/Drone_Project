# Import the pygame module
import pygame
from pygame.locals import *  # Import all constants from pygame.locals

# Note: Importing all constants from pygame.locals is generally not recommended
# for larger projects due to potential namespace pollution, but it's acceptable
# for small scripts where brevity is prioritized.

# The 'sleep' function is not used in the provided code, so it's removed.
# If needed later, it can be imported as: from time import sleep

#  define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0,0,0)

# Initialize pygame
pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Event Handling
# Variable to keep the main loop running
running = True

# Fill the screen with white
screen.fill(black)

# Create a surface and pass in a tuple containing its length and width
surf = pygame.Surface((50, 50))

# Give the surface a color to separate it from the background
rect = surf.get_rect()

# This line says "Draw surf onto the screen at the center"
screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
pygame.display.flip()

class TextWriter:
    def __init__(self, screen, font_size=32, font_name='freesansbold.ttf'):
        self.screen = screen
        self.font = pygame.font.Font(font_name, font_size)

    def write_text(self, input_text, x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2, new_input=True):
        if new_input:
            self.screen.fill(black)
        text = self.font.render(input_text, True, green, black)
        text_rect = text.get_rect(center=(x, y))
        self.screen.blit(text, text_rect)
        pygame.display.update()

# Create an instance of TextWriter
text_writer = TextWriter(screen)

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            key_actions = {
                K_LEFT: lambda: text_writer.write_text('LEFT'),
                K_RIGHT: lambda: text_writer.write_text('RIGHT'),
                K_UP: lambda: text_writer.write_text('UP'),
                K_DOWN: lambda: text_writer.write_text('DOWN'),
                K_w: lambda: text_writer.write_text('w'),
                K_ESCAPE: lambda: exit()
            }
            
            if event.key in key_actions:
                key_actions[event.key]()
        
        elif event.type == QUIT:
            running = False

    pygame.time.Clock().tick(30)  # Limit the frame rate to 30 FPS


