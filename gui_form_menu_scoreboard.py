import sys
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_label import Label
from sql import *
from background import Background


class FormMenuScoreboard(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_background, color_border, active,):
        super().__init__(name, master_surface, x, y, w,
                         h, color_background, color_border, active)

        self.boton1 = Button(master=self, x=20, y=20, w=200, h=50, color_background=None, color_border=None, image_background=r"JUEGO_ON\images\GUI\BOTOn\Button_M_02.png",
                             on_click=self.on_click_boton3, on_click_param="form_menu_A", text="Back", font="Verdana", font_size=30, font_color=C_WHITE)
        self.label2 = Label(master=self, x=30, y=480, w=300, h=50, color_background=None, color_border=None,
                            image_background=None, text="", font="Old London", font_size=30, font_color=C_RED)
        self.label3 = Label(master=self, x=30, y=580, w=300, h=50, color_background=None, color_border=None,
                            image_background=None, text="", font="Old London", font_size=30, font_color=(255, 255, 0))
        self.label4 = Label(master=self, x=30, y=680, w=300, h=50, color_background=None, color_border=None,
                            image_background=None, text="", font="Old London", font_size=30, font_color=C_BLUE)
        self.label5 = Label(master=self, x=600, y=480, w=300, h=50, color_background=None, color_border=None,
                            image_background=None, text="", font="Old London", font_size=30, font_color=C_RED)
        self.label6 = Label(master=self, x=600, y=580, w=300, h=50, color_background=None, color_border=None,
                            image_background=None, text="", font="Old London", font_size=30, font_color=(255, 255, 0))
        self.label7 = Label(master=self, x=600, y=680, w=300, h=50, color_background=None, color_border=None,
                            image_background=None, text="", font="Old London", font_size=30, font_color=C_BLUE)
        self.label8 = Label(master=self, x=1100, y=480, w=300, h=50, color_background=None, color_border=None,
                            image_background=None, text="", font="Old London", font_size=30, font_color=C_RED)
        self.label9 = Label(master=self, x=1100, y=580, w=300, h=50, color_background=None, color_border=None,
                            image_background=None, text="", font="Old London", font_size=30, font_color=(255, 255, 0))
        self.label10 = Label(master=self, x=1100, y=680, w=300, h=50, color_background=None, color_border=None,
                             image_background=None, text="", font="Old London", font_size=30, font_color=C_BLUE)

        self.lista_widget = [self.boton1, self.label2, self.label3, self.label4,
                             self.label5, self.label6, self.label7, self.label8, self.label9, self.label10]

        self.lista_scores_lvl1 = []
        self.lista_scores_lvl2 = []
        self.lista_scores_lvl3 = []

        self.static_background = Background(
            x=0, y=0, width=w, height=h, path=r"JUEGO_ON\images\GUI\background_menu\fondo_score_finish.png")

    def on_click_boton1(self, parametro):
        pass
 
    def on_click_boton2(self, parametro):
        sys.exit()
    
    def on_click_boton3(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)


        import sqlite3
        with sqlite3.connect("JUEGO_ON/db/score_lvl1.db") as conexion:
            cursor=conexion.execute("SELECT nombre,value FROM score ORDER BY value DESC LIMIT 3")
            for fila in cursor:
                try:
                    self.lista_scores_lvl1.append(fila)
                except:
                    pass
        conexion.close()
        try:
            self.label2._text = "{0} {1}".format(self.lista_scores_lvl1[0][0],int(self.lista_scores_lvl1[0][1]))
        except:
            self.label2._text = "aaa 000"
        try:
            self.label3._text = "{0} {1}".format(self.lista_scores_lvl1[1][0] ,int(self.lista_scores_lvl1[1][1]))
        except:
            self.label3._text = "aaa 000"
        try:
            self.label4._text = "{0} {1}".format(self.lista_scores_lvl1[2][0] ,int(self.lista_scores_lvl1[2][1]))
        except:
            self.label4._text = "aaa 000"

        
        with sqlite3.connect("JUEGO_ON/db/score_lvl2.db") as conexion:
            cursor=conexion.execute("SELECT nombre,value FROM score ORDER BY value DESC LIMIT 3")
            for fila in cursor:
                self.lista_scores_lvl2.append(fila)
        conexion.close()
        try:
            self.label5._text = "{0} {1}".format(self.lista_scores_lvl2[0][0] , int(self.lista_scores_lvl2[0][1]))
        except:
            self.label5._text = "aaa 000"
        try:
            self.label6._text = "{0} {1}".format(self.lista_scores_lvl2[1][0] , int(self.lista_scores_lvl2[1][1]))
        except:
            self.label6._text = "aaa 000"
        try:
            self.label7._text = "{0} {1}".format(self.lista_scores_lvl2[2][0] , int(self.lista_scores_lvl2[2][1]))
        except:
            self.label7._text = "aaa 000"

        with sqlite3.connect("JUEGO_ON/db/score_lvl3.db") as conexion:
            cursor=conexion.execute("SELECT nombre,value FROM score ORDER BY value DESC LIMIT 3")
            for fila in cursor:
                self.lista_scores_lvl3.append(fila)
        conexion.close()
        try:
            self.label8._text = "{0} {1}".format(self.lista_scores_lvl3[0][0] , int(self.lista_scores_lvl3[0][1]))
        except:
            self.label8._text = "aaa 000"
        try:
            self.label9._text = "{0} {1}".format(self.lista_scores_lvl3[1][0] , int(self.lista_scores_lvl3[1][1]))
        except:
            self.label9._text = "aaa 000"
        try:
            self.label10._text = "{0} {1}".format(self.lista_scores_lvl3[2][0] , int(self.lista_scores_lvl3[2][1]))
        except:
            self.label10._text = "aaa 000"




    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)
        for aux_widget in self.lista_widget:    
           aux_widget.draw()