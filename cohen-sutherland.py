import matplotlib.pyplot as plt

# Region codes
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

# Clipping window boundaries
x_min, y_min = 50, 50
x_max, y_max = 100, 100

# Function to compute region code for a point (x, y)
def compute_code(x, y):
    code = INSIDE
    if x < x_min:      # to the left of rectangle
        code |= LEFT
    elif x > x_max:    # to the right of rectangle
        code |= RIGHT
    if y < y_min:      # below the rectangle
        code |= BOTTOM
    elif y > y_max:    # above the rectangle
        code |= TOP
    return code

# Cohen-Sutherland clipping algorithm
def cohen_sutherland_clip(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            # Trivially accept
            accept = True
            break
        elif (code1 & code2) != 0:
            # Trivially reject
            break
        else:
            # At least one endpoint is outside
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            # Replace point outside window with intersection
            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)

    if accept:
        return [(x1, y1), (x2, y2)]
    else:
        return None

# Example lines
lines = [
    (20, 20, 120, 120),  # passes through window
    (60, 60, 80, 80),    # completely inside
    (20, 80, 40, 120),   # completely outside
    (70, 20, 110, 90)    # partially inside
]

# Plot
fig, ax = plt.subplots()
# Draw clipping rectangle
ax.plot([x_min, x_max, x_max, x_min, x_min],
        [y_min, y_min, y_max, y_max, y_min], 'k--')

for (x1, y1, x2, y2) in lines:
    # Original line in gray
    ax.plot([x1, x2], [y1, y2], 'gray', linestyle='dotted')

    # Clipped line in red
    clipped = cohen_sutherland_clip(x1, y1, x2, y2)
    if clipped:
        (cx1, cy1), (cx2, cy2) = clipped
        ax.plot([cx1, cx2], [cy1, cy2], 'r', linewidth=2)

ax.set_xlim(0, 150)
ax.set_ylim(0, 150)
ax.set_aspect('equal', adjustable='box')
plt.title("Cohen–Sutherland Line Clipping")
plt.show()
