import pygame
class enermy01():
    pygame.init()
    pygame.mixer.init()
    enermy1walkLeft = [pygame.image.load('DragoWalkLeft%s.png' % frame) for frame in range(1, 9)]
    enermy1walkRight = [pygame.image.load('DragoWalkRight%s.png' % frame) for frame in range(1, 9)]
    enermy1stand = pygame.image.load('DragoLeftModel.png')
    enermy1die = [pygame.image.load('DragoDeadLeft1.png'), pygame.image.load('DragoDeadLeft1.png'),
                   pygame.image.load('DragoDeadLeft1.png'), pygame.image.load('DragoDeadLeft1.png'),
                   pygame.image.load('DragoDeadLeft2.png'), pygame.image.load('DragoDeadLeft2.png'),
                   pygame.image.load('DragoDeadLeft2.png'), pygame.image.load('DragoDeadLeft2.png'),
                   pygame.image.load('DragoDeadLeft3.png'), pygame.image.load('DragoDeadLeft3.png'),
                   pygame.image.load('DragoDeadLeft3.png'), pygame.image.load('DragoDeadLeft3.png'),
                   pygame.image.load('DragoDeadLeft4.png'), pygame.image.load('DragoDeadLeft4.png'),
                   pygame.image.load('DragoDeadLeft4.png'), pygame.image.load('DragoDeadLeft4.png')]
    enermy1die2 = [pygame.image.load('DragoDeadRight1.png'), pygame.image.load('DragoDeadRight1.png'),
                   pygame.image.load('DragoDeadRight1.png'), pygame.image.load('DragoDeadRight1.png'),
                   pygame.image.load('DragoDeadRight2.png'), pygame.image.load('DragoDeadRight2.png'),
                   pygame.image.load('DragoDeadRight2.png'), pygame.image.load('DragoDeadRight2.png'),
                   pygame.image.load('DragoDeadRight3.png'), pygame.image.load('DragoDeadRight3.png'),
                   pygame.image.load('DragoDeadRight3.png'), pygame.image.load('DragoDeadRight3.png'),
                   pygame.image.load('DragoDeadRight4.png'), pygame.image.load('DragoDeadRight4.png'),
                   pygame.image.load('DragoDeadRight4.png'), pygame.image.load('DragoDeadRight4.png')]
    DragoSound = pygame.mixer.Sound('Drago.ogg')
    walkCount = 0
    dieCount = 0
    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.hitbox = (self.x - 5, self.y - 5, 48, 78)
        self.health = health
        self.counter = -1
        self.die = 0
        self.ell = True
        self.mute = False

    def draw(self, win):
        if self.health > 0:
            if self.walkCount + 1 >= 21:
                self.walkCount = 0
            if self.counter < 0:
                win.blit(self.enermy1walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
                if not self.mute and 250 < self.x < 350:
                    self.DragoSound.play()
                if not self.mute and 830 < self.x < 975:
                    self.DragoSound.play()
            if self.counter > 0:
                win.blit(self.enermy1walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
                if not self.mute and 250 < self.x < 350:
                    self.DragoSound.play()
                if not self.mute and 830 < self.x < 975:
                    self.DragoSound.play()
            elif self.counter == 0:
                win.blit(self.enermy1stand, (self.x, self.y))
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 8, self.hitbox[1] - 11, 54, 13))
            pygame.draw.rect(win, (169, 169, 169), (self.hitbox[0] + 10, self.hitbox[1] - 10, 50, 10))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 10, self.hitbox[1] - 10, (self.health/1)*50, 10))
            self.hitbox = (self.x - 5, self.y - 5, 60, 110)
        elif self.health == 0:
            if self.die < 16 and self.counter < 0:
                win.blit(self.enermy1die[self.die], (self.x, self.y))
                self.die += 1
            if self.die < 16 and self.counter > 0:
                win.blit(self.enermy1die2[self.die], (self.x, self.y))
                self.die += 1
            if self.die < 16 and self.counter == 0:
                win.blit(self.enermy1die[self.die], (self.x, self.y))
                self.die += 1
            if self.die == 16:
                self.ell = False
                self.hitbox = (0, 0, 0, 0)

    def spirit(self):
        return self.ell

    def stop(self):
        self.counter = 0

    def left(self):
        self.counter = -1

    def right(self):
        self.counter = 1

    def walk(self, win):
        vel = 1.2
        self.x -= vel

    def uturn(self, win):
        vel = 1.2
        self.x += vel

    def Health(self):
        if self.health > 0:
            self.health -= 1

    def Mute(self):
        if not self.mute:
            self.mute = True
        else:
            self.mute = False

