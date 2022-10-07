import pygame
from pygame.draw import *
RED = (115, 100, 100)
DGREY = (25, 25, 25)
GREY = pygame.Color(25, 25, 25, 15)
pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 750))
rect(screen, (100, 100, 100), (0, 0, 600, 320))
circle(screen, (255, 255, 255), (540, 55), 45)




#2
rect(screen, (52, 43, 0), (180, 270, 140, 200)) 
rect(screen, (50, 22, 0), (195, 410, 27, 35))
rect(screen, (50, 22, 0), (235, 410, 27, 35))
rect(screen, (200, 170, 0), (275, 410, 27, 35))
rect(screen, (35, 35, 35), (170, 350, 167, 23))
rect(screen, (115, 100, 100), (190, 270, 15, 82))
rect(screen, (115, 100, 100), (225, 270, 15, 82))
rect(screen, (115, 100, 100), (260, 270, 15, 82))
rect(screen, (115, 100, 100), (295, 270, 15, 82))
rect(screen, (0, 0, 0), (180, 255, 140, 15)) 
polygon(screen, (0, 0, 0), ([(180, 255), (180, 270), (160, 270)]))
polygon(screen, (0, 0, 0), ([(320, 255), (320, 270), (340, 270)]))

rect(screen, (35, 35, 35), (175, 325, 155, 10))
rect(screen, (35, 35, 35), (190, 330, 8, 25))
rect(screen, (35, 35, 35), (220, 330, 8, 25))
rect(screen, (35, 35, 35), (250, 330, 8, 25))
rect(screen, (35, 35, 35), (280, 330, 8, 25))
rect(screen, (35, 35, 35), (310, 330, 8, 25))
rect(screen, (35, 35, 35), (330, 335, 3, 20))
rect(screen, (35, 35, 35), (173, 335, 3, 20))

rect(screen, (35, 35, 35), (195, 235, 4, 25))
rect(screen, (35, 35, 35), (270, 240, 4, 17))
rect(screen, (35, 35, 35), (305, 235, 5, 30))
rect(screen, (35, 35, 35), (202, 220, 10, 45))
#
ellipse(screen, (80, 80, 80), (-80, 400, 350, 50))

#1
rect(screen, (52, 43, 0), (10, 360, 140, 200)) 
rect(screen, (50, 22, 0), (30, 500, 27, 35))
rect(screen, (50, 22, 0), (70, 500, 27, 35))
rect(screen, (200, 170, 0), (110, 500, 27, 35))
rect(screen, (35, 35, 35), (0, 440, 167, 23))
rect(screen, RED, (20, 360, 15, 82))
rect(screen, (115, 100, 100), (55, 360, 15, 82))
rect(screen, (115, 100, 100), (90, 360, 15, 82))
rect(screen, (115, 100, 100), (125, 360, 15, 82))

rect(screen, (35, 35, 35), (0, 415, 160, 10))
rect(screen, (35, 35, 35), (20, 420, 8, 25))
rect(screen, (35, 35, 35), (50, 420, 8, 25))
rect(screen, (35, 35, 35), (80, 420, 8, 25))
rect(screen, (35, 35, 35), (110, 420, 8, 25))
rect(screen, (35, 35, 35), (140, 420, 8, 25))
rect(screen, (35, 35, 35), (2, 420, 3, 25))
rect(screen, (35, 35, 35), (160, 420, 3, 25))

rect(screen, (35, 35, 35), (30, 323, 4, 25))
rect(screen, (35, 35, 35), (100, 330, 3, 17))
rect(screen, (35, 35, 35), (130, 322, 5, 30))
rect(screen, (35, 35, 35), (40, 310, 10, 40))

#3
rect(screen, (52, 43, 0), (450, 170, 140, 200)) 
rect(screen, (50, 22, 0), (465, 310, 27, 35))
rect(screen, (50, 22, 0), (500, 310, 27, 35))
rect(screen, (200, 170, 0), (540, 310, 27, 35))
rect(screen, (35, 35, 35), (435, 250, 200, 23))
rect(screen, (115, 100, 100), (460, 168, 15, 82))
rect(screen, (115, 100, 100), (495, 168, 15, 82))
rect(screen, (115, 100, 100), (530, 168, 15, 82))
rect(screen, (115, 100, 100), (565, 168, 15, 82))
rect(screen, (0, 0, 0), (450, 160, 140, 15)) 
polygon(screen, (0, 0, 0), ([(450, 160), (430, 175), (450, 175)]))
polygon(screen, (0, 0, 0), ([(590, 160), (590, 175), (610, 175)]))

rect(screen, (35, 35, 35), (445, 225, 155, 10))
rect(screen, (35, 35, 35), (460, 230, 8, 25))
rect(screen, (35, 35, 35), (490, 230, 8, 25))
rect(screen, (35, 35, 35), (525, 230, 8, 25))
rect(screen, (35, 35, 35), (550, 230, 8, 25))
rect(screen, (35, 35, 35), (580, 230, 8, 25))
rect(screen, (35, 35, 35), (442, 235, 3, 20))

rect(screen, (60, 60, 60), (465, 135, 4, 25))
rect(screen, (60, 60, 60), (540, 143, 4, 17))
rect(screen, (60, 60, 60), (575, 135, 5, 30))
rect(screen, (60, 60, 60), (475, 120, 10, 45))

ellipse(screen, (80, 80, 80), (330, 100, 400, 45))
ellipse(screen, GREY, (250, 160, 400, 50))
ellipse(screen, (50, 50, 50), (30, 55, 465, 55))
ellipse(screen, (80, 80, 80), (230, 35, 370, 50))

