import numpy as np
from math import comb  # Python >= 3.8
import matplotlib.pyplot as plt

# ---- Data structure for a point ----
class Point3D:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"({self.x:.3f}, {self.y:.3f}, {self.z:.3f})"

# ---- Compute binomial coefficients ----
def computeCoefficients(n):
    c = [comb(n, k) for k in range(n + 1)]
    return c

# ---- Compute a point on the Bézier curve for a given u ----
def computePoint(u, nControls, controls, coefficients):
    n = nControls - 1
    pt = Point3D()

    for k in range(nControls):
        blend = coefficients[k] * (u ** k) * ((1 - u) ** (n - k))
        pt.x += controls[k].x * blend
        pt.y += controls[k].y * blend
        pt.z += controls[k].z * blend

    return pt

# ---- Generate full Bézier curve ----
def bezier(controls, m):
    nControls = len(controls)
    coefficients = computeCoefficients(nControls - 1)
    curve = []

    for i in range(m + 1):
        u = i / float(m)
        pt = computePoint(u, nControls, controls, coefficients)
        curve.append(pt)

    return curve

# ---- Example usage ----
if __name__ == "__main__":
    # Example control points
    controls = [
        Point3D(0, 0, 0),
        Point3D(1, 2, 0),
        Point3D(3, 3, 0),
        Point3D(4, 0, 0)
    ]

    curve = bezier(controls, m=20)

    print("Generated Bézier curve points:")
    for pt in curve:
        print(pt)
        
# Plotting function (2D only)
xs = [pt.x for pt in curve]
ys = [pt.y for pt in curve]

control_xs = [pt.x for pt in controls]
control_ys = [pt.y for pt in controls]

plt.plot(xs, ys, 'b-', label='Bézier curve')
plt.plot(control_xs, control_ys, 'ro--', label='Control points')
plt.legend()
plt.show()