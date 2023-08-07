# Punto 6 Crear un programa que calcule la suma de los números en una lista dada.

def calcular_suma(lista):
    suma = sum(lista)
    return suma

def main():
    lista_numeros = [30, 40, 50, 60, 70]
    suma_total = calcular_suma(lista_numeros)
    print("La suma de los números en la lista es:", suma_total)
main()