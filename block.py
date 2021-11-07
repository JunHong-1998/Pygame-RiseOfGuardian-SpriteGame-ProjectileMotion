import pygame
class block():
    blockmove = [pygame.image.load('Block1.png'), pygame.image.load('Block1.png'),
                 pygame.image.load('Block1.png'), pygame.image.load('Block1.png'),
                 pygame.image.load('Block1.png'), pygame.image.load('Block1.png'),
                 pygame.image.load('Block1.png'), pygame.image.load('Block1.png'),
                 pygame.image.load('Block2.png'), pygame.image.load('Block2.png'),
                 pygame.image.load('Block2.png'), pygame.image.load('Block2.png'),
                 pygame.image.load('Block2.png'), pygame.image.load('Block2.png'),
                 pygame.image.load('Block2.png'), pygame.image.load('Block2.png'),
                 pygame.image.load('Block3.png'), pygame.image.load('Block3.png'),
                 pygame.image.load('Block3.png'), pygame.image.load('Block3.png'),
                 pygame.image.load('Block3.png'), pygame.image.load('Block3.png'),
                 pygame.image.load('Block3.png'), pygame.image.load('Block3.png'),
                 pygame.image.load('Block4.png'), pygame.image.load('Block4.png'),
                 pygame.image.load('Block4.png'), pygame.image.load('Block4.png'),
                 pygame.image.load('Block4.png'), pygame.image.load('Block4.png'),
                 pygame.image.load('Block4.png'), pygame.image.load('Block4.png'),
                 pygame.image.load('Block5.png'), pygame.image.load('Block5.png'),
                 pygame.image.load('Block5.png'), pygame.image.load('Block5.png'),
                 pygame.image.load('Block5.png'), pygame.image.load('Block5.png'),
                 pygame.image.load('Block5.png'), pygame.image.load('Block5.png'),
                 pygame.image.load('Block6.png'), pygame.image.load('Block6.png'),
                 pygame.image.load('Block6.png'), pygame.image.load('Block6.png'),
                 pygame.image.load('Block6.png'), pygame.image.load('Block6.png'),
                 pygame.image.load('Block6.png'), pygame.image.load('Block6.png'),
                 pygame.image.load('Block7.png'), pygame.image.load('Block7.png'),
                 pygame.image.load('Block7.png'), pygame.image.load('Block7.png'),
                 pygame.image.load('Block7.png'), pygame.image.load('Block7.png'),
                 pygame.image.load('Block7.png'), pygame.image.load('Block7.png'),
                 pygame.image.load('Block8.png'), pygame.image.load('Block8.png'),
                 pygame.image.load('Block8.png'), pygame.image.load('Block8.png'),
                 pygame.image.load('Block8.png'), pygame.image.load('Block8.png'),
                 pygame.image.load('Block8.png'), pygame.image.load('Block8.png'),
                 pygame.image.load('Block9.png'), pygame.image.load('Block9.png'),
                 pygame.image.load('Block9.png'), pygame.image.load('Block9.png'),
                 pygame.image.load('Block9.png'), pygame.image.load('Block9.png'),
                 pygame.image.load('Block9.png'), pygame.image.load('Block9.png'),
                 pygame.image.load('Block10.png'), pygame.image.load('Block10.png'),
                 pygame.image.load('Block10.png'), pygame.image.load('Block10.png'),
                 pygame.image.load('Block10.png'), pygame.image.load('Block10.png'),
                 pygame.image.load('Block10.png'), pygame.image.load('Block10.png')]
    block = pygame.image.load('Block1.png')

    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.hitbox = (self.x - 5, self.y - 5, 48, 78)
        self.health = health
        self.die = 0
        self.ell = True

    def draw(self, win):
        if self.health > 0:
            win.blit(self.block, (self.x, self.y))
        else:
            if self.die < 80:
                win.blit(self.blockmove[self.die], (self.x, self.y))
                self.die += 1
            else:
                self.ell = False
                self.hitbox = (0, 0, 0, 0)

    def spirit(self):
        return self.ell

    def walk(self,win):
        vel = 0.4
        self.x -= vel

    def Health(self):
        if self.health > 0:
            self.health -= 1

