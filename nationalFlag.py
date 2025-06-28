import pygame
import sys

# Initialize pygame
pygame.init()

# Scale factor
scale_factor = 30

# Take input for start point
x1 = int(input("Enter the start x-coordinate of the flag: "))
y1 = int(input("Enter the start y-coordinate of the flag: "))

# Calculate end points (width:height = 10:6)
flag_width = 10 * scale_factor
flag_height = 6 * scale_factor
x2 = x1 + flag_width
y2 = y1 + flag_height

# Window size large enough to fit flag and handle
win_width = max(800, x2 + 100)
win_height = max(600, y2 * 2 + 100)
screen = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Bangladesh Flag")

# Colors
GREEN = (0, 106, 78)
RED = (244, 42, 65)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 235)  # Background

# Fill background with sky blue
screen.fill(SKY_BLUE)

# Draw green rectangle (flag)
pygame.draw.rect(screen, GREEN, (x1, y1, flag_width, flag_height))

# Draw red circle (sun)
circle_radius = 2 * scale_factor
circle_x = x1 + int(0.45 * flag_width)
circle_y = y1 + int(0.5 * flag_height)
pygame.draw.circle(screen, RED, (circle_x, circle_y), circle_radius)

# Draw black handle (flag pole)
pole_width = max(scale_factor // 3, 10)
pygame.draw.rect(screen, BLACK, (x1 - pole_width, y1, pole_width, 2 * flag_height))

# Update the display
pygame.display.update()

# Wait until the user closes the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
