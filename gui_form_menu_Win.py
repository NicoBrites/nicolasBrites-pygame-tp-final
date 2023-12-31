from pygame.locals import *
from gui_form import Form
from gui_button import Button
from background import Background
from constantes import *
import sys


class FormMenuWin(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_background, color_border, active, form_lvl1, form_lvl2, form_lvl3):
        super().__init__(name, master_surface, x, y, w,
                         h, color_background, color_border, active)

        self.form_lvl1 = form_lvl1
        self.form_lvl2 = form_lvl2
        self.form_lvl3 = form_lvl3

        self.boton1 = Button(master=self, x=20, y=220, w=300, h=40, color_background=C_GREEEN_2, color_border=C_YELLOW_2,
                             on_click=self.on_click_boton1, on_click_param="form_menu_A", text="MENU PRINCIPAL", font="Verdana", font_size=30, font_color=C_BLACK)
        self.boton2 = Button(master=self, x=185, y=350, w=300, h=40, color_background=C_PINK, color_border=C_RED,
                             on_click=self.on_click_boton2, on_click_param="", text="SALIR", font="Verdana", font_size=30, font_color=C_BLACK)

        self.static_background = Background(
            x=0, y=0, width=w, height=h, path=r"proyecto_final_lab1\proyecto_final_lab1\images\GUI\background_menu\menu_win_god.png")

    def on_click_boton1(self, parametro):

        self.set_active(parametro)

    def on_click_boton2(self, parametro):
        sys.exit()

    def update(self, lista_eventos, keys, delta_ms):

        if self.form_lvl3.win_menu == True:
            self.lista_widget = [self.boton1, self.boton2]
            self.form_lvl1.win_menu = False
            self.form_lvl2.win_menu = False
            self.form_lvl3.win_menu = False

        if self.form_lvl1.win_menu == True:
            self.boton3 = Button(master=self, x=20, y=270, w=300, h=40, color_background=C_PINK, color_border=C_RED, on_click=self.on_click_boton1,
                                 on_click_param="form_game_L2", text="SIGUIENTE NIVEL", font="Verdana", font_size=30, font_color=C_BLACK)
            self.lista_widget = [self.boton1, self.boton2, self.boton3]
            self.form_lvl1.win_menu = False
            self.form_lvl2.win_menu = False
            self.form_lvl3.win_menu = False

        if self.form_lvl2.win_menu == True:
            self.boton3 = Button(master=self, x=20, y=270, w=300, h=40, color_background=C_PINK, color_border=C_RED, on_click=self.on_click_boton1,
                                 on_click_param="form_game_L3", text="SIGUIENTE NIVEL", font="Verdana", font_size=30, font_color=C_BLACK)
            self.lista_widget = [self.boton1, self.boton2, self.boton3]
            self.form_lvl1.win_menu = False
            self.form_lvl2.win_menu = False
            self.form_lvl3.win_menu = False

        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self):
        super().draw()
        self.static_background.draw(self.surface)
        for aux_widget in self.lista_widget:
            aux_widget.draw()

        
