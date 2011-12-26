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
        self.saltando = False
        self.fsalto= 0

    def actualizar(self, time, keys):
        if self.rect.left >= 0:
            if keys[K_LEFT]:
                self.rect.centerx -= self.speed * time
        if self.rect.right <= WIDTH:
            if keys[K_RIGHT]:
                self.rect.centerx += self.speed * time
        if self.rect.top >= 0:
            if keys[K_SPACE] and self.rect.bottom >= HEIGHT:
                self.saltar()
        if self.saltando:
            self.rect.centery -= self.speed * time
        if self.rect.centery < self.fsalto:
            self.saltando = False
            
    def saltar(self):
        self.saltando = True
        self.fsalto = HEIGHT - (self.rect.height * 2) 

    def gravedad(self, time):
        if self.rect.bottom <= HEIGHT:
            self.rect.centery += 0.2 * time
