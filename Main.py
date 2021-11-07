import pygame
import os
from tkinter import *
from level1 import *
from level2 import *
from level3 import *
from level4 import *
from level5 import*

class mainmenu():
    pygame.init()
    pygame.mixer.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (70, 25)
    bg = pygame.image.load('MainMenu.png')
    pygame.display.set_caption('RISE OF GUARDIAN')
    insbg = pygame.image.load('Instruction.png')
    playOn = pygame.image.load('PlayOn.png')
    playOff = pygame.image.load('PlayOff.png')
    instructionOn = pygame.image.load('InstructionOn.png')
    instructionOff = pygame.image.load('InstructionOff.png')
    exitOn = pygame.image.load('ExitOn.png')
    exitOff = pygame.image.load('ExitOff.png')
    pygame.mixer.music.load('HeartOfCourage.ogg')
    pygame.mixer.music.play(-1)

    def __init__(self):
        self.w = pygame.display.set_mode((1400, 800))
        self.MRun = True
        self.BMenu = False
        self.LL = []
        self.Game = True
        self.level = 1
        self.mute = False
        self.hp = 5
        self.score = 0
        self.decision = 0

    def instruc(self):
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
                if 0 + 60 > mouse[0] > 0 and 0 + 60 > mouse[1] > 0:
                    if click[0] == 1:
                        paused = False
            self.w.blit(self.insbg, (0, 0))
            pygame.display.update()

    def menu(self):
        while self.MRun:
            self.w.blit(self.bg, (0, 0))
            mouse = pygame.mouse.get_pos()

            if 576 + 248 > mouse[0] > 576 and 298 + 68 > mouse[1] > 298 and self.MRun:
                self.w.blit(self.playOn, (576, 298))
            else:
                self.w.blit(self.playOff, (576, 298))
            if 525 + 347 > mouse[0] > 525 and 442 + 68 > mouse[1] > 442 and self.MRun:
                self.w.blit(self.instructionOn, (525, 442))
            else:
                self.w.blit(self.instructionOff, (525, 442))
            if 576 + 248 > mouse[0] > 576 and 586 + 68 > mouse[1] > 586 and self.MRun:
                self.w.blit(self.exitOn, (576, 586))
            else:
                self.w.blit(self.exitOff, (576, 586))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.MRun = False
                    self.BMenu = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 576 + 248 > mouse[0] > 576 and 298 + 68 > mouse[1] > 298 and self.MRun:
                        self.game()
                        self.MRun = False
                    if 525 + 347 > mouse[0] > 525 and 442 + 68 > mouse[1] > 442 and self.MRun:
                        self.instruc()
                    if 576 + 248 > mouse[0] > 576 and 586 + 68 > mouse[1] > 586 and self.MRun:
                        self.MRun = False
                        self.BMenu = False


            pygame.display.update()
            if self.BMenu:
                self.MRun = True

    def game(self):
        self.level = 1
        pygame.mixer.music.load('Evergreen.ogg')
        pygame.mixer.music.play(-1)
        while self.Game:
            if not self.mute:
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.pause()
            if self.level == 1:
                LEVEL1 = Level1(self.w, self.hp, self.score, self.mute)
                GET = LEVEL1.RUN()
                self.hp = GET[0]
                self.score = GET[1]
                self.mute = GET[2]
                self.decision = GET[3]
            elif self.level == 2:
                LEVEL2 = Level2(self.w, self.hp, self.score, self.mute)
                GET = LEVEL2.RUN()
                self.hp = GET[0]
                self.score = GET[1]
                self.mute = GET[2]
                self.decision = GET[3]
            elif self.level == 3:
                LEVEL3 = Level3(self.w, self.hp, self.score, self.mute)
                GET = LEVEL3.RUN()
                self.hp = GET[0]
                self.score = GET[1]
                self.mute = GET[2]
                self.decision = GET[3]
            elif self.level == 4:
                pygame.mixer.music.load('Aeterna.ogg')
                pygame.mixer.music.play(-1)
                LEVEL4 = Level4(self.w, self.hp, self.score, self.mute)
                GET = LEVEL4.RUN()
                self.hp = GET[0]
                self.score = GET[1]
                self.mute = GET[2]
                self.decision = GET[3]
            elif self.level == 5:
                pygame.mixer.music.load('StrengthOfaThousandMen.ogg')
                pygame.mixer.music.play(-1)
                LEVEL5 = Level5(self.w, self.hp, self.score, self.mute)
                GET = LEVEL5.RUN()
                self.hp = GET[0]
                self.score = GET[1]
                self.mute = GET[2]
                self.decision = GET[3]

            if self.decision==-1:
                lose = True
                while lose:
                    self.hp = 5
                    self.score = 0
                    self.LL.append(Level1(self.w,self.hp, self.score, self.mute))
                    GET = self.LL[-1].RUN()
                    if GET[2]==1:
                        self.level += 1
                        lose = False
                    if GET[2]==0:
                        self.BMenu = True
                        if not self.mute:
                            pygame.mixer.music.load('HeartOfCourage.ogg')
                            pygame.mixer.music.play(-1)
                        break

            elif self.decision == 1:
                self.level += 1
            else:
                self.hp = 5
                self.score = 0
                self.BMenu = True
                if not self.mute:
                    pygame.mixer.music.load('HeartOfCourage.ogg')
                    pygame.mixer.music.play(-1)
                break

class exitwindow():
    def __init__(self, top):
        self.top = top
        top.title("RISE OF GUARDIAN")
        top.geometry("1000x600+280+100")
        credit = PhotoImage(file="Credit.png")
        self.label = Label(top, image=credit)
        self.label.image = credit
        self.label.pack(fill="both", expand=True)

M = mainmenu()
M.menu()
pygame.quit()

top = Tk()
my_gui = exitwindow(top)
top.mainloop()

quit()