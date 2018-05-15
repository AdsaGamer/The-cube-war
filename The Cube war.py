import pygame, sys, time
from pygame.locals import *
pygame.init()
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)
clock = pygame.time.Clock()
screen=pygame.display.set_mode((800,600),0,32)
char=pygame.image.load("Primary_character.png").convert_alpha()
background=pygame.image.load("background.jpg").convert()
rocks=pygame.image.load("rock pile.png").convert_alpha()
flame=pygame.image.load("fire.png").convert_alpha()
atile=pygame.image.load("a.png").convert_alpha()
dtile=pygame.image.load("d.png").convert_alpha()
wtile=pygame.image.load("w.png").convert_alpha()
box=pygame.image.load("box.png").convert_alpha()
rock=pygame.image.load("rock.png").convert_alpha()
magbar=pygame.image.load("magbar.png").convert_alpha()
coin=pygame.image.load("coin.png").convert_alpha()
coinimg=pygame.image.load("coin.png").convert_alpha()
healitem=pygame.image.load("health.png").convert_alpha()
magicitem=pygame.image.load("magic.png").convert_alpha()
wall=pygame.image.load("wall.png").convert_alpha()
wallsection=pygame.image.load("wallsection.png").convert_alpha()
buycon=pygame.image.load("buycon.png").convert_alpha()
logo=pygame.image.load("studiologo.png").convert_alpha()
logo=pygame.transform.scale(logo, (800,600))
healitem=pygame.transform.scale(healitem, (50,100))
magicitem=pygame.transform.scale(magicitem, (50,50))
coin=pygame.transform.scale(coin, (50,100))
buycon=pygame.transform.scale(buycon, (50,50))
#cubes and shapes in a war, semicircle is you, all quadrilaterals on one side,
#rounded shapes on the other side, semicircle is born and not accepted
countmagic=0
x,y=0,450
x2,y2=0,0
movex=0
movey=0
chat=0
black=(0,0,0)
count=0
count1=0
rocky=-100
coincount=10
jump=True
jumped=False
falling=False
stoodbox=False
standingbox=False
ability1=False
hp=196
magic=196
studiolift=0
timepast=0
font = pygame.font.SysFont(None, 25)
def message(msg,color,x2,y2):
        screen_text = font.render(msg, True, color)
        screen.blit(screen_text, (x2, y2))
while True:
    screen.blit(background, (x,0))
    if x<=-464 and x>=-810 and y<=400 and y>=396:
        movey=0
        standingbox=True#standing on container
        jump=True
    else:
        standingbox=False
    if jumped==True:
        if count1<=25 and jump==True:
            movey=-4
            count1+=1
        if count<=25 and jump==False:
            jumped=False
        if count1>25:
            count1=0
            movey=+4
            jumped=False
            jump=False
    if jumped==False and y<=460 and standingbox==False:
            movey=+4
    if y>=456 and y<=460 and jumped==False and standingbox==False:
        movey=0
        jump=False
        count1=0
        stuf=True
        jump=True
    clock.tick(100)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_d:
                movex=-3
                char=pygame.image.load("Primary_character.png").convert_alpha()
            elif event.key==K_a:
                movex=+3
                char=pygame.image.load("Primary_characterleft.png").convert_alpha()
            elif event.key==K_e:
                print(x,",",y)
            elif event.key==K_w:
                jumped=True
            elif event.key==K_x:
                ability1=True
        if event.type==KEYUP:
            if event.key==K_d:
                movex=0
            elif event.key==K_a:
                movex=0
            elif event.key==K_x:
                ability1=False
    if x>=321 and x<=325:
        movex=-1#walking into wall
    if x<=-453 and x>=-457 and y<=458 and y>=400:
        movex=+1#walking into box left
    if x>=-837 and x<=-833 and y<=458 and y>=400:
        movex=-1#walking into box right
    if rocky>=600:
        rocky=-6000
    elif rocky<=600:
        rocky+=20
    if ability1==True:
        if magic>0:
            magic-=1
        elif magic==0:
            ability1=False
    if ability1==False:
        if magic<=195:
            if countmagic==400:
                magic+=1
            else:
                countmagic+=1
        elif magic>=196:
            magic=196
            countmagic=0
        if x>=-2955 and x<=-2953:
            movex=+1
        if x>=-3321 and x<=-3319:
            movex=-1
    x+=movex
    y+=movey
    screen.blit(atile, (x+350,400))
    screen.blit(dtile, (x+450,400))
    screen.blit(wtile, (x+1100,400))
    message("Use this to jump", white,x+1000,375)
    message("Use these to move:",white,x+325,350)
    screen.blit(coin, (x+2000, 300))
    screen.blit(box, (x+1000, 470))
    screen.blit(wall, (x+3500,0))
    screen.blit(buycon, (x+3600,200))
    screen.blit(char, (350,y))
    screen.blit(rock, (x+400, rocky))
    screen.blit(flame, (x+50, 440))
    screen.blit(flame, (x+440, 340))
    screen.blit(flame, (x+770, 390))
    screen.blit(flame, (x+1100, 400))
    message("Collect these to buy parts of useful relics:",white,x+1900, 285)
    message("Buy/use these to heal:",white,x+2300, 275)
    message("Use these to regen your magic, it also regens over time:",white,x+2500, 300)
    message("Your magic can be used for a number of things:",white,x+3000, 300)
    message("*Phasing through walls",white,x+3000,325)
    message("*Fixing machines",white,x+3000,350)
    screen.blit(healitem, (x+2400, 300))
    screen.blit(magicitem, (x+2600, 325))
    screen.blit(wallsection, (x+3500,0))
    message("coins x"+str(coincount),white,240,100)
    screen.blit(magbar, (20, 140))
    screen.blit(magbar, (20, 200))
    screen.blit(char, (20, 40))
    screen.blit(coinimg, (220,100))
    pygame.draw.rect(screen, red,(22,142,hp,46))
    pygame.draw.rect(screen, blue,(22,202,magic,46))
    #if timepast>500:
    #    studiolift-=0.0000001
    #elif timepast<=500:
    #    timepast+=1
    #    screen.blit(logo, (0,studiolift))
    #else:
    #    pass
    pygame.display.update()


