import pygame
import json

from parametros_visual import *

pygame.init()

def crear_archivo_puntos():
    datos_iniciales = []
    
    with open("puntos_por_nivel.json", "w") as archivo:
        json.dump(datos_iniciales, archivo)

def guardar_puntos_nivel(puntos_nivel, jugador, puntos_totales):
    datos_nivel = {
        "nivel": 1,  
        "puntos": puntos_nivel,
        "vida": jugador.vida,
        "vidas_restantes": jugador.oportunidades_revivir
    }

    with open("puntos_por_nivel.json", "r") as archivo:
        datos_existentes = json.load(archivo)

    puntos_totales += puntos_nivel

    datos_nivel["puntos_totales"] = puntos_totales

    datos_existentes.append(datos_nivel)

    with open("puntos_por_nivel.json", "w") as archivo:
        json.dump(datos_existentes, archivo)


crear_archivo_puntos()

def cargar_puntos_totales():
    with open("puntos_por_nivel.json", "r") as archivo:
        datos = json.load(archivo)
        puntos_totales_nivel = 0
        if len(datos) > 0:
            puntos_totales_nivel = datos[-1]["puntos"]
        return puntos_totales_nivel
    
def cargar_vida_y_vidas_restantes():
    with open("puntos_por_nivel.json", "r") as archivo:
        datos = json.load(archivo)
        vida_nivel1 = 100
        vidas_restantes_nivel1 = 3
        for dato in datos:
            if dato["nivel"] == 1:
                vida_nivel1 = dato["vida"]
                vidas_restantes_nivel1 = dato["vidas_restantes"]
                break
        return {
            "vida_nivel1": vida_nivel1,
            "vidas_restantes": vidas_restantes_nivel1
        }

def mostrar_puntos(pantalla, puntos, tiempo_restante, oportunidades_revivir):
    fuente = pygame.font.Font(None, 36)
    texto_puntos = fuente.render("Puntos: " + str(puntos), True, (255, 255, 255))
    texto_tiempo = fuente.render("Tiempo: " + str(tiempo_restante), True, (255, 255, 255))
    texto_vidas_generales = fuente.render("Vidas Generales: " + str(oportunidades_revivir), True, (255, 255, 255))

    pantalla.blit(texto_puntos, (300, 100))
    pantalla.blit(texto_tiempo, (490, 100))
    pantalla.blit(texto_vidas_generales, (10, 100))

def dibujar_banner(pantalla):
    #atributos del banner
    color_banner = (0, 0, 0)
    altura_banner = 150

    pygame.draw.rect(pantalla, color_banner, (0, 0, ANCHO, altura_banner))

