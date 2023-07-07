import pygame
import pygame.mixer
from pygame import mixer
from constantes import *
import json

def generar_sonido(path: str, volumen: float):
    '''
    Función que se encarga de generar un sondi
    Recibe el path en donde se encuentra ese sonido y el volumen del mismo
    Retorna el sonido para esperar a que se ejecute
    '''
    sonido = pygame.mixer.Sound(path)
    sonido.set_volume(volumen)
    return sonido

def reescalar_imagen(lista_imagenes, tamaño):

    for i in range(len(lista_imagenes)):
        lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i], tamaño)
        
    return lista_imagenes

def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []

    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))

    return lista_girada

enemigo_walk_r = [pygame.image.load(r"JUEGO_ON\images\ENEMIGO_1\SKELETON_WALK\skeleton-walk1.png"),
                pygame.image.load(r"JUEGO_ON\images\ENEMIGO_1\SKELETON_WALK\skeleton-walk2.png"),
                pygame.image.load(r"JUEGO_ON\images\ENEMIGO_1\SKELETON_WALK\skeleton-walk3.png"),
                pygame.image.load(r"JUEGO_ON\images\ENEMIGO_1\SKELETON_WALK\skeleton-walk4.png"),
                pygame.image.load(r"JUEGO_ON\images\ENEMIGO_1\SKELETON_WALK\skeleton-walk5.png"),
                pygame.image.load(r"JUEGO_ON\images\ENEMIGO_1\SKELETON_WALK\skeleton-walk6.png"),
                pygame.image.load(r"JUEGO_ON\images\ENEMIGO_1\SKELETON_WALK\skeleton-walk7.png"),
                pygame.image.load(r"JUEGO_ON\images\ENEMIGO_1\SKELETON_WALK\skeleton-walk8.png")]

enemigo_walk_r_lvl2 = [pygame.image.load(r"JUEGO_ON\images\ENEMIGO_1\SKELETON_WALK\skeleton-walk1.png"),
                pygame.image.load(r"JUEGO_ON\images\ENEMIGO_1\SKELETON_WALK\skeleton-walk2.png"),
                pygame.image.load(r"JUEGO_ON\images\ENEMIGO_1\SKELETON_WALK\skeleton-walk3.png"),
                pygame.image.load(r"JUEGO_ON\images\ENEMIGO_1\SKELETON_WALK\skeleton-walk4.png"),
                pygame.image.load(r"JUEGO_ON\images\ENEMIGO_1\SKELETON_WALK\skeleton-walk5.png"),
                pygame.image.load(r"JUEGO_ON\images\ENEMIGO_1\SKELETON_WALK\skeleton-walk6.png"),
                pygame.image.load(r"JUEGO_ON\images\ENEMIGO_1\SKELETON_WALK\skeleton-walk7.png"),
                pygame.image.load(r"JUEGO_ON\images\ENEMIGO_1\SKELETON_WALK\skeleton-walk8.png")]

enemigo_walk_l = girar_imagenes(enemigo_walk_r, True, False)

enemigo_walk_l_lvl2 = girar_imagenes(enemigo_walk_r_lvl2, True, False)

enemigo_idle_r = [pygame.image.load(r"JUEGO_ON\images\ENEMIGO_1\Skeleton-IDle\skeleton-idle1.png"),
                pygame.image.load(r"JUEGO_ON\images\ENEMIGO_1\Skeleton-IDle\skeleton-idle2.png"),
                pygame.image.load(r"JUEGO_ON\images\ENEMIGO_1\Skeleton-IDle\skeleton-idle3.png"),
                pygame.image.load(r"JUEGO_ON\images\ENEMIGO_1\Skeleton-IDle\skeleton-idle4.png")]

enemigo_idle_r_lvl2 = [pygame.image.load(r"JUEGO_ON\images\ENEMIGO_1\Skeleton-IDle\skeleton-idle1.png"),
                pygame.image.load(r"JUEGO_ON\images\ENEMIGO_1\Skeleton-IDle\skeleton-idle2.png"),
                pygame.image.load(r"JUEGO_ON\images\ENEMIGO_1\Skeleton-IDle\skeleton-idle3.png"),
                pygame.image.load(r"JUEGO_ON\images\ENEMIGO_1\Skeleton-IDle\skeleton-idle4.png")]

