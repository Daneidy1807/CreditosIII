valores=[4,6,7,8,9 ]
longitud=len(valores)
while longitud<120:
    nuevo_valor=int(input("Agregar nuevo valor: "))

    if longitud<120:
        valores.append(nuevo_valor) 
    break
print("lista de datos: ")
for valor in valores:
    print(f"{valores.index(valor)+1}): {valor}")
    
      