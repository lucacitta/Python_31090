# class My_list():
#     def __init__(self, data):
#         self.data = data

#     def __str__(self):
#         return str(self.data)

#     def __len__(self):
#         return len(self.data)

#     def __getitem__(self, position):
#         return self.data[position]

#     def __setitem__(self, position, value):
#         self.data[position] = value


# var = [1,2,3,4,5]
# python_list = list(var)
# my_list = My_list(var)
# print('----------------------------------------------------\n\n')

# print('python_list', python_list[1])
# python_list[1] = 99
# print('python_list', python_list[1])

# print('\n\n----------------------------------------------------\n\n')
# print('my_list', my_list[0])
# my_list[0] = 99
# print('my_list', my_list[0])

# print('\n\n----------------------------------------------------')






# class Ingredient():
#     def __init__(self, name, expiration, is_natural):
#         self.name = name
#         self.expiration = expiration
#         self.is_natural = is_natural

#     def __str__(self):
#         return self.name


# class Menu():
#     def __init__(self, name, price, ingredients, secret_ingredient):
#         self.name = name
#         self.price = price
#         self.ingredients = ingredients
#         self.__secret_ingredient = secret_ingredient

#     def __str__(self):
#         return self.name

#     def description(self):
#         self.__cualquier_cosa()
#         message = f'El menu se llama {self.name}, su precio es $ {self.price} y sus ingredientes son: '
#         for ingredient in self.ingredients:
#             message += f'{ingredient}, '
#         return message[:-2]

#     def has_ingredient(self, ingredient):
#         if ingredient in self.ingredients or ingredient == self.__secret_ingredient:
#             return True
#         return False

#     def __cualquier_cosa(self):
#         print('cualquier cosa')


# ingredient_1 = Ingredient('Pimiento', '15/07/2022', 'si')
# ingredient_2 = Ingredient('Cebolla', '8/08/2022', 'si')
# ingredient_3 = Ingredient('Pollo', '8/07/2022', 'si')
# ingredient_4 = Ingredient('Saborizante alicante', '20/19/2024', 'no')
# ingredient_5 = Ingredient('Lechuga', '9/07/2022', 'si')
# ingredient_6 = Ingredient('Harina', '8/07/2023', 'no')


# comida_1 = Menu('Wok de verduras', 900, [ingredient_1, ingredient_2, ingredient_3], ingredient_6)

# # print(comida_1.description())
# # print(comida_1.has_ingredient(ingredient_6))

# comida_1.description()


# class Persona():
#     especie = 'humana'
#     pies = 2

#     def __init__(self,nombre,edad,email):
#         self.nombre = nombre
#         self.edad = edad
#         self.email = email

#     def cantar(self):
#         print("La persona canta")

#     def hablar(self, idioma):
#         print(f"Habla {idioma}")

# persona_1 = Persona("Harry ", 23, "harryes@gmail.com")
# persona_2 = Persona("Luca ", 23, "lucacitta@gmail.com")
# persona_1.hablar('Italiano')