ellipse(screen, (80, 80, 80), (100, 285, 530, 50))
ellipse(screen, (80, 80, 80), (230, 350, 450, 50))



#ghost



circle(screen, (190, 190, 190), (415, 570), 15)
circle(screen, (190, 190, 190), (425, 608), 35)
rect(screen, (0, 0, 0), (390, 630, 55, 40))

circle(screen, '#87CEFA', (412, 570), 5)
circle(screen, (255, 255, 255), (412, 569), 2)
circle(screen, (0, 0, 0), (410, 570), 1)

circle(screen, '#87CEFA', (425, 567), 5)
circle(screen, (255, 255, 255), (425, 568), 2)
circle(screen, (0, 0, 0), (422, 567), 1)

ellipse(screen, (190, 190, 190), (397, 625, 15, 10))
ellipse(screen, 'black', (412, 625, 15, 10))
ellipse(screen, (190, 190, 190), (427, 625, 15, 10))
ellipse(screen, 'black', (442, 625, 15, 10))


circle(screen, (190, 190, 190), (480, 570), 20)
circle(screen, (190, 190, 190), (500, 625), 55)

rect(screen, (0, 0, 0), (430, 655, 200, 90))


circle(screen, '#87CEFA', (470, 568), 6)
circle(screen, (255, 255, 255), (473, 567), 3)
circle(screen, (0, 0, 0), (469, 568), 2)

circle(screen, '#87CEFA', (487, 565), 6)
circle(screen, (255, 255, 255), (488, 565), 3)
circle(screen, (0, 0, 0), (485, 565), 2)

ellipse(screen, (190, 190, 190), (455, 645, 22, 15))
ellipse(screen, 'black', (477, 645, 22, 15))
ellipse(screen, (190, 190, 190), (499, 645, 22, 15))
ellipse(screen, 'black', (521, 645, 22, 15))





circle(screen, (190, 190, 190), (100, 600), 15)
circle(screen, (190, 190, 190), (100, 635), 35)

rect(screen, (0, 0, 0), (65, 645, 75, 30))


circle(screen, '#87CEFA', (105, 600), 4)
circle(screen, (255, 255, 255), (106, 600), 1)
circle(screen, (0, 0, 0), (107, 600), 1)

circle(screen, '#87CEFA', (95, 600), 4)
circle(screen, (255, 255, 255), (96, 600), 1)
circle(screen, (0, 0, 0), (97, 600), 1)

ellipse(screen, (190, 190, 190), (65, 640, 15, 10))
ellipse(screen, 'black', (80, 640, 15, 10))
ellipse(screen, (190, 190, 190), (95, 640, 15, 10))
ellipse(screen, 'black', (110, 640, 15, 10))


circle(screen, (190, 190, 190), (150, 620), 15)
circle(screen, (190, 190, 190), (145, 655), 35)

rect(screen, (0, 0, 0), (105, 665, 75, 30))

circle(screen, '#87CEFA', (155, 620), 4)
circle(screen, (255, 255, 255), (156, 621), 1)
circle(screen, (0, 0, 0), (157, 622), 1)

circle(screen, '#87CEFA', (145, 620), 4)
circle(screen, (255, 255, 255), (146, 621), 1)
circle(screen, (0, 0, 0), (147, 622), 1)

ellipse(screen, (190, 190, 190), (110, 660, 15, 10))
ellipse(screen, 'black', (125, 660, 15, 10))
ellipse(screen, (190, 190, 190), (140, 660, 15, 10))
ellipse(screen, 'black', (155, 660, 15, 10))


circle(screen, (190, 190, 190), (525, 435), 20)
circle(screen, (190, 190, 190), (530, 475), 45)

#rect(screen, (0, 0, 0), (65, 645, 75, 30))


circle(screen, '#87CEFA', (532, 430), 5)
circle(screen, (255, 255, 255), (531, 431), 2)
circle(screen, (0, 0, 0), (529, 432), 1)

circle(screen, '#87CEFA', (520, 430), 5)
circle(screen, (255, 255, 255), (521, 431), 2)
circle(screen, (0, 0, 0), (518, 432), 1)

#ellipse(screen, (190, 190, 190), (65, 640, 15, 10))
#ellipse(screen, 'black', (80, 640, 15, 10))
#ellipse(screen, (190, 190, 190), (95, 640, 15, 10))
#ellipse(screen, 'black', (110, 640, 15, 10))


circle(screen, (190, 190, 190), (550, 485), 20)
circle(screen, (190, 190, 190), (550, 525), 45)

rect(screen, (0, 0, 0), (500, 535, 95, 35))

circle(screen, '#87CEFA', (557, 480), 5)
circle(screen, (255, 255, 255), (556, 481), 2)
circle(screen, (0, 0, 0), (554, 482), 1)

circle(screen, '#87CEFA', (545, 480), 5)
circle(screen, (255, 255, 255), (546, 481), 2)
circle(screen, (0, 0, 0), (544, 482), 1)

ellipse(screen, (190, 190, 190), (505, 530, 15, 10))
ellipse(screen, 'black', (520, 530, 15, 10))
ellipse(screen, (190, 190, 190), (535, 530, 15, 10))
ellipse(screen, 'black', (550, 530, 15, 10))
ellipse(screen, (190, 190, 190), (565, 530, 15, 10))
ellipse(screen, 'black', (580, 530, 15, 10))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

