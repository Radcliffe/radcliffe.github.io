import sympy as sp

x, y = sp.symbols("x y")
X, Y = sp.symbols("X Y")


def midpoint(p, q):
    """Return the midpoint of the segment joining p and q."""
    return ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)


def line_through(p, q):
    """Return the equation L(X, Y) = 0 of the line through p and q."""
    return (X - p[0]) * (Y - q[1]) - (X - q[0]) * (Y - p[1])


def intersection(line1, line2):
    """Return the intersection point of the two given lines."""
    solution = sp.solve((line1, line2), (X, Y), dict=True)[0]
    return (solution[X], solution[Y])


def polygon_area(vertices):
    """Return the signed area of a polygon with ordered vertices."""
    n = len(vertices)
    return sp.simplify(
        sum(
            vertices[i - 1][0] * vertices[i][1]
            - vertices[i - 1][1] * vertices[i][0]
            for i in range(n)
        ) / 2
    )


def slope(P, Q):
    return sp.factor(
        sp.simplify(
            (Q[1] - P[1]) / (Q[0] - P[0])
        )
    )


def pretty(expr):
    """Factor and print expressions in a compact human-readable form."""
    expr = sp.factor(sp.simplify(expr))
    return str(expr).replace("**", "^").replace("*", "")


zero = sp.Integer(0)
two = sp.Integer(2)

A = (zero, zero)
B = (two, zero)
C = (x, y)
D = (zero, two)
vertices = [A, B, C, D]

E = midpoint(A, B)
F = midpoint(B, C)
G = midpoint(C, D)
H = midpoint(D, A)

P = intersection(line_through(A, F), line_through(B, G))
Q = intersection(line_through(B, G), line_through(C, H))
R = intersection(line_through(C, H), line_through(D, E))
S = intersection(line_through(D, E), line_through(A, F))
inner_vertices = [P, Q, R, S]

for label, point in zip("PQRS", inner_vertices):
    print(f"{label}x = {pretty(point[0])}")
    print(f"{label}y = {pretty(point[1])}")

outer_area = polygon_area(vertices)
inner_area = polygon_area(inner_vertices)

print(f"\nouter area = {pretty(outer_area)}")
print("inner area:")
print(pretty(inner_area))

print("\nouter area - 5 * inner area =")
print(pretty(outer_area - 5 * inner_area))

print("\n6 * inner area - outer area =")
print(pretty(6 * inner_area - outer_area))
