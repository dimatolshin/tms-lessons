class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_zero(self):
        cardinat = 0
        cardinat = (self.x ** 2) + (self.y ** 2)
        cardinat = cardinat ** 0.5
        return cardinat


p1 = Point(3, 4)
p2 = Point(3, 10)
p3 = Point(10, 10)
print('Distance between p1 and zero point:', p1.distance_to_zero())
print('Distance between p2 and zero point:', p2.distance_to_zero())
print('Distance between p3 and zero point:', p3.distance_to_zero())
