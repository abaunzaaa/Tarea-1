# Punto 5 Crear una función que convierta grados Fahrenheit a grados Celsius.

def fahrenheit_a_celsius(grados_fahrenheit):
    grados_celsius = (grados_fahrenheit - 32) * 5/9
    return grados_celsius

def main():
    grados_fahrenheit = float(input("Ingree la temperatura en grados Fahrenheit: "))
    grados_celsius = fahrenheit_a_celsius(grados_fahrenheit)
    print(f"{grados_fahrenheit} grados Fahrenheit equivale a {grados_celsius:.2f} grados Celsius.")
main()