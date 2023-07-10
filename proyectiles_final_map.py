import pygame
from constantes import *
from configuraciones import *
from auxiliar import Auxiliar


class Proyectiles_lvl3_final_map():
    def __init__(self, x, y, speed_proyectil, direction, ms) -> None:

        self.shoot = reescalar_imagen(proyectil_dragonsito, (32, 32))
        self.proyectil_hit = reescalar_imagen(proyectil_hit, (32, 32))

        self.frame = 0

        self.animation = self.shoot
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed_proyectil = speed_proyectil

        self.colisiono = False
        self.tiempo_colision = 0

        self.direction = direction

    def update(self, ms):
        if (self.frame < len(self.animation) - 1):
            self.frame += 1
        else:
            self.frame = 0
        self.rect.y += self.speed_proyectil

    def draw(self, screen):
        if (DEBUG):
            pygame.draw.rect(screen, RED, self.rect)

        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)
