import pygame
import sys
#classe giocatore con movimento, immagine e caratteristiche varie. 

class Giocatore:
    def __init__(self, x, y):
        self.immagine = pygame.image.load("/Users/dany/Downloads/CtB images/P1.png")
        self.immagine = pygame.transform.scale(self.immagine, (75, 80))
        self.rect = self.immagine.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_gioc = 5

    def dis_pers(self, schermo):
        schermo.blit(self.immagine, self.rect)

    def mov (self, tastiera = None):
        #pos = (gioc_x, gioc_y)
        tastiera = pygame.key.get_pressed()
        if tastiera[pygame.K_a]:
            self.rect.x -= self.vel_gioc
        if tastiera[pygame.K_d]:
            self.rect.x += self.vel_gioc
        if tastiera[pygame.K_w]:
            self.rect.y -= self.vel_gioc
        if tastiera[pygame.K_s]:
            self.rect.y += self.vel_gioc



class Bot:
    def __init__(self, x, y) -> None:
        self.immagine_vivo = pygame.image.load("/Users/dany/Downloads/CtB images/Bot_vivo.png")
        self.immagine_vivo = pygame.transform.scale(self.immagine_vivo, (80, 80))
        self.immagine_vivo_270 = pygame.transform.rotate(self.immagine_vivo, 90)
        self.rect_vivo_270 = self.immagine_vivo_270.get_rect()
        self.immagine_vivo_270 = pygame.transform.rotate(self.immagine_vivo, -90)
        self.rect_vivo_90 = self.immagine_vivo_270.get_rect()
        self.immagine_morto = pygame.image.load("/Users/dany/Downloads/CtB images/Bot_morto.png")
        self.immagine_morto = pygame.transform.scale(self.immagine_morto, (80, 80))
        self.rect_vivo = self.immagine_vivo.get_rect()
        self.rect_vivo.x = x
        self.rect_vivo.y = y
        self.rect_morto = self.immagine_morto.get_rect()
        self.rect_morto.x = x
        self.rect_morto.y = y
        self.rect_vivo.center = (x, y)
        self.rect_vivo.center = (x, y)
        self.rect_vivo_90.x = x
        self.rect_vivo_90.y = y
        self.rect_vivo_270.x = x
        self.rect_vivo_270.y = y

        self.campo_visivo = CampoVisivo(x, y)

    def dis_bot(self, schermo):
        schermo.blit(self.immagine_vivo, self.rect_vivo)
    
    def dis_bot_ruotato0(self, schermo):
        schermo.blit(self.immagine_vivo_270, self.rect_vivo_270)

 
    def dis_bot_morto(self, schermo):
        schermo.blit(self.immagine_morto, self.rect_morto)

    def inserisci_campo_visivo0(self, schermo):
        sup = pygame.surface.Surface((80, 80))
        sup.fill("Red")
        sup_rect = sup.get_rect(midbottom = (self.rect_vivo.midtop))
        schermo.blit(sup, sup_rect)

    def inserisci_campo_visivo90(self, schermo):
        sup = pygame.surface.Surface((80, 80))
        sup.fill("Red")
        sup_rect = sup.get_rect(midleft = (self.rect_vivo_90.midright))
        schermo.blit(sup, sup_rect)
    
    def inserisci_campo_visivo_ruotato270(self, schermo):
        sup = pygame.surface.Surface((80, 80))
        sup.fill("Red")
        sup_rect = sup.get_rect(midright = (self.rect_vivo_270.midleft))
        schermo.blit(sup, sup_rect)
        
        

class CampoVisivo:
    def __init__(self, x, y) -> None:
        self.imm = pygame.surface.Surface((80, 80))
        self.imm.fill("Red")
        self.rect = self.imm.get_rect(midbottom = (x, y))
        self.rect.x = x
        self.rect.y = y


        

            

