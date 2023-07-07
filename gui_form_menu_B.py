import pygame
from pygame.locals import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
#from gui_progressbar import ProgressBar
from constantes import *
from configuraciones import *
from background import Background
from player_about import PlayerAbout

#import sqlite3

class FormMenuB(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.boton1 = Button(master=self,x=1300,y=20,w=150,h=40,color_background=C_RED,color_border=C_BLACK,on_click=self.on_click_boton1,on_click_param="form_menu_A",text="BACK",font="Verdana",font_size=30,font_color=C_BLACK)

        self.static_background = Background(x=0,y=0,width=w,height=h,path=r"JUEGO_ON\images\GUI\background_menu\fondo_about_finish2.png")
        
        self.lista_widget = [self.boton1]

        self.player = PlayerAbout(x=1200,y=300,frame_rate_ms=100)

    def on_click_boton1(self, parametro):
        self.set_active(parametro)


    def on_click_boton2(self):
        pass


    def on_click_boton3(self):
        pass

        
    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
           aux_widget.update(lista_eventos)
        self.player.update(delta_ms=delta_ms)


    def draw(self): 
        super().draw()

        self.static_background.draw(self.surface)
        for aux_widget in self.lista_widget:    
            aux_widget.draw()
        self.player.draw(screen=self.surface)