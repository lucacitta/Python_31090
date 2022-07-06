hay_gente = 'si'
cantidad = 1


while hay_gente == 'si' and cantidad > 0:

    edad = int(input('Ingrese su edad: '))
    if edad >= 18:
        print('Podes pasar, la entrada son $500')
        cantidad -= 1
        if cantidad <= 0:
            print('Se lleno el boliche')
            continue
        else:
            pass
    else:
        print('No podes pasar, sos menor')

    hay_gente = input('Hay mas gente en la fila? (si/no): ' )

print('Termino la ejecucion')