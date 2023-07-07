import pygame
import sys
from pygame.locals import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
#from gui_graph import Graph
#from gui_label import Label
from constantes import *


class FormMenuGameOver(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.boton1 = Button(master=self,x=0,y=150,w=300,h=40,color_background=C_GREEEN_2,color_border=C_YELLOW_2,on_click=self.on_click_boton1,on_click_param="form_menu_A",text="MENU PRINCIPAL",font="Verdana",font_size=30,font_color=C_BLACK)
        self.boton2 = Button(master=self,x=0,y=200,w=300,h=40,color_background=C_PINK,color_border=C_RED,on_click=self.on_click_boton2,on_click_param="",text="SALIR",font="Verdana",font_size=30,font_color=C_BLACK)
        
        self.txt_x1 = TextBox(master=self,x=70,y=100,w=300,h=40,color_background=C_BLACK,color_border=C_RED,image_background=None,text="PERDISTE REYNALDO",font="Verdana",font_size=30,font_color=C_WHITE)


        self.lista_widget = [self.boton1,self.boton2,self.txt_x1]
        # self.lista_widget = [   self.boton1,self.boton2,self.boton3,self.boton4,self.txt_x0,self.txt_y0,self.txt_x1,
        #                         self.txt_y1,self.graph1,self.label_xy0,self.label_xy1,self.label_angulo,
        #                         self.txt_angulo_r,self.txt_angulo_d,self.label_cos,self.label_sin,self.txt_cos,
        #                         self.txt_sin,self.label_longitud ,self.txt_longitud
        #                     ]
  
                   
        

    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def on_click_boton2(self, parametro):
        sys.exit()
       

    def on_click_boton3(self, parametro):
        pass
        # self.graph1.x0 = int(self.txt_x0._text)
        # self.graph1.x1 = int(self.txt_x1._text)
        # self.graph1.y0 = int(self.txt_y0._text)
        # self.graph1.y1 = int(self.txt_y1._text)
        # angulo_radianes = math.atan2(self.graph1.y1 - self.graph1.y0, self.graph1.x1 - self.graph1.x0)
        # longitud_vector = math.sqrt(math.pow(self.graph1.y1 - self.graph1.y0,2)+math.pow(self.graph1.x1 - self.graph1.x0))
        # self.txt_longitud._text = "{0:.8f}".format(longitud_vector)

    def on_click_boton4(self, parametro):
        pass

    def calcular(self):
        pass

        # angulo_radianes = math.atan2(self.graph1.y1 - self.graph1.y0, self.graph1.x1 - self.graph1.x0)
        # longitud_vector = math.sqrt(math.pow(self.graph1.y1 - self.graph1.y0,2)+math.pow(self.graph1.x1 - self.graph1.x0,2))

        # self.txt_angulo_r._text = "r:{0:.2f}".format(angulo_radianes)
        # self.txt_angulo_d._text = "d:{0:.2f}".format(angulo_radianes*180/math.pi)
    
        # self.txt_cos._text  = "{0:.8f}".format(math.cos(angulo_radianes))
        # self.txt_sin._text  = "{0:.8f}".format(math.sin(angulo_radianes))

        # self.txt_longitud._text = "{0:.8f}".format(longitud_vector)

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()

        
