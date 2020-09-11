#mostrar las tablas del 1-10
for tablas in range(1,11):
    print(f" tabla de multiplicar del : {tablas}")
    for numero in range(1,11):
        valor=tablas*numero
        print(f"{tablas}  *  {numero}  es : {valor}")
