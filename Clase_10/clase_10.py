# def agregar_a_lista(lista_funcion):
#     lista_funcion.append(0)
#     print("lista_funcion", lista_funcion)


# lista = [1,2,3,4,5]
# agregar_a_lista(lista[:])
# print('lista',lista)


# lista_1 = [1,2,3]
# lista_2 = lista_1
# lista_1.append(4)
# print(lista_2)

# def duplicar(numero_en_la_funcion):
#     return numero_en_la_funcion * 2

# numero = 5
# numero = duplicar(numero)
# print(numero)


# def suma(*args):
#     resultado = 0
#     for dato in args:
#         resultado += dato
#     return resultado

# print(suma(20, 10, 7, 99, 10, 7, 20))


# def calculadora(*args, **kwargs):
#     resultado = 0
#     if 'cuenta' in kwargs:
#         if kwargs['cuenta'] == 'resta':
#             for dato in args:
#                 resultado -= dato
#         elif kwargs['cuenta'] == 'multiplicar':
#             resultado = 1
#             for dato in args:
#                 resultado *= dato
#     else:
#         for dato in args:
#             resultado += dato
#     return resultado


# print(calculadora(5, 10,20, 30, 50, cuenta='resta'))



















# from time import sleep
# def cuenta_regresiva(numero):
#     numero -= 1
#     if numero > 0:
#         print(numero)
#         sleep(1)
#         cuenta_regresiva(numero)
#     else:
#         print("Boooooooom!")
#         print("Fin de la función", numero)

# cuenta_regresiva(5)












# def factorial(numero):
#     print("Valor inicial ->", numero)
#     if numero > 1:
#         numero = numero * factorial(numero -1)
#     print("valor final ->", numero)
#     return numero

# factorial(3)

# DATO: La profundidad maxima de recursion es 995


# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(4))