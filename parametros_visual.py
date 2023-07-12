##-------------MODULOS-------------##

import pygame

#------------#

from enum import Enum

##-------------CODIGO-------------##

frames = pygame.time.Clock()
FPS = 30

ANCHO = 1920
ALTO = 1065

pantalla = (ANCHO, ALTO)
PANTALLA = pygame.display.set_mode(pantalla)

VELOCIDAD_ANIMACION = 5
VELOCIDAD_ANIMACION_ENEMIGOS = 5

class Colores(Enum):
    ROJO = (169, 50, 38)
    VIOLETA = (108, 52, 131)
    AZUL = (52, 73, 94)
    CELESTE = (52, 152, 219)
    VERDE = (34, 153, 84)
    AMARILLO = (241, 196, 15)
    NARANJA = (202, 111, 30)
    BLANCO = (236, 240, 241)
    GRIS = (215, 219, 221)
    NEGRO = (0, 0, 0)

##-------------BACKGROUNDS/FONDOS-------------##

def fondo_menu():
    fondo_menu = pygame.image.load("Recursos\Fondos\Fondo Menu\Fondo.jpg").convert()
    fondo_menu = pygame.transform.scale(fondo_menu, pantalla)
    return fondo_menu

def fondo_nivel1():
    fondo_nivel1 = pygame.image.load("Recursos/Fondos/Fondos Ciudad/city.png").convert()
    fondo_nivel1 = pygame.transform.scale(fondo_nivel1, pantalla)
    return fondo_nivel1

def fondo_nivel2():
    fondo_nivel1 = pygame.image.load("Recursos\Fondos\Fondos Ciudad\cyberpunk-street.png").convert()
    fondo_nivel1 = pygame.transform.scale(fondo_nivel1, pantalla)
    return fondo_nivel1

##-------------PLATAFORMAS/IMAGENES-------------##



##-------------PERSONAJES/ENEMIGOS-------------##
