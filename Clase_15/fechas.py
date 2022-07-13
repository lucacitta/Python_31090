# Calcular mi edad con la mayor precisión posible:
from datetime import datetime, timedelta
dt = datetime.now()  # dt es clase datetime.datetime

dt1 = datetime(1991, 7, 26, 10, 00)  #dt1 es clase datetime.datetime
print(dt1)
dt2 = datetime(2022,7, 26, 00,00)
edad_precisa = dt - dt1
print(timedelta.total_seconds(edad_precisa)) # Muestra la edad precisa en segundos
print(edad_precisa) # ---> sale en dias, horas, minutos y segundos. Hay alguna forma de pasarlo a años meses dias etc, con algún método o atributo de clase??

proximo_cumple = dt2 - dt
print(timedelta.total_seconds(proximo_cumple)) # ---> segundos restantes para mi próximo cumple.
# print(type(proximo_cumple))
