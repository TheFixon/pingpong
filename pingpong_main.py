from pygame import *

window_width = 600
window_height = 500
back = (200,255,255)
window = display.set_mode((window_width, window_height))

img_ball = "pingpong_ball.png"
img_pong = "pingpong.png"


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def updateL(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[K_s] and self.rect.y<window_height-80:
            self.rect.y+=self.speed

    def updateR(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[K_DOWN] and self.rect.y<window_height-80:
            self.rect.y+=self.speed

game = True
finish = False
clock = time.Clock()
fps = 60
racket1 = Player(img_pong, 30, 280, 50, 150, 4)
racket2 = Player(img_pong, 520, 280, 50, 150, 4)
ball = GameSprite(img_ball, 200, 200, 50, 50, 4)
font.init()
font1 = font.SysFont(None, 35)
lose1=font1.render("Player 1 lose",True, (100, 0, 0))
lose2=font1.render("Player 2 lose",True, (100, 0, 0))
speed_x = 3
speed_y = 3
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        
    racket1.updateL()
    racket2.updateR()
    ball.rect.x+=speed_x
    ball.rect.y+=speed_y
    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_x *= -1
        speed_y *= 1
    if ball.rect.y >= window_height or ball.rect.y <= 0:
        speed_y *= -1
    if ball.rect.x <= 0 or ball.rect.x >= window_width:
        finish = True
        if ball.rect.x <= 0:
            window.blit(lose1, (200,200))
        if ball.rect.x >= window_width:
            window.blit(lose2, (200,200))
    racket1.reset()
    racket2.reset()
    ball.reset()
    clock.tick(fps)
    display.update()
