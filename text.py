import sys
import pygame

# Initialize pygame so it runs in the background and manages things
pygame.init()
#make colors
red = pygame.Color(255,0,0)
orange = pygame.Color(210,100,0)
purple = pygame.Color(150,0,150)

# create a font object
font = pygame.font.SysFont("Garamond", 100)
# create text
text = font.render("HELLO", True, orange)

# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (400, 300) )

# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        print(event)
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
    #fill screen with color
    screen.fill(purple)
    #put text
    screen.blit(text, pygame.mouse.get_pos())
    pygame.display.flip()
