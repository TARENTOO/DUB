#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos

import pygame
from pygame.locals import *

from dub import images

WIDTH = 400
HEIGHT = 128

class Player(pygame.sprite.Sprite):
    def __init__(self, nombre):
        self.nombre = nombre
        pygame.sprite.Sprite.__init__(self)
        self.image = images.load_image("imagenes/explorer.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = 0.5

    def actualizar(self, time, keys):
        if self.rect.left >= 0:
            if keys[K_LEFT]:
                self.rect.centerx -= self.speed * time
        if self.rect.right <= WIDTH:
            if keys[K_RIGHT]:
                self.rect.centerx += self.speed * time
        if self.rect.top >= 0:
            if keys[K_UP]:
                self.rect.centery -= self.speed * time
        if self.rect.bottom <= HEIGHT:
            if keys[K_DOWN]:
                self.rect.centery += self.speed * time
