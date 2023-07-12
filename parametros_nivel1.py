import pygame
import sys

from parametros_nivel2 import nivel_2
from parametros_visual import *
from class_vida import *
from class_trampa import *
from utilidades import mostrar_puntos,dibujar_banner, guardar_puntos_nivel
from class_jugador import Personaje
from class_caja import cajas_nivel1
from class_enemigo import Enemigo, enemigos_nivel1
from class_plataforma import plataformas_nivel1
from parametros_sonido import reproducir_musica_nivel1
from parametros_colisiones import detectar_colision

pygame.init()
reloj = pygame.time.Clock()
puntos_totales = 0 

def nivel_1(tiempo_total):
    nivel = True

    tiempo_inicial = pygame.time.get_ticks()
    puntos = 0
    tiempo_restante = tiempo_total 
    oportunidades_revivir = 3

    reproducir_musica_nivel1()
    fondo_de_nivel = fondo_nivel1()
    mostrar_puntos(PANTALLA, puntos, tiempo_restante, oportunidades_revivir)

    Jugador = Personaje(1878, 850, 100, 100)

    plataformas_del_nivel = plataformas_nivel1
    cajas_del_nivel = cajas_nivel1

    enemigos_aleatorios = []  # Lista de enemigos aleatorios
    cantidad_de_enemigos_aleatorios = 2

    # Generar enemigos aleatorios
    for _ in range(cantidad_de_enemigos_aleatorios):
        enemigo_aleatorio = Enemigo.generar_enemigo_aleatorio(90,90)
        enemigos_aleatorios.append(enemigo_aleatorio)

    while nivel:
        frames.tick(FPS)
        tiempo_transcurrido = pygame.time.get_ticks() - tiempo_inicial
        tiempo_restante = tiempo_total - tiempo_transcurrido // 1000

        teclas = pygame.key.get_pressed()

        Jugador.mover(teclas)
        Jugador.aplicar_gravedad()
        Jugador.limites()

        detectar_colision(Jugador, plataformas_nivel1, cajas_del_nivel, enemigos_nivel1, enemigos_aleatorios, objetos_nivel1, trampas_nivel2)

        Jugador.actualizar_animacion()
        Jugador.perder_vida()

        tiempo_restante -= frames.get_time() / 1000
        if tiempo_restante <= 0:
            tiempo_restante = 0

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Clic izquierdo del mouse
                    pos_mouse = pygame.mouse.get_pos()
                    print(f"Posición del clic: ({pos_mouse[0]}, {pos_mouse[1]})")

        PANTALLA.fill(Colores.NEGRO.value)
        PANTALLA.blit(fondo_de_nivel, (0, 0))

        for plataforma in plataformas_del_nivel:
            plataforma.dibujar(PANTALLA)
            plataforma.mover()

        for caja in cajas_del_nivel:
            caja.dibujar(PANTALLA)

        for cura in objetos_nivel1:
            cura.dibujar(PANTALLA)

        for enemigo in enemigos_nivel1:
            if enemigo.activo:
                enemigo.dibujar(PANTALLA)
                enemigo.mover()
                enemigo.aplicar_gravedad()
                enemigo.limites()

        for enemigo in enemigos_aleatorios:
            if enemigo.activo:
                enemigo.dibujar(PANTALLA)
                enemigo.mover()
                enemigo.aplicar_gravedad()
                enemigo.limites()

        if (Jugador.left_rect.colliderect(pygame.Rect(1900, 1013, 5, 5)) or
            Jugador.right_rect.colliderect(pygame.Rect(1900, 1013, 5, 5)) or
            Jugador.top_rect.colliderect(pygame.Rect(1900, 1013, 5, 5)) or
            Jugador.bottom_rect.colliderect(pygame.Rect(1900, 1013, 2, 2))):
            guardar_puntos_nivel(Jugador.puntos, Jugador, puntos_totales)
            nivel_2(tiempo_total, puntos_totales)  
            nivel = False  

        dibujar_banner(PANTALLA)
        Jugador.dibujar(PANTALLA)
        Jugador.mostrar_vida(PANTALLA)
        mostrar_puntos(PANTALLA, Jugador.puntos, tiempo_restante, Jugador.oportunidades_revivir)
        pygame.display.flip()

