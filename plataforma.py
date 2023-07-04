import pygame
from constantes import *
from configuraciones import *
from auxiliar import Auxiliar

#METODO LECTOR JSON CON PLATAFORMAS Y DEMAS

class Platform:
    def __init__(self,x,y,w,h,type=0) -> None:
        self.image = pygame.transform.scale(pygame.image.load(r"JUEGO_ON\images\Plataformas\0.png"),(w,h))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, GROUND_RECT_H)


    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect)        
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,GREEN,self.rect_ground_collition)  

class Techito(Platform):  
    def __init__(self,x,y,w,h,type=0) -> None:
        super().__init__(x,y,w,h,type=0)
        self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load(r"JUEGO_ON\images\Plataformas\techito\0.png"),(w,h)),False,True)
        self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y+64, self.rect.w, GROUND_RECT_H)
    
    def draw(self,screen):
        pass

class Parecita(Platform):
    def __init__(self, x, y, w, h, type=0) -> None:
        super().__init__(x, y, w, h, type)
        self.image = pygame.transform.scale(pygame.image.load(r"JUEGO_ON\images\Plataformas\parecita\0.png"),(w,h))
        self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y+64, self.rect.w, GROUND_RECT_H)

class Plataforma_lvl2(Platform):
    def __init__(self, x, y, w, h, type=0) -> None:
        super().__init__(x, y, w, h, type)
        self.image = pygame.transform.scale(pygame.image.load(r"JUEGO_ON\images\lvl2\lvl2_tiles\plataforma.png"),(w,h))
        self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, GROUND_RECT_H)

class Piso_lvl2(Platform):
    def __init__(self, x, y, w, h, type=0) -> None:
        super().__init__(x, y, w, h, type)
        self.image = pygame.transform.scale(pygame.image.load(r"JUEGO_ON\images\lvl2\lvl2_tiles\0.png"),(w,h))
        self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, GROUND_RECT_H)

class Plataforma_lvl2_dinamica(Platform):
    def __init__(self, x, y, w, h, type=0) -> None:
        super().__init__(x, y, w, h, type)
        self.image = pygame.transform.scale(pygame.image.load(r"JUEGO_ON\images\lvl2\lvl2_tiles\plataforma.png"),(w,h))
        self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y+5, self.rect.w, GROUND_RECT_H)

        self.tiempo_transcurrido_move = 0
        self.frame_rate_ms = 50
        self.move_x = 0
        self.move_x_l = -10
        self.move_x_r = 10
        self.contador = 0
        self.direction = DIRECTION_L
        
    
    def do_movement(self, delta_ms):
        self.tiempo_transcurrido_move += delta_ms

        if self.tiempo_transcurrido_move >= self.frame_rate_ms:
            self.tiempo_transcurrido_move = 0
            self.add_x(self.move_x)
        if self.contador <= 180:
            self.move_x = self.move_x_l
            self.contador +=1
            self.direction = DIRECTION_L
        elif self.contador <= 200:
            self.move_x = 0
            self.contador +=1
            self.direction = ""
        elif self.contador <= 380:
            self.move_x = self.move_x_r
            self.contador +=1
            self.direction = DIRECTION_R
        elif self.contador <= 400:
            self.move_x = 0
            self.contador +=1
            self.direction = ""
        else:
            self.contador = 0

    def add_x(self,delta_x):
        self.rect.x += delta_x
        self.rect_ground_collition.x +=delta_x

class Plataforma_lvl2_dinamica_y(Platform):
    def __init__(self, x, y, w, h, type=0) -> None:
        super().__init__(x, y, w, h, type)
        self.image = pygame.transform.scale(pygame.image.load(r"JUEGO_ON\images\lvl2\lvl2_tiles\plataforma.png"),(w,h))
        self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y+5, self.rect.w, GROUND_RECT_H)

        self.tiempo_transcurrido_move = 0
        self.frame_rate_ms = 50
        self.move_y = 0
        self.move_y_l = -10
        self.move_y_r = 10
        self.contador = 0
        self.direction = DIRECTION_L
        
    
    def do_movement(self, delta_ms):
        self.tiempo_transcurrido_move += delta_ms

        if self.tiempo_transcurrido_move >= self.frame_rate_ms:
            self.tiempo_transcurrido_move = 0
            self.add_y(self.move_y)
        if self.contador <= 180:
            self.move_y = self.move_y_l
            self.contador +=1
            self.direction = DIRECTION_L
        elif self.contador <= 200:
            self.move_y = 0
            self.contador +=1
            self.direction = ""
        elif self.contador <= 380:
            self.move_y = self.move_y_r
            self.contador +=1
            self.direction = DIRECTION_R
        elif self.contador <= 400:
            self.move_y = 0
            self.contador +=1
            self.direction = ""
        else:
            self.contador = 0

    def add_y(self,delta_y):
        self.rect.y += delta_y
        self.rect_ground_collition.y +=delta_y


    
         


