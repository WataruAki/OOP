import math
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
class Rectangle:
    def __init__(self, corner,  width, height):
        self.corner = corner #Điểm góc dưới bên trái
        self.width = width
        self.height = height
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def distance(p1, p2):
        return math.sqrt(pow(p1.x - p2.x, 2) + pow(p1.y - p2.y, 2))
    
    def point_in_circle(circle, point):
        return Circle.distance(circle.center, point) <= circle.radius
    
    def rect_in_circle(circle, rect):
        #Lấy 4 điểm của hình chữ nhật
        corners = [rect.corner,
                   Point(rect.corner.x + rect.width, rect.corner.y),
                   Point(rect.corner.x, rect.corner.y + rect.height),
                   Point(rect.corner.x + rect.width, rect.corner.y + rect.height)]
        return all(Circle.point_in_circle(circle, p) for p in corners)
    
    def rect_circle_overlap(circle, rect):
        corners = [
            rect.corner,
            Point(rect.corner.x + rect.width, rect.corner.y),
            Point(rect.corner.x, rect.corner.y + rect.height),
            Point(rect.corner.x + rect.width, rect.corner.y + rect.height)
        ]
        # Nếu có bất kì điểm nào của hình chữ nhật nằm trong hình tròn, thì chúng chồng lấp nhau
        return any(Circle.point_in_circle(circle, p) for p in corners)
    
center = Point(150, 100)
circle = Circle(center, 75)

p = Point(160, 110)
print("Point in circle:", Circle.point_in_circle(circle, p))

rect = Rectangle(Point(120, 80), 30, 20)
print("Rectangle in circle:", Circle.rect_in_circle(circle, rect))
print("Rectangle overlap:", Circle.rect_circle_overlap(circle, rect))




