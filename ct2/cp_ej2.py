#añadir valores a un alista mientras len sea menor "x"
lista=[]
#llenando lista
for l in range(1,1000):
    if lista.__len__()<119:
        lista.append(l);


# mostrar lista
print(lista)

print(lista.__len__())