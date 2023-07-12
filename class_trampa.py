import pygame

from class_caja import Caja

class Trampa(Caja):
    def __init__(self, x, y, width, height, hitbox_width, hitbox_height, image_path):
        super().__init__(x, y, width, height, image_path)
        self.hitbox = pygame.Rect(x, y, hitbox_width, hitbox_height)
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))

    def dibujar(self, pantalla):
        # pygame.draw.rect(pantalla, Colores.ROJO.value, self.hitbox)
        self.actualizar_hitbox()
        pantalla.blit(self.image, self.rect.topleft)

trampas_nivel1 = []

trampas_nivel2 = [
    Trampa(620, 950, 150, 150, 40, 40, "Recursos\Trampas\end\\burning_end_4.png"),
    Trampa(680, 950, 150, 150, 40, 40, "Recursos\Trampas\end\\burning_end_1.png"),
    Trampa(1058, 950, 150, 150, 40, 40, "Recursos\Trampas\end\\burning_end_4.png"),
    Trampa(1164, 950, 150, 150, 40, 40, "Recursos\Trampas\end\\burning_end_1.png"),
    Trampa(455, 950, 150, 150, 40, 40, "Recursos\Trampas\end\\burning_end_4.png"),
    Trampa(881, 950, 150, 150, 40, 40, "Recursos\Trampas\end\\burning_end_1.png"),
    Trampa(995, 950, 150, 150, 40, 40, "Recursos\Trampas\end\\burning_end_4.png"),
    Trampa(520, 950, 150, 150, 40, 40, "Recursos\Trampas\end\\burning_end_4.png"),
    Trampa(1045, 400, 150, 150, 40, 40, "Recursos\Trampas\end\\burning_end_4.png"),
    Trampa(990, 400, 150, 150, 40, 40, "Recursos\Trampas\end\\burning_end_4.png"),
]
