import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
import sys
from gui_textbox import TextBox
from background import Background
#from gui_progressbar import ProgressBar


class FormMenuA(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.boton1 = Button(master=self,x=20,y=500,w=140,h=50,color_background=None,color_border=None,image_background=r"JUEGO_ON\images\GUI\BOTOn\Button_M_02.png",on_click=self.on_click_boton3,on_click_param="form_game_L1",text="Nivel 1",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=20,y=600,w=140,h=50,color_background=None,color_border=None,image_background=r"JUEGO_ON\images\GUI\BOTOn\Button_M_02.png",on_click=self.on_click_boton3,on_click_param="form_game_L2",text="Nivel 2",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton3 = Button(master=self,x=20,y=700,w=140,h=50,color_background=None,color_border=None,image_background=r"JUEGO_ON\images\GUI\BOTOn\Button_M_02.png",on_click=self.on_click_boton3,on_click_param="form_game_L3",text="Nivel 3",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton4 = Button(master=self,x=200,y=700,w=140,h=50,color_background=None,color_border=None,image_background=r"JUEGO_ON\images\GUI\BOTOn\Button_M_02.png",on_click=self.on_click_boton2,on_click_param="",text="SALIR :$",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton5 = Button(master=self,x=1100,y=600,w=200,h=50,color_background=None,color_border=None,image_background=r"JUEGO_ON\images\GUI\BOTOn\Button_M_02.png",on_click=self.on_click_boton3,on_click_param="scoreboard",text="HighScores",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton6 = Button(master=self,x=200,y=600,w=140,h=50,color_background=None,color_border=None,image_background=r"JUEGO_ON\images\GUI\BOTOn\Button_M_02.png",on_click=self.on_click_boton3,on_click_param="about",text="About",font="Verdana",font_size=30,font_color=C_WHITE)

        self.txt1 = TextBox(master=self,x=1100,y=700,w=300,h=50,color_background=None,color_border=None,image_background=r"JUEGO_ON\images\GUI\BOTOn\Button_XL_08.png",text="Ingresa tu Nombre",font="Verdana",font_size=30,font_color=C_BLACK)
        #self.pb1 = ProgressBar(master=self,x=200,y=150,w=240,h=50,color_background=None,color_border=None,image_background=r"images/gui/set_gui_01/Comic_Border/Bars/Bar_Background01.png",image_progress="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",value = 3, value_max=8)
        
        self.lista_widget = [self.boton1,self.boton2,self.boton3,self.boton4,self.boton5,self.txt1,self.boton6]
        #self.lista_widget = [self.boton1,self.boton2,self.boton3,self.boton4,self.boton5,self.txt1,self.pb1]

        self.static_background = Background(x=0,y=0,width=w,height=h,path=r"JUEGO_ON\images\GUI\background_menu\title-screen.png")

    def on_click_boton1(self, parametro):
        self.pb1.value += 1
 
    def on_click_boton2(self, parametro):
        sys.exit()
    
    def on_click_boton3(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    # @staticmethod
    # def devolver_txt(self):
    #     return self.txt1._text
    

    def draw(self): 
        super().draw()
        self.static_background.draw(screen=self.surface)

        for aux_widget in self.lista_widget:    
           aux_widget.draw()