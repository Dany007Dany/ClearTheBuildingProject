import pygame
import sys


#classe giocatore con movimento, immagine e caratteristiche varie. 
class Giocatore:
    def __init__(self, hSchermo, lSchermo):
        
        #coordinate mappa
        self.wx = 0
        self.wy = 0

        #immagini giocatore nelle 4 posizioni + rettangoli immagini
        self.immagine = pygame.image.load("/Users/dany/Downloads/CtB images/Player_1.png").convert_alpha()
        self.immagine = pygame.transform.scale(self.immagine, (150, 120))
        self.rect = self.immagine.get_rect()
        self.rect.x = lSchermo // 2 - self.rect.width // 2
        self.rect.y = hSchermo // 2 - self.rect.height // 2

        self.immagine_ruotata_0 = pygame.transform.rotate(self.immagine, 0)
        self.rect_immagine_ruotata_0 = self.immagine_ruotata_0.get_rect()
        self.rect_immagine_ruotata_0.x = lSchermo // 2 - self.rect.width // 2
        self.rect_immagine_ruotata_0.y = hSchermo // 2 - self.rect.height // 2
        self.rect_immagine_ruotata_0.center = (lSchermo // 2 - self.rect.width // 2, hSchermo // 2 - self.rect.height // 2)


        self.immagine_ruotata_90 = pygame.transform.rotate(self.immagine, -90)
        self.rect_immagine_ruotata_90 = self.immagine_ruotata_90.get_rect()
        self.rect_immagine_ruotata_90.x = lSchermo // 2 - self.rect.width // 2
        self.rect_immagine_ruotata_90.y = hSchermo // 2 - self.rect.height // 2
        self.rect_immagine_ruotata_90.center = (lSchermo // 2 - self.rect.width // 2, hSchermo // 2 - self.rect.height // 2)


        self.immagine_ruotata_180 = pygame.transform.rotate(self.immagine, 180)
        self.rect_immagine_ruotata_180 = self.immagine_ruotata_180.get_rect()
        self.rect_immagine_ruotata_180.x = lSchermo // 2 - self.rect.width // 2
        self.rect_immagine_ruotata_180.y = hSchermo // 2 - self.rect.height // 2
        self.rect_immagine_ruotata_180.center = (lSchermo // 2 - self.rect.width // 2, hSchermo // 2 - self.rect.height // 2)

        self.immagine_ruotata_270 = pygame.transform.rotate(self.immagine, 90)
        self.rect_immagine_ruotata_270 = self.immagine_ruotata_270.get_rect()
        self.rect_immagine_ruotata_270.x = lSchermo // 2 - self.rect.width // 2
        self.rect_immagine_ruotata_270.y = hSchermo // 2 - self.rect.height // 2
        self.rect_immagine_ruotata_270.center = (lSchermo // 2 - self.rect.width // 2, hSchermo // 2 - self.rect.height // 2)
        
        #velocità di movimento
        self.vel_gioc = 8


    #funzione per blit del giocatore
    def disegna(self, schermo):
        schermo.blit(self.immagine, self.rect)

    #funzione per movimento del giocatore
    def mov (self, tastiera = None):
        #pos = (gioc_x, gioc_y)
        tastiera = pygame.key.get_pressed()
        if tastiera[pygame.K_a]:
            self.wx -= self.vel_gioc
            self.immagine = self.immagine_ruotata_270
        if tastiera[pygame.K_d]:
            self.wx += self.vel_gioc
            self.immagine = self.immagine_ruotata_90
        if tastiera[pygame.K_w]:
            self.wy -= self.vel_gioc
            self.immagine = self.immagine_ruotata_0
        if tastiera[pygame.K_s]:
            self.wy += self.vel_gioc
            self.immagine = self.immagine_ruotata_180
    
    #funzione per verificare lo stato delle collisioni del personaggio con i campi visivi
    def collisioni(self, bot):
        return self.rect.colliderect(bot.campo_rect)
                

                
            
                



class Bot:
    def __init__(self, x, y, orientamento, stato) -> None:
        
        #posizioni, stato e orientamento
        self.x = x
        self.y = y
        self.stato = stato
        self.orientamento = orientamento
        
        #immagini
        self.immagine_vivo = pygame.image.load("/Users/dany/Downloads/CtB images/Bot_vivo.png").convert_alpha()
        self.immagine_vivo = pygame.transform.scale(self.immagine_vivo, (100, 100))
        self.immagine_vivo_90 = pygame.transform.rotate(self.immagine_vivo, orientamento)
        self.immagine_vivo_180 = pygame.transform.rotate(self.immagine_vivo, orientamento)
        self.immagine_vivo_270 = pygame.transform.rotate(self.immagine_vivo, orientamento)
        self.immagine_morto = pygame.image.load("/Users/dany/Downloads/CtB images/Bot_morto.png").convert_alpha()
        self.immagine_morto = pygame.transform.scale(self.immagine_morto, (80, 80))
        
        #rettangoli
        self.rect_vivo = self.immagine_vivo.get_rect(center = (x, y))
        self.rect_morto = self.immagine_morto.get_rect(center = (x, y))

        #campi visivi
        self.campo = pygame.surface.Surface((80, 80))
        self.campo.fill("Red")
        if self.orientamento == 0:
            self.campo_rect = self.campo.get_rect(midbottom = (self.rect_vivo.midtop))
        if self.orientamento == -90:
            self.campo_rect = self.campo.get_rect(midleft = (self.rect_vivo.midright))
        if self.orientamento == 180:
            self.campo_rect = self.campo.get_rect(midtop = (self.rect_vivo.midbottom))
        if self.orientamento == 90:
            self.campo_rect = self.campo.get_rect(midright = (self.rect_vivo.midleft))
        
    #funzione per blit dei bot
    def disegna(self, schermo, wxplayer, wyplayer):

        #aggiorna posizione
        newx = self.x - wxplayer
        newy = self.y - wyplayer

        self.rect_vivo.x = newx
        self.rect_vivo.y = newy

        if self.orientamento == 0:
            self.campo_rect = self.campo.get_rect(midbottom = (self.rect_vivo.midtop))
        if self.orientamento == -90:
            self.campo_rect = self.campo.get_rect(midleft = (self.rect_vivo.midright))
        if self.orientamento == 180:
            self.campo_rect = self.campo.get_rect(midtop = (self.rect_vivo.midbottom))
        if self.orientamento == 90:
            self.campo_rect = self.campo.get_rect(midright = (self.rect_vivo.midleft))

        #disegna
        if self.stato == False:
            if self.orientamento == 0:
                schermo.blit(self.immagine_vivo, self.rect_vivo)
                schermo.blit(self.campo, self.campo_rect)
            if self.orientamento == -90:
                schermo.blit(self.immagine_vivo_90, self.rect_vivo)
                schermo.blit(self.campo, self.campo_rect)
            if self.orientamento == 180:
                schermo.blit(self.immagine_vivo_180, self.rect_vivo)
                schermo.blit(self.campo, self.campo_rect)
            if self.orientamento == 90:
                schermo.blit(self.immagine_vivo_270, self.rect_vivo)
                schermo.blit(self.campo, self.campo_rect)
        elif self.stato == True:
            schermo.blit(self.immagine_morto, self.rect_morto)
    
    #funzione per uccidere
    def kill (self, tastiera = None):
        tastiera = pygame.key.get_pressed()
        if tastiera == [pygame.K_k]:
            self.stato = True




        
        
