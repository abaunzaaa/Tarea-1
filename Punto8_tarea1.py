# Punto 8 Crear una función que invierta el orden de los elementos en una lista dada.

def invertir_lista(lista):
    lista_invertida = lista[::-1] #Cuando se especifica lista[::-1], el slicing toma todos los elementos de la lista, pero en orden inverso, comenzando desde el último elemento (debido al paso -1) y avanzando hasta el primer elemento.
    return lista_invertida

def main():
    lista_original = [1, 2, 3, 4, 5]

    lista_invertida = invertir_lista(lista_original)
    print("Lista inicial:", lista_original)
    print("Lista invertida:", lista_invertida)
main()    