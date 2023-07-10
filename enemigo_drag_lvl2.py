from configuraciones import *
from auxiliar import *
from proyectiles import *
from proyectiles_lvl2 import *



class Enemigo_drag_lvl2():
    def __init__(self,x,y,frame_rate_ms,move_rate_ms,type = 0) -> None:
        self.type = type
        self.fire_l = reescalar_imagen(enemigo_maguito_shoot,(100,100)) 
        self.idle_l = reescalar_imagen(enemigo_maguito_idle,(100,100)) 

        self.die = reescalar_imagen(Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_ON\images\ENEMIGO_1\explota\big-explosion.png",9,1),(74,51))

        self.frame = 0
        self.exploto = False
        self.tiempo_explotado = 0

        self.proyectil_creado = False

        self.animation = self.idle_l

        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.tiempo_ultimo_pos = 0
        self.contador = 0

        self.frame_rate_ms = frame_rate_ms
        self.tiempo_transcurrido_move = move_rate_ms
        self.tiempo_transcurrido_animation = 0

        self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w /3, self.rect.y + self.rect.h - GROUND_RECT_H, self.rect.w /3, GROUND_RECT_H)

    def do_fire(self, delta_ms,bullet_list):
        self.tiempo_transcurrido_move += delta_ms
        if self.type == 0:
            if self.tiempo_transcurrido_move >= self.frame_rate_ms:
                self.tiempo_transcurrido_move = 0
            if self.contador < 180: 
                self.animation = self.idle_l
                self.contador +=1
            if self.contador == 180:
                bullet_list.append(self.crear_proyectil(delta_ms,DIRECTION_L))
                self.contador +=1
            elif self.contador > 180 and self.contador < 200:
                self.animation = self.fire_l
                self.contador +=1
            elif self.contador <= 200:
                self.animation = self.idle_l
                self.contador +=1
            else:
                self.contador = 0
                self.frame = 0
        else:
            if self.tiempo_transcurrido_move >= self.frame_rate_ms:
                self.tiempo_transcurrido_move = 0
            if self.contador < 150: 
                self.animation = self.idle_l
                self.contador +=1
            if self.contador == 150:
                bullet_list.append(self.crear_proyectil(delta_ms,DIRECTION_L))
                self.contador +=1
            elif self.contador > 150 and self.contador < 200:
                self.animation = self.fire_l
                self.contador +=1
            elif self.contador <= 200:
                self.animation = self.idle_l
                self.contador +=1
            else:
                self.contador = 0
                self.frame = 0
        

    def crear_proyectil(self,ms,direction):
        proyectil = Proyectiles_lvl2_mage(x = self.rect.centerx ,y= self.rect.centery -10 ,speed_proyectil=15,direction=direction,ms=ms)
        self.proyectil_creado = True
        return proyectil
    
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
        self.do_animation(delta_ms)
        self.do_fire(delta_ms,bullet_list)


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