class enermy02():
    pygame.init()
    pygame.mixer.init()
    enermy2walkLeft = [pygame.image.load('DeadthgripperLeft%s.png' % frame) for frame in range(0, 6)]
    enermy2walkRight = [pygame.image.load('DeadthgripperRight%s.png' % frame) for frame in range(0, 6)]
    enermy2die = [pygame.image.load('DeadthgripperLeftDead1.png'),
                  pygame.image.load('DeadthgripperLeftDead1.png'),
                  pygame.image.load('DeadthgripperLeftDead1.png'),
                  pygame.image.load('DeadthgripperLeftDead1.png'),
                  pygame.image.load('DeadthgripperLeftDead2.png'),
                  pygame.image.load('DeadthgripperLeftDead2.png'),
                  pygame.image.load('DeadthgripperLeftDead2.png'),
                  pygame.image.load('DeadthgripperLeftDead2.png'),
                  pygame.image.load('DeadthgripperLeftDead3.png'),
                  pygame.image.load('DeadthgripperLeftDead3.png'),
                  pygame.image.load('DeadthgripperLeftDead3.png'),
                  pygame.image.load('DeadthgripperLeftDead3.png'),
                  pygame.image.load('DeadthgripperLeftDead4.png'),
                  pygame.image.load('DeadthgripperLeftDead4.png'),
                  pygame.image.load('DeadthgripperLeftDead4.png'),
                  pygame.image.load('DeadthgripperLeftDead4.png'),
                  pygame.image.load('DeadthgripperLeftDead5.png'),
                  pygame.image.load('DeadthgripperLeftDead5.png'),
                  pygame.image.load('DeadthgripperLeftDead5.png'),
                  pygame.image.load('DeadthgripperLeftDead5.png')]
    enermy2die2 = [pygame.image.load('DeadthgripperRightDead1.png'),
                   pygame.image.load('DeadthgripperRightDead1.png'),
                   pygame.image.load('DeadthgripperRightDead1.png'),
                   pygame.image.load('DeadthgripperRightDead1.png'),
                   pygame.image.load('DeadthgripperRightDead2.png'),
                   pygame.image.load('DeadthgripperRightDead2.png'),
                   pygame.image.load('DeadthgripperRightDead2.png'),
                   pygame.image.load('DeadthgripperRightDead2.png'),
                   pygame.image.load('DeadthgripperRightDead3.png'),
                   pygame.image.load('DeadthgripperRightDead3.png'),
                   pygame.image.load('DeadthgripperRightDead3.png'),
                   pygame.image.load('DeadthgripperRightDead3.png'),
                   pygame.image.load('DeadthgripperRightDead4.png'),
                   pygame.image.load('DeadthgripperRightDead4.png'),
                   pygame.image.load('DeadthgripperRightDead4.png'),
                   pygame.image.load('DeadthgripperRightDead4.png'),
                   pygame.image.load('DeadthgripperRightDead5.png'),
                   pygame.image.load('DeadthgripperRightDead5.png'),
                   pygame.image.load('DeadthgripperRightDead5.png'),
                   pygame.image.load('DeadthgripperRightDead5.png')]
    enermy2stand = pygame.image.load('DeadthgripperLeft0.png')
    GripperSound = pygame.mixer.Sound('DeathGripper.ogg')
    walkCount = 0
    dieCount = 0
    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.hitbox = (self.x + 5, self.y + 5, 115, 90)
        self.health = health
        self.counter = -1
        self.die = 0
        self.ell = True
        self.mute = False

    def draw(self, win):
        if self.health > 0:
            if self.walkCount + 1 >= 21:
                self.walkCount = 0
            if self.counter < 0:
                win.blit(self.enermy2walkLeft[self.walkCount//4], (self.x, self.y))
                self.walkCount += 1
                if not self.mute and 250 < self.x < 350:
                    self.GripperSound.play()
                if not self.mute and 830 < self.x < 975:
                    self.GripperSound.play()
            if self.counter > 0:
                win.blit(self.enermy2walkRight[self.walkCount // 4], (self.x, self.y))
                self.walkCount += 1
                if not self.mute and 250 < self.x < 350:
                    self.GripperSound.play()
                if not self.mute and 830 < self.x < 975:
                    self.GripperSound.play()
            elif self.counter == 0:
                win.blit(self.enermy2stand, (self.x, self.y))
            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 28, self.hitbox[1] - 11, 54, 13))
            pygame.draw.rect(win, (169, 169, 169), (self.hitbox[0] + 30, self.hitbox[1] - 10, 50, 10))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 30, self.hitbox[1] - 10, (self.health/2)*50, 10))
            self.hitbox = (self.x + 5, self.y + 20, 115, 90)
        elif self.health == 0:
            if self.die < 20 and self.counter < 0:
                win.blit(self.enermy2die[self.die], (self.x, self.y))
                self.die += 1
            if self.die < 20 and self.counter > 0:
                win.blit(self.enermy2die2[self.die], (self.x, self.y))
                self.die += 1
            if self.die < 20 and self.counter == 0:
                win.blit(self.enermy2die[self.die], (self.x, self.y))
                self.die += 1
            if self.die == 20:
                self.ell = False
                self.hitbox = (-1000, -1000, 0, 0)

    def spirit(self):
        return self.ell

    def stop(self):
        self.counter = 0

    def left(self):
        self.counter = -1

    def right(self):
        self.counter = 1

    def walk(self,win):
        vel = 2.4
        self.x -= vel

    def uturn(self, win):
        vel = 2.4
        self.x += vel

    def Health(self):
        if self.health > 0:
            self.health -= 1

    def Mute(self):
        if not self.mute:
            self.mute = True
        else:
            self.mute = False

