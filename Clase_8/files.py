file = open('test/primer_archivo.txt', 'w')
# file.write('Buenas, esto es mi primer archivo!!! :D \n')
# file.write('Buenas, esto es mi primer archivo!!! :D \n')
# file.write('Buenas, esto es mi primer archivo!!! :D ')

# file.close()






















# diccionario = {
#     'nombre':'Esteban',
#     'apellido':'Airaldo',
#     'comision':34650
# }
# file = open('test/diccionario.txt', 'w')    # W de write 
# file.write(diccionario['nombre'] + ',' + diccionario['apellido'] + ','+ str(diccionario['comision']))
# file.close()





# file = open('archivo_lectura.txt', 'r')
# content = file.read()
# print(content)
# file.close()


# file = open('archivo_lectura.txt', 'r')
# content = file.readline()
# print(content)
# file.close()

# file = open('archivo_lectura.txt', 'r')
# content = file.readlines()
# for linea in content:
#     print(linea.replace('\n',''))
# file.close()


# print(r'hola\nbuenas\nchau')


# file = open('archivo_lectura.txt', 'r')
# file.seek(20)
# content = file.read()
# print(content)
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
#         'alumno':'Marco'
#     }
# )
# data['nombres'].append(
#     {
#         'alumno':'Sebastian'
#     }
# )

# with open('mis_alumnos.json', 'w') as file:
#     json.dump(data, file)








# import json

# with open('mis_alumnos.json') as file:
#     datos = json.load(file)
#print(datos['nombres'])

# for alumno in datos['nombres']:
#     print(alumno['alumno'])
#print(datos['nombres'][0]['1_er_alumno'])













import pandas as pd


data = pd.read_csv('divorcios-2019.csv')

print(data.columns)



















# file = open('mascota.txt', 'w')

# data = []
# for vuelta in range(0,3):
#     nombre = input('Ingrese el nombre de la mascota: ')
#     edad = input('Ingrese la edad de la mascota: ')
#     file.write('Mi mascota se llama' + nombre+','+edad+'\n')
# file.close()
