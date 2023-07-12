import pygame

class Cura:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.activo = True
        self.eliminado = False
        self.color = (0, 255, 0)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.actualizar_hitbox()

    def actualizar_hitbox(self):
        hitbox_width = 0.93 * self.width
        hitbox_height = 1 * self.height

        #Hitbox
        self.left_rect = pygame.Rect(self.x - 4, self.y + (self.height - hitbox_height) / 2, 5, hitbox_height)
        self.right_rect = pygame.Rect(self.x + self.width - 2, self.y + (self.height - hitbox_height) / 2, 5, hitbox_height)
        self.top_rect = pygame.Rect(self.x + 0, self.y - 3, hitbox_width, 5)
        self.bottom_rect = pygame.Rect(self.x + 0, self.y + self.height + 0, hitbox_width, 5)

    def eliminacion_de_cura(self):
        self.activo = False
        self.eliminado = True
        self.top_rect = pygame.Rect(0, 0, 0, 0)
        self.right_rect = pygame.Rect(0, 0, 0, 0)
        self.left_rect = pygame.Rect(0, 0, 0, 0)
        self.bottom_rect = pygame.Rect(0, 0, 0, 0)

    def dibujar(self, pantalla):
        if self.activo:
            pygame.draw.rect(pantalla, self.color, self.rect)

objetos_nivel1 = [Cura(1500, 1010, 90, 90),
                    Cura(1000, 1010, 90, 90)
]
