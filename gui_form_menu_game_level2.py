import pygame
from gui_form import *
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_progressbar import ProgressBar
from player import *
from enemigo import *
from plataforma import *
from background import Background
from botin import *
from textos import *
from configuraciones import *
from enemigo_calaca_lvl2 import *
from enemigo_drag_lvl2 import *
from portal import Portal
from sql import *


class FormGameLevel2(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_background, color_border, active):
        super().__init__(name, master_surface, x, y, w,
                         h, color_background, color_border, active)

        self.data = leer_archivo(
            r"proyecto_final_lab1\proyecto_final_lab1\nivel_2.json")
        # --- GUI WIDGET ---
        self.boton1 = Button(master=self, x=ANCHO_VENTANA-550, y=ALTO_VENTANA-50, w=140, h=50, color_background=None, color_border=None, image_background="JUEGO_ON\images\GUI\BOTOn\Button_M_02.png",
                             on_click=self.on_click_boton1, on_click_param="form_menu_pausa", text="PAUSA", font="Verdana", font_size=30, font_color=C_WHITE)
        self.boton2 = Button(master=self, x=ANCHO_VENTANA-1000, y=ALTO_VENTANA-50, w=100, h=50, color_background=None, color_border=None,
                             image_background=r"proyecto_final_lab1\proyecto_final_lab1\images\GUI\BOTOn\audioMute.png", on_click=self.on_click_boton2, on_click_param="", text="", font="Verdana", font_size=30, font_color=C_WHITE)
        self.boton3 = Button(master=self, x=ANCHO_VENTANA-900, y=ALTO_VENTANA-50, w=100, h=50, color_background=None, color_border=None,
                             image_background=r"proyecto_final_lab1\proyecto_final_lab1\images\GUI\BOTOn\audioPlus.png", on_click=self.on_click_boton3, on_click_param="", text="", font="Verdana", font_size=30, font_color=C_WHITE)

        self.pb_lives = ProgressBar(master=self, x=ANCHO_VENTANA-365, y=ALTO_VENTANA-50, w=240, h=50, color_background=None, color_border=None,
                                    image_background="JUEGO_ON\images\GUI\BARS\Bar_Background01.png", image_progress="JUEGO_ON\images\GUI\BARS\Bar_Segment05.png", value=5, value_max=5)
        self.widget_list = [self.pb_lives,
                            self.boton1, self.boton2, self.boton3]

        self.lista_textos = []
        self.lista_textos.append(Score(master_surface=self.surface, x=0, y=ALTO_VENTANA-50, w=2000, h=50,
                                 color_background="Black", color_border="White", font="Helvetica", font_size=30, font_color=RED))
        self.lista_textos.append(Lives(master_surface=self.surface, x=ANCHO_VENTANA-100, y=ALTO_VENTANA-50, w=200,
                                 h=50, color_background="Black", color_border="White", font="Helvetica", font_size=30, font_color=RED))
        self.lista_textos.append(Timer(master_surface=self.surface, x=ANCHO_VENTANA/2, y=ALTO_VENTANA-50, w=300,
                                 h=50, color_background="Black", color_border="White", font="Helvetica", font_size=30, font_color=RED))

        self.static_background = Background(
            x=0, y=0, width=w, height=h, path=r"JUEGO_ON\images\lvl2\level2_background\ultimo_fondo_edit.png")

        # --- GAME ELEMNTS ---

        self.player_1 = self.crear_player(self.data)

        self.lista_enemigos = []
        self.crear_enemigos(self.data)

        self.lista_plataformas = []
        self.crear_plataformas(self.data)

        self.bullet_list = []

        self.lista_botinex = []
        self.crear_botines(self.data)

        self.lista_portal = []

        self.cronometro = 60

        self.stop_music()
        self.play_music()

        self.win = False
        self.win_menu = False
        self.reiniciar = False
        self.pause = False
        self.lose_menu = False

    def crear_player(self, lista_json: list):
        for objetos in lista_json:
            print(objetos)
            for clave, valor in objetos.items():
                print(clave, valor)
                if clave == "player":
                    print("entro")
                    return Player(x=valor["x"], y=valor["y"], speed_walk=valor["speed_walk"], speed_run=valor["speed_run"], gravity=valor["gravity"], jump_power=valor["jump_power"],
                                  frame_rate_ms=valor["frame_rate_ms"], move_rate_ms=valor["move_rate_ms"], jump_heigh=valor["jump_heigh"], tipe=valor["tipe"])

    def crear_plataformas(self, lista_json: list):
        for objetos in lista_json:
            for clave, valor in objetos.items():
                if clave == "plataformas":
                    for plataformas in valor:
                        if plataformas["plataforma"] == "Piso_lvl2":
                            self.lista_plataformas.append(Piso_lvl2(
                                x=plataformas["x"], y=plataformas["y"], w=plataformas["w"], h=plataformas["h"], type=plataformas["type"]))
                        elif plataformas["plataforma"] == "Plataforma_lvl2":
                            self.lista_plataformas.append(Plataforma_lvl2(
                                x=plataformas["x"], y=plataformas["y"], w=plataformas["w"], h=plataformas["h"], type=plataformas["type"]))
                        elif plataformas["plataforma"] == "Plataforma_lvl2_dinamica":
                            self.lista_plataformas.append(Plataforma_lvl2_dinamica(
                                x=plataformas["x"], y=plataformas["y"], w=plataformas["w"], h=plataformas["h"], type=plataformas["type"]))
                        else:
                            self.lista_plataformas.append(Plataforma_lvl2_dinamica_y(
                                x=plataformas["x"], y=plataformas["y"], w=plataformas["w"], h=plataformas["h"], type=plataformas["type"]))

    def crear_enemigos(self, lista_json: list):
        for objetos in lista_json:
            for clave, valor in objetos.items():
                if clave == "enemigos":
                    for enemigos in valor:
                        if enemigos["enemigo"] == "Enemigo_drag_lvl2":
                            self.lista_enemigos.append(Enemigo_drag_lvl2(x=enemigos["x"], y=enemigos["y"],
                                                                            frame_rate_ms=enemigos["frame_rate_ms"], move_rate_ms=enemigos["move_rate_ms"], type=enemigos["type"]))
                        else:
                            self.lista_enemigos.append(Enemigo_calaca_lvl2(x=enemigos["x"], y=enemigos["y"], speed_walk=enemigos["speed_walk"], speed_run=enemigos["speed_run"], gravity=enemigos["gravity"],
                                                                            frame_rate_ms=enemigos["frame_rate_ms"], move_rate_ms=enemigos["move_rate_ms"], type=enemigos["type"]))

    def crear_botines(self, lista_json: list):
        for objetos in lista_json:
            for clave, valor in objetos.items():
                if clave == "botines":
                    for botines in valor:
                        if botines["botin"] == "Botin":
                                self.lista_botinex.append(
                                    Botin(x=botines["x"], y=botines["y"], w=botines["w"], h=botines["h"]))
                        elif botines["botin"] == "Comidita":
                                self.lista_botinex.append(
                                    Comidita(x=botines["x"], y=botines["y"], w=botines["w"], h=botines["h"]))
                        else:
                            self.lista_botinex.append(
                                Console(x=botines["x"], y=botines["y"], w=botines["w"], h=botines["h"]))


    def on_click_boton1(self, parametro):
        self.pause = True
        self.set_active(parametro)  

    def on_click_boton2(self,parametro):
        self.mute()
    def on_click_boton3(self,parametro):
        self.desmute()

    def stop_music(self):
        pygame.mixer.music.stop()

    def play_music(self):
        pygame.mixer.music.load(r"JUEGO_ON\music\musica_fondo\Dangerous_Dungeon.ogg")
        pygame.mixer.music.play(3)
        pygame.mixer.music.set_volume(VOLUMEN_FONDO)
    
    def mute(self):
        pygame.mixer.music.set_volume(0)
    
    def desmute(self):
        pygame.mixer.music.set_volume(VOLUMEN_FONDO)

    def update(self,events,keys,delta_ms,evento_1000ms):

        for aux_widget in self.widget_list:
            aux_widget.update(events)

        for botin in self.lista_botinex:
            if self.player_1.rect.colliderect(botin.rect):
                if type(botin) == Console:
                    if keys[pygame.K_x]:
                        self.player_1.llave = True
                else:
                    self.lista_botinex.remove(botin)
                    SONIDO_COIN.play()
                    if type(botin) == Comidita:
                        self.pb_lives.value += 1
                        self.player_1.lives += 1
                        self.player_1.score += 250
                    else:
                        self.player_1.score += 1000
                    if type(botin) == Escalerita:
                        self.player_1.escalerita = True

        for enemy_element in self.lista_enemigos:  # LOGICA ENEMIGOS, COLISION CON EL PROYECTIL

            enemy_element.update(delta_ms,self.bullet_list)
            if self.player_1.proyectil_creado != False:
                for bullet in self.bullet_list:
                    if type(bullet) == Proyectiles_lvl2:
                        if bullet.rect.colliderect(enemy_element.rect):
                            enemy_element.animation = enemy_element.die
                            bullet.animation = bullet.proyectil_hit
            if enemy_element.exploto == True:
                SONIDO_EXPLOSION.play()
                self.lista_enemigos.remove(enemy_element)
                self.player_1.score += 500

        for bullet in self.bullet_list:
            bullet.update(delta_ms)
            if bullet.tiempo_colision >= 500:
                self.bullet_list.remove(bullet)
                self.player_1.proyectil_creado = False
                SONIDO_EXPLOSION.play()

        for plataforma in self.lista_plataformas:
            if type(plataforma) == Plataforma_lvl2_dinamica:
                plataforma.do_movement(delta_ms)
                if self.player_1.rect_ground_collition.colliderect(plataforma.rect_ground_collition):
                    if plataforma.direction == DIRECTION_L:
                        self.player_1.add_x(-3)
                    elif plataforma.direction == DIRECTION_R:
                        self.player_1.add_x(3)
            if type(plataforma) == Plataforma_lvl2_dinamica_y:
                plataforma.do_movement(delta_ms)
                if self.player_1.rect_ground_collition.colliderect(plataforma.rect_ground_collition):
                    if plataforma.direction == DIRECTION_L:
                        self.player_1.add_y(-4)
                    elif plataforma.direction == DIRECTION_R:
                        self.player_1.add_y(3)

        for event in events:
            if event.type == evento_1000ms:
                self.cronometro -= 1

        if self.player_1.rect.y <= 0:
            self.player_1.jump_power = 0
            self.player_1.add_y(self.player_1.gravity)
            self.player_1.is_jump = True

        self.player_1.events(events, keys, delta_ms, self.bullet_list)
        self.player_1.update(delta_ms, self.lista_plataformas,
                             self.lista_enemigos, self.pb_lives, self.bullet_list)

        for texto in self.lista_textos:
            if type(texto) == Score:
                texto.update(self.player_1.score)
            elif type(texto) == Lives:
                texto.update(self.player_1.lives)
            else:
                texto.update(self.cronometro)

        self.pb_lives.value = self.player_1.lives

        if len(self.lista_portal) > 0:
            for portal in self.lista_portal:
                portal.update(delta_ms)
                print("entro")

        if self.player_1.llave == True:
            self.lista_botinex.append(Escalerita(1450, 650, 48, 54))
            self.lista_portal.append(Portal(1430, 610, 32, 64, 100))
            self.player_1.llave = False

        if self.player_1.escalerita == True:
            self.set_active("form_menu_win")
            self.lista_enemigos = []
            self.lista_botinex = []
            self.bullet_list = []
            self.lista_portal = []
            self.crear_enemigos(self.data)
            self.crear_botines(self.data)
            self.player_1.score += self.cronometro * 10
            Sql.crear_tabla(lvl=2)
            Sql.agregar_datos(Form.devolver_txt(
                "form_menu_A"), self.player_1.score, lvl=2)
            self.player_1 = Player(x=500, y=550, speed_walk=8, speed_run=8, gravity=17,
                                   jump_power=50, frame_rate_ms=50, move_rate_ms=50, jump_heigh=200, tipe=2)
            self.cronometro = 60
            self.win = True
            self.win_menu = True

        if self.player_1.lives == 0 or self.cronometro == 0:
            self.set_active("form_menu_game_over")
            self.lista_enemigos = []
            self.lista_botinex = []
            self.bullet_list = []
            self.lista_portal = []
            self.crear_enemigos(self.data)
            self.crear_botines(self.data)
            Sql.crear_tabla(lvl=2)
            Sql.agregar_datos(Form.devolver_txt(
                "form_menu_A"), self.player_1.score, lvl=2)
            self.player_1 = Player(x=500, y=550, speed_walk=8, speed_run=8, gravity=17,
                                   jump_power=50, frame_rate_ms=50, move_rate_ms=50, jump_heigh=200, tipe=2)
            self.cronometro = 60
            self.lose_menu = True

        if self.reiniciar == True:
            self.lista_enemigos = []
            self.lista_botinex = []
            self.bullet_list = []
            self.lista_portal = []
            self.crear_enemigos(self.data)
            self.crear_botines(self.data)
            self.player_1 = Player(x=500, y=550, speed_walk=8, speed_run=8, gravity=17,
                                   jump_power=50, frame_rate_ms=50, move_rate_ms=50, jump_heigh=200, tipe=2)
            self.cronometro = 60
            self.reiniciar = False

    def draw(self):
        super().draw()
        self.static_background.draw(self.surface)

        for plataforma in self.lista_plataformas:
            plataforma.draw(self.surface)

        for enemy_element in self.lista_enemigos:
            enemy_element.draw(self.surface)

        self.player_1.draw(self.surface)

        for bullet in self.bullet_list:
            bullet.draw(self.surface)

        for botin in self.lista_botinex:
            if type(botin) != Escalerita:
                botin.draw(self.surface)

        for texto in self.lista_textos:
            texto.draw(self.surface)

        for aux_widget in self.widget_list:
            aux_widget.draw()

        if len(self.lista_portal) > 0:
            for portal in self.lista_portal:
                portal.draw(self.surface)


        