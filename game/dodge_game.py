import pygame 
import random 


pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Avoid the ball!")
clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

player_size = 50
player_x = (screen_width - player_size) // 2
player_y = screen_height - player_size
player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
player_speed = 10

ball_size = 30
ball_x = random.randint(0, screen_width - ball_size)
ball_y = -ball_size 
ball_rect = pygame.Rect(ball_x, ball_y, ball_size, ball_size)
ball_speed = 5

running = True 
game_over = False 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.x > 0:
            player_rect.x -= player_speed
        if keys[pygame.K_RIGHT] and player_rect.x < screen_width - player_size:
            player_rect.x += player_speed

        ball_rect.y += ball_speed
        if ball_rect.y > screen_height:
            ball_rect.x = random.randint(0, screen_width - ball_size)
            ball_rect.y = -ball_size 
        
        if player_rect.colliderect(ball_rect):
            game_over = True 
    
    screen.fill(black)

    if not game_over:
        pygame.draw.rect(screen, blue, player_rect)
        pygame.draw.ellipse(screen, red, ball_rect)
    else:
        font = pygame.font.Font(None, 74)
        text = font.render("game over!", True, white)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()