import pygame
from sys import exit
from Classi_Giocatore_e_Bot import Giocatore
from Classi_Giocatore_e_Bot import Bot
from Classi_Mappa_e_Ostacolo import Pavimento
from Classi_Mappa_e_Ostacolo import Ostacolo
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
sfondo = ("Grey")
pygame.display.set_caption("Clear the Building!")
prog_icon = pygame.image.load("CtB images/Icon.png").convert_alpha()
#prog_icon = pygame.image.load("/Users/dany/Downloads/Clear the Building/ClearTheBuildingProject/CtB images/Icon.png").convert_alpha()
pygame.display.set_icon(prog_icon)

#creazione del giocatore
giocatore1 = Giocatore(altezza, larghezza)

#creazione bot
bot1 = Bot(x = 2700, y = 300, orientamento = 0, stato = False)
bot2 = Bot(x = 1600, y = 475, orientamento = -90, stato = False)
bot3 = Bot(x = 2300, y = 1400, orientamento = 180, stato = False)
bot4 = Bot(x = 2600, y = 3700, orientamento = 90, stato = False)
bots = [bot1, bot2, bot3, bot4]

#immagini muri
imm_ostacolo_1_orizzontale = pygame.surface.Surface((4040, 20))
imm_ostacolo_1_orizzontale.fill("Grey20")
imm_ostacolo_2_verticale = pygame.surface.Surface((20, 4000))
imm_ostacolo_2_verticale.fill("Grey20")
imm_ostacolo_3_orizzontale = pygame.surface.Surface((2000, 20))
imm_ostacolo_3_orizzontale.fill("Grey20")
imm_ostacolo_4_verticale = pygame.surface.Surface((20, 2000))


