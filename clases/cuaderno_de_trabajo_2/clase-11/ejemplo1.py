# Crear un diccionario

estudiante = {
    "nombre": "Ana",
    "edad": 21,
    "cursos": ["Python", "Estructura de datos"]
}

# Acceder a elementos
print(estudiante["nombre"])

# Agregar o modificar
estudiante["edad"] = 22
estudiante["carrera"] = "Ing. Software"

# Eliminar método "del"
del estudiante["edad"]

# Eliminar método "pop"
estudiante.pop("ciudad")