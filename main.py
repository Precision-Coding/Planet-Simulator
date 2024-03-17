import asyncio
from sys import exit
from math import inf
from pygame.display import set_mode, flip
from pygame.constants import SCALED
from pygame.event import get
import pygame
import time
import pygame


# Define planet class
class Planet:
    def __init__(self, radius, resolution):
        self.radius = radius
        self.resolution = resolution
        self.surface = pygame.Surface((radius * 4, radius * 4))
        self.draw_circle()

    def draw_circle(self):
        scaled_radius = int(self.radius * self.resolution)
        pygame.draw.circle(self.surface, "darkblue", (scaled_radius * 2, scaled_radius * 2), scaled_radius)

    def draw(self, screen_surface):
        screen_surface.blit(self.surface, self.surface.get_rect(center=(700, 350)))

    def update(self):
        self.surface.fill((0, 0, 0))  # Clear the surface
        self.draw_circle()  # Redraw the circle with updated size


# Define event handler class
class EventHandler:
    def __init__(self):
        self.should_exit = False
        self.resolution = 1

    async def handle_events(self, events_to_handle):
        # Handle events
        for event in events_to_handle:
            if event.type == pygame.QUIT:
                self.should_exit = True
            elif event.type == pygame.MOUSEWHEEL:
                self.resolution += event.y * 0.1  # Adjust the resolution based on the mouse wheel movement


# Initialize pygame
pygame.init()
pygame.display.set_caption("Solar System Simulation")

# Create instances
event_handler = EventHandler()
planet = Planet(150, event_handler.resolution)
drawables = [planet]

async def pygame_loop(framerate_limit=inf):
    loop = asyncio.get_event_loop()
    screen_surface = set_mode((1400, 700), flags=SCALED, vsync=1)
    next_frame_target = 0.0
    limit_frame_duration = 1.0 / framerate_limit

    while not event_handler.should_exit:
        if limit_frame_duration:
            # framerate limiter
            this_frame = time.time()
            delay = next_frame_target - this_frame
            if delay > 0:
                await asyncio.sleep(delay)
            next_frame_target = this_frame + limit_frame_duration

        for drawable in drawables:
            drawable.draw(screen_surface)
            drawable.update()

        events_to_handle = list(get())
        await event_handler.handle_events(events_to_handle)

        await loop.run_in_executor(None, flip)
        pygame.display.update()
    exit()

asyncio.run(pygame_loop(60))