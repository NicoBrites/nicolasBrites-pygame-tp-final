import sys
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from background import Background


class FormMenuPausa(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_background, color_border, active, form_lvl1, form_lvl2, form_lvl3):
        super().__init__(name, master_surface, x, y, w,
                         h, color_background, color_border, active)

        self.form_lvl1 = form_lvl1
        self.form_lvl2 = form_lvl2
        self.form_lvl3 = form_lvl3

        self.boton3 = Button(master=self, x=20, y=220, w=250, h=50, color_background=None, color_border=None, image_background=r"JUEGO_ON\images\GUI\BOTOn\Button_M_02.png",
                             on_click=self.on_click_boton3, on_click_param="form_menu_A", text="Menu Principal", font="Verdana", font_size=30, font_color=C_WHITE)
        self.boton4 = Button(master=self, x=275, y=300, w=140, h=50, color_background=None, color_border=None, image_background=r"JUEGO_ON\images\GUI\BOTOn\Button_M_02.png",
                             on_click=self.on_click_boton2, on_click_param="", text="Salir", font="Verdana", font_size=30, font_color=C_WHITE)

        self.static_background = Background(
            x=0, y=0, width=w, height=h, path=r"proyecto_final_lab1\proyecto_final_lab1\images\GUI\background_menu\menu_pausa_edit.png")

    def on_click_boton1(self, parametro):
        if parametro == "form_game_L1":
            self.form_lvl1.reiniciar = True
        if parametro == "form_game_L2":
            self.form_lvl2.reiniciar = True
        if parametro == "form_game_L3":
            self.form_lvl3.reiniciar = True

    def on_click_boton2(self, parametro):
        sys.exit()

    def on_click_boton3(self, parametro):
        if parametro == "form_game_L1":
            self.form_lvl1.pause = False
            self.set_active(parametro)
        elif parametro == "form_game_L2":
            self.form_lvl2.pause = False
            self.set_active(parametro)
        elif parametro == "form_game_L3":
            self.form_lvl3.pause = False
            self.set_active(parametro)
        else:
            self.set_active(parametro)

    def update(self, lista_eventos, keys, delta_ms):

        if self.form_lvl1.pause == True:
            print("pausa lvl1")
            self.boton1 = Button(master=self, x=20, y=100, w=150, h=50, color_background=None, color_border=None, image_background=r"JUEGO_ON\images\GUI\BOTOn\Button_M_02.png",
                                 on_click=self.on_click_boton3, on_click_param="form_game_L1", text="Reanudar", font="Verdana", font_size=30, font_color=C_WHITE)
            self.boton2 = Button(master=self, x=20, y=160, w=200, h=50, color_background=None, color_border=None, image_background=r"JUEGO_ON\images\GUI\BOTOn\Button_M_02.png",
                                 on_click=self.on_click_boton1, on_click_param="form_game_L1", text="Reiniciar", font="Verdana", font_size=30, font_color=C_WHITE)
            self.form_lvl2.pause = False
            self.form_lvl2.reiniciar = False
            self.form_lvl3.pause = False
            self.form_lvl3.reiniciar = False

        elif self.form_lvl2.pause == True:
            print("pausa lvl2")
            self.boton1 = Button(master=self, x=20, y=100, w=150, h=50, color_background=None, color_border=None, image_background=r"JUEGO_ON\images\GUI\BOTOn\Button_M_02.png",
                                 on_click=self.on_click_boton3, on_click_param="form_game_L2", text="Reanudar", font="Verdana", font_size=30, font_color=C_WHITE)
            self.boton2 = Button(master=self, x=20, y=160, w=200, h=50, color_background=None, color_border=None, image_background=r"JUEGO_ON\images\GUI\BOTOn\Button_M_02.png",
                                 on_click=self.on_click_boton1, on_click_param="form_game_L2", text="Reiniciar", font="Verdana", font_size=30, font_color=C_WHITE)
            self.form_lvl1.pause = False
            self.form_lvl1.reiniciar = False
            self.form_lvl3.pause = False
            self.form_lvl3.reiniciar = False

        elif self.form_lvl3.pause == True:
            print("pausa lvl3")
            self.boton1 = Button(master=self, x=20, y=100, w=150, h=50, color_background=None, color_border=None, image_background=r"JUEGO_ON\images\GUI\BOTOn\Button_M_02.png",
                                 on_click=self.on_click_boton3, on_click_param="form_game_L3", text="Reanudar", font="Verdana", font_size=30, font_color=C_WHITE)
            self.boton2 = Button(master=self, x=20, y=160, w=200, h=50, color_background=None, color_border=None, image_background=r"JUEGO_ON\images\GUI\BOTOn\Button_M_02.png",
                                 on_click=self.on_click_boton1, on_click_param="form_game_L3", text="Reiniciar", font="Verdana", font_size=30, font_color=C_WHITE)
            self.form_lvl1.pause = False
            self.form_lvl1.reiniciar = False
            self.form_lvl2.pause = False
            self.form_lvl2.reiniciar = False

        self.lista_widget = [self.boton1,
                             self.boton2, self.boton3, self.boton4]

        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self):
        super().draw()
        self.static_background.draw(screen=self.surface)

        for aux_widget in self.lista_widget:
           aux_widget.draw()
