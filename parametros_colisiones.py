import pygame

pygame.init()

def detectar_colision(personaje, plataformas, cajas, enemigos, enemigos2, curas, trampas):
    colisionando = False
    personaje.velocidad = 5

#PERSONAJE-PLATAFORMAS
    for plataforma in plataformas:
        if personaje.top_rect.colliderect(plataforma.bottom_rect):
            personaje.velocidad_y = 0

        if personaje.bottom_rect.colliderect(plataforma.top_rect):
            colisionando = True
            personaje.saltando = False
            personaje.velocidad_y = -1

        if not personaje.bottom_rect.colliderect(plataforma.top_rect) and personaje.velocidad_y == -1:
            personaje.velocidad_y = 0

        if personaje.right_rect.colliderect(plataforma.left_rect):
            personaje.velocidad = 0

        if personaje.left_rect.colliderect(plataforma.right_rect):
            personaje.velocidad = 0

#PERSONAJE-CAJAS
    for caja in cajas:
        if personaje.top_rect.colliderect(caja.bottom_rect):
            personaje.velocidad_y = 0

        if personaje.bottom_rect.colliderect(caja.top_rect):
            colisionando = True
            personaje.saltando = False
            personaje.velocidad_y = -1

        if not personaje.bottom_rect.colliderect(caja.top_rect) and personaje.velocidad_y == -1:
            personaje.velocidad_y = 0

        if personaje.right_rect.colliderect(caja.left_rect):
            personaje.x -= personaje.velocidad

        if personaje.left_rect.colliderect(caja.right_rect):
            personaje.x += personaje.velocidad

#PERSONAJE-CURAS
    for cura in curas:
        if personaje.bottom_rect.colliderect(cura.top_rect):
            personaje.ganar_vida()
            cura.eliminacion_de_cura()

        if personaje.top_rect.colliderect(cura.bottom_rect):
            personaje.ganar_vida()
            cura.eliminacion_de_cura()

        if personaje.left_rect.colliderect(cura.right_rect):
            personaje.ganar_vida()
            cura.eliminacion_de_cura()

        if personaje.right_rect.colliderect(cura.left_rect):
            personaje.ganar_vida()
            cura.eliminacion_de_cura()

#PERSONAJE-TRAMPAS
    for trampa in trampas:
        if personaje.bottom_rect.colliderect(trampa.top_rect):
            personaje.recibir_dano()
            personaje.perder_vida()

        if personaje.left_rect.colliderect(trampa.right_rect):
            personaje.recibir_dano()
            personaje.perder_vida()

        if personaje.right_rect.colliderect(trampa.left_rect):
            personaje.recibir_dano()
            personaje.perder_vida()


#PERSONAJE-ENEMIGOS
    for enemigo in enemigos:
        if personaje.bottom_rect.colliderect(enemigo.top_rect):
            personaje.puntos += 1
            enemigo.eliminacion_de_enemigo()

        if personaje.left_rect.colliderect(enemigo.right_rect):
            personaje.recibir_dano()
            personaje.perder_vida()

        if personaje.right_rect.colliderect(enemigo.left_rect):
            personaje.recibir_dano()
            personaje.perder_vida()

    for enemigo in enemigos2:
        if personaje.bottom_rect.colliderect(enemigo.top_rect):
            personaje.puntos += 1
            enemigo.eliminacion_de_enemigo()

        if personaje.left_rect.colliderect(enemigo.right_rect):
            personaje.recibir_dano()
            personaje.perder_vida()

        if personaje.right_rect.colliderect(enemigo.left_rect):
            personaje.recibir_dano()
            personaje.perder_vida()

    if not colisionando and personaje.velocidad_y == 0:
        personaje.y += 8
