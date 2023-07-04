from enemigo import *
from configuraciones import *

class Enemigo_calaca_lvl2():
    def __init__(self,x,y,speed_walk, speed_run,gravity,frame_rate_ms,move_rate_ms,type = 0) -> None:
        self.tipe = type
      
        self.frame = 0

        self.walk_l = reescalar_imagen(enemigo_walk_l_lvl2,(74,51)) 
        self.walk_r = reescalar_imagen(enemigo_walk_r_lvl2, (74,51))
        self.idle_l = reescalar_imagen(enemigo_idle_l_lvl2,(74,51))
        self.idle_r = reescalar_imagen(enemigo_idle_r_lvl2, (74,51))
        self.die = reescalar_imagen(Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_ON\images\ENEMIGO_1\explota\big-explosion.png",9,1),(74,51))
        self.animation = self.walk_r
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

        self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w /3, self.rect.y + self.rect.h - GROUND_RECT_H, self.rect.w /3, GROUND_RECT_H)


    def do_movement(self, delta_ms):
   
        self.tiempo_transcurrido_move += delta_ms

        if self.tipe == 0:
            if self.tiempo_transcurrido_move >= self.frame_rate_ms:
                self.tiempo_transcurrido_move = 0
                self.add_x(self.move_x)
            if self.contador <= 180:
                self.move_x = -self.speed_walk
                self.animation = self.walk_l
                self.contador +=1
            elif self.contador <= 200:
                self.move_x = 0
                self.animation = self.idle_l
                self.contador +=1
            elif self.contador <= 380:
                self.move_x = self.speed_walk
                self.animation = self.walk_r
                self.contador +=1
            elif self.contador <= 400:
                self.move_x = 0
                self.animation = self.idle_r
                self.contador +=1
            else:
                self.contador = 0
                self.frame = 0
        if self.tipe == 2:
            if self.tiempo_transcurrido_move >= self.frame_rate_ms:
                self.tiempo_transcurrido_move = 0
                self.add_x(self.move_x)
            if self.contador <= 200:
                self.move_x = -self.speed_walk
                self.animation = self.walk_l
                self.contador +=1
            elif self.contador <= 400:
                self.move_x = self.speed_walk
                self.animation = self.walk_r
                self.contador +=1
            else:
                self.contador = 0
                self.frame = 0
        if self.tipe == 3:
            if self.tiempo_transcurrido_move >= self.frame_rate_ms:
                self.tiempo_transcurrido_move = 0
                self.add_x(self.move_x)
            if self.contador <= 200:
                self.move_x = self.speed_walk
                self.animation = self.walk_r
                self.contador +=1
            elif self.contador <= 400:
                self.move_x = -self.speed_walk
                self.animation = self.walk_l
                self.contador +=1
            else:
                self.contador = 0
                self.frame = 0


    def add_x(self,delta_x):
        self.rect.x += delta_x
        self.rect_ground_collition.x +=delta_x

    def do_animation(self, delta_ms):

        self.tiempo_transcurrido_animation += delta_ms
       
        if (self.tiempo_transcurrido_animation >=self.frame_rate_ms ):
            self.tiempo_transcurrido_animation = 0
            if (self.frame < len(self.animation) -1):
                self.frame += 1
            else:
                self.frame = 0  

    def is_explosion(self,delta_ms):
        if self.animation == self.die:
            self.tiempo_explotado += delta_ms
        if self.tiempo_explotado >= 500:
            self.exploto = True
            self.frame = 0  


    def update(self, delta_ms,bullet_list):
        if self.animation == self.die:
            self.is_explosion(delta_ms)
        else:
            if self.tipe == 1:
                pass
            else:
                self.do_movement(delta_ms)
        self.do_animation(delta_ms)


    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect)
            pygame.draw.rect(screen,GREEN,self.rect_ground_collition)
        try:
            self.image = self.animation[self.frame]
        except IndexError as e:
            print("Crasheo : {0}".format(e))
            self.image = self.animation[0]
            
        screen.blit(self.image,self.rect)
