class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_car_info(self):
        return f"{self.year} {self.make} {self.model}"

    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year


car = Car("Toyota", "Supra", 1996)
print(car.get_car_info())   

car.set_year(2021)
print(car.get_car_info()) 