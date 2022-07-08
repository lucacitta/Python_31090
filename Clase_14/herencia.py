# print('----------------------------------------------------\n\n')

# class Vehicle():
#     def __init__(self, color, brand, model, year):
#         self.color = color
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def print_data(self):
#         print(f"Color: {self.color}")
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")
#         print(f"Year: {self.year}")

#     def run(self):
#         print("Vehicle is running")

# class Car(Vehicle):

#     def __init__(self, color, brand, model, year, doors):
#         self.color = color
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.doors = doors

#     def run(self):
#         print("Car is running")

#     def run_backwards(self):
#         print("Car is running backwards")

# class Motorcycle(Vehicle):
#     def __init__(self, color, brand, model, year, helmet):
#         super().__init__(color, brand, model, year)
#         self.helmet = helmet

#     def run(self):
#         print("Motorcycle is running")

#     def do_a_wheelie(self):
#         print("Motorcycle is doing a wheelie")

#     def print_data(self):
#         super().print_data()
#         print('helmet: ', self.helmet)


# vehicle_1 = Vehicle('red', 'VW', 'Gol country', 2012)
# car_1 = Car('Black', 'Toyota', 'corolla', 2020, 4)
# moto_1 = Motorcycle('White', 'Yamaha', 'Corver', 1950, 'Aguila')

# vehicle_1.print_data()
# print(car_1.doors)
# moto_1.print_data()


class Clase_1():
    def printear(self):
        print('Estoy en la clase 1')
    pass

class Clase_2():
    def printear(self):
        print('Estoy en la clase 2')
    pass

class Clase_3(Clase_1, Clase_2):
    def printear(self):
        print('Estoy en la clase 3')
    pass

print(dir(Clase_3))

