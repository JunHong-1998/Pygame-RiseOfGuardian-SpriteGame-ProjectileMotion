import pygame
pygame.init()
class lighting():
    lighting = [pygame.image.load('lightningBg%s.png' % frame) for frame in range(61)]
    walkCount = 0

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.counter = -1
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100
        self.mute = False

    def draw(self, win):
        now = pygame.time.get_ticks()
        if self.walkCount + 1 >= 61:
            self.walkCount = 0
        if self.counter < 0:
            win.blit(self.lighting[self.walkCount//1], (self.x, self.y))
            if now - self.last_update > self.frame_rate:
                self.walkCount += 1

    def Mute(self):
        if not self.mute:
            self.mute = True
        else:
            self.mute = False


class base1():
    BASE1 = pygame.image.load('Home5.png')

    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.health = health

    def draw(self, win):
        if self.health > 0:
            win.blit(self.BASE1, (self.x, self.y))
class base2():
    BASE2 = pygame.image.load('Home4.png')

    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.health = health

    def draw(self, win):
        if self.health > 0:
            win.blit(self.BASE2, (self.x, self.y))
class base3():
    BASE3 = pygame.image.load('Home3.png')

    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.health = health

    def draw(self, win):
        if self.health > 0:
            win.blit(self.BASE3, (self.x, self.y))
class base4():
    BASE4 = pygame.image.load('Home2.png')

    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.health = health

    def draw(self, win):
        if self.health > 0:
            win.blit(self.BASE4, (self.x, self.y))
class base5():
    BASE5 = pygame.image.load('Home1.png')

    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.health = health

    def draw(self, win):
        if self.health > 0:
            win.blit(self.BASE5, (self.x, self.y))

class bombCount():
    bombCount = pygame.image.load('bombCount.png')

    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.health = health

    def draw(self, win):
        if self.health > 0:
            win.blit(self.bombCount, (self.x, self.y))

class level1warn():
    lv1warn = pygame.image.load('Level1Warn.png')

    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.health = health

    def draw(self, win):
        if self.health > 0:
            win.blit(self.lv1warn, (self.x, self.y))

    def drawout(self):
        self.health = 1

    def notdraw(self):
        self.health = 0

class level3warn():
    lv3warn = pygame.image.load('Level3Warn.png')

    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.health = health

    def draw(self, win):
        if self.health > 0:
            win.blit(self.lv3warn, (self.x, self.y))

    def drawout(self):
        self.health = 1

    def notdraw(self):
        self.health = 0

class level5warn():
    lv5warn = pygame.image.load('Level5Warn.png')

    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.health = health

    def draw(self, win):
        if self.health > 0:
            win.blit(self.lv5warn, (self.x, self.y))

    def drawout(self):
        self.health = 1

    def notdraw(self):
        self.health = 0

class rectangle():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def draw(self, win):
        self.win = win
        pygame.draw.rect(self.win, (122, 0, 0), [self.x, self.y, self.width, self.height])

class needle():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self, win):
        self.win = win
        pygame.draw.line(self.win, (255, 255, 255), (self.x1, self.y1), (self.x2, self.y2))

class swordbar():
    sword = pygame.image.load('Sword.png')

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def draw(self, win):
        win.blit(self.sword, (self.x, self.y))

class pauseBtn():
    pausebtn = pygame.image.load('PauseBtn.png')

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def draw(self, win):
        win.blit(self.pausebtn, (self.x, self.y))

class defeat():
    DEFEAT = pygame.image.load('defeat.png')

    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.health = health

    def draw(self, win):
        if self.health > 0:
            win.blit(self.DEFEAT, (self.x, self.y))

class lovelove():
    loveleft = pygame.image.load('Life.png')

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def draw(self, win):
        win.blit(self.loveleft, (self.x, self.y))