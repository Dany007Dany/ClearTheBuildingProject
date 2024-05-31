import pygame
from sys import exit
from Classi_Giocatore_e_Bot import Giocatore
from Classi_Giocatore_e_Bot import Bot
from Classi_Mappa_e_Ostacolo import Pavimento
from Classi_Mappa_e_Ostacolo import Ostacolo
from os.path import join
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.init()
#clock
clock = pygame.time.Clock()

#DEVs' tool
dev = False

#creazione finestra 
info = pygame.display.Info()
altezza = 700
larghezza = 1300
dimensioni = (larghezza, altezza)
schermo = pygame.display.set_mode(dimensioni)


#personalizzazione finestra
sfondo = ("Grey")
pygame.display.set_caption("Clear the Building!")
prog_icon = pygame.image.load("CtB images/Icon.png").convert_alpha()
pygame.display.set_icon(prog_icon)
ombra = pygame.image.load("CtB images/Ombra.png").convert_alpha()

#musics and sound effects
background_music = pygame.mixer.music.load("Audio CtB/Theme.mp3")
background_music = pygame.mixer.music.set_volume(0.2)
kill_sound = pygame.mixer.Sound("Audio CtB/Kill-Sound.mp3")
kill_sound.set_volume(0.2)

win_sound = pygame.mixer.Sound("Audio CtB/Mission_Accomplished.mp3")
win_sound.set_volume(0.2)

pygame.mixer.music.play()
#città
imm_città = pygame.image.load("CtB images/sci_riproviamo.jpg")

