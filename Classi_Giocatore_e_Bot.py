import pygame
import sys
#classe giocatore con movimento, immagine e caratteristiche varie. 

class Giocatore:
    def __init__(self, x, y):
        self.immagine = pygame.image.load("/Users/dany/Downloads/CtB images/P1.PNG").convert_alpha()
        self.immagine = pygame.transform.scale(self.immagine, (120, 130))
        self.rect = self.immagine.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.immagine_ruotata_0 = pygame.transform.rotate(self.immagine, 0)
        self.rect_immagine_ruotata_0 = self.immagine_ruotata_0.get_rect()
        self.rect_immagine_ruotata_0.x = x
        self.rect_immagine_ruotata_0.y = y
        self.rect_immagine_ruotata_0.center = (x, y)


        self.immagine_ruotata_90 = pygame.transform.rotate(self.immagine, -90)
        self.rect_immagine_ruotata_90 = self.immagine_ruotata_90.get_rect()
        self.rect_immagine_ruotata_90.x = x
        self.rect_immagine_ruotata_90.y = y
        self.rect_immagine_ruotata_90.center = (x, y)


        self.immagine_ruotata_180 = pygame.transform.rotate(self.immagine, 180)
        self.rect_immagine_ruotata_180 = self.immagine_ruotata_180.get_rect()
        self.rect_immagine_ruotata_180.x = x
        self.rect_immagine_ruotata_180.y = y
        self.rect_immagine_ruotata_180.center = (x, y)

        self.immagine_ruotata_270 = pygame.transform.rotate(self.immagine, 90)
        self.rect_immagine_ruotata_270 = self.immagine_ruotata_270.get_rect()
        self.rect_immagine_ruotata_270.x = x
        self.rect_immagine_ruotata_270.y = y
        self.rect_immagine_ruotata_270.center = (x, y)
        
        self.vel_gioc = 5

    def dis_pers(self, schermo):
        schermo.blit(self.immagine, self.rect)

    def mov (self, tastiera = None):
        #pos = (gioc_x, gioc_y)
        tastiera = pygame.key.get_pressed()
        if tastiera[pygame.K_a]:
            self.rect.x -= self.vel_gioc
            self.immagine = self.immagine_ruotata_270
        if tastiera[pygame.K_d]:
            self.rect.x += self.vel_gioc
            self.immagine = self.immagine_ruotata_90
        if tastiera[pygame.K_w]:
            self.rect.y -= self.vel_gioc
            self.immagine = self.immagine_ruotata_0
        if tastiera[pygame.K_s]:
            self.rect.y += self.vel_gioc
            self.immagine = self.immagine_ruotata_180

    def collisioni(self, bots, schermo, testo_you_lost_render, pos_testo_you_lost):
        for bot in bots:
            if self.rect.colliderect(bot.campo_visivo.rect):
                print("Collisione")
                schermo.fill("Black")
                schermo.blit(testo_you_lost_render, pos_testo_you_lost)
                return True

                
            
                



class Bot:
    def __init__(self, x, y) -> None:
        self.immagine_vivo = pygame.image.load("/Users/dany/Downloads/CtB images/Bot_vivo.png").convert_alpha()
        self.immagine_vivo = pygame.transform.scale(self.immagine_vivo, (80, 80))
        self.rect_vivo = self.immagine_vivo.get_rect()
        self.rect_vivo.x = x
        self.rect_vivo.y = y
        
        self.campo_visivo = CampoVisivo(x, y)
        
        self.immagine_vivo_90 = pygame.transform.rotate(self.immagine_vivo, -90)
        self.rect_vivo_90 = self.immagine_vivo_90.get_rect()
        self.rect_vivo_90.x = x
        self.rect_vivo_90.y = y
        self.rect_vivo_90.center = (x, y)

        self.immagine_vivo_180 = pygame.transform.rotate(self.immagine_vivo, 180)
        self.rect_vivo_180 = self.immagine_vivo_180.get_rect()
        self.rect_vivo_180.x = x
        self.rect_vivo_180.y = y
        self.rect_vivo_180.center = (x, y)

        self.immagine_vivo_270 = pygame.transform.rotate(self.immagine_vivo, 90)
        self.rect_vivo_270 = self.immagine_vivo_270.get_rect()
        self.rect_vivo_270.x = x
        self.rect_vivo_270.y = y
        self.rect_vivo_270.center = (x, y)
        
        self.immagine_morto = pygame.image.load("/Users/dany/Downloads/CtB images/Bot_morto.png").convert_alpha()
        self.immagine_morto = pygame.transform.scale(self.immagine_morto, (80, 80))
        self.rect_morto = self.immagine_morto.get_rect()
        self.rect_morto.x = x
        self.rect_morto.y = y

        


    def dis_bot_ruotato0(self, schermo):
        schermo.blit(self.immagine_vivo, self.rect_vivo)
    
    def dis_bot_ruotato90(self, schermo):
        schermo.blit(self.immagine_vivo_90, self.rect_vivo_90)

    def dis_bot_ruotato_180(self, schermo):
        schermo.blit(self.immagine_vivo_180, self.rect_vivo_180)
    
    def dis_bot_ruotato270(self, schermo):
        schermo.blit(self.immagine_vivo_270, self.rect_vivo_270)
    
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

    def inserisci_campo_visivo180(self, schermo):
        sup = pygame.surface.Surface((80, 80))
        sup.fill("Red")
        sup_rect = sup.get_rect(midtop = (self.rect_vivo_180.midbottom))
        schermo.blit(sup, sup_rect)
    
    def inserisci_campo_visivo_ruotato270(self, schermo):
        sup = pygame.surface.Surface((80, 80))
        sup.fill("Red")
        sup_rect = sup.get_rect(midright = (self.rect_vivo_270.midleft))
        schermo.blit(sup, sup_rect)
        
    def dis_bot_morto(self, schermo):
        schermo.blit(self.immagine_morto, self.rect_morto)

    

class CampoVisivo:
    def __init__(self, x, y) -> None:
        self.imm = pygame.surface.Surface((80, 80))
        self.imm.fill("Red")
        self.rect = self.imm.get_rect(midbottom=(x, y)) 
        self.rect.x = x
        self.rect.y = y

    #def aggiorna(self, rect_giocatore):
        #if self.rect.colliderect(rect_giocatore):
            #pygame.quit()
        

            

