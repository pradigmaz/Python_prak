import math

class ShapeAreaCalculator:
    _calculation_count = 0

    @staticmethod
    def triangle_heron(a, b, c):
        ShapeAreaCalculator._calculation_count += 1

        s = (a + b + c) / 2
        
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area

    @staticmethod
    def triangle_base_height(base, height):
        ShapeAreaCalculator._calculation_count += 1
        
        area = 0.5 * base * height
        return area

    @staticmethod
    def square(side):
        ShapeAreaCalculator._calculation_count += 1
        
        area = side * side
        return area

    @staticmethod
    def rectangle(a, b):
        ShapeAreaCalculator._calculation_count += 1
        
        area = a * b
        return area

    @staticmethod
    def get_calculation_count():
        return ShapeAreaCalculator._calculation_count

area1 = ShapeAreaCalculator.triangle_heron(3, 4, 5)
print(f"Площадь треугольника по формуле Герона (3,4,5): {area1}")

area2 = ShapeAreaCalculator.triangle_base_height(6, 7)
print(f"Площадь треугольника через основание и высоту (6,7): {area2}")

area3 = ShapeAreaCalculator.square(7)
print(f"Площадь квадрата (7): {area3}")

area4 = ShapeAreaCalculator.rectangle(2, 6)
print(f"Площадь прямоугольника (2,6): {area4}")

total_calculations = ShapeAreaCalculator.get_calculation_count()
print(f"Количество подсчетов площади: {total_calculations}")