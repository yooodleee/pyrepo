import pygame 


pygame.init()

# Set screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('My first Pygame')

# Define color 
white = (255, 255, 255)
blue = (0, 0, 255)

# Varialbe for game loop 
running = True 

while running:      # Game Loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    # Game status update(Leave blank here)
    
    # Drawing screen 
    screen.fill(white)
    pygame.draw.circle(screen, blue, (400, 300), 50)    # Draw a blue circle
    pygame.display.flip()

pygame.quit()