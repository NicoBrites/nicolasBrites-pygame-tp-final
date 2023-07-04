import pygame
from constantes import *
from configuraciones import *
from auxiliar import Auxiliar

#METODO LECTOR JSON CON PLATAFORMAS Y DEMAS

class Botin:
    def __init__(self,x,y,w,h,type=0) -> None:
        self.image = pygame.transform.scale(pygame.image.load(r"JUEGO_ON\images\BOTIN\gem_ruby__x1_1_png_1354831652.png"),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, GROUND_RECT_H)


    def draw(self,screen,):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect)        
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,GREEN,self.rect_ground_collition)   

class Comidita(Botin):
    def __init__(self, x, y, w, h, type=0) -> None:
        super().__init__(x, y, w, h, type) 
        self.image =  pygame.transform.scale(pygame.image.load(r"JUEGO_ON\images\BOTIN\cold_taco__x1_iconic_png_1354830854.png"),(w,h))


class Llave(Botin):
    def __init__(self, x, y, w, h, type=0) -> None:
        super().__init__(x, y, w, h, type) 
        self.image = pygame.transform.scale(pygame.image.load(r"JUEGO_ON\images\BOTIN\llavesita.png"),(w,h))


class Escalerita(Botin):
    def __init__(self, x, y, w, h, type=0) -> None:
        super().__init__(x, y, w, h, type) 
        self.image =  pygame.transform.scale(pygame.image.load(r"JUEGO_ON\images\BOTIN\escalera.png"),(w,h))


class Console(Botin):
    def __init__(self, x, y, w, h, type=0) -> None:
        super().__init__(x, y, w, h, type) 
        self.image =  pygame.transform.scale(pygame.image.load(r"JUEGO_ON\images\lvl2\consola\console.png"),(w,h))


class Portal:
    def __init__(self,x,y,w,h,type=0) -> None:
        self.image = pygame.transform.scale(pygame.image.load(r"JUEGO_ON\images\BOTIN\gem_ruby__x1_1_png_1354831652.png"),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, GROUND_RECT_H)

        self.frame = 0
        self.animation = self.image
        self.image = self.animation[self.frame]

    def do_animation(self, delta_ms):

        self.tiempo_transcurrido_animation += delta_ms
       
        if (self.tiempo_transcurrido_animation >=self.frame_rate_ms ):
            self.tiempo_transcurrido_animation = 0
            if (self.frame < len(self.animation) -1):
                self.frame += 1
            else:
                self.frame = 0  

    def update(self, delta_ms):
        self.do_animation( delta_ms)

    def draw(self,screen,):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect)        
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,GREEN,self.rect_ground_collition)   
    
    

