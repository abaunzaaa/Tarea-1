# Punto 7 Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.

def encontrar_maximo(lista):
    maximo = max(lista)
    return maximo

def encontrar_minimo(lista):
    minimo = min(lista)
    return minimo

def main():
    lista_numeros = [10, 45, 3, 78, 25, 1, 100]
    numero_mas_grande = encontrar_maximo(lista_numeros)
    numero_mas_pequeno = encontrar_minimo(lista_numeros)

    print("El número más grande en la lista es:", numero_mas_grande)
    print("El número más pequeño en la lista es:", numero_mas_pequeno)
main()    