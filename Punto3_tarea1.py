# Punto 3 Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.

import random

def generar_lista():
    lista_aleatoria = [random.randint(10, 20) for i in range(10)] 
    print(lista_aleatoria)

generar_lista()
