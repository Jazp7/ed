##Crea una tupla
coordenadas = (13.7, -89.2)

##Acceder
print(coordenadas[0]) 

##contar y econtrar indice
print(coordenadas.count(13.7))
print(coordenadas.index(-89.2))

##Ejercicio de Ejemplo
##crea una lista de compras de frutas a comprar  en el mercado por unidad que incluya:
##Manzanas, Banana, Uva, Manzana. solo que te dicen que no puede ser modificada.

frutas = ("Manzanas", "Banana", "Uva", "Manzana")
print(frutas)

##Acceder a la segunda fruta a comprar
print(frutas[1]) ##Banana

##Recibe un mensaje donde te consultan cuantas frutas traerás
print(len(frutas))

##Ejemplo
##Crear espacio de guardado de información que no se modifique, la cual pueda
##llevar información anidada Ejemplo de las empresas migueleñas y dentro de ella 
##cual es el producto que ofrecen a la población migueleña.

##Crear una tupla anidada
empresa = (
    "Manguito",
    "San Miguel",
    ("Helados", "Mangoneada"),
    1981
)
print(empresa[2])
print(empresa[2][0])