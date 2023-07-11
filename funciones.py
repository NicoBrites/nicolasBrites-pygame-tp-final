from player import Player
from plataforma import *
from enemigo import *
from enemigo_calaca_lvl2 import *
from enemigo_drag_lvl2 import *
from botin import *
from boss_final import Boss



class Funciones:

    def crear_player(lista_json: list):
        for objetos in lista_json:
            for clave, valor in objetos.items():
                if clave == "player":
                    return Player(x=valor["x"], y=valor["y"], speed_walk=valor["speed_walk"], speed_run=valor["speed_run"], gravity=valor["gravity"], jump_power=valor["jump_power"],
                                  frame_rate_ms=valor["frame_rate_ms"], move_rate_ms=valor["move_rate_ms"], jump_heigh=valor["jump_heigh"], tipe=valor["tipe"])

    def crear_plataformas(lista_json: list):
        lista_plataformas = []
        for objetos in lista_json:
            for clave, valor in objetos.items():
                if clave == "plataformas":
                    for plataformas in valor:
                        if plataformas["plataforma"] == "Piso_lvl2":
                            lista_plataformas.append(Piso_lvl2(
                                x=plataformas["x"], y=plataformas["y"], w=plataformas["w"], h=plataformas["h"], type=plataformas["type"]))
                        elif plataformas["plataforma"] == "Plataforma_lvl2":
                            lista_plataformas.append(Plataforma_lvl2(
                                x=plataformas["x"], y=plataformas["y"], w=plataformas["w"], h=plataformas["h"], type=plataformas["type"]))
                        elif plataformas["plataforma"] == "Plataforma_lvl2_dinamica":
                                lista_plataformas.append(Plataforma_lvl2_dinamica(
                                    x=plataformas["x"], y=plataformas["y"], w=plataformas["w"], h=plataformas["h"], type=plataformas["type"]))
                        elif plataformas["plataforma"] == "Plataforma_lvl2_dinamica_y":
                                lista_plataformas.append(Plataforma_lvl2_dinamica_y(
                                    x=plataformas["x"], y=plataformas["y"], w=plataformas["w"], h=plataformas["h"], type=plataformas["type"]))
                        elif plataformas["plataforma"] == "Techito":
                            lista_plataformas.append(Techito(
                                x=plataformas["x"], y=plataformas["y"], w=plataformas["w"], h=plataformas["h"], type=plataformas["type"]))
                        else:
                            lista_plataformas.append(Platform(
                                x=plataformas["x"], y=plataformas["y"], w=plataformas["w"], h=plataformas["h"], type=plataformas["type"]))
        return lista_plataformas

    def crear_enemigos(lista_json: list):
        lista_enemigos = []
        for objetos in lista_json:
            for clave, valor in objetos.items():
                if clave == "enemigos":
                    for enemigos in valor:
                        if enemigos["enemigo"] == "Enemigo_drag_lvl2":
                            lista_enemigos.append(Enemigo_drag_lvl2(x=enemigos["x"], y=enemigos["y"],
                                                                    frame_rate_ms=enemigos["frame_rate_ms"], move_rate_ms=enemigos["move_rate_ms"], type=enemigos["type"]))
                        elif enemigos["enemigo"] == "Enemigo":
                            lista_enemigos.append(Enemigo(x=enemigos["x"], y=enemigos["y"], speed_walk=enemigos["speed_walk"], speed_run=enemigos["speed_run"], gravity=enemigos["gravity"],
                                                          frame_rate_ms=enemigos["frame_rate_ms"], move_rate_ms=enemigos["move_rate_ms"]))
                        else:
                            lista_enemigos.append(Enemigo_calaca_lvl2(x=enemigos["x"], y=enemigos["y"], speed_walk=enemigos["speed_walk"], speed_run=enemigos["speed_run"], gravity=enemigos["gravity"],
                                                                      frame_rate_ms=enemigos["frame_rate_ms"], move_rate_ms=enemigos["move_rate_ms"], type=enemigos["type"]))
        return lista_enemigos

    def crear_botines(lista_json: list):
        lista_botinex = []
        for objetos in lista_json:
            for clave, valor in objetos.items():
                if clave == "botines":
                    for botines in valor:
                        if botines["botin"] == "Botin":
                            lista_botinex.append(
                                Botin(x=botines["x"], y=botines["y"], w=botines["w"], h=botines["h"]))
                        elif botines["botin"] == "Comidita":
                            lista_botinex.append(
                                Comidita(x=botines["x"], y=botines["y"], w=botines["w"], h=botines["h"]))
                        else:
                            lista_botinex.append(
                                Console(x=botines["x"], y=botines["y"], w=botines["w"], h=botines["h"]))
        return lista_botinex

    def crear_boss(lista_json: list):
        for objetos in lista_json:
            for clave, valor in objetos.items():
                if clave == "boss":
                    return Boss(x=valor["x"], y=valor["y"], speed_walk=valor["speed_walk"], speed_run=valor["speed_run"], gravity=valor["gravity"],
                                frame_rate_ms=valor["frame_rate_ms"], move_rate_ms=valor["move_rate_ms"])

    def mute():
        pygame.mixer.music.set_volume(0)

    def desmute():
        pygame.mixer.music.set_volume(VOLUMEN_FONDO)
