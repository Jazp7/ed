import sys

print("\n ----- Números enteros ----- ")
print(f"Tamaño de un entero: {sys.getsizeof(0)} bytes")
print(f"Tamaño de un entero: {sys.getsizeof(100)} bytes")
print(f"Tamaño de un entero: {sys.getsizeof(-100)} bytes")

numero = 10 ** 100
print(f"Número: {numero}")

print("\n ----- Números decimales ----- ")
print(f"Tamaño de un decimal: {sys.float_info.max} bytes")
print(f"Tamaño de un decimal: {sys.float_info.min} bytes")

print("\n ----- Valor Booleano ----- ")
print(True)
print(False)

print(type(True))
print(type(False))

print(int(True))
print(int(False))

cadena = "Hola mundo"
print(cadena)
print(f"Longitud de la palabra: {len(cadena)}")


print("\n Hola mi nombre es \"Josué\"")
print("Hola mi nombre es Arístides \nSoy estudiante de la materia de \nEstructura de Datos")


# Tabla
print("\n ----- Tabla ----- ")
print("Nombre\tNota 1\tNota 2\tNota 3 \nAna \t10 \t10 \t10 \nJosué \t9 \t8 \t7")