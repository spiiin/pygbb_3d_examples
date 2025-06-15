planesVisible = False
facesNormalsVisible = False

A, B, C, D = Point(0, 0, 0), Point(1.87, 0.24, 0), Point(1, 1.75, 0), Point(1, 0.7, 2)

n1 = CrossI(VectorI(A, C), VectorI(A, B))
n2 = CrossI(VectorI(A, B), VectorI(A, D))
n3 = CrossI(VectorI(B, C), VectorI(B, D))
n4 = CrossI(VectorI(C, A), VectorI(C, D))

P = Point(1.8,1.2,0.1)

# Rendering of the edges and faces of the prism
seg1 = [Segment(B, C), Segment(C, A), Segment(A, B)]
seg2 = [Segment(B, D), Segment(D, A), Segment(A, B)]
seg3 = [Segment(C, D), Segment(D, B), Segment(B, C)]
seg4 = [Segment(A, D), Segment(D, C), Segment(C, A)]
faces = Polygon([A, B, C]), Polygon([A, B, D]), Polygon([B, C, D]), Polygon([C, A, D])

# Rendering of the normals to the faces
if facesNormalsVisible:
    for face, n in zip(faces, [n1,n2,n3,n4]):
        c = CentroidI(face)
        debugNormal = Vector(c, Invisible(c + UnitVectorI(n)), is_visible = facesNormalsVisible)
        
# Rendering of the planes constructed on the faces
if planesVisible:
    p1 = Plane(A, B, C, is_visible = planesVisible)
    p2 = Plane(A, B, D, is_visible = planesVisible)
    p3 = Plane(B, C, D, is_visible = planesVisible)
    p4 = Plane(C, A, D, is_visible = planesVisible)

@A.when_moved
@B.when_moved
@C.when_moved
@D.when_moved
@P.when_moved
def on_moved():
    checks = [
        (n1, A),  # face ABC
        (n2, A),  # face ABD
        (n3, B),  # face BCD
        (n4, C)   # face CAD
    ]

    inside = all(Dot(n, VectorI(a, P)) < 0 for n, a in checks)
    P.color = "green" if inside else "red"
    




