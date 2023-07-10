import pygame
from pygame.locals import *


class Texto:
    def __init__(self, master_surface, x, y, w, h, color_background, color_border, font, font_size, font_color) -> None:
        self.surface = master_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border
        self.font_sys = pygame.font.SysFont(font, font_size)
        self.font_color = font_color
        self.score = 0

    def render(self):
        pass

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.slave_surface, self.slave_rect)


class Score(Texto):
    def __init__(self, master_surface, x, y, w, h, color_background, color_border, font, font_size, font_color) -> None:
        super().__init__(master_surface, x, y, w, h, color_background,
                         color_border, font, font_size, font_color)

    def set_score(self, score):
        self.score = score

    def render(self, score):
        self.set_score(score)
        self.text = "Score:{0}".format(self.score)
        image_text = self.font_sys.render(
            self.text, True, self.font_color, self.color_background)

        self.slave_surface = pygame.surface.Surface((self.w, self.h))
        self.slave_rect = self.slave_surface.get_rect()

        self.slave_rect.x = self.x
        self.slave_rect.y = self.y

        pygame.draw.rect(self.slave_surface,
                         self.color_border, self.slave_rect)

        self.slave_surface.fill(self.color_background)

        self.slave_surface.blit(image_text, (10, 10))

    def update(self, score):
        self.render(score)


class Lives(Texto):
    def __init__(self, master_surface, x, y, w, h, color_background, color_border, font, font_size, font_color) -> None:
        super().__init__(master_surface, x, y, w, h, color_background,
                         color_border, font, font_size, font_color)

    def set_lives(self, lives):
        self.lives = lives

    def render(self, lives):
        self.set_lives(lives)
        self.text = "Lives:{0}".format(self.lives)
        image_text = self.font_sys.render(
            self.text, True, self.font_color, self.color_background)

        self.slave_surface = pygame.surface.Surface((self.w, self.h))
        self.slave_rect = self.slave_surface.get_rect()

        self.slave_rect.x = self.x
        self.slave_rect.y = self.y

        pygame.draw.rect(self.slave_surface,
                         self.color_border, self.slave_rect)

        self.slave_surface.fill(self.color_background)

        self.slave_surface.blit(image_text, (10, 10))

    def update(self, lives):
        self.render(lives)


class Timer(Texto):
    def __init__(self, master_surface, x, y, w, h, color_background, color_border, font, font_size, font_color) -> None:
        super().__init__(master_surface, x, y, w, h, color_background,
                         color_border, font, font_size, font_color)

    def set_timer(self, timer):
        self.timer = timer

    def render(self, timer):
        self.set_timer(timer)
        self.text = "Time:{0}".format(self.timer)
        image_text = self.font_sys.render(
            self.text, True, self.font_color, self.color_background)

        self.slave_surface = pygame.surface.Surface((self.w, self.h))
        self.slave_rect = self.slave_surface.get_rect()

        self.slave_rect.x = self.x
        self.slave_rect.y = self.y

        pygame.draw.rect(self.slave_surface,
                         self.color_border, self.slave_rect)

        self.slave_surface.fill(self.color_background)

        self.slave_surface.blit(image_text, (10, 10))

    def update(self, timer):
        self.render(timer)
