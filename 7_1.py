import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 750))
rect(screen, (100, 100, 100), (0, 0, 600, 315))
ellipse(screen, (25, 25, 25), (250, 180, 400, 50))
rect(screen, (52, 43, 0), (30, 150, 280, 393)) 
rect(screen, (50, 22, 0), (60, 420, 55, 70))
rect(screen, (50, 22, 0), (145, 420, 55, 70))
rect(screen, (200, 170, 0), (225, 420, 55, 70))
rect(screen, (30, 30, 30), (0, 316, 345, 40))
circle(screen, (255, 255, 255), (530, 70), 45)
rect(screen, (0, 0, 0), (50, 115, 240, 35)) 
polygon(screen, (0, 0, 0), ([(50, 115), (50, 150), (0, 150)]))
polygon(screen, (0, 0, 0), ([(290, 115), (290, 150), (340, 150)]))
rect(screen, (115, 100, 100), (50, 150, 27, 166))
rect(screen, (115, 100, 100), (110, 150, 27, 166))
rect(screen, (115, 100, 100), (170, 150, 27, 166))
rect(screen, (115, 100, 100), (235, 150, 27, 166))

rect(screen, (30, 30, 30), (20, 256, 300, 20))
rect(screen, (30, 30, 30), (50, 276, 20, 40))
rect(screen, (30, 30, 30), (100, 276, 19, 40))
rect(screen, (30, 30, 30), (149, 276, 19, 40))
rect(screen, (30, 30, 30), (210, 276, 20, 40))
rect(screen, (30, 30, 30), (260, 276, 20, 40))
rect(screen, (30, 30, 30), (10, 276, 10, 40))
rect(screen, (30, 30, 30), (320, 276, 10, 40))

rect(screen, (30, 30, 30), (70, 87, 12, 45))
rect(screen, (30, 30, 30), (200, 85, 12, 30))
ellipse(screen, (80, 80, 80), (350, 115, 400, 45))
ellipse(screen, (50, 50, 50), (30, 45, 470, 55))
ellipse(screen, (80, 80, 80), (230, 30, 350, 50))
rect(screen, (30, 30, 30), (250, 75, 12, 60))
rect(screen, (30, 30, 30), (90, 40, 20, 95))
#ghost
circle(screen, (190, 190, 190), (480, 560), 30)
circle(screen, (190, 190, 190), (500, 625), 75)
circle(screen, (0, 0, 0), (450, 690), 35)
circle(screen, (0, 0, 0), (510, 690), 30)
circle(screen, (0, 0, 0), (550, 670), 25)
circle(screen, (0, 0, 0), (365, 585), 70)
circle(screen, (0, 0, 0), (760, 555), 200)


circle(screen, (0, 250, 250), (465, 555), 6)
circle(screen, (255, 250, 250), (466, 555), 3)
circle(screen, (0, 0, 0), (465, 555), 2)

circle(screen, (0, 250, 250), (490, 550), 6)
circle(screen, (255, 250, 250), (492, 550), 3)
circle(screen, (0, 0, 0), (490, 550), 2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()


