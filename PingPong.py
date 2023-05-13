from pygame import *
from random import *
from time import time as timer


window = display.set_mode((700,500))
display.set_caption('Пинг-понг') 
background = (0,180,255)
window.fill(background)

class gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,rx=20,ry=150):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (rx, ry))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(gamesprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 620:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 620:
            self.rect.y += self.speed
        
class Enemy (gamesprite): 
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.x = randint(80, 620)
            self.rect.y = 0



player1 = Player('racket.png',20, 190, 4)
player2 = Player('racket.png', 660, 190, 4)
ball = gamesprite('bol.png', 250, 250, 3, 30, 30)
font.init()
font1 = font.Font(None, 35) 
lose1 = font1.render('Player 1 LOSE', True, (180, 0, 0)) 
lose2 = font1.render('Player 2 LOSE', True, (180, 0, 0)) 

clock = time.Clock()
FPS = 60

speed_x = 3
speed_y = 3

finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(background)
        player1.reset()
        player1.update1()
        player2.reset()
        player2.update2()
        ball.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1
    if ball.rect.y > 470 or ball.rect.y < 0:
        speed_y *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
    if ball.rect.x > 700:
        finish = True
        window.blit(lose2, (200, 200))

    clock.tick(FPS)
    display.update()