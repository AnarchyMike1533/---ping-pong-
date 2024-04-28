
from pygame import *
from random import randint
from time import time as timer


class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(wight,height))
        self.speed = player_speed
        #Прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >5:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

back = (154, 205, 50)
win_width = 600 
win_height = 500 
window = display.set_mode((win_width,win_height))
window.fill(back)
game = True 
finish = False 
clock = time.Clock()
FPS = 55 

speed_x = 3 
speed_y = 3 

ball = GameSprite('tennis.png',200,200,4,50,50)
racket1 = Player('123.png',30,200,4,50,150)
racket2 = Player('123.png',530,200,4,50,150)

font.init()
font = font.SysFont('Arial',35)
lose1 = font.render('ПОРАЖЕНИЕ!!!-1 игрок',True,(178, 34, 34))
lose2 = font.render('ПОРАЖЕНИЕ!!!-2 игрок',True,(178, 34, 34))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True :
        window.fill(back)
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        racket1.update_l()
        racket2.update_r()

        if ball.rect.x < 0:
            finish = True 
            window.blit(lose1,(200,200))

        if ball.rect.x > win_width-50:
            finish = True 
            window.blit(lose2,(200,200))


        if ball.rect.y > win_width - 150 or ball.rect.y < 0:
            speed_y *= -1 

        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
        
            speed_x *= -1
            speed_y *= 1

            

        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
        

