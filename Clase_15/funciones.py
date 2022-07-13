# def suma(a,b):
#     return a+b

# def multiplcacion(a,b):
#     return a*b

# class Persona():
#     pass

# nombre = 'luca'

class Persona():
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

    def hablar(self):
        print(f'{self.nombre} {self.apellido} está Hablando...')

    def __str__(self) -> str:
        return self.nombre, self.apellido
