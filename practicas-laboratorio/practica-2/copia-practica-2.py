#Lista de reproducción de Musica
canciones = ["Canción 1", "Canción 2", "Canción 3"]

canciones.append("Canción 4")
print(canciones)

canciones.remove("Canción 2")
print(canciones)

info_cancion = ("Canción 1", "Artista: Corey Tylor", 3.50)
print(info_cancion[0])

generos = {"Rock", "Pop", "Electronica", "Rock"}
generos.add("Metal")
print(generos)
print("Pop" in generos)

#Justificación: escogi este ejemplo por que este programa utiliza una de Canciones
#ya que es una estructura Ideal para agregar y quitar canciines en la reproducción en
#cualquier momento, se usa "Tupla" para almacenar la información de la pista (nombres, artistas y duración de la canción)
#y un "set" para registrar los géneros musicales.