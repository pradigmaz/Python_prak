class Rectangle:
    def __init__(self, width=0, height=0, bg=None, border_width=None, border_style=None, border_color=None):
        self.width = width
        self.height = height
        self.bg = bg
        self.border_width = border_width
        self.border_style = border_style
        self.border_color = border_color

    def get_width(self): return self.width
    def get_height(self): return self.height
    def get_bg(self): return self.bg
    def get_border_width(self): return self.border_width
    def get_border_style(self): return self.border_style
    def get_border_color(self): return self.border_color

    def set_width(self, v): self.width = int(v)
    def set_height(self, v): self.height = int(v)
    def set_bg(self, v): self.bg = v
    def set_border_width(self, v): self.border_width = v
    def set_border_style(self, v): self.border_style = v
    def set_border_color(self, v): self.border_color = v

    def print_info(self):
        print("Прямоугольник:")
        print(f"Ширина: {self.width}")
        print(f"Высота: {self.height}")
        if self.bg is not None:
            print(f"Фон: {self.bg}")
        if self.border_width is not None:
            print(f"Ширина рамки: {self.border_width}")
        if self.border_style is not None:
            print(f"Тип рамки: {self.border_style}")
        if self.border_color is not None:
            print(f"Цвет рамки: {self.border_color}")
        print()

# фон
r1 = Rectangle()
r1.set_width(400)
r1.set_height(200)
r1.set_bg("yellow")
r1.print_info()

# рамка
r2 = Rectangle()
r2.set_width(600)
r2.set_height(300)
r2.set_border_width("1px")
r2.set_border_style("solid")
r2.set_border_color("blue")
r2.print_info()
