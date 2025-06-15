A = Point(-1, -1, 0)
B = Point(-1.2, 1.5, 0)
C = Point(1.2, -0.6, 0)
p = Plane(A,B,C)

P = Point(0,0,3)
n = Cross(Vector(A, B), Vector(A, C))
d = Dot(n, Vector(A, P))

Pclip = If(
    Function.compare_LT(d, Number(0)),
    P,
    ClosestPoint(p, P, is_visible = False)
)