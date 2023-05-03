# Función para sumar dos números
def sumar(num1, num2):
    return num1 + num2

# Función para restar dos números
def restar(num1, num2):
    return num1 - num2

# Función para multiplicar dos números
def multiplicar(num1, num2):
    return num1 * num2

# Función para dividir dos números
def dividir(num1, num2):
    if num2 == 0:
        return "Error: no se puede dividir entre cero"
    else:
        return num1 / num2

# Función para mostrar el menú de opciones
def mostrar_menu():
    print("Por favor, selecciona una opción:")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Salir")

# Loop principal del programa
while True:
    mostrar_menu()

    # Pedimos al usuario que seleccione una opción
    opcion = input("Ingresa tu opción (1-5): ")

    # Si el usuario selecciona la opción 5, salimos del loop
    if opcion == "5":
        break

    # Pedimos al usuario que ingrese los dos números a operar
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    # Realizamos la operación correspondiente según la opción seleccionada
    if opcion == "1":
        resultado = sumar(num1, num2)
    elif opcion == "2":
        resultado = restar(num1, num2)
    elif opcion == "3":
        resultado = multiplicar(num1, num2)
    elif opcion == "4":
        resultado = dividir(num1, num2)
    else:
        print("Opción inválida")
        continue

    # Mostramos el resultado al usuario
    print("El resultado es:", resultado)