enemigo_idle_l = girar_imagenes(enemigo_idle_r, True, False)

enemigo_idle_l_lvl2 = girar_imagenes(enemigo_idle_r_lvl2, True, False)

proyectil_shoot_l = [pygame.image.load(r"JUEGO_ON\images\Proyectil\proyectil disparado\player-shoot1.png"),
                     pygame.image.load(r"JUEGO_ON\images\Proyectil\proyectil disparado\player-shoot2.png"),
                     pygame.image.load(r"JUEGO_ON\images\Proyectil\proyectil disparado\player-shoot3.png"),
                     pygame.image.load(r"JUEGO_ON\images\Proyectil\proyectil disparado\player-shoot4.png"),]


proyectil_shoot_r =  girar_imagenes(proyectil_shoot_l, True, False)


proyectil_hit = [pygame.image.load(r"JUEGO_ON\images\Proyectil\proyectil choca\player-shoot-hit1.png"),
                 pygame.image.load(r"JUEGO_ON\images\Proyectil\proyectil choca\player-shoot-hit2.png"),
                 pygame.image.load(r"JUEGO_ON\images\Proyectil\proyectil choca\player-shoot-hit3.png"),
                 pygame.image.load(r"JUEGO_ON\images\Proyectil\proyectil choca\player-shoot-hit4.png")]

shoot_proyectil_l = [pygame.image.load(r"JUEGO_ON\images\BICHITO ESPACIAL\BICHITO SHOOT\player-shoot1.png"),
                     pygame.image.load(r"JUEGO_ON\images\BICHITO ESPACIAL\BICHITO SHOOT\player-shoot1.png"),
                     pygame.image.load(r"JUEGO_ON\images\BICHITO ESPACIAL\BICHITO SHOOT\player-shoot2.png"),
                     pygame.image.load(r"JUEGO_ON\images\BICHITO ESPACIAL\BICHITO SHOOT\player-shoot2.png"),
                     pygame.image.load(r"JUEGO_ON\images\BICHITO ESPACIAL\BICHITO SHOOT\player-shoot3.png"),
                     pygame.image.load(r"JUEGO_ON\images\BICHITO ESPACIAL\BICHITO SHOOT\player-shoot3.png")]

shoot_proyectil_r = girar_imagenes(shoot_proyectil_l, True,False)

volumen_laser  = 0.1
volumen_otros_efectos = 0.2
volumen_fondo = 0.2

flag_sonido = True

if flag_sonido == True:
    pygame.mixer.init()
    # pygame.mixer.music.load(r"JUEGO_ON\music\musica_fondo\Common Fight.ogg")
    # pygame.mixer.music.play(3)
    # pygame.mixer.music.set_volume(VOLUMEN_FONDO)


    SONIDO_DISPARO = generar_sonido(r"JUEGO_ON\music\sonido_disparo\SpaceLaserShot PE1095407.wav", volumen_laser)
    SONIDO_SALTO = generar_sonido(r"JUEGO_ON\music\sonido_salto\SALTO.wav", VOLUMEN_OTROS_EFECTOS)
    SONIDO_EXPLOSION = generar_sonido(r"JUEGO_ON\music\sonido_explosion\EXPLOSIONM.wav", VOLUMEN_OTROS_EFECTOS)
    SONIDO_COIN = generar_sonido(r"JUEGO_ON\music\sonido_coinn\COINN.wav", VOLUMEN_OTROS_EFECTOS)
else:
    pygame.mixer.music.set_volume(0)
    SONIDO_DISPARO = generar_sonido(r"JUEGO_ON\music\sonido_disparo\SpaceLaserShot PE1095407.wav", 0)
    SONIDO_SALTO = generar_sonido(r"JUEGO_ON\music\sonido_salto\SALTO.wav", 0)
    SONIDO_EXPLOSION = generar_sonido(r"JUEGO_ON\music\sonido_explosion\EXPLOSIONM.wav", 0)
    SONIDO_COIN = generar_sonido(r"JUEGO_ON\music\sonido_coinn\COINN.wav", 0)


