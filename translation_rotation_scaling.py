import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------
# 2D point class
# ----------------------------------------
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# ----------------------------------------
# Initialize the global matrix (identity)
# ----------------------------------------
theMatrix = np.identity(3)

# ----------------------------------------
# Matrix multiplication: A * B → B
# ----------------------------------------
def matrixPreMultiply(a, b):
    return np.dot(a, b)

# ----------------------------------------
# Translation matrix
# ----------------------------------------
def translate2(tx, ty):
    global theMatrix
    m = np.identity(3)
    m[0][2] = tx
    m[1][2] = ty
    theMatrix = matrixPreMultiply(m, theMatrix)

# ----------------------------------------
# Scaling matrix around a reference point
# ----------------------------------------
def scale2(sx, sy, refPt):
    global theMatrix
    m = np.identity(3)
    m[0][0] = sx
    m[0][2] = (1 - sx) * refPt.x
    m[1][1] = sy
    m[1][2] = (1 - sy) * refPt.y
    theMatrix = matrixPreMultiply(m, theMatrix)

# ----------------------------------------
# Rotation matrix around a reference point
# ----------------------------------------
def rotate2(a, refPt):
    global theMatrix
    m = np.identity(3)
    rad = np.radians(a)
    cosA = np.cos(rad)
    sinA = np.sin(rad)

    m[0][0] = cosA
    m[0][1] = -sinA
    m[0][2] = refPt.x * (1 - cosA) + refPt.y * sinA

    m[1][0] = sinA
    m[1][1] = cosA
    m[1][2] = refPt.y * (1 - cosA) - refPt.x * sinA

    theMatrix = matrixPreMultiply(m, theMatrix)

# ----------------------------------------
# Apply transformation to all points
# ----------------------------------------
def transformPoints2(points):
    transformed = []
    for pt in points:
        vec = np.array([pt.x, pt.y, 1])
        result = np.dot(theMatrix, vec)
        transformed.append(Point2D(result[0], result[1]))
    return transformed

# ----------------------------------------
# Example: a triangle
# ----------------------------------------
if __name__ == "__main__":
    # Original triangle
    pts = [Point2D(50.0, 50.0), Point2D(150.0, 50.0), Point2D(100.0, 150.0)]
    refPt = Point2D(100.0, 100.0)

    # Reset transformation matrix
    theMatrix = np.identity(3)

    # Apply transformations
    scale2(0.5, 0.5, refPt)
    rotate2(90, refPt)
    translate2(0, 150)

    # Transform points
    transformed_pts = transformPoints2(pts)

    # Plot original and transformed triangle
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Original
    x = [p.x for p in pts] + [pts[0].x]
    y = [p.y for p in pts] + [pts[0].y]
    ax.plot(x, y, 'b-', label='Original')

    # Transformed
    x2 = [p.x for p in transformed_pts] + [transformed_pts[0].x]
    y2 = [p.y for p in transformed_pts] + [transformed_pts[0].y]
    ax.plot(x2, y2, 'r-', label='Transformed')

    ax.legend()
    ax.grid(True)
    ax.set_title('2D Transformations: Scale, Rotate, Translate')
    plt.show()
