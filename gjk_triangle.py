A = Point(-1, -1, 0)
B = Point(-1.2, 1.5, 0)
C = Point(1.2, -0.6, 0)

bca = CrossI(VectorI(B,C), VectorI(B,A))
p = Plane(B, VectorI(B,C), bca, is_visible = True)

P = Point(-3, -3, 3)
p_normal = CrossI(bca, VectorI(B,C))
d = Dot(p_normal, VectorI(B, P))

Pclip = If(
    Function.compare_LT(d, Number(0)),
    ClosestPointI(p, P),
    P
)

segments = [Segment(A,B), Segment(A,C), Segment(B,C)]
tri = Polygon([A,B,C])

#debug
debugLines = True
lineAB = Line(A,B, is_visible = debugLines)
lineAC = Line(A,C, is_visible = debugLines)

ab = VectorI(A, B)
ac = VectorI(A, C)
bc = VectorI(B, C)
ap = VectorI(A, Pclip) #vector to point
bp = VectorI(B, Pclip) #vector to point

abc = CrossI(ab, ac)
directionFromAC = CrossI(CrossI(ac, ap), ac)
directionFromAB = CrossI(CrossI(ab, ap), ab)

#for side resolution
sameDir_abcac_ap = Dot(CrossI(abc, ac), ap)
sameDir_ac_ap = Dot(ac, ap)
sameDir_ababc_ap = Dot(CrossI(ab, abc), ap)
sameDir_ab_ap = Dot(ab, ap)

#debug render direction from AC
midAC = MidpointI(A, C)
dirAC = Vector(midAC, Invisible(midAC + UnitVectorI(directionFromAC)))

#debug render direction from AB
midAB = MidpointI(A, B)
dirAB = Vector(midAB, Invisible(midAB + UnitVectorI(directionFromAB)))

#debug render direction from A
dirBC = Vector(A, Invisible(A + UnitVectorI(ap)))

#debug render direction from ABC face
center = CentroidI(tri)
centerDir = If(
    Function.compare_LT(Dot(abc, ap), Number(0)),
    PointI(0, 0, 1),
    PointI(0, 0, -1)
)
centerDir.is_visible = False
dirABC = Vector(center, Invisible(center + centerDir))

@A.when_moved
@B.when_moved
@C.when_moved
@P.when_moved
def on_moved():
    on_ac_side = sameDir_abcac_ap > 0 and sameDir_ac_ap > 0
    on_ab_side = sameDir_ababc_ap > 0 and sameDir_ab_ap > 0
    on_a_side = sameDir_abcac_ap > 0 and sameDir_ababc_ap > 0
    on_tri_side = not (on_ac_side or on_ab_side or on_a_side)
    dirAC.color = "green" if on_ac_side else "black"
    dirAB.color = "green" if on_ab_side else "black"
    dirBC.color = "green" if on_a_side else "black"
    dirABC.color = "green" if on_tri_side else "black"
    

    