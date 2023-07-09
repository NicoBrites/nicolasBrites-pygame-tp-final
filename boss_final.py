import pygame
from constantes import *
from configuraciones import *
from auxiliar import Auxiliar
from proyectiles import *
from proyectiles_lvl3 import *
from proyectiles_final_map import *
from gui_progressbar import ProgressBar

class Boss:
    def __init__(self,x,y,speed_walk, speed_run,gravity,frame_rate_ms,move_rate_ms,tipe=0) -> None:
        self.tipe = tipe
        
        self.walk_l = reescalar_imagen(boss_final_walk_l,(1152,640)) 
        self.walk_r = reescalar_imagen(boss_final_walk_r, (1152,640))
        self.idle_l = reescalar_imagen(boss_final_idle_l,(1152,640))
        self.atack_l = reescalar_imagen(boss_final_atack_l,(1152,640))
        self.atack_r = reescalar_imagen(boss_final_atack_r, (1152,640))

        self.die = reescalar_imagen(boss_final_death_l, (1152,640))

        self.lives = 5

        self.frame = 0
        self.animation = self.idle_l
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
    
        self.rect.x = x
        self.rect.y = y

        
        self.exploto = False
        self.tiempo_explotado = 0

        self.move_x = 0
        self.move_y = 0
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.gravity = gravity

        self.tiempo_ultimo_pos = 0
        self.contador = 0

        self.frame_rate_ms = frame_rate_ms
        self.tiempo_transcurrido_move = move_rate_ms
        self.tiempo_transcurrido_animation = 0

        self.rect_hit_collition = pygame.Rect(self.rect.x + 450 , self.rect.y + 220  , self.rect.w -900  , self.rect.h - 200 )
        self.rect_hit_collition_atack_l = pygame.Rect(self.rect.x - 100 , self.rect.y + 500  , self.rect.w -900  , self.rect.h - 500 )
        self.rect_hit_collition_atack_r = pygame.Rect(self.rect.x + 800 , self.rect.y + 500  , self.rect.w -900  , self.rect.h - 500 )

      


    def do_movement(self, delta_ms,bullet_list):
   
        self.tiempo_transcurrido_move += delta_ms
        if self.animation != self.die:
            if self.tiempo_transcurrido_move >= self.frame_rate_ms:
                self.tiempo_transcurrido_move = 0
                self.add_x(self.move_x)
            if self.contador <= 180:
                self.move_x = -self.speed_walk
                self.animation = self.walk_l
                self.contador +=1

            elif self.contador == 250:   
                bullet_list.append(self.crear_proyectil(delta_ms,DIRECTION_L))
                bullet_list.append(self.crear_proyectil(delta_ms,DIRECTION_L,1))
                bullet_list.append(self.crear_proyectil(delta_ms,DIRECTION_L,2))
                self.contador +=1
            elif self.contador < 250:
                self.move_x = 0
                self.animation = self.atack_l
            
                self.contador +=1
            elif self.contador <= 430:
                self.move_x = self.speed_walk
                self.animation = self.walk_r
                self.contador +=1

            elif self.contador == 500:   
                bullet_list.append(self.crear_proyectil(delta_ms,DIRECTION_R))
                bullet_list.append(self.crear_proyectil(delta_ms,DIRECTION_R,1))
                bullet_list.append(self.crear_proyectil(delta_ms,DIRECTION_R,2))    
                self.contador +=1
            elif self.contador < 500:
                self.move_x = 0
                self.animation = self.atack_r
                self.contador +=1
            else:
                self.contador = 0
                self.frame = 0

        
    def add_x(self,delta_x):
        self.rect.x += delta_x
        self.rect_hit_collition.x +=delta_x

    def do_animation(self, delta_ms):

        self.tiempo_transcurrido_animation += delta_ms
        if self.animation != self.die:
            if (self.tiempo_transcurrido_animation >=self.frame_rate_ms ):
                self.tiempo_transcurrido_animation = 0
                if (self.frame < len(self.animation) -1):
                    self.frame += 1
                else:
                    self.frame = 0  
        else:
            if (self.tiempo_transcurrido_animation >=self.frame_rate_ms*1.7 ):
                self.tiempo_transcurrido_animation = 0
                if (self.frame < len(self.animation) -1):
                   
                    self.frame += 1
                else:
                    self.frame = 0

    def is_explosion(self,delta_ms):
        if self.animation == self.die:
            self.tiempo_explotado += delta_ms
        print(self.tiempo_explotado)
        if self.tiempo_explotado >= 2000:
            self.exploto = True


    def crear_proyectil(self,ms,direction,type=0):
        if type == 0:
            proyectil = Proyectiles_lvl3(x = self.rect_hit_collition.centerx ,y= self.rect_hit_collition.centery ,speed_proyectil=15,direction=direction,ms=ms)
            self.proyectil_creado = True
            return proyectil
        if type == 1:
            proyectil = Proyectiles_lvl3(x = self.rect_hit_collition.centerx ,y= self.rect_hit_collition.centery -100 ,speed_proyectil=15,direction=direction,ms=ms)
            self.proyectil_creado = True
            return proyectil
        if type == 2:
            proyectil = Proyectiles_lvl3(x = self.rect_hit_collition.centerx ,y= self.rect_hit_collition.centery +100 ,speed_proyectil=15,direction=direction,ms=ms)
            self.proyectil_creado = True
            return proyectil
    

    def update(self, delta_ms,bullet_list):
        if self.animation == self.die:
            self.is_explosion(delta_ms)
        else:
            if self.animation != self.die:
                self.do_movement(delta_ms,bullet_list)
        self.do_animation(delta_ms)


    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect)
            pygame.draw.rect(screen,GREEN,self.rect_hit_collition)
            if (self.animation == self.atack_l ) and (self.frame> 8 and self.frame<12) :
                pygame.draw.rect(screen,BLUE,self.rect_hit_collition_atack_l)
            if (self.animation == self.atack_r ) and (self.frame> 8 and self.frame<12) :    
                pygame.draw.rect(screen,BLUE,self.rect_hit_collition_atack_r)
        try:
            self.image = self.animation[self.frame]
        except IndexError as e:
            print("Crasheo : {0}".format(e))
            self.image = self.animation[0]

            
        screen.blit(self.image,self.rect)