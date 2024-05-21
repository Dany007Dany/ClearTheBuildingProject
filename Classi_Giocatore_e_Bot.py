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

    def disegna(self, schermo):
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

    def collisioni(self, bot):
        return self.rect.colliderect(bot.campo_visivo)
                

                
            
                



class Bot:
    def __init__(self, x, y, orientamento, x1, y1, stato) -> None:
        
        
        self.orientamento = orientamento
        
        self.immagine_vivo = pygame.image.load("/Users/dany/Downloads/CtB images/Bot_vivo.png").convert_alpha()
        self.immagine_vivo = pygame.transform.scale(self.immagine_vivo, (80, 80))
        self.rect_vivo = self.immagine_vivo.get_rect()
        self.rect_vivo.x = x
        self.rect_vivo.y = y
        self.rect_vivo.center = (x, y)
       
        self.campo_visivo = CampoVisivo(x1, y1)
        self.stato = stato
        
        
        self.immagine_vivo_90 = pygame.transform.rotate(self.immagine_vivo, orientamento)
        self.rect_vivo_90 = self.immagine_vivo_90.get_rect()
        self.rect_vivo_90.x = x
        self.rect_vivo_90.y = y
        self.rect_vivo_90.center = (x, y)

        self.immagine_vivo_180 = pygame.transform.rotate(self.immagine_vivo, orientamento)
        self.rect_vivo_180 = self.immagine_vivo_180.get_rect()
        self.rect_vivo_180.x = x
        self.rect_vivo_180.y = y
        self.rect_vivo_180.center = (x, y)

        self.immagine_vivo_270 = pygame.transform.rotate(self.immagine_vivo, orientamento)
        self.rect_vivo_270 = self.immagine_vivo_270.get_rect()
        self.rect_vivo_270.x = x
        self.rect_vivo_270.y = y
        self.rect_vivo_270.center = (x, y)
        
        self.immagine_morto = pygame.image.load("/Users/dany/Downloads/CtB images/Bot_morto.png").convert_alpha()
        self.immagine_morto = pygame.transform.scale(self.immagine_morto, (80, 80))
        self.rect_morto = self.immagine_morto.get_rect()
        self.rect_morto.x = x
        self.rect_morto.y = y
        
        self.sup0 = pygame.surface.Surface((80, 80))
        self.sup0.fill("Red")
        self.sup_rect0 = self.sup0.get_rect(midbottom = (self.rect_vivo.midtop))
        

        self.sup90 = pygame.surface.Surface((80, 80))
        self.sup90.fill("Red")
        self.sup_rect90 = self.sup90.get_rect(midleft = (self.rect_vivo_90.midright))
        
        self.sup180 = pygame.surface.Surface((80, 80))
        self.sup180.fill("Red")
        self.sup_rect180 = self.sup180.get_rect(midtop = (self.rect_vivo_180.midbottom))
        
        
        self.sup270 = pygame.surface.Surface((80, 80))
        self.sup270.fill("Red")
        self.sup_rect270 = self.sup270.get_rect(midright = (self.rect_vivo_270.midleft))
        

    def disegna(self, schermo, orientamento):
        if self.stato == False:
            if orientamento == 0:
                schermo.blit(self.immagine_vivo, self.rect_vivo)
                schermo.blit(self.sup0, self.sup_rect0)
            if orientamento == -90:
                schermo.blit(self.immagine_vivo_90, self.rect_vivo_90)
                schermo.blit(self.sup90, self.sup_rect90)
            if orientamento == 180:
                schermo.blit(self.immagine_vivo_180, self.rect_vivo_180)
                schermo.blit(self.sup180, self.sup_rect180)
            if orientamento == 90:
                schermo.blit(self.immagine_vivo_270, self.rect_vivo_270)
                schermo.blit(self.sup270, self.sup_rect270)
        elif self.stato == True:
            schermo.blit(self.immagine_morto, self.rect_morto)
    
    #def kill (self, tastiera = None):
        #tastiera = pygame.key.get_pressed()
        #if tastiera == [pygame.K_k]:
        #    self.stato = True





class CampoVisivo:
    def __init__(self, x, y) -> None:
        self.imm = pygame.surface.Surface((80, 80))
        self.rect = self.imm.get_rect(center = (x, y))

        
        
