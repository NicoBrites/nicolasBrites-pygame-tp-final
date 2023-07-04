import pygame
import sys
from constantes import *
from player import *
from configuraciones import *
from plataforma import *
from enemigo import Enemigo
from botin import *
from textos import *



screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))


pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

evento_1000ms = pygame.USEREVENT
pygame.time.set_timer(evento_1000ms, 1000)

cronometro = 60

imagen_fondo = pygame.image.load(r"JUEGO_ON\images\2_game_background\2_game_background.png")
imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA,ALTO_VENTANA))

player_1 = Player(x=500,y=610,speed_walk=8,speed_run=8,gravity=17,jump_power=50,frame_rate_ms=50,move_rate_ms=50,jump_heigh=200 )

lista_textos=[]
lista_textos.append(Score(master_surface=screen,x=0,y=ALTO_VENTANA-50,w=2000,h=50,color_background="Black",color_border="White",font="Helvetica",font_size=30,font_color=RED))
lista_textos.append(Lives(master_surface=screen,x=ANCHO_VENTANA-100,y=ALTO_VENTANA-50,w=500,h=50,color_background="Black",color_border="White",font="Helvetica",font_size=30,font_color=RED))
lista_textos.append(Timer(master_surface=screen,x=ANCHO_VENTANA/2,y=ALTO_VENTANA-50,w=500,h=50,color_background="Black",color_border="White",font="Helvetica",font_size=30,font_color=RED))


lista_enemigos = []
lista_enemigos.append(Enemigo(x=1200,y=100,speed_walk=4,speed_run=8,gravity=15,frame_rate_ms=50,move_rate_ms=10))
lista_enemigos.append(Enemigo(x=400,y=100,speed_walk=4,speed_run=8,gravity=15,frame_rate_ms=50,move_rate_ms=10))

lista_plataformas = []
lista_plataformas.append(Platform(400,600,352,64,1))
lista_plataformas.append(Platform(600,400,352,64,1))
lista_plataformas.append(Platform(1000,200,352,64,1))
lista_plataformas.append(Platform(200,200,352,64,1))
lista_plataformas.append(Techito(0,0,ANCHO_VENTANA,64,1))
#lista_plataformas.append(Parecita(0,0,64,ALTO_VENTANA,1))
#lista_plataformas.append(Parecita(ANCHO_VENTANA-64,0,64,ALTO_VENTANA,1))

lista_botinex = []
lista_botinex.append(Botin(1300,150,48,54))
lista_botinex.append(Botin(200,150,48,54))
lista_botinex.append(Comidita(10,300,48,54))

lista_proyectiles = []

widget_list = []
bullet_list = []
'''
lista_plataformas.append(Platform(480,600,80,80,1))
lista_plataformas.append(Platform(560,600,80,80,1))
lista_plataformas.append(Platform(640,600,80,80,1))
lista_plataformas.append(Platform(560,400,80,80,1))
lista_plataformas.append(Platform(640,400,80,80,1))
lista_plataformas.append(Platform(720,400,80,80,1))
lista_plataformas.append(Platform(800,400,80,80,1))
'''
#PISO
#piso = pygame.Rect(0,0,ALTO_VENTANA,20)
#piso.top = player_1.lados["main"].bottom

#lados_piso = obtener_rectangulos(piso)

game_over = pygame.image.load(r"C:\Users\AdministraGod\Desktop\UTN\PROG 1\Juego memotest_alumnes\recursos\Game_Over.jpg")
game_over = pygame.transform.scale(game_over, (ANCHO_VENTANA,ALTO_VENTANA))
rectangulo_game_over = game_over.get_rect()

esta_corriendo = True

while esta_corriendo:

    collision_detected = False
    #colisiono_aux = True
    if terminar_partida(cronometro=cronometro, cantidad_vidas=player_1.lives): 

        screen.fill("White")
        screen.blit(game_over, rectangulo_game_over)
        flag_ganador = True
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                esta_corriendo =False

        pygame.display.flip()
        
    else:
        
        events = pygame.event.get()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:   
                if event.key == pygame.K_z:
                    player_1.shoot()
                    print("tocas te la z")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_z:
                    SONIDO_DISPARO.play()
                    lista_proyectiles.append(player_1.crear_proyectil(delta_ms))

            if event.type == evento_1000ms:
                    cronometro -= 1

            
        keys = pygame.key.get_pressed()


        delta_ms = clock.tick(FPS)

        if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] :
            player_1.walk(DIRECTION_L)
        if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            player_1.walk(DIRECTION_R)
        if (not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and not keys[pygame.K_SPACE] and not keys[pygame.K_z]):
            player_1.stay() 
        if  keys[pygame.K_RIGHT] and keys[pygame.K_LEFT] and not keys[pygame.K_SPACE]and not keys[pygame.K_z]:
            player_1.stay() 
        if keys[pygame.K_SPACE]:
            player_1.jump(True)
            
            

        screen.blit(imagen_fondo,imagen_fondo.get_rect())


        for plataforma in lista_plataformas:
            plataforma.draw(screen)

        for botin in lista_botinex:
            botin.draw(screen)
            if player_1.rect.colliderect(botin.rect):
                    lista_botinex.remove(botin)
                    SONIDO_COIN.play()
                    if type(botin)== Comidita:
                        player_1.lives +=1
                        player_1.score +=250
                    else:
                        player_1.score +=1000
                    if type(botin)== Llave:
                        player_1.llave = True
                

        for enemigo in lista_enemigos:
            enemigo.update(delta_ms, bullet_list)  
            enemigo.draw(screen)
            if player_1.proyectil_creado != False :
                if player_1.proyectil.rect.colliderect(enemigo.rect):
                    enemigo.animation = enemigo.die
                    player_1.proyectil.animation = player_1.proyectil.proyectil_hit
            if enemigo.exploto == True:
                for proyectil in lista_proyectiles:
                    print("exploto prouyectil")
                    lista_proyectiles.remove(proyectil)
                    player_1.proyectil_creado = False
                    SONIDO_EXPLOSION.play()
                lista_enemigos.remove(enemigo)
                player_1.score +=500

           
        player_1.update(delta_ms,lista_plataformas, lista_enemigos, widget_list, bullet_list)
        player_1.draw(screen)

        for texto in lista_textos:
            if type(texto) == Score:
                texto.update(player_1.score)
            elif type(texto) == Lives:
                texto.update(player_1.lives)
            else:
                texto.update(cronometro)
            texto.draw(screen)



        pygame.display.flip()

    
