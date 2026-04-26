from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (3.14 * self.radius ** 2)
    
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return (self.side_length ** 2)
    
def print_area(shape_obj):
    if not isinstance(shape_obj, Shape):
        print("Invalid, Not a Shape Obj")
        return
    print(shape_obj.area())

print_area(Circle(5))
print_area(Square(5))

    