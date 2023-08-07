# Punto 10 Escribir una función que calcule el factorial de un número dado.

def factorial_recursivo(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial_recursivo(numero - 1)

def main():
    numero_dado = 4
    factorial = factorial_recursivo(numero_dado)
    print(f"El factorial de {numero_dado} es: {factorial}")
main()    