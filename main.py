# main
import pygame
from sys import exit
import math

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

def planetCreate(radius, resolution):
    radius = radius * resolution
    planet = pygame.surface.Surface((radius * 4, radius * 4))
    pygame.draw.circle(planet, "darkblue", (radius * 2, radius * 2), radius,)

    return planet


# Event Loop
while True:
    # Game ender
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEWHEEL:
            resolution = resolution + event.y * resolution / 10

    # Surface Updates
    planet = planetCreate(150, resolution)


    screen.blit(planet, planet.get_rect(center = (700, 350)))

    # Updates and tickrate
    pygame.display.update()
    clock.tick(frameRate)