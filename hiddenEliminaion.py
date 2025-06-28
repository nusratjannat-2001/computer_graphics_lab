import pygame
import sys

# Initialize Pygame
pygame.init()

# Colors (R, G, B)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up window
win_width = 400
win_height = 400
screen = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Shape Drawer")

# Fill background with white
screen.fill(WHITE)

# --- Shape functions ---
def draw_triangle():
    x = [10, 50, 100]
    y = [100, 20, 100]
    points = [(x[i], y[i]) for i in range(3)]
    pygame.draw.polygon(screen, YELLOW, points)

def draw_circle():
    pygame.draw.circle(screen, RED, (100, 100), 45)

def draw_rectangle():
    rect_x1 = 80  # 100 - 20
    rect_y1 = 80  # 100 - 20
    rect_x2 = 180
    rect_y2 = 180
    width = rect_x2 - rect_x1
    height = rect_y2 - rect_y1
    pygame.draw.rect(screen, GREEN, (rect_x1, rect_y1, width, height))

# --- Main ---
# Take input sequence (e.g., CRT)
sequence = input("Enter shape sequence (C, R, T): ")

# Draw shapes according to sequence
for char in sequence:
    if char == 'C':
        draw_circle()
    elif char == 'R':
        draw_rectangle()
    else:
        draw_triangle()

# Update the display
pygame.display.update()

# Wait until user closes the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
