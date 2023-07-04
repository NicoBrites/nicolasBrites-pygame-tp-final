import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from player import Player
from enemigo import Enemigo
from plataforma import *
from background import Background
from botin import *
from textos import *
from configuraciones import *
from enemigo_drag_lvl2 import *
from enemigo_calaca_lvl2 import *
import time
from boss_final import Boss
from proyectiles_lvl3 import *

class FormGameLevel3(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.data = leer_archivo(r"JUEGO_ON\nivel_3.json")
        # --- GUI WIDGET --- 
        self.boton1 = Button(master=self,x=ANCHO_VENTANA-550,y=ALTO_VENTANA-50,w=140,h=50,color_background=None,color_border=None,image_background="JUEGO_ON\images\GUI\BOTOn\Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_pausa_lvl2",text="PAUSA",font="Verdana",font_size=30,font_color=C_WHITE)

        self.pb_lives = ProgressBar(master=self,x=ANCHO_VENTANA-365,y=ALTO_VENTANA-50,w=240,h=50,color_background=None,color_border=None,image_background="JUEGO_ON\images\GUI\BARS\Bar_Background01.png",image_progress="JUEGO_ON\images\GUI\BARS\Bar_Segment05.png",value = 5, value_max=5)
        self.widget_list = [self.pb_lives,self.boton1]

        # --- GAME ELEMNTS --- 

        self.static_background = Background(x=0,y=0,width=w,height=h,path=r"JUEGO_ON\images\lvl3\background\fondito_god_lvl3.png")

        self.player_1 = Player(x=200,y=550,speed_walk=8,speed_run=8,gravity=17,jump_power=50,frame_rate_ms=50,move_rate_ms=50,jump_heigh=200,tipe=2)

        self.boss = Boss(x=300,y=50,speed_walk=4,speed_run=8,gravity=15,frame_rate_ms=50,move_rate_ms=10)

        self.lista_enemigos = []
        self.lista_enemigos.append(self.boss)

        self.lista_plataformas = []
        self.crear_plataformas(self.data)

        self.bullet_list = []

        self.lista_botinex = []
        # self.lista_botinex.append(Botin(1100,190,24,27))
        # self.lista_botinex.append(Botin(200,190,24,27))
        # self.lista_botinex.append(Comidita(10,340,24,27))
        # self.lista_botinex.append(Console(1050,350,48,54))
        
       

        self.lista_textos=[]
        self.lista_textos.append(Score(master_surface=self.surface,x=0,y=ALTO_VENTANA-50,w=2000,h=50,color_background="Black",color_border="White",font="Helvetica",font_size=30,font_color=RED))
        self.lista_textos.append(Lives(master_surface=self.surface,x=ANCHO_VENTANA-100,y=ALTO_VENTANA-50,w=200,h=50,color_background="Black",color_border="White",font="Helvetica",font_size=30,font_color=RED))
        self.lista_textos.append(Timer(master_surface=self.surface,x=ANCHO_VENTANA/2,y=ALTO_VENTANA-50,w=300,h=50,color_background="Black",color_border="White",font="Helvetica",font_size=30,font_color=RED))

        self.lista_portal = []

        self.cronometro = 60
        self.start_time = 0
        self.flag_timer = False

    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def crear_plataformas(self,lista_json:list):
        for objetos in lista_json:
            for clave,valor in objetos.items():
                if clave == "plataformas":
                    for plataformas in valor:                    
                        if plataformas["plataforma"] == "Piso_lvl2":
                            self.lista_plataformas.append(Piso_lvl2(x=plataformas["x"],y=plataformas["y"],w=plataformas["w"],h=plataformas["h"],type=plataformas["type"]))
                        elif plataformas["plataforma"] == "Plataforma_lvl2":
                            self.lista_plataformas.append(Plataforma_lvl2(x=plataformas["x"],y=plataformas["y"],w=plataformas["w"],h=plataformas["h"],type=plataformas["type"]))
                        elif plataformas["plataforma"] == "Plataforma_lvl2_dinamica":
                            self.lista_plataformas.append(Plataforma_lvl2_dinamica(x=plataformas["x"],y=plataformas["y"],w=plataformas["w"],h=plataformas["h"],type=plataformas["type"]))
                        else:
                            self.lista_plataformas.append(Plataforma_lvl2_dinamica_y(x=plataformas["x"],y=plataformas["y"],w=plataformas["w"],h=plataformas["h"],type=plataformas["type"]))

    def update(self,events,keys,delta_ms,evento_1000ms):

        for aux_widget in self.widget_list:
           aux_widget.update(events)
        
       
  
        # for botin in self.lista_botinex:
        #     if self.player_1.rect.colliderect(botin.rect):
        #                 if type(botin)== Console :
        #                     if keys[pygame.K_x]:
        #                         self.player_1.llave = True
        #                 else:
        #                     self.lista_botinex.remove(botin)
        #                     SONIDO_COIN.play()
        #                     if type(botin)== Comidita:
        #                         self.pb_lives.value +=1
        #                         self.player_1.lives +=1
        #                         self.player_1.score +=250
        #                     else:
        #                         self.player_1.score +=1000
        #                     if type(botin)== Escalerita:
        #                         self.player_1.escalerita = True
                               
                                


        # for enemy_element in self.lista_enemigos: # LOGICA ENEMIGOS, COLISION CON EL PROYECTIL
 
        #     enemy_element.update(delta_ms,self.bullet_list)    no descomentar
        #     if self.player_1.proyectil_creado != False :
        #         for bullet in self.bullet_list:
        #             if type(bullet) == Proyectiles_lvl2:
        #                 if bullet.rect.colliderect(enemy_element):
        #                     enemy_element.lives -= 1
        #                     bullet.animation = bullet.proyectil_hit
        #                     if bullet.is_explosion(delta_ms):
        #                         self.bullet_list.remove(bullet)
        #                         self.player_1.proyectil_creado = False
        #                     SONIDO_EXPLOSION.play()

            # if enemy_element.exploto == True:   no descomentar
            #     for bullet in self.bullet_list:
            #         print("exploto prouyectil")
            #         if bullet.animation == bullet.proyectil_hit:
            #             self.bullet_list.remove(bullet)
            #             self.player_1.proyectil_creado = False
            #         SONIDO_EXPLOSION.play()
            #     self.lista_enemigos.remove(enemy_element)
            #     self.player_1.score +=500

        # for bullet in self.bullet_list:
        #     bullet.update(delta_ms)


        for event in events:
            if event.type == evento_1000ms:
                    self.cronometro -= 1
                    
        # if self.player_1.rect.y <= 0:
        #     self.player_1.jump_power = 0
        #     self.player_1.add_y(self.player_1.gravity)
        #     self.player_1.is_jump = True
        
        
       # if self.player_1.proyectil_creado != False :
            # for bullet in self.bullet_list:
            #     if type(bullet) == Proyectiles_lvl2:
            #         if bullet.rect.colliderect(self.boss.rect_hit_collition):
            #             bullet.animation = bullet.proyectil_hit
            #             if bullet.colisiono == True:
            #                 self.boss.lives -= 1
                            # self.bullet_list.remove(bullet)
                            # self.player_1.proyectil_creado = False
                            # SONIDO_EXPLOSION.play()
        
        # if self.boss.lives == 0 and self.boss.exploto == False:
        #     self.boss.animation == self.boss.die


        # for bullet in self.bullet_list:
        #     bullet.update(delta_ms)
        #     if type(bullet) == Proyectiles_lvl2:
        #         if bullet.rect.colliderect(self.boss.rect_hit_collition):
        #             bullet.animation = bullet.proyectil_hit
        #             if bullet.colisiono == True:
        #                 self.boss.lives -= 1  
        #                 if self.boss.lives <= 0:
        #                     print("entre vidas 0")
        #                     self.boss.animation == self.boss.die
        #     if bullet.tiempo_colision >= 500:
        #         self.bullet_list.remove(bullet)
        #         self.player_1.proyectil_creado = False
        #         SONIDO_EXPLOSION.play()

        if len(self.lista_enemigos) > 0:
            for enemy_element in self.lista_enemigos: # LOGICA ENEMIGOS, COLISION CON EL PROYECTIL
                enemy_element.update(delta_ms,self.bullet_list)
                if enemy_element.exploto == True:
                    self.lista_enemigos.remove(enemy_element)

            for bullet in self.bullet_list:
                bullet.update(delta_ms)
                if type(bullet) == Proyectiles_lvl2:
                    if bullet.rect.colliderect(enemy_element.rect_hit_collition):
                        bullet.animation = bullet.proyectil_hit
                        if bullet.colisiono == True:
                            enemy_element.lives -= 1
                            if enemy_element.lives <= 0:
                                enemy_element.frame = 0
                                enemy_element.animation = enemy_element.die
                if bullet.tiempo_colision >= 500 :
                    self.bullet_list.remove(bullet)
                    self.player_1.proyectil_creado = False
                    SONIDO_EXPLOSION.play()         
        #     if enemy_element.exploto == True:
        #         # for bullet in self.bullet_list:
        #         #     print("exploto prouyectil")
        #         #     if bullet.animation == bullet.proyectil_hit:
        #         #         self.bullet_list.remove(bullet)
        #         #         self.player_1.proyectil_creado = False
        #         SONIDO_EXPLOSION.play()
        #         self.lista_enemigos.remove(enemy_element)
        #         self.player_1.score +=500

        # for bullet in self.bullet_list:
        #     bullet.update(delta_ms)
        #     if bullet.tiempo_colision >= 500:
        #         self.bullet_list.remove(bullet)
        #         self.player_1.proyectil_creado = False
        #         SONIDO_EXPLOSION.play()

        self.player_1.events(events,keys,delta_ms,self.bullet_list)
        self.player_1.update(delta_ms,self.lista_plataformas,self.lista_enemigos,self.pb_lives, self.bullet_list)

        #self.boss.update(delta_ms=delta_ms,bullet_list=self.bullet_list)

       

       # print(self.boss.lives)

        for texto in self.lista_textos:
            if type(texto) == Score:
                texto.update(self.player_1.score)
            elif type(texto) == Lives:
                texto.update(self.player_1.lives)
            else:    
                texto.update(self.cronometro)

        self.pb_lives.value = self.player_1.lives 


        if len(self.lista_enemigos) == 0:
            self.set_active("form_menu_win")
            self.player_1 = Player(x=200,y=550,speed_walk=8,speed_run=8,gravity=17,jump_power=50,frame_rate_ms=50,move_rate_ms=50,jump_heigh=200,tipe=2)
            self.boss = Boss(x=300,y=50,speed_walk=4,speed_run=8,gravity=15,frame_rate_ms=50,move_rate_ms=10)
            self.lista_enemigos.append(self.boss)
            self.cronometro =60
        if self.player_1.lives == 0 or self.cronometro == 0:
            self.set_active("form_menu_game_over")
            self.player_1 = Player(x=200,y=550,speed_walk=8,speed_run=8,gravity=17,jump_power=50,frame_rate_ms=50,move_rate_ms=50,jump_heigh=200,tipe=2)
            self.boss = Boss(x=300,y=50,speed_walk=4,speed_run=8,gravity=15,frame_rate_ms=50,move_rate_ms=10)
            self.lista_enemigos.append(self.boss)
            self.cronometro =60


    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)

        for plataforma in self.lista_plataformas:
            plataforma.draw(self.surface)

        self.player_1.draw(self.surface)
        
        if len(self.lista_enemigos) > 0:
            self.boss.draw(self.surface)

        for bullet in self.bullet_list:
            bullet.draw(self.surface)
        
        # # for botin in self.lista_botinex:
        # #     if type(botin) != Escalerita:
        # #         botin.draw(self.surface)

        for texto in self.lista_textos:
            texto.draw(self.surface)

        for aux_widget in self.widget_list:    
            aux_widget.draw()
        
        # if len(self.lista_portal) > 0:
        #     for portal in self.lista_portal:
        #         portal.draw(self.surface)


        