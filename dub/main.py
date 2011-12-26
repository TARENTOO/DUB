#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos

import sys, os

sys.path.append(os.path.abspath(".."))

import pygame
from pygame.locals import *

from dub import images
from dub import objetos

WIDTH = 400
HEIGHT = 128

IMAGES = os.path.abspath(".") + "\imagenes"

# Constantes
 
# Clases
# ---------------------------------------------------------------------
 
# ---------------------------------------------------------------------
 
# Funciones
# ---------------------------------------------------------------------
 
# ---------------------------------------------------------------------
 
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dub game")
    
    background = images.load_image(IMAGES + "\mountains.png")
    valdemar = objetos.Player("Valdemar")
    
    clock = pygame.time.Clock()
    
    while True:
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
        valdemar.gravedad(time)
        valdemar.actualizar(time, keys)
        screen.blit(background, (0, 0))
        screen.blit(valdemar.image, valdemar.rect)
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()
