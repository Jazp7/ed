producto = {
    "codigo": "P001",
    "nombre": "Teclado mecánico",
    "precio": 45.99,
    "stock": 20,
    "disponible": True
}

# Podemos consultar el nombre del producto:
print(producto["nombre"])

# Cambiar la disponibilidad del producto y el stock a 0
producto["stock"] = 0
producto["disponible"] = None