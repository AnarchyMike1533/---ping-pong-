
from pygame import *
from random import randint
from time import time as timer







class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,player_speed, wight, height, size_x, size_y):
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

ball = GameSprite('Tennis.png',100,100,4,50,50,50,50)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if finish != True :
            window.fill(back)
            ball.reset()
        display.update()
        clock.tick(FPS)
        
