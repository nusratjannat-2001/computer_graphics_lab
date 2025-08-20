
import turtle
import math
import time

def draw_koch_curve(pen, start, end, depth):
    """Draw Koch curve from start to end point with given depth"""
    
    # Base case: draw straight line
    if depth == 0:
        pen.penup()
        pen.goto(start)
        pen.pendown()
        pen.goto(end)
        return
    
    # Calculate the four points for Koch transformation
    dx = (end[0] - start[0]) / 3
    dy = (end[1] - start[1]) / 3
    
    # Points at 1/3 and 2/3 of the line
    p1 = (start[0] + dx, start[1] + dy)
    p3 = (start[0] + 2*dx, start[1] + 2*dy)
    
    # Peak of equilateral triangle
    px = p1[0] + (p3[0] - p1[0])/2 + math.sqrt(3) * (p3[1] - p1[1])/2
    py = p1[1] + (p3[1] - p1[1])/2 - math.sqrt(3) * (p3[0] - p1[0])/2
    p2 = (px, py)
    
    # Recursively draw four segments
    draw_koch_curve(pen, start, p1, depth - 1)
    draw_koch_curve(pen, p1, p2, depth - 1)
    draw_koch_curve(pen, p2, p3, depth - 1)
    draw_koch_curve(pen, p3, end, depth - 1)

def draw_triangle(pen, vertices, color="black", width=3):
    """Draw a simple triangle"""
    pen.pencolor(color)
    pen.pensize(width)
    
    # Draw the three sides
    for i in range(3):
        pen.penup()
        pen.goto(vertices[i])
        pen.pendown()
        pen.goto(vertices[(i + 1) % 3])

def draw_iteration(pen, vertices, depth, iteration_num):
    """Draw one complete iteration of the Koch snowflake"""
    
    # Choose color based on iteration
    colors = ["black", "red", "blue", "green", "purple", "orange"]
    color = colors[iteration_num % len(colors)]
    
    pen.pencolor(color)
    pen.pensize(2)
    
    # Draw all three sides
    for i in range(3):
        start = vertices[i]
        end = vertices[(i + 1) % 3]
        draw_koch_curve(pen, start, end, depth)

def show_transformation_process(pen, vertices, max_depth):
    """Show the step-by-step transformation from triangle to Koch snowflake"""
    
    for iteration in range(max_depth + 1):
        # Clear previous drawing
        pen.clear()
        
        # Draw title
        pen.penup()
        pen.goto(-350, 280)
        pen.pencolor("black")
        pen.pensize(1)
        pen.write(f"Koch Snowflake - Iteration {iteration}", 
                 font=("Arial", 18, "bold"))
        
        # Draw description
        pen.goto(-350, 250)
        if iteration == 0:
            pen.write("Starting with a simple triangle", font=("Arial", 12, "normal"))
        else:
            pen.write(f"Each line segment replaced with 4 segments (Depth {iteration})", 
                     font=("Arial", 12, "normal"))
        
        # Draw current iteration
        print(f"\nIteration {iteration}:")
        if iteration == 0:
            print("Drawing basic triangle...")
            draw_triangle(pen, vertices, "black", 3)
        else:
            print(f"Drawing Koch snowflake with depth {iteration}...")
            draw_iteration(pen, vertices, iteration, iteration)
        
        # Update screen and pause
        screen.update()
        
        # Longer pause for first iteration, shorter for others
        pause_time = 3 if iteration == 0 else 2
        print(f"Pausing for {pause_time} seconds...")
        time.sleep(pause_time)
    
    print(f"\nTransformation complete! Final iteration has depth {max_depth}")

# Setup screen
screen = turtle.Screen()
screen.title("Koch Snowflake Transformation Process")
screen.setup(900, 700)
screen.bgcolor("white")
screen.tracer(0)

# Setup pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# Define triangle vertices (equilateral triangle)
triangle_vertices = [
    (0, 150),      # Top
    (-130, -75),   # Bottom left
    (130, -75)     # Bottom right
]

# Show the transformation process
max_iterations = 4
show_transformation_process(pen, triangle_vertices, max_iterations)

# Keep window open
screen.exitonclick()