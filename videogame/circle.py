'''Circle Sprite'''

import pygame
from videogame import rgbcolors

class Circle(pygame.Surface):
    '''Class creating circle sprite that can be used in Pong'''
    def __init__(
            self, radius, color, background_color=rgbcolors.white, name=None
            ):
          '''initialize the circle sprite'''
          width = radius * 2
          super().__init__((width, width))
          center = (radius, radius)
          self.color = color
          self.name = name
          self.fill(background_color)
          pygame.draw.circle(self, self._color, center, radius)

          