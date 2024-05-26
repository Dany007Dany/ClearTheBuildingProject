import sys
import pygame

class Pavimento:
    def __init__(self, x, y, lSchermo) -> None:
        self.x = x
        self.y = y
        self.imm_pav = pygame.image.load("CtB images\Texture Pavimento.jpeg").convert_alpha()
        self.imm_pav = pygame.transform.scale(self.imm_pav, (500, 500))
        self.rect_pav = self.imm_pav.get_rect()
        self.rect_pav.center = ((x,y))
    
    def dis_pav (self, schermo, px, py):
        niu_x = self.x - px
        niu_y = self.y - py
        self.rect_pav.x = niu_x
        self.rect_pav.y = niu_y
        schermo.blit(self.imm_pav, self.rect_pav)