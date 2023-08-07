# Punto 14 Escribir una función que calcule la media aritmética de una lista de números.

def calcular_media_aritmetica(lista):
    suma_total = sum(lista)
    cantidad_elementos = len(lista)
    media_aritmetica = suma_total / cantidad_elementos
    return media_aritmetica

def main():
    lista_numeros = [10, 20, 30, 40, 50]
    media = calcular_media_aritmetica(lista_numeros)
    print(f"La media aritmética de la lista es: {media}")
main()      