proyectil_dragonsito = [pygame.image.load(r"JUEGO_ON\images\lvl2\ENEMY_dispara\proyectil_dragon\fireball1.png"),
                  pygame.image.load(r"JUEGO_ON\images\lvl2\ENEMY_dispara\proyectil_dragon\fireball2.png"),
                  pygame.image.load(r"JUEGO_ON\images\lvl2\ENEMY_dispara\proyectil_dragon\fireball3.png"),
                  pygame.image.load(r"JUEGO_ON\images\lvl2\ENEMY_dispara\proyectil_dragon\fireball4.png")]

enemigo_maguito_idle=[pygame.image.load(r"JUEGO_ON/images/lvl2/ENEMY_dispara/maguito/maguito_idle/wizard-idle-1.png"),
                        pygame.image.load(r"JUEGO_ON/images/lvl2/ENEMY_dispara/maguito/maguito_idle/wizard-idle-2.png"),
                        pygame.image.load(r"JUEGO_ON/images/lvl2/ENEMY_dispara/maguito/maguito_idle/wizard-idle-3.png"),
                        pygame.image.load(r"JUEGO_ON/images/lvl2/ENEMY_dispara/maguito/maguito_idle/wizard-idle-4.png"),
                        pygame.image.load(r"JUEGO_ON/images/lvl2/ENEMY_dispara/maguito/maguito_idle/wizard-idle-5.png"),]

enemigo_maguito_shoot = [pygame.image.load(r"JUEGO_ON\images\lvl2\ENEMY_dispara\maguito\maguito_shoot\fire1.png"),
                         pygame.image.load(r"JUEGO_ON\images\lvl2\ENEMY_dispara\maguito\maguito_shoot\fire2.png"),
                         pygame.image.load(r"JUEGO_ON\images\lvl2\ENEMY_dispara\maguito\maguito_shoot\fire3.png"),
                         pygame.image.load(r"JUEGO_ON\images\lvl2\ENEMY_dispara\maguito\maguito_shoot\fire4.png"),
                         pygame.image.load(r"JUEGO_ON\images\lvl2\ENEMY_dispara\maguito\maguito_shoot\fire5.png"),
                         pygame.image.load(r"JUEGO_ON\images\lvl2\ENEMY_dispara\maguito\maguito_shoot\fire6.png"),
                         pygame.image.load(r"JUEGO_ON\images\lvl2\ENEMY_dispara\maguito\maguito_shoot\fire7.png"),
                         pygame.image.load(r"JUEGO_ON\images\lvl2\ENEMY_dispara\maguito\maguito_shoot\fire8.png"),
                         pygame.image.load(r"JUEGO_ON\images\lvl2\ENEMY_dispara\maguito\maguito_shoot\fire9.png")]

portal = [pygame.image.load(r"JUEGO_ON\images\lvl2\portal\force-field1.png"),
          pygame.image.load(r"JUEGO_ON\images\lvl2\portal\force-field2.png"),
          pygame.image.load(r"JUEGO_ON\images\lvl2\portal\force-field3.png"),
          pygame.image.load(r"JUEGO_ON\images\lvl2\portal\force-field4.png"),
          pygame.image.load(r"JUEGO_ON\images\lvl2\portal\force-field5.png")]

boss_final_walk_l = [pygame.image.load(r"JUEGO_ON\images\lvl3\boss\02_demon_walk\demon_walk_1.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\02_demon_walk\demon_walk_2.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\02_demon_walk\demon_walk_3.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\02_demon_walk\demon_walk_4.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\02_demon_walk\demon_walk_5.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\02_demon_walk\demon_walk_6.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\02_demon_walk\demon_walk_7.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\02_demon_walk\demon_walk_8.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\02_demon_walk\demon_walk_9.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\02_demon_walk\demon_walk_10.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\02_demon_walk\demon_walk_11.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\02_demon_walk\demon_walk_12.png")]

boss_final_walk_r = girar_imagenes(boss_final_walk_l, True, False)


boss_final_idle_l = [pygame.image.load(r"JUEGO_ON\images\lvl3\boss\01_demon_idle\demon_idle_1.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\01_demon_idle\demon_idle_2.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\01_demon_idle\demon_idle_3.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\01_demon_idle\demon_idle_4.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\01_demon_idle\demon_idle_5.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\01_demon_idle\demon_idle_6.png")]

