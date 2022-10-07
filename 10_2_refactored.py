import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))

#переменные
color_sky = (31, 241, 244)
color_grass = (27, 248, 31)
color_sun = (255, 255, 102)
color_leaves = (5, 70, 2)
color_apples = (244, 148, 205)
color_trunk = (255, 255, 255)
color_leaves_outline = (134, 166, 89)
color_unic_body = (255, 255, 255)
color_hair_1 = (244, 148, 205)
color_hair_2 = (202, 123, 223)
color_hair_3 = (157, 141, 207)
color_sclera = (244, 148, 205)
color_iris = (255, 255, 255)
color_horn = (157, 141, 207)
color_pupil = (0, 0, 0)

x_uni_dist_right = 400         #дальний правый единорог
y_uni_dist_right = 195                  
N_uni_dist_right = 2.5
x_uni_dist_left = 250          #дальний левый
y_uni_dist_left = 225
N_uni_dist_left = 2
x_uni_close_left = 150         #ближний левый
y_uni_close_left = 350 
N_uni_close_left = 1
x_uni_close_right = 350        #ближний правый
y_uni_close_right = 300
N_uni_close_right= 1.2

x_dist_tree = 150              #дальнее дерево
y_dist_tree = 150
N_dist_tree = 1.5
x_central_left_tree = 175      #центральное левое дерево
y_central_left_tree = 263
N_central_left_tree = 2
x_central_right_tree = 25      #центральное правое дерево
y_central_right_tree = 275
N_central_right_tree = 2
x_second_close_tree = 115      #второе спереди дерево
y_second_close_tree = 330
N_second_close_tree = 1.8
x_close_tree = 50              #ближнее дерево
y_close_tree = 390
N_close_tree = 2




#фон
rect(screen, color_sky, (0, 0, 500, 500))
rect(screen, color_grass, (0, 200, 500, 300))


#солнце

for i in range(0, 100):
    sun = pygame.Surface((500, 160))
    sun.fill(color_sky)
    sun.set_colorkey((255, 175, 45))
    sun.set_alpha(75 - i / 0.9)
    circle(sun, color_sun, (320, 70), i)
    screen.blit(sun, (75, 0))
    


#правый единорог

