import math

def prism():
    A, B, C, D = Point(3, 3, 0), Point(5, 3.24, 0), Point(4, 4.75, 0), Point(4, 3.7, 2)
    seg1 = [Segment(B, C), Segment(C, A), Segment(A, B)]
    seg2 = [Segment(B, D), Segment(D, A), Segment(A, B)]
    seg3 = [Segment(C, D), Segment(D, B), Segment(B, C)]
    seg4 = [Segment(A, D), Segment(D, C), Segment(C, A)]
    faces = Polygon([A, B, C]), Polygon([A, B, D]), Polygon([B, C, D]), Polygon([C, A, D])
    return A, B, C, D
    
points = prism()

O = Point(0, 0, 0)

dirPoint = Point(0, 1, 0)
dirVector = Vector(O, dirPoint)

support_planes = [PerpendicularPlaneI(support_point, dirVector) for support_point in points]

@dirPoint.when_moved
def on_moved():
    proj = [Dot(dirVector, VectorI(O, p)) for p in points]
    max_proj = max(proj)
    max_index = proj.index(max_proj)
    for i, support_plane in enumerate(support_planes):
        support_plane.is_visible = i == max_index
    
    

