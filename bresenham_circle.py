import matplotlib.pyplot as plt

def bresenham_circle(xc, yc, r):
    """
    Midpoint Circle Drawing Algorithm (Bresenham’s Circle).
    Returns list of points forming the circle.
    """
    x = 0
    y = r
    d = 3 - 2 * r
    points = []

    while y >= x:
        # 8-way symmetry
        points.extend([
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),
            (xc + y, yc + x),
            (xc - y, yc + x),
            (xc + y, yc - x),
            (xc - y, yc - x),
        ])

        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1
        x += 1

    return points

# --- demo & plot ---
if __name__ == "__main__":
    xc, yc = 50, 50   # circle center
    r = 30            # radius

    pts = bresenham_circle(xc, yc, r)
    xs, ys = zip(*pts)

    plt.figure(figsize=(6, 6))
    plt.scatter(xs, ys, s=30, marker='s', color='blue')  # circle pixels
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Bresenham Circle Drawing")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, linewidth=0.5)
    plt.show()