def unicorn_right(screen, x, y, N, color):
    ellipse(screen, color, (x, y, 150 // N, 60 // N))
    rect(screen, color, (x + 115 // N, y - 40 // N, 30 // N, 60 // N))
    circle(screen, color, (x + 140 // N, y - 40 // N), 15 // N)
    ellipse(screen, color,
                        (x + 140 // N, y - 45 // N, 30 // N, 15 // N))
    ellipse(screen, color_hair_1,
                        (x + 110 // N, y - 60 // N, 30 // N, 15 // N))
    ellipse(screen, color_hair_1,
                        (x + 100 // N, y - 50 // N, 30 // N, 15 // N))
    ellipse(screen, color_hair_1,
                        (x + 90 // N, y - 40 // N, 40 // N, 15 // N))
    ellipse(screen, color_hair_1,
                        (x + 100 // N, y - 20 // N, 30 // N, 10 // N))
    ellipse(screen, color_hair_2,
                        (x + 80 // N, y - 20 // N, 40 // N, 10 // N))
    ellipse(screen, color_hair_1,
                        (x + 85 // N, y - 30 // N, 35 // N, 10 // N))
    ellipse(screen, color_hair_1,
                        (x + 70 // N, y - 7 // N, 40 // N, 10 // N))
    ellipse(screen, color_hair_3,
                        (x + 92 // N, y - 25 // N, 40 // N, 10 // N))
    ellipse(screen, color_hair_1,
                        (x + 90 // N, y - 10 // N, 40 // N, 15 // N))
    ellipse(screen, color_hair_3,
                        (x + 80 // N, y - 15 // N, 40 // N, 10 // N))
    ellipse(screen, color_hair_3,
                        (x + 83 // N, y, 40 // N, 10 // N))
    ellipse(screen, color_hair_3,
                        (x + 107 // N, y - 43 // N, 27 // N, 10 // N))
    ellipse(screen, color_hair_2,
                        (x + 95 // N, y - 35 // N, 20 // N, 7 // N))
    ellipse(screen, color_hair_1,
                        (x + 10 // N, y, 30 // N, 15 // N))
    ellipse(screen, color_hair_1,
                        (x, y + 10 // N, 30 // N, 15 // N))
    ellipse(screen, color_hair_1,
                        (x - 10 // N, y + 20 // N, 40 // N, 15 // N))
    ellipse(screen, color_hair_1,
                        (x, y + 40 // N, 30 // N, 10 // N))
    ellipse(screen, color_hair_2,
                        (x - 20 // N, y + 40 // N, 40 // N, 10 // N))
    ellipse(screen, color_hair_1,
                        (x - 15 // N, y + 30 // N, 35 // N, 10 // N))
    ellipse(screen, color_hair_1,
                        (x - 30 // N, y + 53 // N, 40 // N, 10 // N))
    ellipse(screen, color_hair_3,
                        (x - 8 // N, y + 35 // N, 40 // N, 10 // N))
    ellipse(screen, color_hair_1,
                        (x - 10 // N, y + 50 // N, 40 // N, 15 // N))
    ellipse(screen, color_hair_3,
                        (x - 20 // N, y + 45 // N, 40 // N, 10 // N))
    ellipse(screen, color_hair_3,
                        (x - 17 // N, y + 60 // N, 40 // N, 10 // N))
    ellipse(screen, color_hair_3,
                        (x + 7 // N, y + 17 // N, 27 // N, 10 // N))
    ellipse(screen, color_hair_2,
                        (x - 5 // N, y + 25 // N, 20 // N, 7 // N))
    rect(screen, color, (x + 105 // N, y + 20 // N, 10 // N, 70 // N))
    rect(screen, color, (x + 130 // N, y + 40 // N, 10 // N, 70 // N))
    rect(screen, color, (x + 35 // N, y + 20 // N, 10 // N, 70 // N))
    rect(screen, color, (x + 60 // N, y + 40 // N, 10 // N, 70 // N))
    circle(screen, color_sclera, (x + 142 // N, y - 42 // N), 7 // N)
    ellipse(screen, color_iris,
                        (x + 138 // N, y - 42 // N, 9 // N, 2 // N))
    circle(screen, color_pupil, (x + 147 // N, y - 42 // N), 3 // N)
    polygon(
        screen, color_horn,
        [[x + 132 // N, y - 55 // N], [x + 140 // N, y - 55 // N],
         [x + 145 // N, y - 90 // N]])


#левый единорог

def unicorn_left(screen, x, y, N, color):
    x = x + 150 // N
    ellipse(screen, color, (x - 150 // N, y, 150 // N, 60 // N))
    rect(screen, color, (x - 145 // N, y - 40 // N, 30 // N, 60 // N))
    circle(screen, color, (x - 140 // N, y - 40 // N), 15 // N)
    ellipse(screen, color,
                        (x - 170 // N, y - 45 // N, 30 // N, 15 // N))
    ellipse(screen, color_hair_1,
                        (x - 140 // N, y - 60 // N, 30 // N, 15 // N))
    ellipse(screen, color_hair_1,
                        (x - 130 // N, y - 50 // N, 30 // N, 15 // N))
    ellipse(screen, color_hair_1,
                        (x - 130 // N, y - 40 // N, 40 // N, 15 // N))
    ellipse(screen, color_hair_1,
                        (x - 130 // N, y - 20 // N, 30 // N, 10 // N))
    ellipse(screen, color_hair_2,
                        (x - 120 // N, y - 20 // N, 40 // N, 10 // N))
    ellipse(screen, color_hair_1,
                        (x - 120 // N, y - 30 // N, 35 // N, 10 // N))
    ellipse(screen, color_hair_1,
                        (x - 110 // N, y - 7 // N, 40 // N, 10 // N))
    ellipse(screen, color_hair_3,
                        (x - 132 // N, y - 25 // N, 40 // N, 10 // N))
    ellipse(screen, color_hair_1,
                        (x - 130 // N, y - 10 // N, 40 // N, 15 // N))
    ellipse(screen, color_hair_3,
                        (x - 120 // N, y - 15 // N, 40 // N, 10 // N))
    ellipse(screen, color_hair_3,
                        (x - 123 // N, y, 40 // N, 10 // N))
    ellipse(screen, color_hair_3,
                        (x - 134 // N, y - 43 // N, 27 // N, 10 // N))
    ellipse(screen, color_hair_2,
                        (x - 115 // N, y - 35 // N, 20 // N, 7 // N))
    ellipse(screen, color_hair_1,
                        (x - 40 // N, y, 30 // N, 15 // N))
    ellipse(screen, color_hair_1,
                        (x - 30 // N, y + 10 // N, 30 // N, 15 // N))
    ellipse(screen, color_hair_1,
                        (x - 30 // N, y + 20 // N, 40 // N, 15 // N))
    ellipse(screen, color_hair_1,
                        (x - 30 // N, y + 40 // N, 30 // N, 10 // N))
    ellipse(screen, color_hair_2,
                        (x - 20 // N, y + 40 // N, 40 // N, 10 // N))
    ellipse(screen, color_hair_1,
                        (x - 20 // N, y + 30 // N, 35 // N, 10 // N))
    ellipse(screen, color_hair_1,
                        (x - 10 // N, y + 53 // N, 40 // N, 10 // N))
    ellipse(screen, color_hair_3,
                        (x - 32 // N, y + 35 // N, 40 // N, 10 // N))
    ellipse(screen, color_hair_1,
                        (x - 30 // N, y + 50 // N, 40 // N, 15 // N))
    ellipse(screen, color_hair_3,
                        (x - 20 // N, y + 45 // N, 40 // N, 10 // N))
    ellipse(screen, color_hair_3,
                        (x - 23 // N, y + 60 // N, 40 // N, 10 // N))
    ellipse(screen, color_hair_3,
                        (x - 20 // N, y + 17 // N, 27 // N, 10 // N))
    ellipse(screen, color_hair_2,
                        (x - 15 // N, y + 25 // N, 20 // N, 7 // N))
    rect(screen, color, (x - 115 // N, y + 20 // N, 10 // N, 70 // N))
    rect(screen, color, (x - 140 // N, y + 40 // N, 10 // N, 70 // N))
    rect(screen, color, (x - 45 // N, y + 20 // N, 10 // N, 70 // N))
    rect(screen, color, (x - 70 // N, y + 40 // N, 10 // N, 70 // N))
    circle(screen, color_sclera, (x - 142 // N, y - 42 // N), 7 // N)
    ellipse(screen, color_iris,
                        (x - 147 // N, y - 42 // N, 9 // N, 2 // N))
    circle(screen, color_pupil, (x - 147 // N, y - 42 // N), 3 // N)
    polygon(
        screen, color_horn,
        [[x - 132 // N, y - 55 // N], [x - 140 // N, y - 55 // N],
         [x - 145 // N, y - 90 // N]])


#деревья

def tree(screen, color_leaves, color_apples, color_trunk, x, y, N):
    rect(screen, color_trunk, (x, y, 30 // N, 100 // N))
    ellipse(screen, color_leaves,
                        (x - 45 // N, y - 230 // N, 120 // N, 150 // N))
    ellipse(screen, color_leaves_outline,
                        (x - 45 // N, y - 230 // N, 120 // N, 150 // N), 2)     #верхний овал
    ellipse(screen, color_leaves,
                        (x - 85 // N, y - 150 // N, 200 // N, 100 // N))
    ellipse(screen, color_leaves_outline,
                        (x - 85 // N, y - 150 // N, 200 // N, 100 // N), 2)     #средний овал
    ellipse(screen, color_leaves,
                        (x - 45 // N, y - 80 // N, 120 // N, 100 // N))
    ellipse(screen, color_leaves_outline,
                        (x - 45 // N, y - 80 // N, 120 // N, 100 // N), 2)      #нижний овал
    circle(screen, color_apples, (x + 30 // N, y - 180 // N), 15 // N)
    circle(screen, color_apples, (x + 50 // N, y - 20 // N), 15 // N)
    circle(screen, color_apples, (x + 75 // N, y - 90 // N), 15 // N)
    circle(screen, color_apples, (x - 45 // N, y - 100 // N), 15 // N)


#вызываем рисунки

unicorn_left(screen, x_uni_dist_right, y_uni_dist_right, N_uni_dist_right, color_unic_body)    #дальний правый
unicorn_right(screen, x_uni_dist_left, y_uni_dist_left, N_uni_dist_left, color_unic_body)     #дальний левый
unicorn_right(screen, x_uni_close_left, y_uni_close_left, N_uni_close_left, color_unic_body)     #ближний левый
unicorn_left(screen, x_uni_close_right, y_uni_close_right, N_uni_close_right, color_unic_body)    #ближний правый

tree(screen, color_leaves, color_apples, color_trunk, x_dist_tree, y_dist_tree, N_dist_tree)   #дальнее дерево
tree(screen, color_leaves, color_apples, color_trunk, x_central_left_tree, y_central_left_tree, N_central_left_tree)     #центральное правое дерево
tree(screen, color_leaves, color_apples, color_trunk, x_central_right_tree, y_central_right_tree, N_central_right_tree)      #центральное левое дерево
tree(screen, color_leaves, color_apples, color_trunk, x_second_close_tree, y_second_close_tree, N_second_close_tree)   #второе спереди дерево
tree(screen, color_leaves, color_apples, color_trunk, x_close_tree, y_close_tree, N_close_tree)      #ближнее дерево

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()