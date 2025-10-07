class Automobile:
    def __init__(self, model_name, year, manufacturer, engine_power, color, price):
        self.model_name = model_name
        self.year = year
        self.manufacturer = manufacturer
        self.engine_power = engine_power
        self.color = color
        self.price = price

    def show_data(self):
        print("********** Данные автомобиля **********")
        print(f"Название модели: {self.model_name}")
        print(f"Год выпуска: {self.year}")
        print(f"Производитель: {self.manufacturer}")
        print(f"Мощность двигателя: {self.engine_power} л.с.")
        print(f"Цвет машины: {self.color}")
        print(f"Цена: {self.price}")
        print("=====================================")


        return self.price

    def set_price(self, new_price):
        print(f"\nЦена на {self.model_name} изменена с {self.price} на {new_price}\n")
        self.price = new_price

car_bmw = Automobile(
    model_name="X7 M50i", 
    year=2021, 
    manufacturer="BMW", 
    engine_power=530, 
    color="white", 
    price=10790000
)

car_bmw.show_data()

current_price = car_bmw.get_price()
print(f"Отдельно получили цену: {current_price}")

car_bmw.set_price(11500000)

car_bmw.show_data()