boss_final_atack_l =[pygame.image.load(r"JUEGO_ON\images\lvl3\boss\03_demon_cleave\demon_cleave_1.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\03_demon_cleave\demon_cleave_2.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\03_demon_cleave\demon_cleave_3.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\03_demon_cleave\demon_cleave_4.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\03_demon_cleave\demon_cleave_5.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\03_demon_cleave\demon_cleave_6.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\03_demon_cleave\demon_cleave_7.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\03_demon_cleave\demon_cleave_8.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\03_demon_cleave\demon_cleave_9.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\03_demon_cleave\demon_cleave_10.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\03_demon_cleave\demon_cleave_11.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\03_demon_cleave\demon_cleave_12.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\03_demon_cleave\demon_cleave_13.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\03_demon_cleave\demon_cleave_14.png"),
                     pygame.image.load(r"JUEGO_ON\images\lvl3\boss\03_demon_cleave\demon_cleave_15.png")]

boss_final_atack_r = girar_imagenes(boss_final_atack_l, True, False)

boss_final_death_l = [pygame.image.load(r"JUEGO_ON\images\lvl3\boss\05_demon_death\demon_death_1.png"),
                      pygame.image.load(r"JUEGO_ON\images\lvl3\boss\05_demon_death\demon_death_2.png"),
                      pygame.image.load(r"JUEGO_ON\images\lvl3\boss\05_demon_death\demon_death_3.png"),
                      pygame.image.load(r"JUEGO_ON\images\lvl3\boss\05_demon_death\demon_death_4.png"),
                      pygame.image.load(r"JUEGO_ON\images\lvl3\boss\05_demon_death\demon_death_5.png"),
                      pygame.image.load(r"JUEGO_ON\images\lvl3\boss\05_demon_death\demon_death_6.png"),
                      pygame.image.load(r"JUEGO_ON\images\lvl3\boss\05_demon_death\demon_death_7.png"),
                      pygame.image.load(r"JUEGO_ON\images\lvl3\boss\05_demon_death\demon_death_8.png"),
                      pygame.image.load(r"JUEGO_ON\images\lvl3\boss\05_demon_death\demon_death_9.png"),
                      pygame.image.load(r"JUEGO_ON\images\lvl3\boss\05_demon_death\demon_death_10.png"),
                      pygame.image.load(r"JUEGO_ON\images\lvl3\boss\05_demon_death\demon_death_11.png"),
                      pygame.image.load(r"JUEGO_ON\images\lvl3\boss\05_demon_death\demon_death_12.png"),
                      pygame.image.load(r"JUEGO_ON\images\lvl3\boss\05_demon_death\demon_death_13.png"),
                      pygame.image.load(r"JUEGO_ON\images\lvl3\boss\05_demon_death\demon_death_14.png"),
                      pygame.image.load(r"JUEGO_ON\images\lvl3\boss\05_demon_death\demon_death_15.png"),
                      pygame.image.load(r"JUEGO_ON\images\lvl3\boss\05_demon_death\demon_death_16.png"),
                      pygame.image.load(r"JUEGO_ON\images\lvl3\boss\05_demon_death\demon_death_17.png"),
                      pygame.image.load(r"JUEGO_ON\images\lvl3\boss\05_demon_death\demon_death_18.png"),
                      pygame.image.load(r"JUEGO_ON\images\lvl3\boss\05_demon_death\demon_death_19.png"),
                      pygame.image.load(r"JUEGO_ON\images\lvl3\boss\05_demon_death\demon_death_20.png"),
                      pygame.image.load(r"JUEGO_ON\images\lvl3\boss\05_demon_death\demon_death_21.png"),
                      pygame.image.load(r"JUEGO_ON\images\lvl3\boss\05_demon_death\demon_death_22.png")]


proyectil_boss = [pygame.image.load(r"JUEGO_ON\images\lvl3\boss\proyectil\fireball1.png"),
                  pygame.image.load(r"JUEGO_ON\images\lvl3\boss\proyectil\fireball1.png"),
                  pygame.image.load(r"JUEGO_ON\images\lvl3\boss\proyectil\fireball1.png")]


def leer_archivo(string_de_archivo_json):
    '''
    La funcion lee un json y lo devuelve como una lista
    Recibe: una direccion de donde se encuentra el archivo
    Devuelve: el archivo transformado a lista
    '''
    lista= []
    with open(string_de_archivo_json, "r") as archivo:
        dict = json.load(archivo)
        lista = dict["nivel"]

    return lista