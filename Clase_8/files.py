# file = open('primer_archivo.txt', 'w')
# file.write('Buenas, esto es mi primer archivo!!! :D ')
# file.close()

# file = open('test/diccionario.txt', 'w')    # W de write 
# file.write(diccionario['nombre'] + ',' + diccionario['apellido'] + ','+ str(diccionario['comision']))
# file.close()


# file = open('alumnos.txt', 'w')
# lista_alumnos = []
# hay_mas = 'si'
# while hay_mas == 'si':
#     alumno = input('ingrese el nombre del alumno: ')
#     lista_alumnos.append(alumno)
#     hay_mas = input('hay mas alumnos?: ')

# for alumno in lista_alumnos:
#     file.write(alumno +',')

# file.close()

# file = open('archivo_lectura.txt', 'r') #r de read
# file.seek(0)
# contenido = file.read()
# file.close()

# print(contenido)



# import json

# data = {}
# data['nombres'] = []
# data['nombres'].append(
#     {
#         '1_er_alumno':'Marco'
#     }
# )
# data['nombres'].append(
#     {
#         '2do_alumno':'Sebastian'
#     }
# )
# with open('mis_alumnos.json', 'w') as file:
#     json.dump(data, file)

# import json

# with open('mis_alumnos.json') as file:
#     datos = json.load(file)

# print(datos)

# import pandas as pd

# data = pd.read_csv('dataset_reporte_covid_sitio_gobierno.csv')

# print(data)

file = open('mascota.txt', 'w')

data = []
for vuelta in range(0,3):
    nombre = input('Ingrese el nombre de la mascota: ')
    edad = input('Ingrese la edad de la mascota: ')
    file.write('Mi mascota se llama' + nombre+','+edad+'\n')
file.close()
