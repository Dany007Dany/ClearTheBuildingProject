import sys
import pygame

class Pavimento:
    def __init__(self, x, y, px, py) -> None:
        self.x = x
        self.y = y
        self.imm_pav = pygame.image.load("CtB images/Floor.png").convert_alpha()
        surf_pav = pygame.surface.Surface((5000 - 300, 5000 - 240))
        self.rect_pav = surf_pav.get_rect()
        #self.rect_pav.topleft = ((x + 150 ,y + 120))


        #self.confine_top = pygame.surface.Surface(5000, 1)
        #self.confine_top_rect = self.confine_top.get_rect(topleft = self.imm_pav)
    
    def dis_pav (self, schermo, px, py):

        #aggiorna pos
        niu_x = self.x - px
        niu_y = self.y - py
        self.rect_pav.x = niu_x
        self.rect_pav.y = niu_y
        
        #disegna
        schermo.blit(self.imm_pav, self.rect_pav)