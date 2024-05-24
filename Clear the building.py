import pygame
from sys import exit
from Classi_Giocatore_e_Bot import Giocatore
from Classi_Giocatore_e_Bot import Bot

pygame.init()


#clock
clock = pygame.time.Clock()


#creazione finestra 
info = pygame.display.Info()
altezza = info.current_h -70
larghezza = info.current_w -30
dimensioni = (larghezza, altezza)
schermo = pygame.display.set_mode(dimensioni)

#personalizzazione finestra
sfondo = ("Black")
pygame.display.set_caption("Clear the Building!")
#prog_icon = pygame.image.load("CtB images\Icon.png").convert_alpha()
prog_icon = pygame.image.load("/Users/dany/Downloads/Clear the Building/ClearTheBuildingProject/CtB images/Icon.png").convert_alpha()
pygame.display.set_icon(prog_icon)

#creazione del giocatore
giocatore1 = Giocatore(altezza, larghezza)

#creazione bot
bot1 = Bot(x = 300, y = 300, orientamento = 0, stato = False)
bot2 = Bot(x = 1400, y = 600, orientamento = -90, stato = False)
bot3 = Bot(x = 1300, y = 400, orientamento = 180, stato = False)
bot4 = Bot(x = 600, y = 700, orientamento = 90, stato = False)
bots = [bot1, bot2, bot3, bot4]

#immagine "Sei stato scoperto!"
#SSS_immagine = pygame.image.load("CtB images\SSS.jpg").convert_alpha()
SSS_immagine = pygame.image.load("/Users/dany/Downloads/Clear the Building/ClearTheBuildingProject/CtB images/SSS.jpg").convert_alpha()
SSS_rect = SSS_immagine.get_rect()
SSS_pos = (larghezza // 2 - SSS_rect.width // 2, altezza // 2 - SSS_rect.height // 2 - 200)
game_over = False


#ciclo principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #modifiche e movimento al giocatore
    if not game_over:
        giocatore1.mov()
        giocatore1.animazione()

    #AGIORNAMENTO SCHERMO
    schermo.fill(sfondo)
    
    if game_over:
        schermo.fill(sfondo)
        schermo.blit(SSS_immagine, SSS_pos)


    #blit del personaggio
    giocatore1.disegna(schermo)

    #collisioni
    for bot in bots:
        if bot.stato == False and giocatore1.collisioni(bot):
            game_over = True
        giocatore1.kill(bot)

    #blit dei bot
    for bot in bots:
        bot.disegna(schermo, giocatore1.wx, giocatore1.wy)
    
    #aggiornamenti vari e eventuali 
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
