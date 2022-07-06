# def suma(num1, num2, num3):
#     sumatoria = num1 + num2 + num3
#     if sumatoria >= 6:
#         return 'la suma da mas de 6 o 6'
#     return 'la suma da menos de 6'

# sumatoria = suma(1, 2, 3)

# print(sumatoria)


# def separar(list):
#     ordenada = lista.copy()
#     ordenada.sort()
#     pares, impares = [], []

#     for i in ordenada:
#         if i % 2 == 0 and i not in pares:
#             pares.append(i)
#         elif i % 2 != 0 and i not in impares:
#             impares.append(i)
#     return pares, impares


# lista = [1,5,8,6,3,7,10, 2, 2, 2, 2,2]   
# pares, impares = separar(lista)

# print(lista) 
# print(f"pares = {pares} ; impares = {impares}")


# import math
# print(math.pi)
# mi_pi = round(math.pi, 3)
# print(mi_pi)

x = input("ingrese la cantidad de numeros a ingresar en \n la lista , debe ser valor numerico : ")
while not x.isnumeric():
    if x[0] == '-' and x[1:].isnumeric():
        break
    print("Error el caracter ingresado es incorrecto, intente nuevamente.")
    x = input("ingrese la cantidad de numeros a ingresar en \n la lista , debe ser valor numerico : ")
x=int(x)
