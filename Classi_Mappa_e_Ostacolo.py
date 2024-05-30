import sys
import pygame

class Pavimento:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.imm_pav = pygame.image.load("CtB images/Floor.png").convert_alpha()
        #self.imm_pav = pygame.surface.Surface((5000, 5000))
        #self.imm_pav.fill("White")
        self.rect_pav = self.imm_pav.get_rect()



        #self.confine_top = pygame.surface.Surface(5000, 1)
        #self.confine_top_rect = self.confine_top.get_rect(topleft = self.imm_pav)
    
    def dis_pav (self, schermo, px, py):

        #aggiorna pos
        new_x = self.x - px
        new_y = self.y - py
        self.rect_pav.x = new_x
        self.rect_pav.y = new_y
        
        #disegna
        schermo.blit(self.imm_pav, self.rect_pav)



class Ostacolo:
    def __init__(self, immagine, x, y) -> None:
        self.immagine = immagine
        self.x = x
        self.y = y
        self.rect = self.immagine.get_rect()



    def disegna(self, schermo, px, py):
        
        new_x = self.x - px
        new_y = self.y - py
        self.rect.x = new_x 
        self.rect.y = new_y

        schermo.blit(self.immagine, self.rect)

    