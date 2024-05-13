import pygame
from sys import exit
from Classi_Giocatore_e_Bot import Giocatore
from Classi_Giocatore_e_Bot import Bot
from Classi_Giocatore_e_Bot import CampoVisivo

pygame.init()


#clock
clock = pygame.time.Clock()


#creazione finestra 
altezza = 1000
larghezza = 1600
dimensioni = (larghezza, altezza)
schermo = pygame.display.set_mode(dimensioni)

#personalizzazione finestra
colore_sfondo_1 = (0, 0, 0)
sfondo = colore_sfondo_1
pygame.display.set_caption("Clear the Building!")
prog_icon = pygame.image.load("/Users/dany/Downloads/CtB images/Icona_Stivale.png")

pygame.display.set_icon(prog_icon)

#creazione del giocatore
Giocatore1 = Giocatore(x = 1500, y = 900)
Giocatore2 = Giocatore(x = 600, y = 900)
#creazione bot
Bot1 = Bot(x = 300, y = 300)
Bot2 = Bot(x = 400, y = 1000)
Bot3 = Bot(x = 1300, y = 400)
Bot4 = Bot(x = 600, y = 700)
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
    Bot1.dis_bot(schermo)
    
    Bot4.dis_bot_ruotato0(schermo)
    #Bot2.dis_bot_morto(schermo)


    #blit del campo al Bot1
    Bot1.inserisci_campo_visivo0(schermo)
    Bot4.inserisci_campo_visivo_ruotato270(schermo)
    #blit del personaggio
    Giocatore1.dis_pers(schermo)
    

    #aggiornamenti vari e eventuali 
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)


