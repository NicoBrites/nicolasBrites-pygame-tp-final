import pygame
from constantes import *
from configuraciones import *


class Proyectiles:
    def __init__(self, x, y, speed_proyectil, direction, ms) -> None:
        self.shoot_r = reescalar_imagen(proyectil_shoot_l, (64, 64))
        self.shoot_l = reescalar_imagen(proyectil_shoot_r, (64, 64))
        self.proyectil_hit = reescalar_imagen(proyectil_hit, (64, 64))

        self.frame = 0

        self.speed_proyectil = speed_proyectil

        self.animation = self.shoot_l
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.colisiono = False
        self.tiempo_colision = 0

        self.direction = direction

    def update(self, ms):
        if self.animation == self.proyectil_hit:
            self.is_explosion(ms)
            if (self.frame < len(self.animation) - 1):
                self.frame += 1
            else:
                self.frame = 0
        else:
            if self.direction == DIRECTION_L:
                if (self.frame < len(self.animation) - 1):
                    self.frame += 1
                else:
                    self.frame = 0
                self.rect.x -= self.speed_proyectil
            else:
                self.animation = self.shoot_r
                if (self.frame < len(self.animation) - 1):
                    self.frame += 1
                else:
                    self.frame = 0
                self.rect.x += self.speed_proyectil

    def is_explosion(self, delta_ms):
        if self.animation == self.proyectil_hit:
            self.tiempo_colision += delta_ms
        print(self.tiempo_colision)
        if self.tiempo_colision >= 500:
            self.colisiono = True
            self.frame = 0

    def draw(self, screen):
        if (DEBUG):
            pygame.draw.rect(screen, RED, self.rect)

        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)

class Proyectiles_lvl2(Proyectiles):
    def __init__(self, x, y, speed_proyectil, direction, ms) -> None:
        super().__init__(x, y, speed_proyectil, direction, ms)

        self.shoot_r = reescalar_imagen(proyectil_shoot_l, (32, 32))
        self.shoot_l = reescalar_imagen(proyectil_shoot_r, (32, 32))
        self.proyectil_hit = reescalar_imagen(proyectil_hit, (32, 32))

        self.animation = self.shoot_l
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