#pavimento
pav_base = Pavimento(larghezza//4,altezza//4)

#immagini arredamenti
imm_scrivaniaadangolo = pygame.image.load("CtB images/ScrivaniaAngolo.png")
imm_scrivaniaadangolo = pygame.transform.scale(imm_scrivaniaadangolo, (200, 200))
imm_scrivania = pygame.image.load("CtB images/Scrivania.png")
imm_pianta = pygame.image.load("CtB images/Pianta.png")
imm_scaffale = pygame.image.load("CtB images/Scaffale.png")
imm_tavolo = pygame.image.load("CtB images/Tavolo.png")


#muri esterni
ostacolo_1_muro = Ostacolo(imm_ostacolo_1_orizzontale, larghezza//4 - 20,altezza//4)
ostacolo_2_muro = Ostacolo(imm_ostacolo_2_verticale, larghezza//4, altezza//4)
ostacolo_3_muro = Ostacolo(imm_ostacolo_1_orizzontale, larghezza//4, altezza//4 + 4000)
ostacolo_4_muro = Ostacolo(imm_ostacolo_2_verticale, larghezza//4 + 4000, altezza//4)
#muri interi
ostacolo_5_muro = Ostacolo(imm_ostacolo_3_orizzontale, larghezza//4, pav_base.rect_pav.height//5)
ostacolo_6_muro = Ostacolo(imm_ostacolo_4_verticale, 3400, 500)
#ostacoli
ostacolo_1 = Ostacolo(imm_scrivaniaadangolo, 350, 400)

ostacoli = [ostacolo_1]

#immagine "Sei stato scoperto!"
SSS_immagine = pygame.image.load("CtB images/SSS.jpg").convert_alpha()
SSS_rect = SSS_immagine.get_rect()
SSS_pos = (larghezza // 2 - SSS_rect.width // 2, altezza // 2 - SSS_rect.height // 2 - 200)
game_over = False

#settings
stg_img = pygame.image.load("CtB images/Settings.png").convert_alpha()
stg_img = pygame.transform.scale(stg_img, (80, 80))
stg_pos = (larghezza - larghezza // 17, 0)
stg_rect = stg_img.get_rect(topleft = stg_pos)

#settings interface
settings = False
interface_imm = pygame.image.load("CtB images/Interface.png").convert_alpha()
interface_imm = pygame.transform.scale(interface_imm, (larghezza, altezza))
interface_x = pygame.image.load("CtB images/K_x.png").convert_alpha()
interface_x = pygame.transform.scale(interface_x, (larghezza // 16, larghezza // 16))
interface_exit_game = pygame.image.load("CtB images/Exit_game.png").convert_alpha()
interface_exit_game = pygame.transform.scale(interface_exit_game, (larghezza // 16, larghezza // 16))
interface_exit_game_rect = interface_exit_game.get_rect()
interface_imm_pos = (0, 0)
interface_x_pos = (larghezza - interface_x.get_width() * 3.2, altezza // 4.5)
interface_exit_pos = (larghezza - interface_x.get_width() * 3.2, altezza // 1.47)
bottone_x = interface_x.get_rect(topleft = interface_x_pos)
bottone_exit_game = interface_exit_game.get_rect(topleft = interface_exit_pos)

#lascia gioco
font_leave = pygame.font.Font("SIXTY.TTF", 40)
leave_render = font_leave.render("Premi Sp_azio per uscire", True, "White")




#ciclo principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if stg_rect.collidepoint(pos):
                settings = True
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if bottone_x.collidepoint(pos):
                settings = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if bottone_exit_game.collidepoint(pos) and settings == True:
                pygame.quit()
                exit()
        

       
    
    #modifiche e movimento al giocatore
    if not game_over:
        
        giocatore1.mov(rectpav = pav_base.rect_pav)
        giocatore1.animazione()
        #collisioni
        for bot in bots:
            giocatore1.killSTAT(bots)
            if bot.stato == False and giocatore1.collisioni(bot):
                game_over = True
            giocatore1.kill(bot)
        

        #if giocatore1.confini(pav_base):
        #    game_over = False
        #else:
        #   game_over = True


    
    #AGIORNAMENTO SCHERMO
    schermo.fill(sfondo)
    
    #blit pavimento
    pav_base.dis_pav(schermo, giocatore1.wx, giocatore1.wy)
    
    #blit muri esterni
    ostacolo_1_muro.disegna(schermo, giocatore1.wx, giocatore1.wy + ostacolo_1_muro.rect.height)
    ostacolo_2_muro.disegna(schermo, giocatore1.wx + ostacolo_2_muro.rect.width, giocatore1.wy)
    ostacolo_3_muro.disegna(schermo, giocatore1.wx + ostacolo_3_muro.rect.height, giocatore1.wy)
    ostacolo_4_muro.disegna(schermo, giocatore1.wx, giocatore1.wy)
    #blit muri interni
    ostacolo_5_muro.disegna(schermo, giocatore1.wx, giocatore1.wy)
    ostacolo_6_muro.disegna(schermo, giocatore1.wx, giocatore1.wy)
    
    
    #blit osctacoli
    #for ostacolo in ostacoli:
        #ostacolo.disegna(schermo, giocatore1.wx, giocatore1.wy)
    
    
    #blit settings
    schermo.blit(stg_img, stg_pos)


    #blit dei bot
    for bot in bots:
        bot.disegna(schermo, giocatore1.wx, giocatore1.wy)


    #blit del personaggio
    giocatore1.disegna(schermo)

    #contatore
    cont = 0
    for bot in bots:
        if bot.stato == True:
            cont += 1

    if game_over:
        schermo.fill("Black")
        schermo.blit(SSS_immagine, SSS_pos)
        txt = pygame.font.Font("SIXTY.TTF", 55)
        txt_srf = txt.render(f"Numero di guardie eliminate: {cont}", False, "White")
        txt_rect = txt_srf.get_rect(midtop = (larghezza//2, altezza//2))
        schermo.blit(txt_srf, txt_rect)
        txt_cmm = pygame.font.Font("SIXTY.TTF", 55)
        #commenti
        if cont/len(bots) <= 0.3:
            txt_srf_cmm = txt_cmm.render(f"Patetico, non avrai mai una promozione", False, "Red")
        if cont/len(bots) > 0.3 and cont/len(bots) <= 0.5:
            txt_srf_cmm = txt_cmm.render(f"Cosa pensavi di fare? Volevi forse farci uccidere?", False, "Red")
        if cont/len(bots) > 0.5 and cont/len(bots) <= 0.7:
            txt_srf_cmm = txt_cmm.render(f"Ti sembra il caso di scherzare? Potevi fare molto meglio", False, "Red")
        if cont/len(bots) > 0.7 and cont/len(bots) <= 0.9:
            txt_srf_cmm = txt_cmm.render(f"Quasi, ma hai fallito lo stesso", False, "Red")
        #blit dei commenti
        txt_rect_cmm = txt_srf_cmm.get_rect(midtop = (larghezza//2, altezza//2 +55))
        schermo.blit(txt_srf_cmm, txt_rect_cmm)
        schermo.blit(leave_render, (larghezza // 2 - leave_render.get_width() // 2, altezza // 1.3))
        tastiera = pygame.key.get_pressed()
        if tastiera[pygame.K_SPACE]:
            pygame.quit()
            exit()
    
    #blit delle impostazioni
    if settings:
        schermo.blit(interface_imm, interface_imm_pos)
        schermo.blit(interface_x, interface_x_pos)
        schermo.blit(interface_exit_game, interface_exit_pos)


    
    
    #aggiornamenti vari e eventuali 
    pygame.display.flip()
    pygame.display.update()
    clock.tick(240)
