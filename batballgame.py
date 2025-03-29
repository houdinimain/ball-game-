import pgzrun
import random

WIDTH = 800
HEIGHT = 750

score = 0   


ball = Rect((0,0),(20,20))
bat = Rect((200,700),(50,20))

speedx = 4
speedy = 4

def draw():
    screen.clear()
    screen.fill("white")
    screen.draw.filled_rect(ball,"red")
    screen.draw.filled_rect(bat,"green")
     


def update():
    global speedx,speedy
    ball.x += speedx
    ball.y += speedy
    if keyboard.d:
        bat.x+= 4
    if keyboard.a:
        bat.x-= 4
    if ball.right > WIDTH or ball.left < 0:
        speedx =- speedx
    
    if ball.top < 0:
        speedy =- speedy

    if ball.colliderect(bat):
        speedy =- speedy












pgzrun.go()

















