import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def dist(self, Point):
        distance = (((self.x - Point.x) ** 2) + ((self.y - Point.y) ** 2) )** 0.5
        return distance

p1 = Point(1.5, 1)
p2 = Point(1.5, 2)

print(p1.dist(p2))