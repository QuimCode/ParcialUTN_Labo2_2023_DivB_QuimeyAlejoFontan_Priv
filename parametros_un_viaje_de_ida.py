##-------------MODULOS-------------##

import pygame
import sys

##-------------ARCHIVOS-------------##

from parametros_visual import *
from parametros_nivel1 import nivel_1
from parametros_sonido import reproducir_musica_menu

##-------------CODIGO-------------##

def render_texto(texto, tamanio, color, posicion):
    fuente = pygame.font.Font(None, tamanio)
    texto_renderizado = fuente.render(texto, True, color)
    rectangulo = texto_renderizado.get_rect()
    rectangulo.topleft = posicion
    return texto_renderizado, rectangulo

titulo_texto, titulo_rectangulo = render_texto("Un Viaje de ida", 60, Colores.AMARILLO.value, (20, 120))
mensaje_texto, mensaje_rectangulo = render_texto("Presiona Enter para comenzar", 50, Colores.AMARILLO.value, (20, 230))

def mostrar_menu():
    menu = True 

    pygame.init()
    pygame.display.set_caption("Microcentro un viaje de ida - Menu")

    fondo_del_menu = fondo_menu()
    reproducir_musica_menu() 

    while menu:
        frames.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif evento.key == pygame.K_RETURN:
                    nivel_1(60)

        PANTALLA.fill(Colores.NEGRO.value)
        PANTALLA.blit(fondo_del_menu, (0, 0))
        PANTALLA.blit(titulo_texto, titulo_rectangulo)
        PANTALLA.blit(mensaje_texto, mensaje_rectangulo)
        pygame.display.flip()


mostrar_menu()