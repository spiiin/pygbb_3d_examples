def prism(pt):
    vals = [(pt[0] + p[0], pt[1] + p[1], pt[2] + p[2]) for p in [(3, 3, 0), (5, 3.24, 0), (4, 4.75, 0), (4, 3.7, 2)]]
    
    A, B, C, D = Point(*vals[0]), Point(*vals[1]), Point(*vals[2]), Point(*vals[3])
    seg1 = [Segment(B, C), Segment(C, A), Segment(A, B)]
    seg2 = [Segment(B, D), Segment(D, A), Segment(A, B)]
    seg3 = [Segment(C, D), Segment(D, B), Segment(B, C)]
    seg4 = [Segment(A, D), Segment(D, C), Segment(C, A)]
    faces = Polygon([A, B, C]), Polygon([A, B, D]), Polygon([B, C, D]), Polygon([C, A, D])
    return A, B, C, D
    
pts1 = prism((3,0,0))
pts2 = prism((0,0,0))

diffPoints = []
diffPointsProj2d = []
for p1 in pts1:
    for p2 in pts2:
        diffPt = p2 - p1
        diffPoints.append(diffPt)
        diffPtProj = TranslateI(diffPt, VectorI(PointI(0 ,0, -diffPt.z)))
        diffPointsProj2d.append(diffPtProj)
hull2d = ConvexHull(diffPointsProj2d)