città_ost = Ostacolo(imm_città, -larghezza // 4, -altezza // 2)


#pavimento
pav_base = Pavimento(larghezza//4,0)

#freccia + scritta
fnt = pygame.font.Font("Bleeding_Cowboys.ttf", 42)
fnt2 = pygame.font.Font("Bleeding_Cowboys.ttf", 21)
txt_rnd = fnt.render("Da questa parte", True, "firebrick3")
imm_frcc = pygame.image.load("CtB images/Freccia.png").convert_alpha()
imm_ost_frcc = Ostacolo(imm_frcc, larghezza//2.5, -50)
txt_ost = Ostacolo(txt_rnd,larghezza//1.8,pav_base.rect_pav.height // 14.5)
txt_rnd2 = fnt2.render("Guarda i comandi premendo", True, "firebrick3")
txt_ost2 = Ostacolo(txt_rnd2, larghezza + larghezza//25,pav_base.rect_pav.height // 14.5)


#creazione bot
bot1 = Bot(x = 4000, y = 350, orientamento = 90, stato = False)
bot2 = Bot(x = larghezza // 4 + pav_base.rect_pav.width // 3, y = pav_base.rect_pav.height // 14.5, orientamento = -90, stato = False)
bot3 = Bot(x = pav_base.rect_pav.width//2 - 100, y = pav_base.rect_pav.height//2 - 50, orientamento = 90, stato = False)
bot4 = Bot(x = 1450, y = 3700, orientamento = -90, stato = False)
#5 e 3
bot5 = Bot(x = pav_base.rect_pav.width//2 + 650, y = pav_base.rect_pav.height//2 - 50, orientamento = -90, stato = False)
bot6 = Bot(x = pav_base.rect_pav.width//4 - 470, y = pav_base.rect_pav.height - 800, orientamento = 0, stato = False)
bot7 = Bot(x = pav_base.rect_pav.width-pav_base.rect_pav.width//5 + 325, y = pav_base.rect_pav.height - 950, orientamento = 180, stato = False)
bot8 = Bot(x = pav_base.rect_pav.width//2 + 240, y = pav_base.rect_pav.height - 780, orientamento = -90, stato = False)
bot9 = Bot(x = 3825, y = pav_base.rect_pav.height//2, orientamento = 0, stato = False)
bot10 = Bot(x = larghezza // 4 + pav_base.rect_pav.width*2//3 - 150, y = pav_base.rect_pav.height // 4 , orientamento = 0, stato = False)


bots = [bot1, bot2, bot3, bot4, bot5, bot6, bot7, bot8, bot9, bot10]

#immagini muri
imm_ostacolo_1_orizzontale = pygame.surface.Surface((4040, 20))
imm_ostacolo_1_orizzontale.fill("Grey20")
imm_ostacolo_2_verticale = pygame.surface.Surface((20, 4000))
imm_ostacolo_2_verticale.fill("Grey20")
imm_ostacolo_3_orizzontale = pygame.surface.Surface((2000, 20))
imm_ostacolo_3_orizzontale.fill("Grey20")
imm_ostacolo_4_verticale = pygame.surface.Surface((20, 2000))
imm_ostacolo_4_verticale.fill("Grey20")
imm_ostacolo_5_orizzontale = pygame.surface.Surface((3500, 20))
imm_ostacolo_5_orizzontale.fill("Grey20")
imm_ostacolo_6_orizzontale = pygame.surface.Surface((3300,20))
imm_ostacolo_6_orizzontale.fill("Grey20")
imm_ostacolo_7_vericale = pygame.surface.Surface((20,800))
imm_ostacolo_7_vericale.fill("Grey20")
imm_ostacolo_8_orizzontale = pygame.surface.Surface((800,20))
imm_ostacolo_8_orizzontale.fill("Grey20")
imm_ostacolo_9_orizzontale = pygame.surface.Surface((2000,20))
imm_ostacolo_9_orizzontale.fill("Grey20")
imm_ostacolo_10_verticale = pygame.surface.Surface((20,800))
imm_ostacolo_10_verticale.fill("Grey20")
imm_ostacolo_11_orizziontale = pygame.surface.Surface((1120,20))
imm_ostacolo_11_orizziontale.fill("lightskyblue1")

#immagini arredamenti
imm_scrivaniaadangolo = pygame.image.load("CtB images/ScrivaniaAngolo.png")
imm_scrivaniaadangolo = pygame.transform.scale(imm_scrivaniaadangolo, (200, 200))
imm_scrivania = pygame.image.load("CtB images/Scrivania.png")
imm_scrivania = pygame.transform.scale(imm_scrivania, (250,200))
imm_scrivaniaRT = pygame.transform.rotate(imm_scrivania, 90)
imm_pianta = pygame.image.load("CtB images/Pianta.png")
imm_scaffale = pygame.image.load("CtB images/Scaffale.png")
imm_tavolo = pygame.image.load("CtB images/Tavolo.png")
imm_tavolo = pygame.transform.scale(imm_tavolo, (350,250))


#muri esterni
ostacolo_1_muro = Ostacolo(imm_ostacolo_1_orizzontale, larghezza//4 - 20,0)
ostacolo_2_muro = Ostacolo(imm_ostacolo_2_verticale, larghezza//4, 0)
ostacolo_3_muro = Ostacolo(imm_ostacolo_1_orizzontale, larghezza//4, 4000)
ostacolo_4_muro = Ostacolo(imm_ostacolo_2_verticale, larghezza//4 + 4000, 0)
#muri interi
ostacolo_5_muro = Ostacolo(imm_ostacolo_3_orizzontale, larghezza//4, pav_base.rect_pav.height//4.9 - altezza//4)
ostacolo_6_muro = Ostacolo(imm_ostacolo_4_verticale, 3400, 500)
ostacolo_7_muro = Ostacolo(imm_ostacolo_5_orizzontale, pav_base.rect_pav.width//3 - 500, -altezza//2 + 2850)
ostacolo_8_muro = Ostacolo(imm_ostacolo_6_orizzontale,pav_base.rect_pav.width//3 - 500,pav_base.rect_pav.height*3//4)
ostacolo_9_muro = Ostacolo(imm_ostacolo_7_vericale,pav_base.rect_pav.width//3,pav_base.rect_pav.height*3//4)
ostacolo_10_muro = Ostacolo(imm_ostacolo_8_orizzontale, larghezza//4,pav_base.rect_pav.height - 500)
ostacolo_11_muro = Ostacolo(imm_ostacolo_9_orizzontale,1400 ,(pav_base.rect_pav.height//4.9 - altezza//4)*2)
ostacolo_12_muro = Ostacolo(imm_ostacolo_10_verticale,pav_base.rect_pav.width-pav_base.rect_pav.width//4,pav_base.rect_pav.height - 800)
ostacolo_13_muro = Ostacolo(imm_ostacolo_11_orizziontale,pav_base.rect_pav.width-pav_base.rect_pav.width//4 +20,pav_base.rect_pav.height - 650)
#arredamenti
ostacolo_14_pianta = Ostacolo(imm_pianta, larghezza//4,pav_base.rect_pav.height - 480)
ostacolo_15_pianta = Ostacolo(imm_pianta, pav_base.rect_pav.width-pav_base.rect_pav.width//4 + 20,pav_base.rect_pav.height - 800)
ostacolo_16_pianta = Ostacolo(imm_pianta,1400 - 40,(pav_base.rect_pav.height//4.9 - altezza//4)*2 - 10)
ostacolo_17_pianta = Ostacolo(imm_pianta,3400 - 40,(pav_base.rect_pav.height//4.9 - altezza//4)*2 - 40)
ostacolo_18_pianta = Ostacolo(imm_pianta, 3390, 2520)
ostacolo_19_tavolo_riunioni = Ostacolo(imm_tavolo, 3700, pav_base.rect_pav.height//2 - 1050)
ostacolo_20_tavolo_riunioni = Ostacolo(imm_tavolo,pav_base.rect_pav.width//2 + 150,pav_base.rect_pav.height//2 - 130)
ostacolo_21_scrivania = Ostacolo(imm_scrivania,pav_base.rect_pav.width//3 - 245,pav_base.rect_pav.height*3//4 + 10)
ostacolo_22_scrivania = Ostacolo(imm_scrivaniaRT,315,pav_base.rect_pav.height*3//4 + 260)
ostacolo_23_tavolo_riunioni = Ostacolo(imm_tavolo,615,pav_base.rect_pav.height*3//4 + 640)



#ostacoli
ostacolo_1 = Ostacolo(imm_scrivaniaadangolo, 350, 400)

lst_ost = [ostacolo_5_muro, ostacolo_6_muro, ostacolo_7_muro, ostacolo_8_muro, ostacolo_9_muro, ostacolo_10_muro, ostacolo_11_muro, ostacolo_12_muro,ostacolo_13_muro, ostacolo_14_pianta, ostacolo_15_pianta, ostacolo_16_pianta, ostacolo_17_pianta, ostacolo_18_pianta, ostacolo_19_tavolo_riunioni, ostacolo_20_tavolo_riunioni, ostacolo_21_scrivania, ostacolo_22_scrivania, ostacolo_23_tavolo_riunioni]

ostacoli = [ostacolo_1]

#creazione del giocatore
giocatore1 = Giocatore(altezza, larghezza, lst_ost)

#immagine "Sei stato scoperto!"
SSS_immagine = pygame.image.load("CtB images/SSS.jpg").convert_alpha()
SSS_immagine = pygame.transform.scale(SSS_immagine, (800, 200))
SSS_rect = SSS_immagine.get_rect()
SSS_pos = (larghezza // 2 - SSS_rect.width // 2, altezza // 2 - SSS_rect.height // 2 - 100)
game_over = False

#immagine "you won"!
imm_you_won = pygame.image.load("CtB images/You_Won.png")
imm_you_won = pygame.transform.scale(imm_you_won, (1000, 250))
rect_you_won = imm_you_won.get_rect()
imm_you_won_pos = (larghezza // 2 - rect_you_won.width // 2, altezza // 2 - rect_you_won.height // 2)
win = False
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
#setting_tutorial
bottone_ost = Ostacolo(stg_img, larghezza + larghezza//8.5,pav_base.rect_pav.height // 13.5)
#lascia gioco
font_leave = pygame.font.Font("SIXTY.TTF", 40)
leave_render = font_leave.render("Premi Sp_azio per uscire", True, "White")





#ciclo principale
while True:
    for event in pygame.event.get():
        #if event.type == pygame.QUIT:
            #pygame.quit()
            #exit()
            
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

    
        
    cont = 0
    for bot in bots:
        if bot.stato == True:
            cont += 1
        

    
    
    #modifiche e movimento al giocatore
    if not game_over:
        giocatore1.mov(rectpav = pav_base.rect_pav)
        giocatore1.animazione()
        
        #collisioni
        for bot in bots:
            giocatore1.killSTAT(bots)
            if bot.stato == False and giocatore1.collisioni(bot):
                game_over = True
                pygame.mixer.music.stop()
                you_lost_music = pygame.mixer.music.load("Audio CtB/Mission Failed.mp3")
                you_lost_music = pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.play(-1)
            giocatore1.kill(bot)
            if giocatore1.kill(bot):    
                kill_sound.play()


    
    #AGIORNAMENTO SCHERMO
    #contatore
 
    
    schermo.fill(sfondo)
    
    città_ost.disegna(schermo, giocatore1.wx, giocatore1.wy)

    #blit pavimento
    pav_base.dis_pav(schermo, giocatore1.wx, giocatore1.wy)

    #blit scritta
    bottone_ost.disegna(schermo, giocatore1.wx, giocatore1.wy)
    txt_ost.disegna(schermo, giocatore1.wx, giocatore1.wy)
    imm_ost_frcc.disegna(schermo, giocatore1.wx, giocatore1.wy)
    txt_ost2.disegna(schermo, giocatore1.wx, giocatore1.wy)
    
    
    #blit muri esterni
    ostacolo_1_muro.disegna(schermo, giocatore1.wx, giocatore1.wy + ostacolo_1_muro.rect.height)
    ostacolo_2_muro.disegna(schermo, giocatore1.wx + ostacolo_2_muro.rect.width, giocatore1.wy)
    ostacolo_3_muro.disegna(schermo, giocatore1.wx + ostacolo_3_muro.rect.height, giocatore1.wy)
    ostacolo_4_muro.disegna(schermo, giocatore1.wx, giocatore1.wy)
    #blit muri interni

    for ostacolo in lst_ost:
        ostacolo.disegna(schermo,giocatore1.wx,giocatore1.wy)
    



    #blit dei bot
    for bot in bots:
        bot.disegna(schermo, giocatore1.wx, giocatore1.wy)


    #blit del personaggio
    giocatore1.disegna_gioc(schermo)
    
    
    if cont == len(bots):
        win = True
    if win:
        pygame.mixer.music.stop()

        win_sound.play()
        
        schermo.fill("Black")
        schermo.blit(imm_you_won, imm_you_won_pos)
        schermo.blit(leave_render,(larghezza // 2 - leave_render.get_width() // 2, altezza // 1.3))
        tastiera = pygame.key.get_pressed()
        if tastiera[pygame.K_SPACE]:
            pygame.quit()
            exit()

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

        

    if not dev: schermo.blit(ombra, (0, 0))
    if not game_over and not win and not settings:
        giocatore1.disegna_kill(schermo)

    #blit settings
    schermo.blit(stg_img, stg_pos)
    if not game_over and not win and not settings: 
        font = pygame.font.Font("SIXTY.TTF", 55)
        kills = font.render(f"Kills: {cont}", True, "White")
        schermo.blit(kills, (10,10))  
    #blit delle impostazioni
    if settings:
        schermo.blit(interface_imm, interface_imm_pos)
        schermo.blit(interface_x, interface_x_pos)
        schermo.blit(interface_exit_game, interface_exit_pos)


    
    
    #aggiornamenti vari e eventuali 
    pygame.display.flip()
    pygame.display.update()
    clock.tick(240)
