class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        return area

    def perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter


class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        area = self.side_length * self.side_length
        return area

    def perimeter(self):
        perimeter = 4 * self.side_length
        return perimeter


square1 = Square(2)
print(square1.area())
