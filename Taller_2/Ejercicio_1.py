Numeros=[18,24,3,67,24,2,10,50]
for numero in Numeros:
    print(f"Elemento: {numero}")

Numeros.sort()
print(f"Elementos ordenado: {Numeros}")

longitud=len(Numeros)
print(f"La longitud es: {longitud}")

Buscar=int(input("Bucar numero: "))
print(Buscar in Numeros)

   
