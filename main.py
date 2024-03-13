# main
import pygame
from sys import exit

windowWidth, windowHeight = 1400, 700 # Size of actual window
resolution = 1

# Framerate
frameRate = 60
clock = pygame.time.Clock() # I honestly don't know what this

# Screen Setup
pygame.init()
screen = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Planet-Simulator")

# Font
pygame.font.init()
baseFont = pygame.font.SysFont("helvetica", 20 * resolution)

# Event Loop
while True:
    # Game ender
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEWHEEL:
            resolution = resolution + event.y / 25

    #PLANET
    radius = 150 * resolution
    planet = pygame.surface.Surface((1400, 700))
    pygame.draw.circle(planet, "red", (700,350), radius,)

    screen.blit(planet, (0,0))
    # Updates and tickrate
    pygame.display.update()
    clock.tick(frameRate)