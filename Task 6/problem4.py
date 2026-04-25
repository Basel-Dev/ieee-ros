class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

rect = Rectangle(10, 5)
rectArea = rect.get_area()

print(f"Area of rectangle is {rectArea} cm^2")