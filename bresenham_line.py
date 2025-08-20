import matplotlib.pyplot as plt

def bresenham(x0, y0, x1, y1):
    """
    Integer Bresenham line algorithm (handles all octants).
    Returns a list of (x, y) pixel coordinates from (x0, y0) to (x1, y1).
    """
    points = []

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    x, y = x0, y0
    while True:
        points.append((x, y))
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy

    return points

# --- demo & plot ---
if __name__ == "__main__":
    # try different endpoints here
    x0, y0 = 3, 2
    x1, y1 = 23, 14

    pts = bresenham(x0, y0, x1, y1)

    xs, ys = zip(*pts)

    plt.figure(figsize=(6, 6))
    # draw the raster points
    plt.scatter(xs, ys, s=40, marker='s')         # filled pixels
    # optional: draw the ideal straight line for reference
    plt.plot([x0, x1], [y0, y1], linestyle='--', linewidth=1)

    # make it look like a pixel grid
    xmin = min(x0, x1) - 2
    xmax = max(x0, x1) + 2
    ymin = min(y0, y1) - 2
    ymax = max(y0, y1) + 2
    plt.xticks(range(xmin, xmax + 1))
    plt.yticks(range(ymin, ymax + 1))
    plt.grid(True, which='both', linewidth=0.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Bresenham Line Drawing")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
