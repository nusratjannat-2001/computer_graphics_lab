import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Window dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Travel")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Star class
class Star:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.size = random.uniform(1, 3)
        self.speed = random.uniform(1, 4)

    def move(self):
        self.x += self.speed
        if self.x > WIDTH:
            self.x = 0
            self.y = random.uniform(0, HEIGHT)

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), int(self.size))

# Create stars
num_stars = 100
stars = [Star() for _ in range(num_stars)]

# Clock for smooth FPS
clock = pygame.time.Clock()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    # Move and draw stars
    for star in stars:
        star.move()
        star.draw()

    # Draw the man (simple circle here — replace with your image later!)
    pygame.draw.circle(screen, (255, 0, 0), (WIDTH // 2, HEIGHT // 2), 20)

    pygame.display.update()
    clock.tick(60)
