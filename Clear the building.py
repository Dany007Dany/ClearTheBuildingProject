import pygame
from sys import exit
from Classi_Giocatore_e_Bot import Giocatore
from Classi_Giocatore_e_Bot import Bot

pygame.init()


#clock
clock = pygame.time.Clock()


#creazione finestra 
altezza = 1000
larghezza = 1600
dimensioni = (larghezza, altezza)
schermo = pygame.display.set_mode(dimensioni)

#personalizzazione finestra
colore_sfondo_1 = ("Black")
sfondo = colore_sfondo_1
pygame.display.set_caption("Clear the Building!")
prog_icon = pygame.image.load("/Users/dany/Downloads/CtB images/Icona_Stivale.png").convert_alpha()

pygame.display.set_icon(prog_icon)

#creazione del giocatore
Giocatore1 = Giocatore(x = 1500, y = 900)
#creazione bot
Bot1 = Bot(x = 300, y = 300, orientamento = 0, x1 = 300, y1 = 220)
Bot2 = Bot(x = 1400, y = 600, orientamento = -90, x1 = 1480, y1 = 600)
Bot3 = Bot(x = 1300, y = 400, orientamento = 180, x1 = 1300, y1 = 480)
Bot4 = Bot(x = 600, y = 700, orientamento = 90, x1 = 520, y1 = 700)

#YOU LOST
testo_you_lost = "Sei stato scoperto"
colore_testo_iniziale = ("White")
font_you_lost = pygame.font.Font(None, 112)
testo_you_lost_render = font_you_lost.render(testo_you_lost, True, colore_testo_iniziale)
pos_testo_you_lost = (500, 500)
you_lost_visibile = False



#vettore
objs = [Giocatore1, Bot1, Bot2, Bot3, Bot4]




#ciclo principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #modifiche e movimento ai Giocatori 
    Giocatore1.mov()       
    

    #modifiche e movimento dei Bot
    
    #aggiornamento schermo
    schermo.fill(sfondo)
    
    #blit dei bot
    Bot1.disegna(schermo, 0, True)
    Bot2.disegna(schermo, -90, False)
    Bot3.disegna(schermo, 180, False)
    Bot4.disegna(schermo, 90, False)
    #Bot2.dis_bot_morto(schermo)


    #blit del personaggio
    Giocatore1.disegna(schermo)
    Giocatore1.collisioni([Bot1, Bot2, Bot3, Bot4], schermo, testo_you_lost_render, pos_testo_you_lost)

        
    #aggiornamenti vari e eventuali 
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)

