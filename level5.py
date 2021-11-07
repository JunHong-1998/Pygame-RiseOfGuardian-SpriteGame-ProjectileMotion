import pygame
import pygame.font
import math
from ball import *
from block import *
from cannon import *
from allenermy import *
from other import *

class Level5:
    pygame.init()
    pygame.mixer.init()
    bg = pygame.image.load('Background.png')
    hole = pygame.image.load('GateHole.png')
    CannonMoveSound = pygame.mixer.Sound('CannonMove.ogg')
    font = pygame.font.SysFont('algerian', 45)
    clock = pygame.time.Clock()

    def __init__(self, win, love, score, mute):
        self.win = win
        self.shoot = False
        self.kill = False
        self.walk = True
        self.space = False
        self.hold = False
        self.backhold = False
        self.activate = False
        self.run = True
        self.WAVE = False
        self.mute = mute
        self.right = [False, False, False, False, False, False]
        self.walkCount = 0
        self.angle = 0
        self.time = 0
        self.power = 0
        self.die = 0
        self.hitrange = 50
        self.wave = 0
        self.love = love
        self.distance = 80
        self.secondtime = 0
        self.clocktime = 0
        self.level = 5
        self.timeleft = 0
        self.score = score
        self.lighting = lighting(0, 0, 1400, 800)
        self.bomber = ball(173, 335, 5, (255, 255, 255))
        self.forcebar = rectangle(560, 720, 10, 20)
        self.needle = needle(80, 700, 160, 700)
        self.cannon = cannon(126, 233, 170, 200, 1)
        self.enermy1 = enermy02(1400, 430, 115, 90, 2)
        self.enermy2 = enermy01(1470, 450, 60, 110, 1)
        self.enermy3 = enermy02(1540, 430, 115, 90, 2)
        self.enermy4 = enermy01(1610, 450, 60, 110, 1)
        self.enermy5 = enermy02(1680, 430, 115, 90, 2)
        self.enermy6 = enermy03(1030, 2, 160, 100, 3)
        self.block1 = block(975, 452, 57, 106, 1)
        self.block2 = block(830, 452, 57, 106, 1)
        self.block3 = block(655, 452, 57, 106, 1)
        self.block4 = block(450, 452, 57, 106, 1)
        self.block5 = gate(250, 432, 80, 147, 1)
        self.base1 = base1(-9, 81, 146, 320, 1)
        self.base2 = base2(-9, 81, 146, 320, 1)
        self.base3 = base3(-9, 81, 146, 320, 1)
        self.base4 = base4(-9, 81, 146, 320, 1)
        self.base5 = base5(-9, 81, 146, 320, 1)
        self.sword = swordbar(25, 655, 1155, 154)
        self.bomb1 = bombCount(340, 688, 75, 89, 1)
        self.bomb2 = bombCount(278, 688, 75, 89, 1)
        self.bomb3 = bombCount(216, 688, 75, 89, 1)
        self.bomb4 = bombCount(153, 688, 75, 89, 1)
        self.bomb5 = bombCount(91, 688, 75, 89, 1)
        self.warn1 = level1warn(0, 0, 1400, 800, 0)
        self.warn2 = level3warn(0, 0, 1400, 800, 0)
        self.warn3 = level5warn(0, 0, 1400, 800, 0)
        self.pauseBtn = pauseBtn(1357, 14, 38, 39)
        self.bombs = [self.bomb1, self.bomb2, self.bomb3, self.bomb4, self.bomb5]
        self.bases = [self.base5, self.base4, self.base3, self.base2, self.base1]
        self.enermys = [self.block1, self.enermy1, self.enermy2, self.enermy3, self.enermy4, self.enermy5, self.enermy6]
        self.blocks = [self.block1, self.block2, self.block3, self.block4]
        self.next = 0
        if self.mute:
            self.bomber.Mute()
            self.cannon.Mute()
            self.enermy1.Mute()
            self.enermy2.Mute()
            self.enermy3.Mute()
            self.enermy4.Mute()
            self.enermy5.Mute()
            self.enermy6.Mute()

    def recharge(self):
        self.needle.x2 = 160
        self.needle.y2 = 700
        self.forcebar.width = 10
        self.forcebar.height = 20
        self.time = 0
        self.secondtime = 0
        self.angle = 0
        self.kill = True
        self.shoot = False
        if not self.WAVE:
            self.wave += 1
            self.WAVE = True
        for i in range(1, len(self.enermys)-1):
            if self.enermys[i].hitbox[0] + self.enermys[i].width < self.bomber.hitbox[0] \
                    and self.enermys[i].hitbox[0] + self.enermys[i].width > self.bomber.hitbox[0] - self.hitrange \
                    or self.enermys[i].hitbox[0] > self.bomber.hitbox[0] \
                    and self.enermys[i].hitbox[0] < self.bomber.hitbox[0] + self.hitrange + self.bomber.radius:
                self.enermys[i].Health()
                self.score += 100

    def redrawWindow(self):
        self.win.blit(Level5.bg, (0, 0))
        self.lighting.draw(self.win)
        self.forcebar.draw(self.win)
        self.bomber.draw(self.win)
        for i in range(len(self.bases)):
            self.bases[i].draw(self.win)
        self.cannon.draw(self.win)
        self.block5.draw(self.win)
        for i in range(len(self.enermys)):
            self.enermys[i].draw(self.win)
        self.sword.draw(self.win)
        for i in range(len(self.bombs)):
            self.bombs[i].draw(self.win)
        text = Level5.font.render('LEVEL ' + str(self.level) + ' / ' + 'WAVE ' + str(self.wave + 1), 1, (255, 255, 255))
        self.win.blit(text, (500, 10))
        text = Level5.font.render(str(self.score), 1, (255, 255, 255))
        self.win.blit(text, (1230, 710))
        text = Level5.font.render(str(int(self.timeleft)), 1, (255, 255, 255))
        self.win.blit(text, (50, 15))
        self.block1.draw(self.win)
        self.block2.draw(self.win)
        self.block3.draw(self.win)
        self.block4.draw(self.win)
        self.win.blit(Level5.hole, (0, 442))
        self.pauseBtn.draw(self.win)
        self.warn1.draw(self.win)
        self.warn2.draw(self.win)
        self.warn3.draw(self.win)
        pygame.display.update()

    def findAngle(self, pos):
        sX = self.needle.x1
        sY = self.needle.y1
        try:
            self.angle = math.atan((sY - pos[1]) / (sX - pos[0]))
        except:
            self.angle = math.pi / 2

        if pos[1] < sY and pos[0] > sX:
            self.angle = abs(self.angle)
        elif pos[1] < sY and pos[0] < sX:
            self.angle = math.pi - self.angle
        elif pos[1] > sY and pos[0] < sX:
            self.angle = math.pi + abs(self.angle)
        elif pos[1] > sY and pos[0] > sX:
            self.angle = (math.pi * 2) - self.angle

        return self.angle

    def pause1(self):
        battleOff = pygame.image.load('BattleOff.png')
        battleOn = pygame.image.load('BattleOn.png')
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = False
                        self.warn3.health = 0
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 569+256 > mouse[0] > 569 and 641+76 > mouse[1] > 641:
                self.win.blit(battleOn, (569, 641))
                if click[0] == 1:
                    paused = False
                    self.warn3.health = 0
            else:
                self.win.blit(battleOff, (569, 641))
            pygame.display.update()

    def pause2(self):
        pause = pygame.image.load('Pause.png')
        resumeOn = pygame.image.load('ResumeOn.png')
        resumeOff = pygame.image.load('ResumeOff.png')
        menuOn = pygame.image.load('MenuOn.png')
        menuOff = pygame.image.load('MenuOff.png')
        muteOn = pygame.image.load('MuteOn.png')
        muteOff = pygame.image.load('MuteOff.png')
        unmuteOn = pygame.image.load('UnmuteOn.png')
        unmuteOff = pygame.image.load('UnmuteOff.png')
        paused = True
        while paused:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 561 + 259 > mouse[0] > 561 and 424 + 74 > mouse[1] > 424:
                        if not self.mute:
                            self.bomber.Mute()
                            self.cannon.Mute()
                            self.enermy1.Mute()
                            self.enermy2.Mute()
                            self.enermy3.Mute()
                            self.enermy4.Mute()
                            self.enermy5.Mute()
                            self.enermy6.Mute()
                            pygame.mixer.music.pause()
                            self.mute = True
                        else:
                            self.bomber.Mute()
                            self.cannon.Mute()
                            self.enermy1.Mute()
                            self.enermy2.Mute()
                            self.enermy3.Mute()
                            self.enermy4.Mute()
                            self.enermy5.Mute()
                            self.enermy6.Mute()
                            pygame.mixer.music.unpause()
                            self.mute = False

                    if 561 + 259 > mouse[0] > 561 and 290 + 74 > mouse[1] > 290:
                        paused = False
            self.win.blit(pause, (0, 0))
            click = pygame.mouse.get_pressed()
            if 561 + 259 > mouse[0] > 561 and 290 + 74 > mouse[1] > 290:
                self.win.blit(resumeOn, (561, 290))
            else:
                self.win.blit(resumeOff, (561, 290))

            if 561 + 259 > mouse[0] > 561 and 424 + 74 > mouse[1] > 424:
                if not self.mute:
                    self.win.blit(muteOn, (561, 424))
                else:
                    self.win.blit(unmuteOn, (561, 424))
            else:
                if not self.mute:
                    self.win.blit(muteOff, (561, 424))
                else:
                    self.win.blit(unmuteOff, (561, 424))
            if 561 + 259 > mouse[0] > 561 and 556 + 74 > mouse[1] > 556:
                self.win.blit(menuOn, (561, 556))
                if click[0] == 1:
                    paused = False
                    self.next = 0
                    self.run = False
            else:
                self.win.blit(menuOff, (561, 556))
            pygame.display.update()

    def pausewin(self):
        congrats = pygame.image.load('Congrats.png')
        quitOff = pygame.image.load('QuitOff.png')
        quitOn = pygame.image.load('QuitOn.png')
        TryAgainOff = pygame.image.load('TryAgainOff.png')
        TryAgainOn = pygame.image.load('TryAgainOn.png')
        live = pygame.image.load('Life.png')
        font = pygame.font.SysFont('algerian', 50)
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = False
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            self.win.blit(congrats, (0, 0))
            text = font.render(str(self.score), 1, (219, 149, 248))
            self.win.blit(text, (764, 368))
            if self.love == 5:
                self.win.blit(live, (405, 434))
                self.win.blit(live, (528, 434))
                self.win.blit(live, (651, 434))
                self.win.blit(live, (774, 434))
                self.win.blit(live, (897, 434))
            if self.love == 4:
                self.win.blit(live, (405, 434))
                self.win.blit(live, (528, 434))
                self.win.blit(live, (651, 434))
                self.win.blit(live, (774, 434))
            if self.love == 3:
                self.win.blit(live, (405, 434))
                self.win.blit(live, (528, 434))
                self.win.blit(live, (651, 434))
            if self.love == 2:
                self.win.blit(live, (405, 434))
                self.win.blit(live, (528, 434))
            if self.love == 1:
                self.win.blit(live, (405, 434))
            if 377 + 259 > mouse[0] > 377 and 558 + 74 > mouse[1] > 558:
                self.win.blit(quitOn, (377, 558))
                if click[0] == 1:
                    paused = False
                    self.next = 0
                    self.run = False
            else:
                self.win.blit(quitOff, (377, 558))
            if 755 + 259 > mouse[0] > 755 and 558 + 74 > mouse[1] > 558:
                self.win.blit(TryAgainOn, (755, 558))
                self.next = 1
                self.run = False
                if click[0] == 1:
                    paused = False
                    self.next = -1
                    self.run = False
            else:
                self.win.blit(TryAgainOff, (755, 558))
            pygame.display.update()

    def pausedefeat(self):
        defeat = pygame.image.load('Defeat.png')
        quitOff = pygame.image.load('QuitOff.png')
        quitOn = pygame.image.load('QuitOn.png')
        TryAgainOff = pygame.image.load('TryAgainOff.png')
        TryAgainOn = pygame.image.load('TryAgainOn.png')
        font = pygame.font.SysFont('algerian', 50)
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = False
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            self.win.blit(defeat, (0, 0))
            text = font.render(str(self.score), 1, (219, 149, 248))
            self.win.blit(text, (764, 368))
            if 377 + 259 > mouse[0] > 377 and 558 + 74 > mouse[1] > 558:
                self.win.blit(quitOn, (377, 558))
                if click[0] == 1:
                    paused = False
                    self.next = 0
                    self.run = False
            else:
                self.win.blit(quitOff, (377, 558))
            if 755 + 259 > mouse[0] > 755 and 558 + 74 > mouse[1] > 558:
                self.win.blit(TryAgainOn, (755, 558))
                if click[0] == 1:
                    paused = False
                    self.next = -1
                    self.run = False
            else:
                self.win.blit(TryAgainOff, (755, 558))
            pygame.display.update()

    def WaveProcess(self):
        if self.bomber.x == 173 and self.bomber.y == 335:
            self.shoot = False
            self.kill = False
            self.WAVE = False
        if self.secondtime == 10:
            self.activate = True
            self.secondtime = 0

    def Mute(self):
        if not self.mute:
            self.mute = True
        else:
            self.mute = False

    def RUN(self):
        while self.run:
            self.clocktime += Level5.clock.tick_busy_loop(45)

            if self.clocktime >= 1000:
                self.secondtime += 1
                self.clocktime = 0
            if self.enermy1.x == 1397.6:
                self.warn3.drawout()
            if self.enermy1.x == 1395.1999999999998:
                self.pause1()
            if self.secondtime == 1:
                self.timeleft = 10
            if self.secondtime == 2:
                self.timeleft = 9
            if self.secondtime == 3:
                self.timeleft = 8
            if self.secondtime == 4:
                self.timeleft = 7
            if self.secondtime == 5:
                self.timeleft = 6
            if self.secondtime == 6:
                self.timeleft = 5
            if self.secondtime == 7:
                self.timeleft = 4
            if self.secondtime == 8:
                self.timeleft = 3
            if self.secondtime == 9:
                self.timeleft = 2
            if self.secondtime == 10:
                self.timeleft = 1

            if self.enermy6.x == 600:
                self.enermy6.attack()

            if self.activate == True:
                if not self.space:
                    self.power = 51.67
                self.hold = False
                self.backhold = False
                self.cannon.move()
                self.cannon.Angle(int(self.angle))
                if not self.shoot:
                    pos = (self.needle.x2, self.needle.y2)
                    self.shoot = True
                    self.angle = self.findAngle(pos)

            if self.backhold:
                self.power -= 0.13
                self.forcebar.width -= 3.5
                if self.forcebar.width <= 10:
                    self.hold = True
                    self.backhold = False

            if self.hold:
                self.forcebar.width += 3.5
                self.power += 0.13
                if self.forcebar.width >= 500:
                    self.hold = False
                    self.backhold = True

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 1357 + 38 > mouse[0] > 1357 and 14 + 39 > mouse[1] > 14:
                if click[0] == 1:
                    self.pause2()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.pause2()

                    if event.key == pygame.K_UP and self.angle > -80 and self.bomber.x == 173 \
                            and self.bomber.y == 335:
                        if not self.mute:
                            self.CannonMoveSound.play()
                        self.angle -= 10
                        self.cannon.notmove()
                        self.cannon.Angle(int(self.angle))
                        self.needle.x2 = self.needle.x1 + math.cos(math.radians(self.angle)) * 80
                        self.needle.y2 = self.needle.y1 + math.sin(math.radians(self.angle)) * 80

                    if event.key == pygame.K_DOWN and self.angle < 0 and self.bomber.x == 173 \
                            and self.bomber.y == 335:
                        if not self.mute:
                            self.CannonMoveSound.play()
                        self.angle += 10
                        self.cannon.notmove()
                        self.cannon.Angle(int(self.angle))
                        self.needle.x2 = self.needle.x1 + math.cos(math.radians(self.angle)) * 80
                        self.needle.y2 = self.needle.y1 + math.sin(math.radians(self.angle)) * 80

                    if event.key == pygame.K_SPACE and self.bomber.x == 173 and self.bomber.y == 335:
                        self.power = 51.67
                        self.hold = True
                        self.space = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE and self.bomber.x == 173 and self.bomber.y == 335 \
                            or self.activate == True:
                        self.hold = False
                        self.backhold = False
                        self.cannon.move()
                        self.cannon.Angle(int(self.angle))
                        if not self.shoot:
                            pos = (self.needle.x2, self.needle.y2)
                            self.shoot = True
                            self.angle = self.findAngle(pos)
                if event.type == pygame.QUIT:
                    self.run = False

            if not self.kill:
                for i in range(0, len(self.blocks)):
                    if self.bomber.hitbox[0] >= self.blocks[i].hitbox[0] \
                            and self.bomber.hitbox[0] <= self.blocks[i].hitbox[0] + self.blocks[i].width \
                            and self.bomber.hitbox[1] >= self.blocks[i].hitbox[1] \
                            and self.bomber.hitbox[1] <= self.blocks[i].hitbox[1] + self.blocks[i].height:
                        self.bomber.explo()
                        self.recharge()
                for i in range(1, len(self.enermys)-1):
                    if self.bomber.hitbox[0] >= self.enermys[i].hitbox[0] \
                            and self.bomber.hitbox[0] <= self.enermys[i].hitbox[0] + self.enermys[i].width \
                            and self.bomber.hitbox[1] >= self.enermys[i].hitbox[1] \
                            and self.bomber.hitbox[1] <= self.enermys[i].hitbox[1] + self.enermys[i].height:
                        self.bomber.explo()
                        self.enermys[i].Health()
                        self.score += 100
                        self.recharge()
                if self.bomber.hitbox[0] >= self.enermy6.hitbox[0] \
                        and self.bomber.hitbox[0] <= self.enermy6.hitbox[0] + self.enermy6.width \
                        and self.bomber.hitbox[1] >= self.enermy6.hitbox[1] \
                        and self.bomber.hitbox[1] <= self.enermy6.hitbox[1] + self.enermy6.height:
                    self.kill = True
                    self.shoot = False
                    self.bomber.explo()
                    self.time = 0
                    self.enermy6.Health()
                    self.recharge()
                    self.secondtime = 0
                    self.angle = 0
                    self.score += 100
                    if not self.WAVE:
                        self.wave += 1
                        self.WAVE = True

            if self.wave < 5:
                self.activate = False
                for i in range(1, len(self.enermys)):
                    if self.enermys[i].health <= 0 and not self.enermys[i].spirit():
                        self.enermys[i].x = self.enermys[i - 1].x
                if self.wave == 0:
                    for i in range(1, 4):
                        if i == 2:
                            width = 240
                        else:
                            width = self.enermys[i].width
                        if self.enermys[i].x <= self.block1.x + self.distance:
                            self.right[i - 1] = True
                        elif self.enermys[i].x >= 1400 - width:
                            self.right[i - 1] = False
                        if self.enermys[i].x > self.block1.x + self.distance and not self.right[i - 1]:
                            self.enermys[i].left()
                            self.enermys[i].walk(self.win)
                        elif self.right[i - 1]:
                            self.enermys[i].right()
                            self.enermys[i].uturn(self.win)
                else:
                    for i in range(1, len(self.enermys)-1):
                        if i == 2 or i == 4 or i == 6:
                            width = 240
                        else:
                            width = self.enermys[i].width
                        if self.enermys[i].x <= self.block1.x + self.distance:
                            self.right[i - 1] = True
                        elif self.enermys[i].x >= 1400 - width:
                            self.right[i - 1] = False
                        if self.enermys[i].x > self.block1.x + self.distance and not self.right[i - 1]:
                            self.enermys[i].left()
                            self.enermys[i].walk(self.win)
                        elif self.right[i - 1]:
                            self.enermys[i].right()
                            self.enermys[i].uturn(self.win)

                if self.shoot:
                    if self.bomber.y < 540 - self.bomber.radius:
                        self.time += 0.25
                        po = self.bomber.ballPath(173, 335, self.power, self.angle, self.time)
                        self.bomber.x = po[0]
                        self.bomber.y = po[1]
                        if self.bomber.y > 530 - self.bomber.radius \
                                and self.bomber.y < 540 - self.bomber.radius:
                            self.bomber.land()
                            self.bomber.explo()

                    else:
                        self.recharge()
                        
            if self.enermy6.finish():
                self.cannon.health = 0
                self.bomber.x = -1000
                self.bomber.y = -1000
                for i in range(len(self.bases)):
                    self.bases[i].health = 0
                self.block1.x = self.block5.x
                self.block2.x = self.block5.x
                self.block3.x = self.block5.x
                self.block4.x = self.block5.x
                self.block1.health = 0
                self.block2.health = 0
                self.block3.health = 0
                self.block4.health = 0
                self.block5.health = 0
                self.love = 0
                self.wave = 5

            if self.enermy1.health <= 0 and self.enermy2.health <= 0 and self.enermy3.health <= 0 \
                    and self.enermy4.health <= 0 and self.enermy5.health <= 0 and self.bomber.x == -1000 \
                    and self.bomber.y == -1000:
                self.enermy6.health = 0

            if self.love == 4:
                self.base1.health = 0
            if self.love == 3:
                self.base1.health = 0
                self.base2.health = 0
            if self.love == 2:
                self.base1.health = 0
                self.base2.health = 0
                self.base3.health = 0
            if self.love == 1:
                self.base1.health = 0
                self.base2.health = 0
                self.base3.health = 0
                self.base4.health = 0
            if self.love == 0:
                self.base1.health = 0
                self.base2.health = 0
                self.base3.health = 0
                self.base4.health = 0
                self.base5.health = 0

            if self.wave == 0:
                self.WaveProcess()
            if self.wave == 1:
                self.WaveProcess()
                self.block1.health = 0
                self.bomb1.health = 0
                if self.block1.health <= 0 and not self.block1.spirit():
                    self.block1.x = self.block2.x
            if self.wave == 2:
                self.WaveProcess()
                self.block2.health = 0
                self.bomb2.health = 0
                if self.block2.health <= 0 and not self.block2.spirit():
                    self.block1.x = self.block3.x
                    self.block2.x = self.block3.x
            if self.wave == 3:
                self.WaveProcess()
                self.block3.health = 0
                self.bomb3.health = 0
                if self.block3.health <= 0 and not self.block3.spirit():
                    self.block1.x = self.block4.x
                    self.block2.x = self.block4.x
                    self.block3.x = self.block4.x
            if self.wave == 4:
                self.WaveProcess()
                self.block4.health = 0
                self.bomb4.health = 0
                if self.block4.health <= 0 and not self.block4.spirit():
                    self.block1.x = self.block5.x
                    self.block2.x = self.block5.x
                    self.block3.x = self.block5.x
                    self.block4.x = self.block5.x
            if self.wave == 5:
                self.activate = False
                if self.block4.health <= 0 and not self.block4.spirit():
                    self.block1.x = self.block5.x - 100
                    self.block2.x = self.block5.x - 100
                    self.block3.x = self.block5.x - 100
                    self.block4.x = self.block5.x - 100
                self.block5.health = 0
                self.bomb5.health = 0
                for i in range(1, len(self.enermys)-1):
                    if self.enermys[i].x >= self.block1.x:
                        self.enermys[i].left()
                        self.enermys[i].walk(self.win)
                    if self.enermys[i].health > 0 and self.enermys[i].x <= self.block1.x:
                        self.enermys[i].health = -1
                        self.love -= 1

            if self.enermy1.health <= 0 and self.enermy2.health <= 0 and self.enermy3.health <= 0 \
                    and self.enermy4.health <= 0 and self.enermy5.health <= 0 and self.enermy6.health <= 0:
                if self.love > 0 and self.bomber.x == 173 and self.bomber.y == 335:
                    self.pausewin()
                if self.love <= 0:
                    self.pausedefeat()

            self.redrawWindow()

        return self.love, self.score, self.mute, self.next