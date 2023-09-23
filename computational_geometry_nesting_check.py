class Polygon:
    def __init__(self):
        self.name = "polygon"
        self.points = []
        self.direction = ">"

def double_s_abc(a, b, c):
    return (a[0] * b[1] + b[0] * c[1] + a[1] * c[0]) - (b[1] * c[0] + a[1] * b[0] + a[0] * c[1])

def check_ray_edge_intersection(point, edge_point1, edge_point2) -> (-1|0|1): # O(1)
    p1x = edge_point1[0] - point[0]
    p1y = edge_point1[1] - point[1]
    p2x = edge_point2[0] - point[0]
    p2y = edge_point2[1] - point[1]
    if (p1y * p2y > 0):
        return 1
    m = p1x * p2y - p1y * p2x
    m = 1 if m > 0 else 0 if m == 0 else -1
    if (m == 0):
        if (p1x * p2x <= 0):
            return 0
        return 1
    if (p1y < 0):
        return -m
    if (p2y < 0):
        return m
    return 1

def point_categorization(point, polygon): # O(N)
    result = 1
    i = 0
    j = len(polygon) - 1
    while i <= len(polygon) - 1:
        current = check_ray_edge_intersection(point, polygon[j], polygon[i])
        if current == 0:
            return 0
        result *= current
        j = i
        i += 1
    return result

def check_edge_polygon_intersection(edge_point1, edge_point2, polygon: Polygon) -> (True|False): # O(N)
    vertices = polygon.points
    i = 0
    j = len(vertices) - 1
    while i <= len(vertices) - 1:
        s1 = double_s_abc(edge_point1, edge_point2, vertices[j])
        s2 = double_s_abc(edge_point1, edge_point2, vertices[i])
        s3 = double_s_abc(vertices[j], vertices[i], edge_point1)
        s4 = double_s_abc(vertices[j], vertices[i], edge_point2)
        if (s1 * s2 < 0 and s3 * s4 < 0):
            return True
        elif ((s3 * s4 < 0 or ((s3 == 0 or s4 == 0) and s3 != s4)) and s1 == 0):
            k = j - 1
            k = k if k >= 0 else len(vertices) - 1
            s5 = double_s_abc(vertices[k], vertices[j], vertices[i])
            s6 = double_s_abc(vertices[k], vertices[j], edge_point1)
            s7 = double_s_abc(vertices[k], vertices[j], edge_point2)
            if (polygon.direction == ">" and s5 > 0 or polygon.direction == "<" and s5 < 0 or s5 == 0):
                if (polygon.direction == ">" and (s3 > 0 and s6 > 0 or s4 > 0 and s7 > 0) or 
                        polygon.direction == "<" and (s3 < 0 and s6 < 0 or s4 < 0 and s7 < 0)):
                    return True
            else:
                if ((polygon.direction == ">" and not (s3 <= 0 and s6 <= 0 and s4 <= 0 and s7 <= 0)) or 
                        (polygon.direction == "<" and not (s3 >= 0 and s6 >= 0 and s4 >= 0 and s7 >= 0))):
                    return True
        elif ((s3 * s4 < 0 or ((s3 == 0 or s4 == 0) and s3 != s4)) and s2 == 0):
            k = i + 1
            k = k if k <= len(vertices) - 1 else 0
            s5 = double_s_abc(vertices[j], vertices[i], vertices[k])
            s6 = double_s_abc(vertices[i], vertices[k], edge_point1)
            s7 = double_s_abc(vertices[i], vertices[k], edge_point2)
            if (polygon.direction == ">" and s5 > 0 or polygon.direction == "<" and s5 < 0 or s5 == 0):
                if (polygon.direction == ">" and (s3 > 0 and s6 > 0 or s4 > 0 and s7 > 0) or 
                        polygon.direction == "<" and (s3 < 0 and s6 < 0 or s4 < 0 and s7 < 0)):
                    return True
            else:
                if ((polygon.direction == ">" and not (s3 <= 0 and s6 <= 0 and s4 <= 0 and s7 <= 0)) or 
                        (polygon.direction == "<" and not (s3 >= 0 and s6 >= 0 and s4 >= 0 and s7 >= 0))):
                    return True
        elif (s1 * s2 < 0 and s3 == 0):
            if (polygon.direction == ">" and s4 > 0 or polygon.direction == "<" and s4 < 0):
                return True
        elif (s1 * s2 < 0 and s4 == 0):
            if (polygon.direction == ">" and s3 > 0 or polygon.direction == "<" and s3 < 0):
                return True
        j = i
        i += 1
    return False

def check_polygon_in_polygon(A: Polygon, B: Polygon) -> (True|False): # O(N^2)
    verticesA = A.points
    verticesB = B.points
    prev_point = verticesA[-1]
    prev_point_category = point_categorization(prev_point, verticesB)
    if (prev_point_category == 1):
        return False
    for v in verticesA:
        point_category = point_categorization(v, verticesB)
        if (point_category == 1 or check_edge_polygon_intersection(prev_point, v, B)):
            return False
    return True

def nesting_check(A: Polygon, B: Polygon) -> str: # O(N^2)
    a_in_b = check_polygon_in_polygon(A, B)
    b_in_a = check_polygon_in_polygon(B, A)
    if (a_in_b and b_in_a):
        return "equal"
    if (a_in_b):
        return A.name
    if (b_in_a):
        return B.name
    return "false"