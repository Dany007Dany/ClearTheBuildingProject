import pygame
from sys import exit


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


#personaggio principale
perc_p1 = "/Users/dany/Downloads/CtB images/P1.png"
image_p1 = pygame.image.load(perc_p1)
image_p1 = pygame.transform.scale(image_p1, (80, 80))
image_p1.convert_alpha()






while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #blit del personaggio
    schermo.blit(image_p1, (0, 0))
    pygame.display.flip()
    pygame.display.update()
    clock.tick
