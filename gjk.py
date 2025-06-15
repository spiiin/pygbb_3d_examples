import math

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
pts2 = prism((2,0,0))
O = Point(0, 0, 0, caption = "O")

diffPoints = []
for p1 in pts1:
    for p2 in pts2:
        diffPt = p1 - p2
        diffPoints.append(diffPt)
        
def find_furthest_point(obj, direction):
    proj = [Dot(direction, VectorI(O, p)) for p in obj]
    max_proj = max(proj)
    max_index = proj.index(max_proj)
    return obj[max_index]

def get_support(obj1, obj2, direction):
    a = find_furthest_point(obj1, direction)
    #a.color = "red"
    b = find_furthest_point(obj2, Invisible(-direction))
    #b.color = "red"
    return Invisible(a - b)
    
def next_step(simplex, direction):
    def line(simplex, direction):
        a, b = simplex[0], simplex[1]
        ab = VectorI(a, b)
        ao = VectorI(a, O)
        if Dot(ab, ao) > 0:
            return False, CrossI(CrossI(ab, ao), ab)
        else:
            simplex[:] = [a]
            return False, ao
        return False, None
        
    def triangle(simplex, direction):
        a, b, c = simplex[0], simplex[1], simplex[2]
        ac = VectorI(a, c)
        ao = VectorI(a, O)
        ab = VectorI(a, b)
        abc = CrossI(ab, ac)
        if Dot(CrossI(abc, ac), ao) > 0:
            if Dot(ac, ao) > 0:
                simplex[:] = [a, c]
                return False, CrossI(CrossI(ac, ao), ac)
            else:
                return line([a,b], direction)
        else:
            if Dot(CrossI(ab, abc), ao) > 0:
                if Dot(ab, ao) > 0:
                    simplex[:] = [a, b]
                    return False, CrossI(CrossI(ab, ao), ab)
                else:
                    simples[:] = a
                    return ao
            else:
                if Dot(abc, ao):
                    return None, abc
                else:
                    simplex[:] = [a, c, b]
                    return None, Invisible(-abc)
        return False, None
        
    def prism(simplex, direction):
        a,b,c,d = simplex[0], simplex[1], simplex[2], simplex[3]
        abc = CrossI(VectorI(a, b), VectorI(a, c))
        acd = CrossI(VectorI(a, c), VectorI(a, d))
        adb = CrossI(VectorI(a, d), VectorI(a, b))
        ao = VectorI(a, O)
        if Dot(abc, ao) > 0:
            return triangle([a, b, c], direction)
        if Dot(acd, ao) > 0:
            return triangle([a, c, d], direction)
        if Dot(abc, ao) > 0:
            return triangle([a, b, d], direction)
        return True, None
    
    #print(simplex)
    if len(simplex) == 2:
        return line(simplex, direction)
    if len(simplex) == 3:
        return triangle(simplex, direction)
    if len(simplex) == 4:
        return prism(simplex, direction)
    return False, direction

def gjk(pts1, pts2):
    current_points = []    
    support = get_support(pts1, pts2, VectorI(O, PointI(0, 0, 1))) #any direction as first step
    current_points.append(support)
    direction = VectorI(support, O)
    while True:
        support = get_support(pts1, pts2, direction)
        current_points = [support, *current_points]
        if Dot(VectorI(O, support), direction) <= 0:
            return False #no collision
        is_finish, direction = next_step(current_points, direction)
        if is_finish:
            return True

@O.when_clicked
def when_point_clicked():
    intersect = gjk(pts1, pts2)
    print(intersect)

when_point_clicked()

