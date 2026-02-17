import pygame 
import random 


pygame.init()

width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dino Game!")

white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)


class Dino:
    def __init__(self):
        self.rect = pygame.Rect(50, 300, 40, 40)
        self.jumping = False 
        self.velocity_y = 0 

    def jump(self):
        if not self.jumping:
            self.jumping = True 
            self.velocity_y = -10
    
    def update(self):
        self.rect.y += self.velocity_y
        self.velocity_y += 0.5      # gravity 

        if self.rect.y > 300:
            self.rect.y = 300
            self.jumping = False 
            self.velocity_y = 0 

class Obstacle:
    def __init__(self):
        self.rect = pygame.Rect(width, 300, 40, 40)
    
    def update(self):
        self.rect.x -= 5 


if __name__ == "__main__":
    clock = pygame.time.Clock()
    dino = Dino()
    isRunning = True 
    obstacles = []

    while isRunning:
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dino.jump()

        if random.randint(1, 100) <= 3:
            obstacles.append(Obstacle())
        
        for obs in obstacles[:]:
            obs.update()
            if obs.rect.x < 0:
                obstacles.remove(obs)
            
            if dino.rect.colliderect(obs):
                isRunning = False 
        
        dino.update()

        pygame.draw.rect(screen, green, dino.rect)
        for obstacle in obstacles:
            pygame.draw.rect(screen, red, obstacle.rect)
        
        pygame.display.flip()
        clock.tick(60)