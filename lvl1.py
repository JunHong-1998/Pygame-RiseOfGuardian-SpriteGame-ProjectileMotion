from tkinter import *
import os
# import pygame
import pygame.font
from ball import *
from needle import *
from rectangle import *
from enermy import *

pygame.init()

wScreen = 1400
hScreen = 750
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (70, 50)
win = pygame.display.set_mode((wScreen, hScreen))
pygame.display.set_caption('MCG')

import pygame

def recharge():
    golfBall.x = 100
    golfBall.y = 370
    needle.x2 = 160
    needle.y2 = 700
    forcebar.width = 10
    forcebar.height = 20

def redrawWindow():
    win.fill((64,64,64))
    forcebar.draw(win)
    needle.draw(win)
    for i in range(len(enermys)):
        enermys[i].draw(win)
    text = font.render('HP: ' + str(love), 1, (255, 255, 255))
    win.blit(text, (50, 10))
    text = font.render('Score: ' + str(enermy.score), 1, (255, 255, 255))
    win.blit(text, (400, 10))
    block1.draw(win)
    block2.draw(win)
    block3.draw(win)
    block4.draw(win)
    block5.draw(win)
    golfBall.draw(win)
    pygame.display.update()

def findAngle(pos):
    sX = needle.x1
    sY = needle.y1
    try:
        angle = math.atan((sY - pos[1]) / (sX - pos[0]))
    except:
        angle = math.pi / 2

    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi - angle
    elif pos[1] > sY and pos[0] < sX:
        angle = math.pi + abs(angle)
    elif pos[1] > sY and pos[0] > sX:
        angle = (math.pi * 2) - angle

    return angle

font = pygame.font.SysFont('comicsans', 45)
golfBall = ball(100,370,5,(255,255,255))
forcebar = rectangle(250,670,10,20)
needle = needle(80,700,160,700)
enermy1 = enermy(1400, 510, 40, 70, 1)
enermy2 = enermy(1450, 510, 40, 70, 1)
enermy3 = enermy(1500, 510, 40, 70, 1)
enermy4 = enermy(1550, 510, 40, 70, 1)
enermy5 = enermy(1600, 510, 40, 70, 1)
block1 = rec(1100, 480, 20, 70, 1)
block2 = rec(1000, 510, 20, 70, 1)
block3 = rec(800, 510, 20, 70, 1)
block4 = rec(500, 510, 20, 70, 1)
block5 = rec(200, 510, 20, 70, 1)
enermys = [block1, enermy1, enermy2, enermy3, enermy4, enermy5]
blocks = [block1, block2, block3, block4, block5]
angle = 0
time = 0
power = 0
hitrange = 50
wave = 0
love = 5
distance = 60
shoot = False
kill = False
walk = True
space = True
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(200)
    for event in pygame.event.get():
        if golfBall.x == 100 and golfBall.y == 370:
            shoot = False
            kill = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and angle > -80:
                angle -= 10
                needle.x2 = needle.x1 + math.cos(math.radians(angle)) * 80
                needle.y2 = needle.y1 + math.sin(math.radians(angle)) * 80

            if event.key == pygame.K_DOWN and angle < 0:
                angle += 10
                needle.x2 = needle.x1 + math.cos(math.radians(angle)) * 80
                needle.y2 = needle.y1 + math.sin(math.radians(angle)) * 80

            if event.key == pygame.K_a:
                if not shoot:
                    x = golfBall.x
                    y = golfBall.y
                    pos = (needle.x2, needle.y2)
                    shoot = True
                    power = forcebar.width / 8
                    angle = findAngle(pos)

        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and forcebar.width <= 680 and space:
        forcebar.width += 1
        if forcebar.width == 650:
            forcebar.width = 10

    if not kill:
        for i in range(0, len(enermys)):
            if golfBall.hitbox[0] >= enermys[i].hitbox[0]:
                if golfBall.hitbox[0] <= enermys[i].hitbox[0]+enermys[i].width:
                    if golfBall.hitbox[1] >= enermys[i].hitbox[1]:
                        if golfBall.hitbox[1] <= enermys[i].hitbox[1]+enermys[i].height:
                            kill = True
                            shoot = False
                            time = 0
                            wave += 1
                            recharge()
                            enermys[i].Health()
                            for i in range(0, len(enermys)):
                                if enermys[i].hitbox[0]+enermys[i].width < golfBall.hitbox[0]\
                                        and enermys[i].hitbox[0]+enermys[i].width > golfBall.hitbox[0]-hitrange\
                                        or enermys[i].hitbox[0] > golfBall.hitbox[0]\
                                        and enermys[i].hitbox[0] < golfBall.hitbox[0]+hitrange + golfBall.radius:
                                    enermys[i].Health()

    if wave < 5:
        for i in range(1, len(enermys)):
            if enermys[i].health <= 0:
                enermys[i].x = enermys[i-1].x
        for i in range(1,len(enermys)):
            if enermys[i].x > enermys[i-1].x + distance:
                enermys[i].walk(win)


        if shoot:
            if golfBall.y < 580 - golfBall.radius:
                time += 0.05
                po = ball.ballPath(x, y, power, angle, time)
                golfBall.x = po[0]
                golfBall.y = po[1]

            else:
                wave += 1
                shoot = False
                time = 0
                recharge()
                for i in range(1, len(enermys)):
                    if enermys[i].hitbox[0] + enermys[i].width < golfBall.hitbox[0] \
                            and enermys[i].hitbox[0] + enermys[i].width > golfBall.hitbox[0] - hitrange \
                            or enermys[i].hitbox[0] > golfBall.hitbox[0] \
                            and enermys[i].hitbox[0] < golfBall.hitbox[0] + hitrange + golfBall.radius:
                        enermys[i].Health()

        if wave == 1:
            block1.x = block2.x
        if wave == 2:
            block1.x = block3.x
            block2.x = block3.x
        if wave == 3:
            block1.x = block4.x
            block2.x = block4.x
            block3.x = block4.x
        if wave == 4:
            block1.x = block5.x
            block2.x = block5.x
            block3.x = block5.x
            block4.x = block5.x

    if wave == 5:
        for i in range(1, len(enermys)):
            if enermys[i].x >= block1.x:
                enermys[i].walk(win)
            if enermys[i].health > 0 and enermys[i].x <= block1.x:
                enermys[i].health -= 3
                love -= 1

    redrawWindow()


pygame.quit()
quit()