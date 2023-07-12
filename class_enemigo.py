import pygame
import random

from parametros_visual import *
from class_plataforma import plataformas_nivel1
from class_caja import cajas_nivel1

class Enemigo:
    def __init__(self, x, y, width, height, coordenada_inicial, coordenada_final, velocidad):
        self.rect = pygame.Rect(x, y, width, height)
        self.hitbox = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocidad = 0 
        self.velocidad_y = 0
        self.gravedad = 0.1
        self.cayendo = True
        self.en_suelo = False
        self.en_plataforma = True

        self.solido = True 
        self.visible = True
        self.activo = True

        self.coordenada_inicial = coordenada_inicial
        self.coordenada_final = coordenada_final
        self.velocidad = velocidad
        self.direccion = 1

        self.imagenes_derecha = self.obtener_imagen_animacion_derecha()
        self.imagenes_izquierda = self.obtener_imagen_animacion_izquierda()
        self.indice_animacion = 0
        self.contador_animacion = 0

        self.actualizar_hitbox()
        self.actualizar_imagen()

    def obtener_imagen_animacion_derecha(self):
        return [
            pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Enemigo Caminando\Walk1.png"), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Enemigo Caminando\Walk2.png"), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Enemigo Caminando\Walk2.png"), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Enemigo Caminando\Walk2.png"), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Enemigo Caminando\Walk3.png"), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Enemigo Caminando\Walk4.png"), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Enemigo Caminando\Walk1.png"), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Enemigo Caminando\Walk2.png"), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Enemigo Caminando\Walk2.png"), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Enemigo Caminando\Walk2.png"), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Enemigo Caminando\Walk3.png"), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Enemigo Caminando\Walk4.png"), (self.width, self.height))
        ]
    
    def obtener_imagen_animacion_izquierda(self):
        return [pygame.transform.flip(img, True, False) for img in self.imagenes_derecha]

    def actualizar_hitbox(self):
        hitbox_width = 0.44 * self.width
        hitbox_height = 0.7 * self.height

        self.left_rect = pygame.Rect(self.x + 25, self.y + (self.height - hitbox_height) / 2, 8, hitbox_height)
        self.right_rect = pygame.Rect(self.x + self.width - 25, self.y + (self.height - hitbox_height) / 2, 8, hitbox_height)
        self.top_rect = pygame.Rect(self.x + 30, self.y + 12, hitbox_width, 8)
        self.bottom_rect = pygame.Rect(self.x + 30, self.y + self.height - 12, hitbox_width, 10)

    def actualizar_imagen(self):
        self.contador_animacion += 1
        if self.contador_animacion >= VELOCIDAD_ANIMACION_ENEMIGOS:
            self.contador_animacion = 0
            self.indice_animacion += 1

        if self.direccion == 1:
            self.imagenes_actuales = self.imagenes_derecha  # Usar imágenes de caminata hacia la derecha
        else:
            self.imagenes_actuales = self.imagenes_izquierda  # Usar imágenes de caminata hacia la izquierda

        self.indice_animacion += 1
        if self.indice_animacion >= len(self.imagenes_actuales):
            self.indice_animacion = 0

        self.imagen = self.imagenes_actuales[self.indice_animacion]

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, (255, 0, 0), self.left_rect, 2)
        pygame.draw.rect(pantalla, (255, 0, 0), self.right_rect, 2)
        pygame.draw.rect(pantalla, (255, 0, 0), self.top_rect, 2)
        pygame.draw.rect(pantalla, (255, 0, 0), self.bottom_rect, 2)
        pantalla.blit(self.imagen, (self.x, self.y))

    def limites(self):
        if self.x < 0:
            self.x = 0
        elif self.x > ANCHO - self.width:
            self.x = ANCHO - self.width

        if self.y < 0:
            self.y = 0
            self.velocidad_y = 0
        elif self.y > ALTO - self.height:
            self.y = ALTO - self.height
            self.cayendo = False
            self.en_suelo = True

    def aplicar_gravedad(self):
        if not self.en_suelo and self.cayendo and not self.en_plataforma: 
            self.y += self.velocidad_y
            self.velocidad_y += self.gravedad

    def mover(self):
        if not self.cayendo:
            self.cayendo = True
            self.velocidad_y = 0  # Reiniciamos la velocidad en el eje y
            self.en_plataforma = False

        self.detectar_colision_plataformas(plataformas_nivel1, cajas_nivel1)

        if not self.en_plataforma:
            self.aplicar_gravedad()

        self.x += self.direccion * self.velocidad

        if self.direccion == 1 and self.x >= self.coordenada_final:
            self.x = self.coordenada_final
            self.direccion = -1
        elif self.direccion == -1 and self.x <= self.coordenada_inicial:
            self.x = self.coordenada_inicial
            self.direccion = 1

        self.actualizar_hitbox()
        self.actualizar_imagen()

    def detectar_colision_plataformas(self, plataformas, cajas):
        for plataforma in plataformas:
            if self.bottom_rect.colliderect(plataforma.top_rect):
                self.velocidad_y = 0
                self.cayendo = False
                self.en_plataforma = True

        for caja in cajas:
            if self.bottom_rect.colliderect(caja.top_rect):
                self.velocidad_y = 0
                self.cayendo = False
                self.en_plataforma = True
            else:
                self.en_plataforma = False

            if self.right_rect.colliderect(caja.left_rect):
                self.x -= self.velocidad
                self.direccion *= -1

            if self.left_rect.colliderect(caja.right_rect):
                self.x += self.velocidad
                self.direccion *= -1

    def eliminacion_de_enemigo(self):
        self.activo = False
        self.eliminado = True
        self.top_rect = pygame.Rect(0, 0, 0, 0)
        self.right_rect = pygame.Rect(0, 0, 0, 0)
        self.left_rect = pygame.Rect(0, 0, 0, 0)
        self.bottom_rect = pygame.Rect(0, 0, 0, 0)

    @staticmethod
    def generar_enemigo_aleatorio(width, height):
        x = random.randint(560, 1100 - width)  # Coordenada x aleatoria
        y = 100  # Coordenada y aleatoria
        coordenada_inicial = random.randint(0, ANCHO)
        coordenada_final = random.randint(coordenada_inicial, ANCHO)
        velocidad = random.randint(2, 4)

        return Enemigo(x, y, width, height, coordenada_inicial, coordenada_final, velocidad)



enemigos_nivel1 = [Enemigo(1500, 1010, 90, 90, 1500, 1750, 3),
                    Enemigo(1000, 1010, 90, 90, 810, 1420, 3),
                    Enemigo(465, 1010, 90, 90, 465, 920, 3),
                    Enemigo(1860, 300, 90, 90, 1390, 1620, 3),
                    Enemigo(342, 304, 90, 90, 342, 1620, 3),
                    Enemigo(940, 0, 90, 90, 810, 1030, 3),
                    Enemigo(0, 455, 90, 90, 0, 265, 3)
]

enemigos_nivel2 = [Enemigo(1500, 1010, 90, 90, 1500, 1750, 4),
                    Enemigo(1000, 1010, 90, 90, 810, 1420, 4),
                    Enemigo(465, 1010, 90, 90, 465, 920, 4),
                    Enemigo(1860, 300, 90, 90, 1390, 1620, 4),
                    Enemigo(0, 455, 90, 90, 0, 265, 4)
]
