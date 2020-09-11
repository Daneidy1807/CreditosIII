def tabla(numero):
    print(f"Tabla de multiplicar del número: {numero}")

    for contador in range(11):
        operacion = numero*contador
        print(f"{numero} x {contador} = {operacion}")
    print("\n")
tabla(3)
tabla(7)
tabla(12)
#-----------------------------------------------
for numero_tabla in range(1, 11):
    tabla(numero_tabla)