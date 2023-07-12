import pygame

from parametros_visual import *

class Caja:
    def __init__(self, x, y, width, height, image_path):
        self.rect = pygame.Rect(x, y, width, height)
        self.rect = pygame.Rect(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.solido = True 
        
        self.actualizar_hitbox()

    def actualizar_hitbox(self):
        hitbox_width = 0.93 * self.width
        hitbox_height = 1 * self.height

        #Hitbox
        self.left_rect = pygame.Rect(self.x - 4, self.y + (self.height - hitbox_height) / 2, 5, hitbox_height)
        self.right_rect = pygame.Rect(self.x + self.width - 2, self.y + (self.height - hitbox_height) / 2, 5, hitbox_height)
        self.top_rect = pygame.Rect(self.x + 0, self.y - 3, hitbox_width, 5)
        self.bottom_rect = pygame.Rect(self.x + 0, self.y + self.height + 0, hitbox_width, 5)

    def dibujar(self, pantalla):
        # pygame.draw.rect(pantalla, (255, 255, 0), self.left_rect, 2)
        # pygame.draw.rect(pantalla, (255, 255, 0), self.right_rect, 2)
        # pygame.draw.rect(pantalla, (255, 255, 0), self.top_rect, 2)
        # pygame.draw.rect(pantalla, (255, 255, 0), self.bottom_rect, 2)
        pantalla.blit(self.image, self.rect.topleft)
        self.actualizar_hitbox()


cajas_nivel1 = [
    Caja(215, 450, 50, 50, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(40, 480, 50, 50, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(40, 530, 50, 50, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(40, 580, 70, 70, "Recursos\Super Grotto Escape Files\Props\Sprites\\big-crate.png"),
    Caja(315, 1010, 50, 50, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(665, 600, 50, 50, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(545, 350, 50, 50, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(1529, 650, 50, 50, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(690, 880, 50, 50, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(1355, 505, 50, 50, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(1130, 800, 50, 50, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(1720, 770, 50, 50, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(370, 1000, 60, 60, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(375, 945, 55, 55, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(1500, 415, 45, 45, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(1830, 370, 45, 45, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(1105, 850, 70, 70, "Recursos\Super Grotto Escape Files\Props\Sprites\\big-crate.png"),
    Caja(1750, 990, 70, 70, "Recursos\Super Grotto Escape Files\Props\Sprites\\big-crate.png"),

]

cajas_nivel2 = [
    Caja(315, 1010, 50, 50, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(370, 1000, 60, 60, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(375, 945, 55, 55, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(1178, 825, 50, 50, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(1230, 700, 30, 30, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(1230, 730, 40, 40, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(1230, 770, 50, 50, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(1230, 820, 50, 50, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(1230, 870, 60, 60, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(1230, 930, 60, 60, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(1230, 990, 70, 70, "Recursos\Super Grotto Escape Files\Props\Sprites\\big-crate.png"),
    Caja(1300, 990, 70, 70, "Recursos\Super Grotto Escape Files\Props\Sprites\\big-crate.png"),
    Caja(1300, 930, 60, 60, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(1021, 785, 50, 50, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png"),
    Caja(825, 698, 50, 50, "Recursos\Super Grotto Escape Files\Props\Sprites\crate.png")

]
