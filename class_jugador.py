import pygame
from parametros_visual import *

class Personaje:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocidad = 5
        self.en_suelo = True
        self.velocidad_y = 0
        self.gravedad = 0.8
        self.saltando = False

        self.imagen_corazones_actual = pygame.image.load("Recursos\Modelos\PNG Objetos\\4 corazones.png")

        self.imagen = self.obtener_imagen_animacion_quieto()[0]
        self.imagenes_quieto = self.obtener_imagen_animacion_quieto()
        self.imagenes_quieto_inverso = self.obtener_imagen_animacion_quieto_inverso()
        self.imagenes_derecha = self.obtener_imagen_animacion_derecha()
        self.imagenes_izquierda = self.obtener_imagen_animacion_izquierda()
        self.indice_animacion = 0
        self.contador_animacion = 0
        self.ultimo_movimiento_derecha = True
        self.movimiento_derecha = False
        self.movimiento_izquierda = False
        self.movimiento_quieto = True

        self.puntos = 0
        self.vida = 100
        self.vida += 25
        self.dano_enemigo = 25
        self.oportunidades_revivir = 3
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

    def obtener_imagen_animacion_derecha(self):
        return [
            pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Corriendo\\run cycle 48x48.png"), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Corriendo\\run cycle 48x49.png"), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Corriendo\\run cycle 48x50.png"), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Corriendo\\run cycle 48x51.png"), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Corriendo\\run cycle 48x52.png"), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Corriendo\\run cycle 48x53.png"), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Corriendo\\run cycle 48x54.png"), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Corriendo\\run cycle 48x55.png"), (self.width, self.height))
        ]

    def obtener_imagen_animacion_izquierda(self):
        return [pygame.transform.flip(img, True, False) for img in self.imagenes_derecha]

    def obtener_imagen_animacion_quieto(self):
        return [
            pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x48.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x48.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x49.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x50.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x51.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x52.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x53.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x54.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x55.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x56.png'), (self.width, self.height)),
            pygame.transform.scale(pygame.image.load('Recursos/Modelos/PNG Respiracion/Character Idle Rig 48x57.png'), (self.width, self.height))
        ]

    def obtener_imagen_animacion_quieto_inverso(self):
        return [pygame.transform.flip(img, True, False) for img in self.imagenes_quieto]

    def obtener_imagen_ascendente(self):
        return pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Salto\player jump 48x48.png"), (self.width, self.height))

    def obtener_imagen_descendente(self):
        return pygame.transform.scale(pygame.image.load("Recursos\Modelos\PNG Salto\player jump 48x50.png"), (self.width, self.height))

    def actualizar_animacion(self):
        self.contador_animacion += 1
        if self.contador_animacion >= VELOCIDAD_ANIMACION:
            self.contador_animacion = 0
            self.indice_animacion += 1
            
            if self.movimiento_derecha:
                animaciones = self.obtener_imagen_animacion_derecha()
            elif self.movimiento_izquierda:
                animaciones = self.obtener_imagen_animacion_izquierda()
            else:
                if self.ultimo_movimiento_derecha:
                    animaciones = self.obtener_imagen_animacion_quieto()
                else:
                    animaciones = self.obtener_imagen_animacion_quieto_inverso()

            if self.saltando:
                    if self.velocidad_y > 0:
                        self.imagen = self.obtener_imagen_ascendente()
                    else:
                        self.imagen = self.obtener_imagen_descendente()
                    return  # Salir del método para evitar la animación durante el salto

            if self.indice_animacion >= len(animaciones):
                self.indice_animacion = 0

            self.imagen = animaciones[self.indice_animacion]

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
            self.saltando = False
            self.en_suelo = True  # Agregar esta línea

    def aplicar_gravedad(self):
        if self.velocidad_y > 0:
            self.y -= self.velocidad_y
            self.velocidad_y -= self.gravedad

            if self.velocidad_y < 0:
                self.velocidad_y = 0

    def mover(self, teclas):
        if teclas[pygame.K_a]:
            self.x -= self.velocidad
            self.movimiento_izquierda = True
            self.movimiento_derecha = False
            self.movimiento_quieto = False
            self.ultimo_movimiento_derecha = False  

        elif teclas[pygame.K_d]:
            self.x += self.velocidad
            self.movimiento_izquierda = False
            self.movimiento_derecha = True
            self.movimiento_quieto = False
            self.ultimo_movimiento_derecha = True

        else:
            self.movimiento_izquierda = False
            self.movimiento_derecha = False
            self.movimiento_quieto = True

        if not self.saltando and teclas[pygame.K_w]:
            if self.saltando:
                if self.velocidad_y > 0:
                    self.imagen = self.obtener_imagen_ascendente()
                else:
                    self.imagen = self.obtener_imagen_descendente()
            self.saltando = True
            self.velocidad_y = 15

        # if self.y < enemigo.y + enemigo.height and self.velocidad_y < 0:
        #     if self.hitbox.colliderect(enemigo.hitbox):
        #         enemigo.recibir_dano(25)

        self.actualizar_hitbox()
        self.actualizar_animacion()

    def mostrar_vida(self, pantalla):
        nueva_imagen_corazones = pygame.transform.scale(self.imagen_corazones_actual, (160, 50)) 
        pantalla.blit(nueva_imagen_corazones, (10, 30))

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

        if self.vida >= 100:
            self.imagen_corazones_actual = pygame.image.load("Recursos\Modelos\PNG Objetos\\4 corazones.png")
        elif self.vida >= 75:
            self.imagen_corazones_actual = pygame.image.load("Recursos\Modelos\PNG Objetos\\3 corazones.png")
        elif self.vida >= 50:
            self.imagen_corazones_actual = pygame.image.load("Recursos\Modelos\PNG Objetos\\2 corazones.png")
        elif self.vida >= 25:
            self.imagen_corazones_actual = pygame.image.load("Recursos\Modelos\PNG Objetos\\1 corazones.png")
        else:
            self.imagen_corazones_actual = pygame.image.load("Recursos\Modelos\PNG Objetos\muerto.png")

    def perder_vida(self):
        if self.vida <= 0:
            if self.oportunidades_revivir > 0:
                self.x = 10  # Posición x inicial
                self.y = 850  # Posición y inicial
                self.vida = 100  # Vida inicial
                self.oportunidades_revivir -= 1

    def ganar_vida(self):
        self.vida += 25
