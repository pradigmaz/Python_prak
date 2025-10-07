class Student:
    def __init__(self, name):
        self.name = name
        self.laptop = None  # будет содержать экземпляр Laptop

    class Laptop:
        def __init__(self, model, processor, memory):
            self.model = model
            self.processor = processor
            self.memory = memory

        def __str__(self):
            return f"{self.model}, {self.processor}, {self.memory}"

    def set_laptop(self, model, processor, memory):
        self.laptop = Student.Laptop(model, processor, memory)

    def print_info(self):
        if self.laptop:
            print(f"{self.name} => {self.laptop}")
        else:
            print(f"{self.name} => нет ноутбука")

s1 = Student("Roman")
s1.set_laptop("HP", "i7", "16")
s1.print_info()

s2 = Student("Vladimir")
s2.set_laptop("HP", "i7", "16")
s2.print_info()
