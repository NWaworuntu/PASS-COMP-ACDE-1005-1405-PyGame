# Example showing player movement
import pygame

# pygame setup
pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Creates a screen for the game 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# GAME VARIABLES
playerX = SCREEN_WIDTH / 2
playerY = SCREEN_HEIGHT / 2
playerSpeed = 100

deltaTime = 0

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
    pygame.draw.circle(screen, "white", (playerX, playerY), 16)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        playerY -= playerSpeed * deltaTime
    if keys[pygame.K_s]:
        playerY += playerSpeed * deltaTime
    if keys[pygame.K_a]:
        playerX -= playerSpeed * deltaTime
    if keys[pygame.K_d]:
        playerX += playerSpeed * deltaTime

    # Use the flip() to update the screen. Sends draw commands to the screen.
    pygame.display.flip()
    # Limits FPS to 60 and calculates deltaTime for physics calculations.
    deltaTime = clock.tick(60) / 1000 

pygame.quit()