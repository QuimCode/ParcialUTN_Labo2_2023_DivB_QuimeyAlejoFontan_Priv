##-------------MODULOS-------------##

import pygame

##-------------CODIGO-------------##

pygame.init()
pygame.mixer.init()

def reproducir_musica_menu():
    pygame.mixer.music.load("Recursos\Musica\Charly García, Pedro Aznar Gustavo Cerati - Vampiro.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.4)

def reproducir_musica_nivel1():
    pygame.mixer.music.load("Recursos\Musica\Mariposa Tecknicolor 8bits (128 kbps).mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)

def reproducir_musica_nivel2():
    pygame.mixer.music.load("Recursos\Musica\Soda Stereo Te Hacen Falta Vitaminas 8bits (128 kbps).mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.4)

def reproducir_musica_nivel3():
    pygame.mixer.music.load("Recursos\Musica\Rezo por vos 8bits (128 kbps).mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.4)
