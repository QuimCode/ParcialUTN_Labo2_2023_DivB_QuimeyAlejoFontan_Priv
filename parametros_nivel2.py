import pygame
import sys
import json

from utilidades import *
from parametros_nivel3 import nivel_3
from parametros_visual import *
from class_vida import objetos_nivel1
from class_trampa import *
from utilidades import mostrar_puntos, dibujar_banner, guardar_puntos_nivel, cargar_puntos_totales, cargar_vida_y_vidas_restantes
from class_jugador import Personaje
from class_caja import cajas_nivel2
from class_enemigo import Enemigo, enemigos_nivel2
from class_plataforma import plataformas_nivel2
from parametros_sonido import reproducir_musica_nivel2
from parametros_colisiones import detectar_colision

pygame.init()
reloj = pygame.time.Clock()

def nivel_2(tiempo_total, puntos_totales):
    nivel = True

    tiempo_inicial = pygame.time.get_ticks()
    puntos = 0
    tiempo_restante = tiempo_total 
    oportunidades_revivir = 3

    puntos_totales = cargar_puntos_totales()

    reproducir_musica_nivel2()
    fondo_de_nivel = fondo_nivel2()
    mostrar_puntos(PANTALLA, puntos, tiempo_restante, oportunidades_revivir)

    Jugador = Personaje(10, 850, 100, 100)

    datos_personaje = cargar_vida_y_vidas_restantes()
    vida_nivel1 = datos_personaje["vida_nivel1"]
    vidas_restantes_nivel1 = datos_personaje["vidas_restantes"]

    if vida_nivel1 >= 100:
        Jugador.imagen_corazones_actual = pygame.image.load("Recursos\Modelos\PNG Objetos\\4 corazones.png")
    elif vida_nivel1 >= 75:
        Jugador.imagen_corazones_actual = pygame.image.load("Recursos\Modelos\PNG Objetos\\3 corazones.png")
    elif vida_nivel1 >= 50:
        Jugador.imagen_corazones_actual = pygame.image.load("Recursos\Modelos\PNG Objetos\\2 corazones.png")
    else:
        Jugador.imagen_corazones_actual = pygame.image.load("Recursos\Modelos\PNG Objetos\\1 corazones.png")

    Jugador.vida = vida_nivel1
    Jugador.oportunidades_revivir = vidas_restantes_nivel1
    Jugador.puntos = puntos_totales

    plataformas_del_nivel = plataformas_nivel2
    cajas_del_nivel = cajas_nivel2

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

        detectar_colision(Jugador, plataformas_nivel2, cajas_del_nivel, enemigos_nivel2, enemigos_aleatorios, objetos_nivel1, trampas_nivel2)

        Jugador.actualizar_animacion()
        Jugador.perder_vida()

        tiempo_restante -= frames.get_time() / 1000
        if tiempo_restante <= 0:
            tiempo_restante = 0

        
        puntos = Jugador.puntos

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

        for enemigo in enemigos_nivel2:
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

        for trampa in trampas_nivel2:
            trampa.dibujar(PANTALLA)

        if (Jugador.left_rect.colliderect(pygame.Rect(1900, 1013, 1, 1)) or
            Jugador.right_rect.colliderect(pygame.Rect(1900, 1013, 1, 1)) or
            Jugador.top_rect.colliderect(pygame.Rect(1900, 1013, 1, 1)) or
            Jugador.bottom_rect.colliderect(pygame.Rect(1900, 1013, 1, 1))):
            print("j")
            guardar_puntos_nivel(Jugador.puntos, Jugador, puntos_totales)
            nivel_3(tiempo_total, puntos_totales)
            nivel = False  

        dibujar_banner(PANTALLA)
        Jugador.dibujar(PANTALLA)
        Jugador.mostrar_vida(PANTALLA)
        mostrar_puntos(PANTALLA, Jugador.puntos, tiempo_restante, Jugador.oportunidades_revivir)
        pygame.display.flip()
