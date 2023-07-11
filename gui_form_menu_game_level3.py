import pygame
import random
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_progressbar import ProgressBar
from background import Background
from textos import *
from configuraciones import *
from enemigo_drag_lvl2 import *
from sql import *
from proyectiles_lvl3 import *
from proyectiles_final_map import Proyectiles_lvl3_final_map
from funciones import Funciones

class FormGameLevel3(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_background, color_border, active):
        super().__init__(name, master_surface, x, y, w,
                         h, color_background, color_border, active)

        self.data = leer_archivo(
            r"proyecto_final_lab1\proyecto_final_lab1\nivel_3.json")
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
            x=0, y=0, width=w, height=h, path=r"proyecto_final_lab1\proyecto_final_lab1\images\lvl3\background\fondito_lvl3_finish.png")

        # --- GAME ELEMNTS ---

        self.player_1 = Funciones.crear_player(self.data)

        self.boss = Funciones.crear_boss(self.data)

        self.lista_enemigos = []
        self.lista_enemigos.append(self.boss)

        self.lista_plataformas = Funciones.crear_plataformas(self.data)

        self.bullet_list = []

        self.lista_botinex = []

        self.lista_portal = []

        self.cronometro = 60
        self.contador = 0
        self.flag_timer = False

        self.stop_music()
        self.play_music()
        self.reiniciar = False
        self.pause = False
        self.win_menu = False
        self.lose_menu = False

    def on_click_boton1(self, parametro):
        self.pause = True
        self.set_active(parametro)

    def on_click_boton2(self, parametro):
        Funciones.mute()

    def on_click_boton3(self, parametro):
        Funciones.desmute()

    def crear_lluvia(self, delta_ms, bullet_list):
        self.contador += 1
        if self.contador == 50:
            bullet_list.append(Proyectiles_lvl3_final_map(x=random.randint(
                0, ANCHO_VENTANA), y=0, speed_proyectil=10, direction=DIRECTION_L, ms=delta_ms))
            bullet_list.append(Proyectiles_lvl3_final_map(x=random.randint(
                0, ANCHO_VENTANA), y=0, speed_proyectil=10, direction=DIRECTION_L, ms=delta_ms))
            bullet_list.append(Proyectiles_lvl3_final_map(x=random.randint(
                0, ANCHO_VENTANA), y=0, speed_proyectil=10, direction=DIRECTION_L, ms=delta_ms))
            self.contador += 1
        if self.contador > 50:
            self.contador = 0

    def stop_music(self):
        pygame.mixer.music.stop()

    def play_music(self):
        pygame.mixer.music.load(r"JUEGO_ON\music\musica_fondo\Boss_Fight.ogg")
        pygame.mixer.music.play(3)
        pygame.mixer.music.set_volume(VOLUMEN_FONDO)

    def update(self, events, keys, delta_ms, evento_1000ms):

        self.crear_lluvia(delta_ms, self.bullet_list)

        for aux_widget in self.widget_list:
           aux_widget.update(events)

        for event in events:
            if event.type == evento_1000ms:
                self.cronometro -= 1

        if len(self.lista_enemigos) > 0:
            for enemy_element in self.lista_enemigos:  # LOGICA ENEMIGOS, COLISION CON EL PROYECTIL
                enemy_element.update(delta_ms, self.bullet_list)
                if enemy_element.exploto == True:
                    self.lista_enemigos.remove(enemy_element)
                    self.player_1.score += 10000

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
                if bullet.tiempo_colision >= 500:
                    self.bullet_list.remove(bullet)
                    self.player_1.proyectil_creado = False
                    SONIDO_EXPLOSION.play()

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

        if len(self.lista_enemigos) == 0:
            self.set_active("form_menu_win")
            self.player_1.score += self.cronometro * 10
            Sql.crear_tabla(lvl=3)
            Sql.agregar_datos(Form.devolver_txt(
                "form_menu_A"), self.player_1.score, lvl=3)
            self.lista_enemigos = []
            self.bullet_list = []
            self.player_1 = Funciones.crear_player(self.data)
            self.boss = Funciones.crear_boss(self.data)
            self.lista_enemigos.append(self.boss)
            self.cronometro = 60
            self.win_menu = True
            self.pb_lives.value = 5

        if self.player_1.lives == 0 or self.cronometro == 0:
            self.set_active("form_menu_game_over")
            Sql.crear_tabla(lvl=2)
            Sql.agregar_datos(Form.devolver_txt(
                "form_menu_A"), self.player_1.score, lvl=2)
            self.player_1 = Funciones.crear_player(self.data)
            self.lista_enemigos = []
            self.bullet_list = []
            self.boss = Funciones.crear_boss(self.data)
            self.lista_enemigos.append(self.boss)
            self.cronometro = 60
            self.lose_menu = True
            self.pb_lives.value = 5

        if self.reiniciar == True:
            self.player_1 = Funciones.crear_player(self.data)
            self.lista_enemigos = []
            self.bullet_list = []
            self.boss = Funciones.crear_boss(self.data)
            self.lista_enemigos.append(self.boss)
            self.cronometro = 60
            self.reiniciar = False
            self.pb_lives.value = 5

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

        for texto in self.lista_textos:
            texto.draw(self.surface)

        for aux_widget in self.widget_list:
            aux_widget.draw()




        