class gate():
    gatemove = [pygame.image.load('Gate1.png'), pygame.image.load('Gate1.png'),
                pygame.image.load('Gate1.png'), pygame.image.load('Gate1.png'),
                pygame.image.load('Gate1.png'), pygame.image.load('Gate1.png'),
                pygame.image.load('Gate1.png'), pygame.image.load('Gate1.png'),
                pygame.image.load('Gate2.png'), pygame.image.load('Gate2.png'),
                pygame.image.load('Gate2.png'), pygame.image.load('Gate2.png'),
                pygame.image.load('Gate2.png'), pygame.image.load('Gate2.png'),
                pygame.image.load('Gate2.png'), pygame.image.load('Gate2.png'),
                pygame.image.load('Gate3.png'), pygame.image.load('Gate3.png'),
                pygame.image.load('Gate3.png'), pygame.image.load('Gate3.png'),
                pygame.image.load('Gate3.png'), pygame.image.load('Gate3.png'),
                pygame.image.load('Gate3.png'), pygame.image.load('Gate3.png'),
                pygame.image.load('Gate4.png'), pygame.image.load('Gate4.png'),
                pygame.image.load('Gate4.png'), pygame.image.load('Gate4.png'),
                pygame.image.load('Gate4.png'), pygame.image.load('Gate4.png'),
                pygame.image.load('Gate4.png'), pygame.image.load('Gate4.png'),
                pygame.image.load('Gate5.png'), pygame.image.load('Gate5.png'),
                pygame.image.load('Gate5.png'), pygame.image.load('Gate5.png'),
                pygame.image.load('Gate5.png'), pygame.image.load('Gate5.png'),
                pygame.image.load('Gate5.png'), pygame.image.load('Gate5.png'),
                pygame.image.load('Gate6.png'), pygame.image.load('Gate6.png'),
                pygame.image.load('Gate6.png'), pygame.image.load('Gate6.png'),
                pygame.image.load('Gate6.png'), pygame.image.load('Gate6.png'),
                pygame.image.load('Gate6.png'), pygame.image.load('Gate6.png'),
                pygame.image.load('Gate7.png'), pygame.image.load('Gate7.png'),
                pygame.image.load('Gate7.png'), pygame.image.load('Gate7.png'),
                pygame.image.load('Gate7.png'), pygame.image.load('Gate7.png'),
                pygame.image.load('Gate7.png'), pygame.image.load('Gate7.png'),
                pygame.image.load('Gate8.png'), pygame.image.load('Gate8.png'),
                pygame.image.load('Gate8.png'), pygame.image.load('Gate8.png'),
                pygame.image.load('Gate8.png'), pygame.image.load('Gate8.png'),
                pygame.image.load('Gate8.png'), pygame.image.load('Gate8.png'),
                pygame.image.load('Gate9.png'), pygame.image.load('Gate9.png'),
                pygame.image.load('Gate9.png'), pygame.image.load('Gate9.png'),
                pygame.image.load('Gate9.png'), pygame.image.load('Gate9.png'),
                pygame.image.load('Gate9.png'), pygame.image.load('Gate9.png'),
                pygame.image.load('Gate10.png'), pygame.image.load('Gate10.png'),
                pygame.image.load('Gate10.png'), pygame.image.load('Gate10.png'),
                pygame.image.load('Gate10.png'), pygame.image.load('Gate10.png'),
                pygame.image.load('Gate10.png'), pygame.image.load('Gate10.png'),
                pygame.image.load('Gate11.png'), pygame.image.load('Gate11.png'),
                pygame.image.load('Gate11.png'), pygame.image.load('Gate11.png'),
                pygame.image.load('Gate11.png'), pygame.image.load('Gate11.png'),
                pygame.image.load('Gate11.png'), pygame.image.load('Gate11.png'),
                pygame.image.load('Gate12.png'), pygame.image.load('Gate12.png'),
                pygame.image.load('Gate12.png'), pygame.image.load('Gate12.png'),
                pygame.image.load('Gate12.png'), pygame.image.load('Gate12.png'),
                pygame.image.load('Gate12.png'), pygame.image.load('Gate12.png'),
                pygame.image.load('Gate13.png'), pygame.image.load('Gate13.png'),
                pygame.image.load('Gate13.png'), pygame.image.load('Gate13.png'),
                pygame.image.load('Gate13.png'), pygame.image.load('Gate13.png'),
                pygame.image.load('Gate13.png'), pygame.image.load('Gate13.png'),
                pygame.image.load('Gate14.png'), pygame.image.load('Gate14.png'),
                pygame.image.load('Gate14.png'), pygame.image.load('Gate14.png'),
                pygame.image.load('Gate14.png'), pygame.image.load('Gate14.png'),
                pygame.image.load('Gate14.png'), pygame.image.load('Gate14.png'),
                pygame.image.load('Gate15.png'), pygame.image.load('Gate15.png'),
                pygame.image.load('Gate15.png'), pygame.image.load('Gate15.png'),
                pygame.image.load('Gate15.png'), pygame.image.load('Gate15.png'),
                pygame.image.load('Gate15.png'), pygame.image.load('Gate15.png'),
                pygame.image.load('Gate16.png'), pygame.image.load('Gate16.png'),
                pygame.image.load('Gate16.png'), pygame.image.load('Gate16.png'),
                pygame.image.load('Gate16.png'), pygame.image.load('Gate16.png'),
                pygame.image.load('Gate16.png'), pygame.image.load('Gate16.png')]
    gate = pygame.image.load('Gate1.png')
    gate2 = pygame.image.load('Gate16.png')

    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.hitbox = (self.x - 5, self.y - 5, 48, 78)
        self.health = health
        self.die = 0
        self.ell = True

    def draw(self, win):
        if self.health > 0:
            win.blit(self.gate, (self.x, self.y))
            self.walkCount = 0
            self.angle = -90
        else:
            if self.die < 128:
                win.blit(self.gatemove[self.die], (self.x, self.y))
                self.die += 1
            else:
                win.blit(self.gate2, (self.x, self.y))
                self.ell = False
                self.hitbox = (0, 0, 0, 0)

    def spirit(self):
        return self.ell

    def walk(self, win):
        vel = 0.4
        self.x -= vel

    def Health(self):
        if self.health > 0:
            self.health -= 1
