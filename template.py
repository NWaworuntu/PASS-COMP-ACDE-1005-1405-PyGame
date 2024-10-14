# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Creates a screen for the game 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# GAME LOOP
running = True
while running:
    # Every frame check for events. If a QUIT event happens, end game loop.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color to wipe away anything from last frame.
    screen.fill("black")

    # RENDER YOUR GAME HERE

    # Use the flip() to update the screen. Sends draw commands to the screen.
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()