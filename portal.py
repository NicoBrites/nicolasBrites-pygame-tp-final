import pygame
from constantes import *
from configuraciones import *



class Portal:
    def __init__(self,x,y,w,h,frame_rate_ms,type=0) -> None:
        self.portal = reescalar_imagen(portal,(w,h))
 

        self.frame = 0
        self.animation = self.portal
        self.image = self.animation[self.frame]
        self.frame_rate_ms = frame_rate_ms
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, GROUND_RECT_H)

        self.tiempo_transcurrido_animation = 0

    def update(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
       
        if (self.tiempo_transcurrido_animation >=self.frame_rate_ms ):
            if (self.frame < len(self.animation) - 1):
                self.frame += 1
            else:
                self.frame = 0


    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect) 
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,GREEN,self.rect_ground_collition)   
    
    

