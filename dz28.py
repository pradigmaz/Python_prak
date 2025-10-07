from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def print_info(self):
        pass


class Square(Shape):
    def __init__(self, side, color):
        super().__init__(color)
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side * self.side

    def draw(self):
        for _ in range(self.side):
            print("*" * self.side)

    def print_info(self):
        print("===Квадрат===")
        print(f"Сторона: {self.side}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.area()}")
        print(f"Периметр: {self.perimeter()}")
        self.draw()
        print()


class Rectangle(Shape):
    def __init__(self, length, width, color):
        super().__init__(color)
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def draw(self):
        for _ in range(self.width):
            print("*" * self.length)

    def print_info(self):
        print("===Прямоугольник===")
        print(f"Длина: {self.length}")
        print(f"Ширина: {self.width}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.area()}")
        print(f"Периметр: {self.perimeter()}")
        self.draw()
        print()


class Triangle(Shape):
    def __init__(self, side1, side2, side3, color):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        s = self.perimeter() / 2
        return round(
            math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3)), 2
        )

    def draw(self):
        for i in range(1, self.side1 + 1):
            print(" " * (self.side1 - i) + "*" * i)

    def print_info(self):
        print("===Треугольник===")
        print(f"Сторона 1: {self.side1}")
        print(f"Сторона 2: {self.side2}")
        print(f"Сторона 3: {self.side3}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.area()}")
        print(f"Периметр: {self.perimeter()}")
        self.draw()
        print()


# квадрат
sq = Square(3, "red")
sq.print_info()

# прямоугольник
rect = Rectangle(3, 7, "green")
rect.print_info()

# треугольник
tri = Triangle(11, 6, 6, "yellow")
tri.print_info()
