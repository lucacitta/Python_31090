class Auto():
    ruedas = 4
    tiene_motor = True

    def __init__(self, puertas, marca, color=None):
        self.color = color
        self.puertas = puertas
        self.marca = marca

    def cargar_datos(self, caballos):
        self.caballos = caballos

    def andar(self):
        print(f'el auto {self.color} esta andando')


mi_primer_auto = Auto(5, 'VW', 'rojo')
# mi_segundo_auto = Auto('gris', 3, 'Fiat')
# mi_tercer_auto = Auto('amarillo', 5, 'Fiat')

mi_primer_auto.cargar_datos(150)
print(mi_primer_auto.color)
mi_primer_auto.color = 'verde'
print(mi_primer_auto.color)
print(mi_primer_auto.caballos)
