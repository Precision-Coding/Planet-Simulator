# main
import pygame
from sys import exit
import math


def planetCreate(radius, resolution):
    radius = radius / resolution
    planet = pygame.surface.Surface((radius * 3, radius * 3))
    pygame.draw.circle(planet, "darkblue", (radius * 1.5, radius * 1.5), radius,)
    planet_x, planet_y = 700, 350
    planet_pos = planet.get_rect(center = (planet_x, planet_y))

    return planet, planet_pos

def cometCreate(radius, resolution, distance, size):
    radius = radius * resolution
    pixel_distance = distance / resolution
    comet = pygame.surface.Surface((radius * 4, radius * 4))
    pygame.draw.circle(comet, "darkblue", (radius * 2, radius * 2), radius,)
    comet_x, comet_y = 0 / resolution + 700, 0 / resolution + 350
    comet_pos = comet.get_rect(center = (comet_x, comet_y))

    return comet, comet_pos

def scaleCreate(resolution, window_width, font):
    scale_bar = pygame.surface.Surface((window_width, 50))
    scale_bar.fill((25, 25, 25))
    for distance in range(1, 12):
        pixel_space = window_width / 11
        pygame.draw.line(scale_bar, "white", (distance * pixel_space, 0), (distance * pixel_space, 50))

    text = font.render(f"{distance * pixel_space * resolution / 1000} Km", True, "white")
    return scale_bar

window_width, window_height = 1400, 700 # Size of actual window
resolution = 100000

# Framerate
frame_rate = 60
clock = pygame.time.Clock() # I honestly don't know what this

# Screen Setup
pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Planet-Simulator")

# Font
pygame.font.init()
base_font = pygame.font.SysFont("helvetica", 20 * resolution)

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
    planet, planet_pos = planetCreate(12000000, resolution)
    scale_bar = scaleCreate(resolution, window_width, base_font)

    #Blits
    screen.blit(planet, planet_pos)
    screen.blit(scale_bar, (0, 0))
    # Updates and tickrate
    pygame.display.update()
    clock.tick(frame_rate)