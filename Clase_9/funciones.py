#print(len('hola'))


# def len_luca(variable):
#     count = 0
#     for elemento in variable:
#         count += 1
#     print(count)

#retorno = len_luca('hola')

#print(retorno)

# def saludar_con_nombre(nombre):
#     print('hola mi querido', nombre)


# saludar_con_nombre('luca')

# def suma(a=int, b=int) -> float:

#     #variable local
#     c = a + b

    
#     nombre = 'Carlos'
#     print(nombre)
#     return a + b
#     print('hola')


# #variable global
# nombre = 'luca'
# resultado = suma(5.1, 10)
# print(resultado)


# def multiplicar(a,b):
#     c = a*b
#     return a, b, c

# num1, num2, num3 = multiplicar(5,10)

# print(num1, num2, num3)


# '''
# Esta funcion recibe obligatoriamente un parametro b y 
#     opcionalmente un parametro a, de no pasarlo, le asigna 10
# '''
# def dividir(b, a=10):
#     return a/b

# dividir(5, a=2)


# def par_o_impar(numero):

#     numero = str(numero)

#     while not numero.isnumeric():
#         numero = input('Ingrese un numero: ')

#     numero = int(numero)

#     if numero % 2 == 0:
#         return 'Par'
#     else:
#         return 'Impar'

# print(par_o_impar('2.3.'))



# def par_o_impar(numero):
#     numero=str(numero)
#     while not numero.isnumeric():
#         numero = input("Ingrese un num: ")
#     numero = int(numero)
#     if numero % 2 == 0:
#         return "Par"
#     else:
#         return "Impar"
# print(par_o_impar('hola'))
