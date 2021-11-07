import pygame
pygame.init()
class cannon():
    cannonshoot0 = [pygame.image.load('Cannon00.png'), pygame.image.load('Cannon01.png'),
                    pygame.image.load('Cannon02.png'), pygame.image.load('Cannon03.png'),
                    pygame.image.load('Cannon04.png'), pygame.image.load('Cannon05.png'),
                    pygame.image.load('Cannon05.png'), pygame.image.load('Cannon05.png'),
                    pygame.image.load('Cannon05.png'), pygame.image.load('Cannon05.png'),
                    pygame.image.load('Cannon06.png'), pygame.image.load('Cannon06.png'),
                    pygame.image.load('Cannon06.png'), pygame.image.load('Cannon06.png'),
                    pygame.image.load('Cannon07.png'), pygame.image.load('Cannon07.png'),
                    pygame.image.load('Cannon07.png'), pygame.image.load('Cannon07.png')]
    cannonshoot1 = [pygame.image.load('Cannon10.png'), pygame.image.load('Cannon11.png'),
                    pygame.image.load('Cannon12.png'), pygame.image.load('Cannon13.png'),
                    pygame.image.load('Cannon14.png'), pygame.image.load('Cannon15.png'),
                    pygame.image.load('Cannon15.png'), pygame.image.load('Cannon15.png'),
                    pygame.image.load('Cannon15.png'), pygame.image.load('Cannon15.png'),
                    pygame.image.load('Cannon16.png'), pygame.image.load('Cannon16.png'),
                    pygame.image.load('Cannon16.png'), pygame.image.load('Cannon16.png'),
                    pygame.image.load('Cannon17.png'), pygame.image.load('Cannon17.png'),
                    pygame.image.load('Cannon17.png'), pygame.image.load('Cannon17.png')]
    cannonshoot2 = [pygame.image.load('Cannon20.png'), pygame.image.load('Cannon21.png'),
                    pygame.image.load('Cannon22.png'), pygame.image.load('Cannon23.png'),
                    pygame.image.load('Cannon24.png'), pygame.image.load('Cannon25.png'),
                    pygame.image.load('Cannon25.png'), pygame.image.load('Cannon25.png'),
                    pygame.image.load('Cannon25.png'), pygame.image.load('Cannon25.png'),
                    pygame.image.load('Cannon26.png'), pygame.image.load('Cannon26.png'),
                    pygame.image.load('Cannon26.png'), pygame.image.load('Cannon26.png'),
                    pygame.image.load('Cannon27.png'), pygame.image.load('Cannon27.png'),
                    pygame.image.load('Cannon27.png'), pygame.image.load('Cannon27.png')]
    cannonshoot3 = [pygame.image.load('Cannon30.png'), pygame.image.load('Cannon31.png'),
                    pygame.image.load('Cannon32.png'), pygame.image.load('Cannon33.png'),
                    pygame.image.load('Cannon34.png'), pygame.image.load('Cannon35.png'),
                    pygame.image.load('Cannon35.png'), pygame.image.load('Cannon35.png'),
                    pygame.image.load('Cannon35.png'), pygame.image.load('Cannon35.png'),
                    pygame.image.load('Cannon36.png'), pygame.image.load('Cannon36.png'),
                    pygame.image.load('Cannon36.png'), pygame.image.load('Cannon36.png'),
                    pygame.image.load('Cannon37.png'), pygame.image.load('Cannon37.png'),
                    pygame.image.load('Cannon37.png'), pygame.image.load('Cannon37.png')]
    cannonshoot4 = [pygame.image.load('Cannon40.png'), pygame.image.load('Cannon41.png'),
                    pygame.image.load('Cannon42.png'), pygame.image.load('Cannon43.png'),
                    pygame.image.load('Cannon44.png'), pygame.image.load('Cannon45.png'),
                    pygame.image.load('Cannon45.png'), pygame.image.load('Cannon45.png'),
                    pygame.image.load('Cannon45.png'), pygame.image.load('Cannon45.png'),
                    pygame.image.load('Cannon46.png'), pygame.image.load('Cannon46.png'),
                    pygame.image.load('Cannon46.png'), pygame.image.load('Cannon46.png'),
                    pygame.image.load('Cannon47.png'), pygame.image.load('Cannon47.png'),
                    pygame.image.load('Cannon47.png'), pygame.image.load('Cannon47.png')]
    cannonshoot5 = [pygame.image.load('Cannon50.png'), pygame.image.load('Cannon51.png'),
                    pygame.image.load('Cannon52.png'), pygame.image.load('Cannon53.png'),
                    pygame.image.load('Cannon54.png'), pygame.image.load('Cannon55.png'),
                    pygame.image.load('Cannon55.png'), pygame.image.load('Cannon55.png'),
                    pygame.image.load('Cannon55.png'), pygame.image.load('Cannon55.png'),
                    pygame.image.load('Cannon56.png'), pygame.image.load('Cannon56.png'),
                    pygame.image.load('Cannon56.png'), pygame.image.load('Cannon56.png'),
                    pygame.image.load('Cannon57.png'), pygame.image.load('Cannon57.png'),
                    pygame.image.load('Cannon57.png'), pygame.image.load('Cannon57.png')]
    cannonshoot6 = [pygame.image.load('Cannon60.png'), pygame.image.load('Cannon61.png'),
                    pygame.image.load('Cannon62.png'), pygame.image.load('Cannon63.png'),
                    pygame.image.load('Cannon64.png'), pygame.image.load('Cannon65.png'),
                    pygame.image.load('Cannon65.png'), pygame.image.load('Cannon65.png'),
                    pygame.image.load('Cannon65.png'), pygame.image.load('Cannon65.png'),
                    pygame.image.load('Cannon66.png'), pygame.image.load('Cannon66.png'),
                    pygame.image.load('Cannon66.png'), pygame.image.load('Cannon66.png'),
                    pygame.image.load('Cannon67.png'), pygame.image.load('Cannon67.png'),
                    pygame.image.load('Cannon67.png'), pygame.image.load('Cannon67.png')]
    cannonshoot7 = [pygame.image.load('Cannon70.png'), pygame.image.load('Cannon71.png'),
                    pygame.image.load('Cannon72.png'), pygame.image.load('Cannon73.png'),
                    pygame.image.load('Cannon74.png'), pygame.image.load('Cannon75.png'),
                    pygame.image.load('Cannon75.png'), pygame.image.load('Cannon75.png'),
                    pygame.image.load('Cannon75.png'), pygame.image.load('Cannon75.png'),
                    pygame.image.load('Cannon76.png'), pygame.image.load('Cannon76.png'),
                    pygame.image.load('Cannon76.png'), pygame.image.load('Cannon76.png'),
                    pygame.image.load('Cannon77.png'), pygame.image.load('Cannon77.png'),
                    pygame.image.load('Cannon77.png'), pygame.image.load('Cannon77.png')]
    cannonshoot8 = [pygame.image.load('Cannon80.png'), pygame.image.load('Cannon81.png'),
                    pygame.image.load('Cannon82.png'), pygame.image.load('Cannon83.png'),
                    pygame.image.load('Cannon84.png'), pygame.image.load('Cannon85.png'),
                    pygame.image.load('Cannon85.png'), pygame.image.load('Cannon85.png'),
                    pygame.image.load('Cannon85.png'), pygame.image.load('Cannon85.png'),
                    pygame.image.load('Cannon86.png'), pygame.image.load('Cannon86.png'),
                    pygame.image.load('Cannon86.png'), pygame.image.load('Cannon86.png'),
                    pygame.image.load('Cannon87.png'), pygame.image.load('Cannon87.png'),
                    pygame.image.load('Cannon87.png'), pygame.image.load('Cannon87.png')]
    cannon0 = pygame.image.load('Cannon00.png')
    cannon1 = pygame.image.load('Cannon10.png')
    cannon2 = pygame.image.load('Cannon20.png')
    cannon3 = pygame.image.load('Cannon30.png')
    cannon4 = pygame.image.load('Cannon40.png')
    cannon5 = pygame.image.load('Cannon50.png')
    cannon6 = pygame.image.load('Cannon60.png')
    cannon7 = pygame.image.load('Cannon70.png')
    cannon8 = pygame.image.load('Cannon80.png')
    score = 0
    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.walkCount = 0
        self.angle = -90
        self.notmoving = False
        self.health = health
        self.mute = False

    def draw(self, win):
        if self.health > 0:
            if self.angle == 0 and self.notmoving:
                win.blit(self.cannon0, (self.x, self.y))
                self.walkCount = 0
            if self.angle == -10 and self.notmoving:
                win.blit(self.cannon1, (self.x, self.y))
                self.walkCount = 0
            if self.angle == -20 and self.notmoving:
                win.blit(self.cannon2, (self.x, self.y))
                self.walkCount = 0
            if self.angle == -30 and self.notmoving:
                win.blit(self.cannon3, (self.x, self.y))
                self.walkCount = 0
            if self.angle == -40 and self.notmoving:
                win.blit(self.cannon4, (self.x, self.y))
                self.walkCount = 0
            if self.angle == -50 and self.notmoving:
                win.blit(self.cannon5, (self.x, self.y))
                self.walkCount = 0
            if self.angle == -60 and self.notmoving:
                win.blit(self.cannon6, (self.x, self.y))
                self.walkCount = 0
            if self.angle == -70 and self.notmoving:
                win.blit(self.cannon7, (self.x, self.y))
                self.walkCount = 0
            if self.angle == -80 and self.notmoving:
                win.blit(self.cannon8, (self.x, self.y))
                self.walkCount = 0
            if self.angle == 0 and self.walkCount < 18:
                win.blit(self.cannonshoot0[self.walkCount], (self.x, self.y))
                self.walkCount += 1
            elif self.angle == -10 and self.walkCount < 18:
                win.blit(self.cannonshoot1[self.walkCount], (self.x, self.y))
                self.walkCount += 1
            elif self.angle == -20 and self.walkCount < 18:
                win.blit(self.cannonshoot2[self.walkCount], (self.x, self.y))
                self.walkCount += 1
            elif self.angle == -30 and self.walkCount < 18:
                win.blit(self.cannonshoot3[self.walkCount], (self.x, self.y))
                self.walkCount += 1
            elif self.angle == -40 and self.walkCount < 18:
                win.blit(self.cannonshoot4[self.walkCount], (self.x, self.y))
                self.walkCount += 1
            elif self.angle == -50 and self.walkCount < 18:
                win.blit(self.cannonshoot5[self.walkCount], (self.x, self.y))
                self.walkCount += 1
            elif self.angle == -60 and self.walkCount < 18:
                win.blit(self.cannonshoot6[self.walkCount], (self.x, self.y))
                self.walkCount += 1
            elif self.angle == -70 and self.walkCount < 18:
                win.blit(self.cannonshoot7[self.walkCount], (self.x, self.y))
                self.walkCount += 1
            elif self.angle == -80 and self.walkCount < 18:
                win.blit(self.cannonshoot8[self.walkCount], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.cannon0, (self.x, self.y))
                self.walkCount = 0
                self.angle = -90

    def Angle(self, a):
        for i in reversed(range(-90, 1)):
            if a == i:
                self.angle = i

    def notmove(self):
        self.notmoving = True

    def move(self):
        self.notmoving = False

    def Mute(self):
        if not self.mute:
            self.mute = True
        else:
            self.mute = False

