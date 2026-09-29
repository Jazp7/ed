#Crea un conjunto de lenguaje de programación utilizadas por cada uno de los desarrolladores
#en el proyecto
#Lenguajes = Python - Java - JavaScript - PHP - Python - PHP

Lenguajes = {
    "Python",
    "Java",
    "JavaScript",
    "PHP",
    "Python",
    "PHP"
}

print(Lenguajes)

# 1. Creación y eliminación automática de duplicados
numeros = {1, 1, 1, 2, 2, 3}
print(numeros)

# 2. Agregar y eliminar elementos (Mutabilidad)
frutas = {"manzana", "banana"}
frutas.add("naranja")     
frutas.remove("banana")   
frutas.discard("pera")    
print(frutas)

# 3. Comprobar pertenencia con 'in'
usuarios_activos = {"admin", "invitado", "editor"}
print("admin" in usuarios_activos)    
print("root" in usuarios_activos)     

# 4. Crear un set vacío (¡Ojo con esto!)
set_vacio = set()       
no_es_set = {}

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)             
print(a & b)             
print(a - b)             
print(a ^ b)