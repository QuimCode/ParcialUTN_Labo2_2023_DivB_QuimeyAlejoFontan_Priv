import pygame

from class_plataforma import plataformas_nivel1
from class_enemigo import Enemigo
from parametros_visual import *

class EnemigoBoss(Enemigo):
    def __init__(self, x, y, width, height, coordenada_inicial, coordenada_final, velocidad):
        super().__init__(x, y, width, height, coordenada_inicial, coordenada_final, velocidad)
        self.vida = 100
        self.tiempo_entre_danos = 1000
        self.ultimo_dano = pygame.time.get_ticks()

        self.actualizar_hitbox()

    def actualizar_hitbox(self):
        hitbox_width = 0.44 * self.width
        hitbox_height = 0.7 * self.height

        #Hitbox
        self.left_rect = pygame.Rect(self.x + 25, self.y + (self.height - hitbox_height) / 2, 8, hitbox_height)
        self.right_rect = pygame.Rect(self.x + self.width - 25, self.y + (self.height - hitbox_height) / 2, 8, hitbox_height)
        self.top_rect = pygame.Rect(self.x + 30, self.y + 15, hitbox_width, 10)
        self.bottom_rect = pygame.Rect(self.x + 30, self.y + self.height - 20, hitbox_width, 5)

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
        # pygame.draw.rect(pantalla, (255, 0, 0), self.left_rect, 2)
        # pygame.draw.rect(pantalla, (255, 0, 0), self.right_rect, 2)
        # pygame.draw.rect(pantalla, (255, 0, 0), self.top_rect, 2)
        # pygame.draw.rect(pantalla, (255, 0, 0), self.bottom_rect, 2)
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

        self.detectar_colision_plataformas(plataformas_nivel1)

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

    def recibir_dano(self):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.ultimo_dano >= self.tiempo_entre_danos:
            self.vida -= self.dano_enemigo
            self.ultimo_dano = tiempo_actual
            if self.vida <= 0:
                if self.oportunidades_revivir > 0:
                    self.vida = 100  # Vida inicial
                    self.oportunidades_revivir -= 1
                else:
                    self.vida = 0

    def eliminacion_de_enemigo(self):
        self.activo = False
        self.eliminado = True
        self.top_rect = pygame.Rect(0, 0, 0, 0)
        self.right_rect = pygame.Rect(0, 0, 0, 0)
        self.left_rect = pygame.Rect(0, 0, 0, 0)
        self.bottom_rect = pygame.Rect(0, 0, 0, 0)

