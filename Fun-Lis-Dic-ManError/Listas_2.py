peliculas=["Batman", "Spiderman", "El señor de los anillos"]
nueva_pelicula = ""

while nueva_pelicula != "parar":
      nueva_pelicula=input("Agregar nombre de la Pelicula: ")

      if nueva_pelicula!="parar":
         peliculas.append(nueva_pelicula)

print("lista de peliculas: ")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}.{pelicula}")

