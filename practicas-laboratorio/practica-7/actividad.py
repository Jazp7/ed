# Ejercicio 1: Inventario de productos
inventario = [
    [15, 12, 10],
    [8, 10, 7],
    [20, 18, 15],
    [12, 14, 11]
]

print("Ejercicio 1: Inventario de productos")
print("Matriz de inventario:")
for fila in inventario:
    print(fila)

print("\nTotal disponible de cada producto:")
for indice, fila in enumerate(inventario, start=1):
    print(f"Producto {indice}: {sum(fila)}")

print("\nTotal registrado en cada día:")
for dia in range(len(inventario[0])):
    total = 0
    for producto in range(len(inventario)):
        total += inventario[producto][dia]
    print(f"Día {dia + 1}: {total}")

print("\nModificar una cantidad del inventario")
try:
    indice_producto = int(input(f"Indique el producto (1-{len(inventario)}): ")) - 1
    columna = int(input(f"Indique el día (1-{len(inventario[0])}): ")) - 1
    nueva_cantidad = int(input("Indique la nueva cantidad: "))

    if not (
        0 <= indice_producto < len(inventario)
        and 0 <= columna < len(inventario[0])
    ):
        print("Error: el producto o el día indicado no existe.")
    elif nueva_cantidad < 0:
        print("Error: la cantidad no puede ser negativa.")
    else:
        inventario[indice_producto][columna] = nueva_cantidad
        print("Inventario actualizado:")
        for registro in inventario:
            print(registro)
except ValueError:
    print("Error: ingrese números enteros.")


# Ejercicio 2: Registro de temperaturas
temperaturas = [
    [24, 28, 25],
    [23, 29, 26],
    [25, 30, 27],
    [22, 27, 24],
    [24, 28, 26]
]

print("\nEjercicio 2: Registro de temperaturas")
print("Matriz de temperaturas:")
for fila in temperaturas:
    print(fila)

print("\nPromedio de temperatura de cada día:")
for dia, fila in enumerate(temperaturas, start=1):
    promedio = sum(fila) / len(fila)
    print(f"Día {dia}: {promedio:.2f} °C")

print("\nPromedio de cada momento del día:")
for momento in range(len(temperaturas[0])):
    total = 0
    for dia in range(len(temperaturas)):
        total += temperaturas[dia][momento]
    promedio = total / len(temperaturas)
    print(f"Momento {momento + 1}: {promedio:.2f} °C")

temperatura_maxima = max(max(fila) for fila in temperaturas)
print(f"\nTemperatura más alta registrada: {temperatura_maxima} °C")


# Ejercicio 3: Registro de asistencia
asistencia = [
    [1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0],
    [0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1]
]

print("\nEjercicio 3: Registro de asistencia")
print("Matriz de asistencia (1 = asistencia, 0 = inasistencia):")
for fila in asistencia:
    print(fila)

asistencias_por_estudiante = []
print("\nAsistencias de cada estudiante:")
for indice, fila in enumerate(asistencia, start=1):
    total = sum(fila)
    asistencias_por_estudiante.append(total)
    print(f"Estudiante {indice}: {total}")

print("\nEstudiantes que asistieron cada día:")
for dia in range(len(asistencia[0])):
    total = 0
    for estudiante in range(len(asistencia)):
        total += asistencia[estudiante][dia]
    print(f"Día {dia + 1}: {total}")

maximo_asistencias = max(asistencias_por_estudiante)
estudiantes_con_mas_asistencias = [
    indice + 1
    for indice, total in enumerate(asistencias_por_estudiante)
    if total == maximo_asistencias
]
print(
    f"\nMayor cantidad de asistencias: {maximo_asistencias}, "
    f"estudiante(s): {', '.join(map(str, estudiantes_con_mas_asistencias))}"
)
