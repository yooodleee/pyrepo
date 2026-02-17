import pygame 
import random 


WIDTH = 800
HEIGHT = 600

player = Actor('player', (WIDTH // 2, HEIGHT - 50))
balls = []
game_over = False 


def create_ball():
    if not game_over:
        ball = Actor('ball', (random.randint(0, WIDTH), - 50))
        ball.speed = random.randint(3, 8)
        balls.append(ball)

clock.schedule_interval(create_ball, 1.0)

def update():
    global game_over
    if game_over:
        return 
    
    if keyboard.left:
        player.x -= 5 
    if keyboard.right:
        player.x += 5
    
    for ball in balls[:]:
        ball.y += ball.speed
        if ball.colliderect(player):
            game_over = True 
        if ball.y > HEIGHT:
            balls.remove(ball)

def draw():
    screen.clear()
    if not game_over:
        player.draw()
        for ball in balls:
            ball.draw()
    else:
        screen.draw.text('game over!', center=(WIDTH//2, HEIGHT//2), color='red', fontsize=60)

pgzrun.go()