class enermy03():
    pygame.init()
    pygame.mixer.init()
    enermy3transform = [pygame.image.load('CRDragonTransform0.png'), pygame.image.load('CRDragonTransform0.png'),
                        pygame.image.load('CRDragonTransform0.png'), pygame.image.load('CRDragonTransform0.png'),
                        pygame.image.load('CRDragonTransform0.png'), pygame.image.load('CRDragonTransform0.png'),
                        pygame.image.load('CRDragonTransform1.png'), pygame.image.load('CRDragonTransform1.png'),
                        pygame.image.load('CRDragonTransform1.png'), pygame.image.load('CRDragonTransform1.png'),
                        pygame.image.load('CRDragonTransform1.png'), pygame.image.load('CRDragonTransform1.png'),
                        pygame.image.load('CRDragonTransform2.png'), pygame.image.load('CRDragonTransform2.png'),
                        pygame.image.load('CRDragonTransform2.png'), pygame.image.load('CRDragonTransform2.png'),
                        pygame.image.load('CRDragonTransform2.png'), pygame.image.load('CRDragonTransform2.png'),
                        pygame.image.load('CRDragonTransform3.png'), pygame.image.load('CRDragonTransform3.png'),
                        pygame.image.load('CRDragonTransform3.png'), pygame.image.load('CRDragonTransform3.png'),
                        pygame.image.load('CRDragonTransform3.png'), pygame.image.load('CRDragonTransform3.png'),
                        pygame.image.load('CRDragonTransform4.png'), pygame.image.load('CRDragonTransform4.png'),
                        pygame.image.load('CRDragonTransform4.png'), pygame.image.load('CRDragonTransform4.png'),
                        pygame.image.load('CRDragonTransform4.png'), pygame.image.load('CRDragonTransform4.png'),
                        pygame.image.load('CRDragonTransform5.png'), pygame.image.load('CRDragonTransform5.png'),
                        pygame.image.load('CRDragonTransform5.png'), pygame.image.load('CRDragonTransform5.png'),
                        pygame.image.load('CRDragonTransform5.png'), pygame.image.load('CRDragonTransform5.png'),
                        pygame.image.load('CRDragonTransform6.png'), pygame.image.load('CRDragonTransform6.png'),
                        pygame.image.load('CRDragonTransform6.png'), pygame.image.load('CRDragonTransform6.png'),
                        pygame.image.load('CRDragonTransform6.png'), pygame.image.load('CRDragonTransform6.png'),
                        pygame.image.load('CRDragonTransform7.png'), pygame.image.load('CRDragonTransform7.png'),
                        pygame.image.load('CRDragonTransform7.png'), pygame.image.load('CRDragonTransform7.png'),
                        pygame.image.load('CRDragonTransform7.png'), pygame.image.load('CRDragonTransform7.png'),
                        pygame.image.load('CRDragonTransform8.png'), pygame.image.load('CRDragonTransform8.png'),
                        pygame.image.load('CRDragonTransform8.png'), pygame.image.load('CRDragonTransform8.png'),
                        pygame.image.load('CRDragonTransform8.png'), pygame.image.load('CRDragonTransform8.png'),
                        pygame.image.load('CRDragonTransform9.png'), pygame.image.load('CRDragonTransform9.png'),
                        pygame.image.load('CRDragonTransform9.png'), pygame.image.load('CRDragonTransform9.png'),
                        pygame.image.load('CRDragonTransform10.png'), pygame.image.load('CRDragonTransform10.png'),
                        pygame.image.load('CRDragonTransform10.png'), pygame.image.load('CRDragonTransform10.png'),
                        pygame.image.load('CRDragonTransform11.png'), pygame.image.load('CRDragonTransform11.png'),
                        pygame.image.load('CRDragonTransform11.png'), pygame.image.load('CRDragonTransform11.png'),
                        pygame.image.load('CRDragonTransform12.png'), pygame.image.load('CRDragonTransform12.png'),
                        pygame.image.load('CRDragonTransform12.png'), pygame.image.load('CRDragonTransform12.png'),
                        pygame.image.load('CRDragonTransform13.png'), pygame.image.load('CRDragonTransform13.png'),
                        pygame.image.load('CRDragonTransform13.png'), pygame.image.load('CRDragonTransform13.png'),
                        pygame.image.load('CRDragonTransform14.png'), pygame.image.load('CRDragonTransform14.png'),
                        pygame.image.load('CRDragonTransform14.png'), pygame.image.load('CRDragonTransform14.png'),
                        pygame.image.load('CRDragonTransform15.png'), pygame.image.load('CRDragonTransform15.png'),
                        pygame.image.load('CRDragonTransform15.png'), pygame.image.load('CRDragonTransform15.png'),
                        pygame.image.load('CRDragonTransform16.png'), pygame.image.load('CRDragonTransform16.png'),
                        pygame.image.load('CRDragonTransform16.png'), pygame.image.load('CRDragonTransform16.png'),
                        pygame.image.load('CRDragonTransform17.png'), pygame.image.load('CRDragonTransform17.png'),
                        pygame.image.load('CRDragonTransform17.png'), pygame.image.load('CRDragonTransform17.png'),
                        pygame.image.load('CRDragonTransform18.png'), pygame.image.load('CRDragonTransform18.png'),
                        pygame.image.load('CRDragonTransform18.png'), pygame.image.load('CRDragonTransform18.png'),
                        pygame.image.load('CRDragonTransform19.png'), pygame.image.load('CRDragonTransform19.png'),
                        pygame.image.load('CRDragonTransform19.png'), pygame.image.load('CRDragonTransform19.png'),
                        pygame.image.load('CRDragonTransform20.png'), pygame.image.load('CRDragonTransform20.png'),
                        pygame.image.load('CRDragonTransform20.png'), pygame.image.load('CRDragonTransform20.png'),
                        pygame.image.load('CRDragonTransform21.png'), pygame.image.load('CRDragonTransform21.png'),
                        pygame.image.load('CRDragonTransform21.png'), pygame.image.load('CRDragonTransform21.png'),
                        pygame.image.load('CRDragonTransform22.png'), pygame.image.load('CRDragonTransform22.png'),
                        pygame.image.load('CRDragonTransform22.png'), pygame.image.load('CRDragonTransform22.png'),
                        pygame.image.load('CRDragonTransform23.png'), pygame.image.load('CRDragonTransform23.png'),
                        pygame.image.load('CRDragonTransform23.png'), pygame.image.load('CRDragonTransform23.png'),
                        pygame.image.load('CRDragonTransform24.png'), pygame.image.load('CRDragonTransform24.png'),
                        pygame.image.load('CRDragonTransform24.png'), pygame.image.load('CRDragonTransform24.png'),
                        pygame.image.load('CRDragonTransform25.png'), pygame.image.load('CRDragonTransform25.png'),
                        pygame.image.load('CRDragonTransform25.png'), pygame.image.load('CRDragonTransform25.png'),
                        pygame.image.load('CRDragonTransform26.png'), pygame.image.load('CRDragonTransform26.png'),
                        pygame.image.load('CRDragonTransform26.png'), pygame.image.load('CRDragonTransform26.png'),
                        pygame.image.load('CRDragonTransform27.png'), pygame.image.load('CRDragonTransform27.png'),
                        pygame.image.load('CRDragonTransform27.png'), pygame.image.load('CRDragonTransform27.png'),
                        pygame.image.load('CRDragonTransform28.png'), pygame.image.load('CRDragonTransform28.png'),
                        pygame.image.load('CRDragonTransform28.png'), pygame.image.load('CRDragonTransform28.png')]
    enermy3walkLeft = [pygame.image.load('CrystalRubyDragon1.png'), pygame.image.load('CrystalRubyDragon1.png'),
                       pygame.image.load('CrystalRubyDragon1.png'), pygame.image.load('CrystalRubyDragon1.png'),
                       pygame.image.load('CrystalRubyDragon1.png'), pygame.image.load('CrystalRubyDragon1.png'),
                       pygame.image.load('CrystalRubyDragon2.png'), pygame.image.load('CrystalRubyDragon2.png'),
                       pygame.image.load('CrystalRubyDragon2.png'), pygame.image.load('CrystalRubyDragon2.png'),
                       pygame.image.load('CrystalRubyDragon2.png'), pygame.image.load('CrystalRubyDragon2.png'),
                       pygame.image.load('CrystalRubyDragon3.png'), pygame.image.load('CrystalRubyDragon3.png'),
                       pygame.image.load('CrystalRubyDragon3.png'), pygame.image.load('CrystalRubyDragon3.png'),
                       pygame.image.load('CrystalRubyDragon3.png'), pygame.image.load('CrystalRubyDragon3.png'),
                       pygame.image.load('CrystalRubyDragon4.png'), pygame.image.load('CrystalRubyDragon4.png'),
                       pygame.image.load('CrystalRubyDragon4.png'), pygame.image.load('CrystalRubyDragon4.png'),
                       pygame.image.load('CrystalRubyDragon4.png'), pygame.image.load('CrystalRubyDragon4.png'),
                       pygame.image.load('CrystalRubyDragon5.png'), pygame.image.load('CrystalRubyDragon5.png'),
                       pygame.image.load('CrystalRubyDragon5.png'), pygame.image.load('CrystalRubyDragon5.png'),
                       pygame.image.load('CrystalRubyDragon5.png'), pygame.image.load('CrystalRubyDragon5.png'),
                       pygame.image.load('CrystalRubyDragon6.png'), pygame.image.load('CrystalRubyDragon6.png'),
                       pygame.image.load('CrystalRubyDragon6.png'), pygame.image.load('CrystalRubyDragon6.png'),
                       pygame.image.load('CrystalRubyDragon6.png'), pygame.image.load('CrystalRubyDragon6.png'),
                       pygame.image.load('CrystalRubyDragon7.png'), pygame.image.load('CrystalRubyDragon7.png'),
                       pygame.image.load('CrystalRubyDragon7.png'), pygame.image.load('CrystalRubyDragon7.png'),
                       pygame.image.load('CrystalRubyDragon7.png'), pygame.image.load('CrystalRubyDragon7.png'),
                       pygame.image.load('CrystalRubyDragon8.png'), pygame.image.load('CrystalRubyDragon8.png'),
                       pygame.image.load('CrystalRubyDragon8.png'), pygame.image.load('CrystalRubyDragon8.png'),
                       pygame.image.load('CrystalRubyDragon8.png'), pygame.image.load('CrystalRubyDragon8.png')]
    enermy3die = [pygame.image.load('CrystalRubyDragonDead1.png'), pygame.image.load('CrystalRubyDragonDead1.png'),
                  pygame.image.load('CrystalRubyDragonDead1.png'), pygame.image.load('CrystalRubyDragonDead1.png'),
                  pygame.image.load('CrystalRubyDragonDead1.png'), pygame.image.load('CrystalRubyDragonDead1.png'),
                  pygame.image.load('CrystalRubyDragonDead1.png'), pygame.image.load('CrystalRubyDragonDead1.png'),
                  pygame.image.load('CrystalRubyDragonDead2.png'), pygame.image.load('CrystalRubyDragonDead2.png'),
                  pygame.image.load('CrystalRubyDragonDead2.png'), pygame.image.load('CrystalRubyDragonDead2.png'),
                  pygame.image.load('CrystalRubyDragonDead2.png'), pygame.image.load('CrystalRubyDragonDead2.png'),
                  pygame.image.load('CrystalRubyDragonDead2.png'), pygame.image.load('CrystalRubyDragonDead2.png'),
                  pygame.image.load('CrystalRubyDragonDead3.png'), pygame.image.load('CrystalRubyDragonDead3.png'),
                  pygame.image.load('CrystalRubyDragonDead3.png'), pygame.image.load('CrystalRubyDragonDead3.png'),
                  pygame.image.load('CrystalRubyDragonDead3.png'), pygame.image.load('CrystalRubyDragonDead3.png'),
                  pygame.image.load('CrystalRubyDragonDead3.png'), pygame.image.load('CrystalRubyDragonDead3.png'),
                  pygame.image.load('CrystalRubyDragonDead4.png'), pygame.image.load('CrystalRubyDragonDead4.png'),
                  pygame.image.load('CrystalRubyDragonDead4.png'), pygame.image.load('CrystalRubyDragonDead4.png'),
                  pygame.image.load('CrystalRubyDragonDead4.png'), pygame.image.load('CrystalRubyDragonDead4.png'),
                  pygame.image.load('CrystalRubyDragonDead4.png'), pygame.image.load('CrystalRubyDragonDead4.png'),
                  pygame.image.load('CrystalRubyDragonDead5.png'), pygame.image.load('CrystalRubyDragonDead5.png'),
                  pygame.image.load('CrystalRubyDragonDead5.png'), pygame.image.load('CrystalRubyDragonDead5.png'),
                  pygame.image.load('CrystalRubyDragonDead5.png'), pygame.image.load('CrystalRubyDragonDead5.png'),
                  pygame.image.load('CrystalRubyDragonDead5.png'), pygame.image.load('CrystalRubyDragonDead5.png'),
                  pygame.image.load('CrystalRubyDragonDead6.png'), pygame.image.load('CrystalRubyDragonDead6.png'),
                  pygame.image.load('CrystalRubyDragonDead6.png'), pygame.image.load('CrystalRubyDragonDead6.png'),
                  pygame.image.load('CrystalRubyDragonDead6.png'), pygame.image.load('CrystalRubyDragonDead6.png'),
                  pygame.image.load('CrystalRubyDragonDead6.png'), pygame.image.load('CrystalRubyDragonDead6.png'),
                  pygame.image.load('CrystalRubyDragonDead7.png'), pygame.image.load('CrystalRubyDragonDead7.png'),
                  pygame.image.load('CrystalRubyDragonDead7.png'), pygame.image.load('CrystalRubyDragonDead7.png'),
                  pygame.image.load('CrystalRubyDragonDead7.png'), pygame.image.load('CrystalRubyDragonDead7.png'),
                  pygame.image.load('CrystalRubyDragonDead7.png'), pygame.image.load('CrystalRubyDragonDead7.png'),
                  pygame.image.load('CrystalRubyDragonDead8.png'), pygame.image.load('CrystalRubyDragonDead8.png'),
                  pygame.image.load('CrystalRubyDragonDead8.png'), pygame.image.load('CrystalRubyDragonDead8.png'),
                  pygame.image.load('CrystalRubyDragonDead8.png'), pygame.image.load('CrystalRubyDragonDead8.png'),
                  pygame.image.load('CrystalRubyDragonDead8.png'), pygame.image.load('CrystalRubyDragonDead8.png')]
    enermy3attack = [pygame.image.load('CRDragonAttack1.png'), pygame.image.load('CRDragonAttack1.png'),
                     pygame.image.load('CRDragonAttack1.png'), pygame.image.load('CRDragonAttack1.png'),
                     pygame.image.load('CRDragonAttack1.png'), pygame.image.load('CRDragonAttack1.png'),
                     pygame.image.load('CRDragonAttack2.png'), pygame.image.load('CRDragonAttack2.png'),
                     pygame.image.load('CRDragonAttack2.png'), pygame.image.load('CRDragonAttack2.png'),
                     pygame.image.load('CRDragonAttack2.png'), pygame.image.load('CRDragonAttack2.png'),
                     pygame.image.load('CRDragonAttack3.png'), pygame.image.load('CRDragonAttack3.png'),
                     pygame.image.load('CRDragonAttack3.png'), pygame.image.load('CRDragonAttack3.png'),
                     pygame.image.load('CRDragonAttack3.png'), pygame.image.load('CRDragonAttack3.png'),
                     pygame.image.load('CRDragonAttack4.png'), pygame.image.load('CRDragonAttack4.png'),
                     pygame.image.load('CRDragonAttack4.png'), pygame.image.load('CRDragonAttack4.png'),
                     pygame.image.load('CRDragonAttack4.png'), pygame.image.load('CRDragonAttack4.png'),
                     pygame.image.load('CRDragonAttack5.png'), pygame.image.load('CRDragonAttack5.png'),
                     pygame.image.load('CRDragonAttack5.png'), pygame.image.load('CRDragonAttack5.png'),
                     pygame.image.load('CRDragonAttack5.png'), pygame.image.load('CRDragonAttack5.png'),
                     pygame.image.load('CRDragonAttack6.png'), pygame.image.load('CRDragonAttack6.png'),
                     pygame.image.load('CRDragonAttack6.png'), pygame.image.load('CRDragonAttack6.png'),
                     pygame.image.load('CRDragonAttack6.png'), pygame.image.load('CRDragonAttack6.png'),
                     pygame.image.load('CRDragonAttack7.png'), pygame.image.load('CRDragonAttack7.png'),
                     pygame.image.load('CRDragonAttack7.png'), pygame.image.load('CRDragonAttack7.png'),
                     pygame.image.load('CRDragonAttack7.png'), pygame.image.load('CRDragonAttack7.png'),
                     pygame.image.load('CRDragonAttack8.png'), pygame.image.load('CRDragonAttack8.png'),
                     pygame.image.load('CRDragonAttack8.png'), pygame.image.load('CRDragonAttack8.png'),
                     pygame.image.load('CRDragonAttack8.png'), pygame.image.load('CRDragonAttack8.png'),
                     pygame.image.load('CRDragonAttack9.png'), pygame.image.load('CRDragonAttack9.png'),
                     pygame.image.load('CRDragonAttack9.png'), pygame.image.load('CRDragonAttack9.png'),
                     pygame.image.load('CRDragonAttack9.png'), pygame.image.load('CRDragonAttack9.png'),
                     pygame.image.load('CRDragonAttack10.png'), pygame.image.load('CRDragonAttack10.png'),
                     pygame.image.load('CRDragonAttack10.png'), pygame.image.load('CRDragonAttack10.png'),
                     pygame.image.load('CRDragonAttack10.png'), pygame.image.load('CRDragonAttack10.png'),
                     pygame.image.load('CRDragonAttack11.png'), pygame.image.load('CRDragonAttack11.png'),
                     pygame.image.load('CRDragonAttack11.png'), pygame.image.load('CRDragonAttack11.png'),
                     pygame.image.load('CRDragonAttack11.png'), pygame.image.load('CRDragonAttack11.png'),
                     pygame.image.load('CRDragonAttack12.png'), pygame.image.load('CRDragonAttack12.png'),
                     pygame.image.load('CRDragonAttack12.png'), pygame.image.load('CRDragonAttack12.png'),
                     pygame.image.load('CRDragonAttack12.png'), pygame.image.load('CRDragonAttack12.png'),
                     pygame.image.load('CRDragonAttack13.png'), pygame.image.load('CRDragonAttack13.png'),
                     pygame.image.load('CRDragonAttack13.png'), pygame.image.load('CRDragonAttack13.png'),
                     pygame.image.load('CRDragonAttack13.png'), pygame.image.load('CRDragonAttack13.png'),
                     pygame.image.load('CRDragonAttack14.png'), pygame.image.load('CRDragonAttack14.png'),
                     pygame.image.load('CRDragonAttack14.png'), pygame.image.load('CRDragonAttack14.png'),
                     pygame.image.load('CRDragonAttack14.png'), pygame.image.load('CRDragonAttack14.png')]
    enermy3bomb = [pygame.image.load('BoomAttack1.png'), pygame.image.load('BoomAttack1.png'),
                   pygame.image.load('BoomAttack1.png'), pygame.image.load('BoomAttack1.png'),
                   pygame.image.load('BoomAttack1.png'), pygame.image.load('BoomAttack1.png'),
                   pygame.image.load('BoomAttack2.png'), pygame.image.load('BoomAttack2.png'),
                   pygame.image.load('BoomAttack2.png'), pygame.image.load('BoomAttack2.png'),
                   pygame.image.load('BoomAttack2.png'), pygame.image.load('BoomAttack2.png'),
                   pygame.image.load('BoomAttack3.png'), pygame.image.load('BoomAttack3.png'),
                   pygame.image.load('BoomAttack3.png'), pygame.image.load('BoomAttack3.png'),
                   pygame.image.load('BoomAttack3.png'), pygame.image.load('BoomAttack3.png'),
                   pygame.image.load('BoomAttack4.png'), pygame.image.load('BoomAttack4.png'),
                   pygame.image.load('BoomAttack4.png'), pygame.image.load('BoomAttack4.png'),
                   pygame.image.load('BoomAttack4.png'), pygame.image.load('BoomAttack4.png'),
                   pygame.image.load('BoomAttack5.png'), pygame.image.load('BoomAttack5.png'),
                   pygame.image.load('BoomAttack5.png'), pygame.image.load('BoomAttack5.png'),
                   pygame.image.load('BoomAttack5.png'), pygame.image.load('BoomAttack5.png'),
                   pygame.image.load('BoomAttack6.png'), pygame.image.load('BoomAttack6.png'),
                   pygame.image.load('BoomAttack6.png'), pygame.image.load('BoomAttack6.png'),
                   pygame.image.load('BoomAttack6.png'), pygame.image.load('BoomAttack6.png'),
                   pygame.image.load('BoomAttack7.png'), pygame.image.load('BoomAttack7.png'),
                   pygame.image.load('BoomAttack7.png'), pygame.image.load('BoomAttack7.png'),
                   pygame.image.load('BoomAttack7.png'), pygame.image.load('BoomAttack7.png'),
                   pygame.image.load('BoomAttack8.png'), pygame.image.load('BoomAttack8.png'),
                   pygame.image.load('BoomAttack8.png'), pygame.image.load('BoomAttack8.png'),
                   pygame.image.load('BoomAttack8.png'), pygame.image.load('BoomAttack8.png'),
                   pygame.image.load('BoomAttack9.png'), pygame.image.load('BoomAttack9.png'),
                   pygame.image.load('BoomAttack9.png'), pygame.image.load('BoomAttack9.png'),
                   pygame.image.load('BoomAttack9.png'), pygame.image.load('BoomAttack9.png'),
                   pygame.image.load('BoomAttack10.png'), pygame.image.load('BoomAttack10.png'),
                   pygame.image.load('BoomAttack10.png'), pygame.image.load('BoomAttack10.png'),
                   pygame.image.load('BoomAttack10.png'), pygame.image.load('BoomAttack10.png'),
                   pygame.image.load('BoomAttack11.png'), pygame.image.load('BoomAttack11.png'),
                   pygame.image.load('BoomAttack11.png'), pygame.image.load('BoomAttack11.png'),
                   pygame.image.load('BoomAttack11.png'), pygame.image.load('BoomAttack11.png'),
                   pygame.image.load('BoomAttack12.png'), pygame.image.load('BoomAttack12.png'),
                   pygame.image.load('BoomAttack12.png'), pygame.image.load('BoomAttack12.png'),
                   pygame.image.load('BoomAttack12.png'), pygame.image.load('BoomAttack12.png'),
                   pygame.image.load('BoomAttack13.png'), pygame.image.load('BoomAttack13.png'),
                   pygame.image.load('BoomAttack13.png'), pygame.image.load('BoomAttack13.png'),
                   pygame.image.load('BoomAttack13.png'), pygame.image.load('BoomAttack13.png'),
                   pygame.image.load('BoomAttack14.png'), pygame.image.load('BoomAttack14.png'),
                   pygame.image.load('BoomAttack14.png'), pygame.image.load('BoomAttack14.png'),
                   pygame.image.load('BoomAttack14.png'), pygame.image.load('BoomAttack14.png'),
                   pygame.image.load('BoomAttack15.png'), pygame.image.load('BoomAttack15.png'),
                   pygame.image.load('BoomAttack15.png'), pygame.image.load('BoomAttack15.png'),
                   pygame.image.load('BoomAttack15.png'), pygame.image.load('BoomAttack15.png'),
                   pygame.image.load('BoomAttack16.png'), pygame.image.load('BoomAttack16.png'),
                   pygame.image.load('BoomAttack16.png'), pygame.image.load('BoomAttack16.png'),
                   pygame.image.load('BoomAttack16.png'), pygame.image.load('BoomAttack16.png')]
    DragonSound = pygame.mixer.Sound('Dragon.ogg')
    DragonAttackSound = pygame.mixer.Sound('DragonAttack.ogg')
    BigExplosionSound = pygame.mixer.Sound('BigExplosion.ogg')
    TransformSound = pygame.mixer.Sound('Transform.ogg')
    walkCount = 0
    walkCount2 = 0
    attackCount = 0
    bombattack = 0
    dieCount = 0
    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.hitbox = (self.x + 60, self.y + 180, 160, 100)
        self.health = health
        self.counter = 100
        self.cba = 0
        self.startbomb = 0
        self.die = 0
        self.ell = True
        self.walk = True
        self.finsihbomb = False
        self.mute = False

    def draw(self, win):
        if self.health > 0:
            if self.walkCount + 1 >= 48:
                self.walkCount = 0
            if self.attackCount == 84:
                self.counter = -1
                self.startbomb = 1
                self.walk = True
            if self.startbomb == 1:
                if self.bombattack < 96:
                    win.blit(self.enermy3bomb[self.bombattack], (-20, 40))
                    self.bombattack += 1
                if self.bombattack == 18:
                    self.finsihbomb = True
            if self.counter == -1 and self.walk:
                win.blit(self.enermy3walkLeft[self.walkCount//1], (self.x - 100, self.y))
                self.walkCount += 1
                if self.x >= 600:
                    self.x -= 0.5
            if self.counter == 100:
                if self.walkCount2 < 134:
                    win.blit(self.enermy3transform[self.walkCount2], (self.x, self.y))
                    self.walkCount2 += 1
                    if not self.mute and self.walkCount2 == 4:
                        self.TransformSound.play()
                    if not self.mute and self.walkCount2 == 100:
                        self.DragonSound.play()
                else:
                    self.counter = -1
            if self.cba == 1000:
                self.walk = False
                self.counter = 0
                if self.attackCount < 84:
                    win.blit(self.enermy3attack[self.attackCount], (self.x, self.y))
                    self.attackCount += 1
                    if not self.mute and self.attackCount == 2:
                        self.DragonAttackSound.play()
                        self.BigExplosionSound.play()
                    if not self.mute and self.attackCount == 62:
                        self.DragonSound.play()

            pygame.draw.rect(win, (0, 0, 0), (self.hitbox[0] + 108, self.hitbox[1] - 111, 54, 13))
            pygame.draw.rect(win, (169, 169, 169), (self.hitbox[0] + 110, self.hitbox[1] - 110, 50, 10))
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0] + 110, self.hitbox[1] - 110, (self.health / 3) * 50, 10))
            self.hitbox = (self.x + 60, self.y + 180, 160, 100)

        elif self.health <= 0:
            win.blit(self.enermy3die[self.dieCount // 1], (self.x - 100, self.y))
            self.dieCount += 1
            if self.dieCount >= 64:
                self.dieCount = 0

    def spirit(self):
        return self.ell

    def left(self):
        self.counter = -1

    def attack(self):
        self.cba = 1000

    def Health(self):
        if self.health > 0:
            self.health -= 1

    def finish(self):
        return self.finsihbomb

    def Mute(self):
        if not self.mute:
            self.mute = True
        else:
            self.mute = False

