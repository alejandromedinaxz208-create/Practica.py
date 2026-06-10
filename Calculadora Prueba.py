# Calculadora

print("== CALCULADORA ==")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Potencia")

opcion = int(input("Elige una opción (1-5): "))

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

if opcion == 1:
    resultado = num1 + num2
    print("Resultado:", resultado)

elif opcion == 2:
    resultado = num1 - num2
    print("Resultado:", resultado)

elif opcion == 3:
    resultado = num1 * num2
    print("Resultado:", resultado)

elif opcion == 4:
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado:", resultado)
    else:
        print("No se puede dividir entre 0")

elif opcion == 5:
    resultado = num1 ** num2
    print("Resultado:", resultado)

else:
    print("Opción no válida")