#sacar los nuemros impares
n1= int(input("ingresa el primer numero "))
n2= int(input("ingresa el segundo numero "))


for numeros in range(n1,n2):  
    if numeros%2==0:
        print("")

    else:
         print(f"este numero es impar {numeros}")