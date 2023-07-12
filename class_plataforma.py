import pygame
from parametros_visual import *

class Plataforma:
    def __init__(self, x, y, width, height, image_path, movil=False, coordenada_inicial=None, coordenada_final=None, velocidad=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.movil = movil  # Indica si la plataforma es móvil
        self.coordenada_inicial = coordenada_inicial
        self.coordenada_final = coordenada_final
        self.velocidad = velocidad
        self.x_actual = x 

        if image_path is not None:
            try:
                self.image = pygame.image.load(image_path)
                self.image = pygame.transform.scale(self.image, (width, height))
            except FileNotFoundError:
                self.image = None
        else:
            self.image = None

        self.actualizar_hitbox()

    def actualizar_hitbox(self):
        hitbox_width = 0.9 * self.width
        hitbox_height = 0.52 * self.height

        self.left_rect = pygame.Rect(self.rect.x + 15, self.rect.y + (self.height - hitbox_height + 21.5) / 2, 2, hitbox_height)
        self.right_rect = pygame.Rect(self.rect.x + self.width - 15, self.rect.y + (self.height - hitbox_height + 21.5) / 2, 2, hitbox_height)
        self.top_rect = pygame.Rect(self.rect.x + 15, self.rect.y + 20, hitbox_width, 10)
        self.bottom_rect = pygame.Rect(self.rect.x + 15, self.rect.y + self.height - 0, hitbox_width, 10)

    def dibujar(self, pantalla):
        if self.image is not None:
            pantalla.blit(self.image, self.rect.topleft)
            pygame.draw.rect(pantalla, (255, 0, 0), self.left_rect, 2)
            pygame.draw.rect(pantalla, (255, 0, 0), self.right_rect, 2)
            pygame.draw.rect(pantalla, (255, 0, 0), self.top_rect, 2)
            pygame.draw.rect(pantalla, (255, 0, 0), self.bottom_rect, 2)
            pygame.draw.rect(pantalla, (0, 0, 255), self.rect, 2)
        else:
            pygame.draw.rect(pantalla, (255, 0, 0), self.rect)

        if self.image is not None:
            pantalla.blit(self.image, self.rect.topleft)

        self.actualizar_hitbox() 

    def mover(self):
        if self.movil:
            self.x_actual += self.velocidad

            if self.x_actual >= self.coordenada_final:
                self.x_actual = self.coordenada_final
                self.velocidad *= -1  # Invertir la velocidad para cambiar la dirección
            elif self.x_actual <= self.coordenada_inicial:
                self.x_actual = self.coordenada_inicial
                self.velocidad *= -1  # Invertir la velocidad para cambiar la dirección

            self.rect.x = self.x_actual
            self.actualizar_hitbox()  # Actualizar todas las hitboxes de la plataforma

        self.actualizar_hitbox() 

# Crear objetos de plataforma
plataformas_nivel1 = [
    # Plataforma(453, 627, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(10, 627, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(440, 900, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(885, 900, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(950, 580, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(490, 627, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(1370, 800, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(1607, 395, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(305, 377, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(810, 313, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    # Plataforma(1077, 173, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(0, ALTO - 10, ANCHO, 10, None)
]

plataformas_nivel2 = [
    # Plataforma(453, 627, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(10, 627, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(440, 900, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png", movil=True, coordenada_inicial=440, coordenada_final=890, velocidad=4),
    # Plataforma(885, 900, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(874, 525, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(421, 627, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(1370, 800, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(1607, 395, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(305, 377, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(810, 313, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    # Plataforma(1077, 173, 300, 40, "Recursos/Super Grotto Escape Files/Props/Sprites/vent-pipes.png"),
    Plataforma(0, ALTO - 10, ANCHO, 10, None)
]
