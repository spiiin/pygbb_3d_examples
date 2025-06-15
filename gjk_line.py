debugPlanes = False
debugDir = True

A = Point(2, 1.1, 0)
B = Point(-1.25, -6.3, 3.2)
O = Point(0, 0, 0)

ab = Vector(A, B)
ao = Vector(A, O)
n = CrossI(ab, ao)
newDir = CrossI(n, ab)

p1 = PerpendicularPlane(A, n, is_visible = debugPlanes)
p2 = PerpendicularPlane(A, newDir, is_visible = debugPlanes)

if debugDir:
    C = MidpointI(A,B)
    debugNewDir = Vector(C, Invisible(C + UnitVectorI(newDir)), color = "blue")