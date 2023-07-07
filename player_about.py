from auxiliar import Auxiliar
from configuraciones import *


class PlayerAbout:
    def __init__(self,x,y,frame_rate_ms) -> None:
  
        self.spin = reescalar_imagen(Auxiliar.getSurfaceFromSpriteSheet(r"JUEGO_ON\images\BICHITO ESPACIAL\spritesheets\player-spin.png",8,1),(150,180))
        self.animation = self.spin
        self.frame = 0
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.frame_rate_ms = frame_rate_ms

        self.tiempo_transcurrido_animation = 0

    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animation += delta_ms

        if (self.tiempo_transcurrido_animation >=self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if (self.frame < len(self.animation) - 1):
                self.frame += 1
            else:
                self.frame = 0
       
    def update(self, delta_ms,):
        self.do_animation(delta_ms)

    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,RED,self.rect)

        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
