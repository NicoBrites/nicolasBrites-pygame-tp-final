import pygame
import sys
from constantes import *
from player import *
from configuraciones import *
from plataforma import Platform
from enemigo import Enemigo
from gui_form_menu_A import FormMenuA
from gui_form_menu_B import FormMenuB
from gui_form_menu_Win import *
from gui_form_menu_game_level1 import FormGameLevel1
from gui_form import Form
from gui_form_menu_game_level2 import FormGameLevel2
from gui_form_menu_Pausa import *
from gui_form_menu_game_over import *
from gui_form_menu_game_level3 import FormGameLevel3
from gui_form_menu_scoreboard import *

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

pygame.init()
clock = pygame.time.Clock()

evento_1000ms = pygame.USEREVENT
pygame.time.set_timer(evento_1000ms, 1000)

cronometro = 60


form_game_L1 = FormGameLevel1(name="form_game_L1",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False)
form_game_L2 = FormGameLevel2(name="form_game_L2",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA+10,color_background=(0,255,255),color_border=(255,0,255),active=False)
form_game_L3 = FormGameLevel3(name="form_game_L3",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA+10,color_background=(0,255,255),color_border=(255,0,255),active=True)

form_menu_A = FormMenuA(name="form_menu_A",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(255,255,0),color_border=(255,0,255),active=False,form_lvl1=form_game_L1,form_lvl2=form_game_L2)
form_menu_B = FormMenuB(name="about",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False)
form_menu_win = FormMenuWin(name="form_menu_win",master_surface = screen,x=300,y=200,w=500,h=400,color_background=(0,255,255),color_border=(255,0,255),active=False,form_lvl1=form_game_L1,form_lvl2=form_game_L2,form_lvl3=form_game_L3)
form_menu_game_over = FormMenuGameOver(name="form_menu_game_over",master_surface = screen,x=300,y=200,w=500,h=400,color_background=(0,255,255),color_border=(255,0,255),active=False,form_lvl1=form_game_L1,form_lvl2=form_game_L2,form_lvl3=form_game_L3)
form_menu_menu_Pausa = FormMenuPausa(name="form_menu_pausa",master_surface = screen,x=300,y=200,w=427,h=354,color_background=(255,255,0),color_border=(255,0,255),active=False,form_lvl1=form_game_L1,form_lvl2=form_game_L2,form_lvl3=form_game_L3)
form_menu_scoreboard = FormMenuScoreboard(name="scoreboard",master_surface= screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,0,0),color_border=(0,0,0),active=False)


while True:


    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    keys = pygame.key.get_pressed()

    delta_ms = clock.tick(FPS)


    aux_form_active = Form.get_active()
    if(aux_form_active != None):
        if type(aux_form_active) == FormMenuA :
            aux_form_active.update(events,keys,delta_ms)
        elif type(aux_form_active) == FormMenuB:
            aux_form_active.update(events,keys,delta_ms)
        elif type(aux_form_active) == FormGameLevel1:
            aux_form_active.update(events,keys,delta_ms,evento_1000ms)
        elif type(aux_form_active) == FormGameLevel2:
            aux_form_active.update(events,keys,delta_ms,evento_1000ms)
        elif type(aux_form_active) == FormGameLevel3:
            aux_form_active.update(events,keys,delta_ms,evento_1000ms)
        else:
            aux_form_active.update(events,keys,delta_ms)
        aux_form_active.draw()

        
    pygame.display.flip()
