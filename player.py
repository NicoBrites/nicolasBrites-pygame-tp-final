import pygame
from constantes import *
from configuraciones import *
from auxiliar import Auxiliar
from proyectiles import *
from plataforma import *
from gui_progressbar import *
from proyectiles_lvl2 import *
from boss_final import *
from proyectiles_lvl3 import *

class Player:
    def __init__(self,x,y,speed_walk, speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_heigh,tipe=0) -> None:
        self.tipe = tipe
        if self.tipe == 0:
            self.walk_l = reescalar_imagen(Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_ON\images\BICHITO ESPACIAL\spritesheets\player-run.png",6,1,True),(100,120))
            self.walk_r = reescalar_imagen(Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_ON\images\BICHITO ESPACIAL\spritesheets\player-run.png",6,1),(100,120))
            self.stay_r = reescalar_imagen(Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_ON\images\BICHITO ESPACIAL\spritesheets\player-idle.png",6,1),(100,120))
            self.stay_l = reescalar_imagen(Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_ON\images\BICHITO ESPACIAL\spritesheets\player-idle.png",6,1,True),(100,120))
            self.jump_imagen_l = reescalar_imagen(Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_ON\images\BICHITO ESPACIAL\spritesheets\player_jump3.png",6,1,True),(100,120))
            self.jump_imagen_r = reescalar_imagen(Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_ON\images\BICHITO ESPACIAL\spritesheets\player_jump3.png",6,1),(100,120))

            self.shoot_proyectil_l = reescalar_imagen(Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_ON\images\BICHITO ESPACIAL\spritesheets\bichito_shoot.png",6,1,True),(100,120))
            self.shoot_proyectil_r = reescalar_imagen(Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_ON\images\BICHITO ESPACIAL\spritesheets\bichito_shoot.png",6,1),(100,120))

            self.hurt_l = reescalar_imagen(Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_ON\images\BICHITO ESPACIAL\spritesheets\Player_hurttt.png",6,1,True),(100,120))
            self.hurt_r = reescalar_imagen(Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_ON\images\BICHITO ESPACIAL\spritesheets\Player_hurttt.png",6,1),(100,120))

        if self.tipe == 2:

            self.walk_l = reescalar_imagen(Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_ON\images\BICHITO ESPACIAL\spritesheets\player-run.png",6,1,True),(50,60))
            self.walk_r = reescalar_imagen(Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_ON\images\BICHITO ESPACIAL\spritesheets\player-run.png",6,1),(50,60))
            self.stay_r = reescalar_imagen(Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_ON\images\BICHITO ESPACIAL\spritesheets\player-idle.png",6,1),(50,60))
            self.stay_l = reescalar_imagen(Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_ON\images\BICHITO ESPACIAL\spritesheets\player-idle.png",6,1,True),(50,60))
            self.jump_imagen_l = reescalar_imagen(Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_ON\images\BICHITO ESPACIAL\spritesheets\player_jump3.png",6,1,True),(50,60))
            self.jump_imagen_r = reescalar_imagen(Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_ON\images\BICHITO ESPACIAL\spritesheets\player_jump3.png",6,1),(50,60))

            self.shoot_proyectil_l = reescalar_imagen(Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_ON\images\BICHITO ESPACIAL\spritesheets\bichito_shoot.png",6,1,True),(50,60))
            self.shoot_proyectil_r = reescalar_imagen(Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_ON\images\BICHITO ESPACIAL\spritesheets\bichito_shoot.png",6,1),(50,60))

            self.hurt_l = reescalar_imagen(Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_ON\images\BICHITO ESPACIAL\spritesheets\Player_hurttt.png",6,1,True),(50,60))
            self.hurt_r = reescalar_imagen(Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_ON\images\BICHITO ESPACIAL\spritesheets\Player_hurttt.png",6,1),(50,60))

        self.frame = 0
        self.lives = 5
        self.score = 0

        self.move_x = 0
        self.move_y = 0

        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.gravity = gravity
        self.jump_power = jump_power

        self.animation = self.stay_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.is_jump = False
        self.direction = DIRECTION_R

        self.frame_rate_ms = frame_rate_ms
        self.tiempo_transcurrido_move = move_rate_ms
        self.tiempo_transcurrido_animation = 0

        self.y_start_jump =0
        self.jump_heigh = jump_heigh

        self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w /3, self.rect.y + self.rect.h - GROUND_RECT_H, self.rect.w /3, GROUND_RECT_H)

        self.proyectil_creado = False
        self.colisiono_parecita_l = False
        self.colisiono_parecita_r = False
        self.colisiono_enemigo = False
        self.colisiono_bullet = False
        self.tiempo_hurt = 0
        self.llave = False
        self.escalerita = False

    def walk(self,direction):
        if self.direction != direction or self.animation != self.walk_l and self.animation != self.walk_r:
            self.frame = 0
            self.direction = direction
            if self.animation == self.hurt_l or self.animation == self.hurt_r:
                if direction == DIRECTION_R:
                    self.move_x = self.speed_walk
                    self.animation = self.hurt_r
                else:
                    self.move_x = -self.speed_walk
                    self.animation = self.hurt_l
            else:
                if direction == DIRECTION_R:
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                else:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l
        
    def jump(self,on_off):
        if on_off and self.is_jump == False:
            self.y_start_jump = self.rect.y
            if self.is_under_techito() and self.move_y < 0:
                self.jump_power = 0
                self.move_y =self.gravity
            else:
                if self.direction == DIRECTION_R:
                    self.move_y = -self.jump_power
                    self.animation = self.jump_imagen_r
                    self.move_x = self.speed_run
                else:
                    self.move_y = -self.jump_power
                    self.animation = self.jump_imagen_l
                    self.move_x = -self.speed_run         
            self.frame = 0
            self.is_jump = True
            SONIDO_SALTO.play()
        if on_off == False :
            self.is_jump = False
            self.stay()

    def stay(self):
        if self.animation != self.stay_l and self.animation != self.stay_r:
            if self.direction == DIRECTION_R:
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def shoot(self):
        if self.direction == DIRECTION_R:
            self.animation = self.shoot_proyectil_r 
        else:
            self.animation = self.shoot_proyectil_l

    def is_hurt(self):
        if self.direction == DIRECTION_L:
            self.animation =  self.hurt_l
        else:
            self.animation =  self.hurt_r


    def collisiono_enemigo(self, lista_enemigos,pb_lives):
        collision_detected = False
        for enemigo in lista_enemigos:
            if type(enemigo) == Boss:
                if self.rect.colliderect(enemigo.rect_hit_collition):
                    collision_detected = True
                    break
            elif self.rect.colliderect(enemigo.rect):
                collision_detected = True
                break
        if collision_detected:
            if not self.colisiono_enemigo:
                pb_lives.value -= 1
                self.is_hurt()
                self.lives -=1
                self.colisiono_enemigo = True
        else:
            self.colisiono_enemigo = False
 
        
    def events(self,events,keys,delta_ms,bullet_list):      

        for event in events:
            if event.type == pygame.KEYDOWN:   
                if event.key == pygame.K_z:
                        self.shoot()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_z:
                    SONIDO_DISPARO.play()
                    bullet_list.append(self.crear_proyectil(delta_ms))
 
        if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] :
            self.walk(DIRECTION_L)
        if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.walk(DIRECTION_R)
        if (not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and not keys[pygame.K_SPACE]) :
            self.stay() 
        if  keys[pygame.K_RIGHT] and keys[pygame.K_LEFT] and not keys[pygame.K_SPACE]:
            self.stay() 
        if keys[pygame.K_SPACE]:
            self.jump(True)
        if keys[pygame.K_z]:
            self.shoot()
            SONIDO_DISPARO.play()

   
    def crear_proyectil(self,ms):
        if self.tipe== 0:
            proyectil = Proyectiles(x = self.rect.centerx ,y= self.rect.centery -10 ,speed_proyectil=15,direction = self.direction,ms=ms)
        else:
             proyectil = Proyectiles_lvl2(x = self.rect.centerx ,y= self.rect.centery -10 ,speed_proyectil=15,direction = self.direction,ms=ms)
        self.proyectil_creado = True
        return proyectil

    def do_movement(self, delta_ms,lista_plataformas):
        self.tiempo_transcurrido_move += delta_ms

        if self.tiempo_transcurrido_move >= self.frame_rate_ms:
            if abs(self.y_start_jump) - abs(self.rect.y) > self.jump_heigh and self.is_jump:
                self.move_y = 0
            if self.rect.y <=0 :
                self.jump_power = 0
                self.add_y(self.gravity)
                self.is_jump = True
            self.tiempo_transcurrido_move = 0
            self.add_y(self.move_y)
            if self.animation == self.walk_r and self.rect.x <= 1400 :
                self.add_x(self.move_x)
            elif self.animation == self.walk_l and self.rect.x >= 0:
                 self.add_x(self.move_x)
            else:
                 self.add_x(0)

            if self.is_on_platform(lista_plataformas) ==False:
                self.add_y(self.gravity)
                self.is_jump = True
            elif self.is_jump:
                self.is_jump = False
                self.jump_power = 50
           
    def is_on_platform(self,lista_plataformas):
        retorno = False
        if self.rect.y >= GROUND_LVL:
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if self.rect_ground_collition.colliderect(plataforma.rect_ground_collition):
                    retorno = True
                    break
        return retorno
    
    def is_under_techito(self):
        retorno = False
        if self.rect.y <= 0:
            retorno = True
        return retorno

    def is_collision_parecita(self):
        retorno = False
        if self.rect.x <= 0 :
            retorno = True
            self.colisiono_parecita_l = True    
        if self.rect.x >=1400:
            self.colisiono_parecita_r = True
            retorno = True
        return retorno


    def add_x(self,delta_x):
        self.rect.x += delta_x
        self.rect_ground_collition.x +=delta_x

    def add_y(self,delta_y):
        self.rect.y += delta_y
        self.rect_ground_collition.y +=delta_y


    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animation += delta_ms

        if (self.tiempo_transcurrido_animation >=self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if (self.frame < len(self.animation) - 1):
                self.frame += 1
            else:
                self.frame = 0

    def collisiono_bullet(self, bullet_list,pb_lives):
        collision_detected = False
        for bullet in bullet_list:
            if type(bullet) == Proyectiles_lvl2_mage or type(bullet) == Proyectiles_lvl3 or type(bullet) == Proyectiles_lvl3_final_map:
                if self.rect.colliderect(bullet.rect):
                    collision_detected = True
                    break
        if collision_detected:
            if not self.colisiono_bullet:
                pb_lives.value -= 1
                self.is_hurt()
                self.lives -=1
                self.colisiono_bullet = True
        else:
            self.colisiono_bullet = False

    def update(self, delta_ms,lista_plataformas, lista_enemigos,widget_list, bullet_list):
        self.do_movement(delta_ms,lista_plataformas)
        self.do_animation(delta_ms)
        self.collisiono_enemigo(lista_enemigos,widget_list)
        self.collisiono_bullet(bullet_list,widget_list)

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect)
            pygame.draw.rect(screen,GREEN,self.rect_ground_collition)

        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
