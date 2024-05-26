import pygame
from sys import exit
from Classi_Giocatore_e_Bot import Giocatore
from Classi_Giocatore_e_Bot import Bot
from Mappa import Pavimento
pygame.init()

#clock
clock = pygame.time.Clock()

#creazione finestra 
info = pygame.display.Info()
altezza = info.current_h -70
larghezza = info.current_w -30
dimensioni = (larghezza, altezza)
schermo = pygame.display.set_mode(dimensioni)
print(dimensioni)

#personalizzazione finestra
sfondo = ("Grey")
pygame.display.set_caption("Clear the Building!")
prog_icon = pygame.image.load("CtB images/Icon.png").convert_alpha()
#prog_icon = pygame.image.load("/Users/dany/Downloads/Clear the Building/ClearTheBuildingProject/CtB images/Icon.png").convert_alpha()
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
SSS_immagine = pygame.image.load("CtB images/SSS.jpg").convert_alpha()
#SSS_immagine = pygame.image.load("/Users/dany/Downloads/Clear the Building/ClearTheBuildingProject/CtB images/SSS.jpg").convert_alpha()
SSS_rect = SSS_immagine.get_rect()
SSS_pos = (larghezza // 2 - SSS_rect.width // 2, altezza // 2 - SSS_rect.height // 2 - 200)
game_over = False

#settings
#stg_img = pygame.image.load("/Users/dany/Downloads/Clear the Building/ClearTheBuildingProject/CtB images/Settings.png").convert_alpha()
stg_img = pygame.image.load("CtB images/Settings.png").convert_alpha()
stg_img = pygame.transform.scale(stg_img, (80, 80))
stg_pos = (larghezza - larghezza // 17, 0)
stg_rect = stg_img.get_rect(topleft = stg_pos)

#settings interface
#interface_imm = pygame.image.load("/Users/dany/Downloads/Clear the Building/ClearTheBuildingProject/CtB images/Interface.png").convert_alpha()
interface_imm = pygame.image.load("CtB images/Interface.png").convert_alpha()
interface_imm = pygame.transform.scale(interface_imm, (larghezza, altezza))
#interface_wasd = pygame.image.load("/Users/dany/Downloads/Clear the Building/ClearTheBuildingProject/CtB images/K_wasd.png").convert_alpha()
interface_wasd = pygame.image.load("CtB images/K_wasd.png").convert_alpha()
interface_wasd = pygame.transform.scale(interface_wasd, (300, 300))
interface_k = pygame.image.load("CtB images/K_k.png").convert_alpha()
#interface_k = pygame.image.load("/Users/dany/Downloads/Clear the Building/ClearTheBuildingProject/CtB images/K_k.png").convert_alpha()
#interface_k = pygame.transform.scale(interface_k, (300, 300))
interface_x = pygame.image.load("CtB images/K_x.png").convert_alpha()
#interface_x = pygame.image.load("/Users/dany/Downloads/Clear the Building/ClearTheBuildingProject/CtB images/K_x.png").convert_alpha()
interface_x = pygame.transform.scale(interface_x, (300, 300))
interface_shift = pygame.image.load("CtB images/SHIFT.png").convert_alpha()
#interface_shift = pygame.image.load("/Users/dany/Downloads/Clear the Building/ClearTheBuildingProject/CtB images/SHIFT.png").convert_alpha()
interface_shift = pygame.transform.scale(interface_shift, (300, 300))


wasd = pygame.font.Font("SIXTY.TTF", 100)
scritta_wasd = wasd.render("Move", True, "Black")
k = pygame.font.Font("SIXTY.TTF", 100)
scritta_kill = k.render("Kill", True, "Black")

interface_imm_pos = (0, 0)
interface_wasd_pos = (larghezza // 3 - interface_wasd.get_width() // 2, altezza // 2 - altezza // 3.5)
interface_k_pos = (larghezza // 3 - interface_k.get_width() * 2 // 2.5, altezza // 2 - interface_k.get_height() // 2)
interface_shift_pos = (larghezza // 3 - interface_shift.get_width() * 2 // 2.5, altezza // 1.25 - interface_shift.get_height())

interface_x_pos = (larghezza - interface_x.get_width() * 2, altezza // 10)
srcitta_wasd__pos = (larghezza // 2 - interface_wasd.get_width() * 1.5, altezza // 3.5)
scritta_kill_pos = (larghezza // 1.95, altezza // 3.5)


bottone_x = interface_x.get_rect(topleft = interface_x_pos)
settings = False

#pavimento
pav_base = Pavimento(200,200,larghezza)

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

       

    #modifiche e movimento al giocatore
    if not game_over:
        giocatore1.mov()
        giocatore1.animazione()
        #collisioni
        for bot in bots:
            giocatore1.killSTAT(bots)
            if bot.stato == False and giocatore1.collisioni(bot):
                game_over = True
            giocatore1.kill(bot)
        

    
    #AGIORNAMENTO SCHERMO
    schermo.fill(sfondo)
    
    
    #blit pavimento
    pav_base.dis_pav(schermo, giocatore1.wx, giocatore1.wy)

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


    
    #blit delle impostazioni
    if settings:
        schermo.blit(interface_imm, interface_imm_pos)
        schermo.blit(interface_wasd, interface_wasd_pos)
        schermo.blit(interface_k, interface_k_pos)
        schermo.blit(interface_x, interface_x_pos)
        schermo.blit(scritta_wasd, srcitta_wasd__pos)
        schermo.blit(scritta_kill, scritta_kill_pos)
        schermo.blit(interface_shift, interface_shift_pos)

    
    
    #aggiornamenti vari e eventuali 
    pygame.display.flip()
    pygame.display.update()
    clock.tick(6000)
