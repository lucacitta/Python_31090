# variable = "Hola"
# variable2 = 6
# if variable:
#     print(variable)

# #print(hola)
# 5/ int(input('ingrese un numero'))

#si b = 0
#si no llegan datos o si llegan mas
#si no sin int o float

# def dividir(a = None, b = None, *args, **kwargs):
#     if a == None or b == None:
#         return None
#     if not type(a) in [int, float] or not type(b) in [int, float]:
#         return None
#     if b == 0:
#         return None
#     return a//b


# validar = True
# while validar:
#     print('entre')
#     break
#     validar = False
# else:
#     print('sali')




# a = 10 
# b = 5
# print(dividir(a, b))

# validar = True

# while validar:
#     try: # Ejecuta esto, si hay excepciones, anda al except, sino al else
#         edad = int(input('ingresa tu edad: ')) # 5
#     except:
#         print('Te dije que ingreses tu edad!!!')
#     else:
#         if edad >= 18:
#             print('entras al boliche!!')
#         else:
#             print('no entras al boliche!!')
#         validar = False
#     finally:
#         print('esto se ejecuta si o si')



try:
    numero = int(input("Introduce un número: "))
    print(5/numero)
except TypeError:
    print('tipo de dato incorrecto')
except ValueError:
    print('Che, tenes que ingresar un numero!!!')
except ZeroDivisionError:
    print('dale papa, no podes dividir por 0, no era tan dificil...')
except Exception as e:  # guardamos la excepción como una variable e
    print("Ha ocurrido un error =>", type(e).__name__)

