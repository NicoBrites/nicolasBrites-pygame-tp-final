import pygame

class Auxiliar:
    @staticmethod
    def getSurfaceFromSpriteSheet(path, columnas, filas, flip = False):
        lista = []
        surface_imagen = pygame.image.load(path).convert_alpha()
        fotograma_ancho = int(surface_imagen.get_width()/columnas)
        fotograma_alto = int(surface_imagen.get_height()/filas)
        x = 0
        for fila in range(filas):
            for columna in range(columnas):
                x =  columna * fotograma_ancho
                y = fila * fotograma_alto
                surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
                if(flip):
                    surface_fotograma = pygame.transform.flip(surface_fotograma,True,False)
                lista.append(surface_fotograma)
        return lista
