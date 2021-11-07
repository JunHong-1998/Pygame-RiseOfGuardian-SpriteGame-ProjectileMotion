import pygame
import math
class ball(object):
    pygame.init()
    pygame.mixer.init()
    BombExplosionSound = pygame.mixer.Sound('BombExplosion.ogg')
    bomb = [pygame.image.load('Bomb%s.png' % frame) for frame in range(1, 9)]
    walkCount = 0
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.hitbox = (self.x, self.y, 15, 15)
        self.vel = 2
        self.explode = False
        self.LAND = False
        self.explu = 0
        self.mute = False

    def draw(self, win):
        if self.walkCount + 1 >= 21:
            self.walkCount = 0
        if self.vel > 0:

            win.blit(self.bomb[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        if self.explode and self.explu < 15:
            if not self.LAND and self.explu < 9:
                explosion = [pygame.image.load('Explosion%s.png' % frame) for frame in range(1, 10)]
                win.blit(explosion[self.explu], (self.x - 44, self.y - 44))
                if self.explu == 8:
                    self.explu = 14
                if not self.mute:
                    self.BombExplosionSound.play()
            else:
                explosion = [pygame.image.load('Explosion%s.png' % frame) for frame in range(1, 16)]
                win.blit(explosion[self.explu], (self.x - 44, self.y - 84))
                if not self.mute:
                    self.BombExplosionSound.play()
            self.explu += 1
            if self.explu == 15:
                self.x = 173
                self.y = 335
        else:
            self.explu = 0
            self.explode = False
            self.LAND = False

        self.hitbox = (self.x, self.y, 25, 25)

    @staticmethod
    def ballPath(startx, starty, power, ang, time):
        angle = ang
        velx = math.cos(angle) * power
        vely = math.sin(angle) * power

        distX = velx * time
        distY = (vely * time) + ((-4.9 * (time ** 2)) / 2)

        newx = round(distX + startx)
        newy = round(starty - distY)

        return (newx, newy)

    def explo(self):
        self.explode = True

    def expla(self):
        return self.explode

    def land(self):
        self.LAND = True

    def Mute(self):
        if not self.mute:
            self.mute = True
        else:
            self.mute = False
