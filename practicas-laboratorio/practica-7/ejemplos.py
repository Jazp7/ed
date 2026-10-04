# 1. Recorrido y suma de cada fila
# Para obtener un total por cada fila, se puede recorrer la matriz y utilizar un acumulador independiente para cada fila.

ventas = [
    [15, 12, 10],
    [8, 10, 7],
    [20, 18, 15]
]

for indice, fila in enumerate(ventas, start=1):
    total = 0
    for valor in fila:
        total += valor
    print(f"Total de la fila {indice}: {total}")

# 2. Recorrido por columnas
# Para trabajar con los valores de una columna determinada, se puede utilizar su índice y recorrer las diferentes filas de la matriz.

temperaturas = [
    [24, 28, 25],
    [23, 29, 26],
    [25, 30, 27],
    [22, 27, 24]
]

filas = len(temperaturas)
columnas = len(temperaturas[0])

for columna in range(columnas):
    total = 0
    for indice_fila in range(filas):
        total += temperaturas[indice_fila][columna]
    promedio = total / filas
    print(f"Promedio de la columna {columna + 1}: {promedio:.2f}")


# 3. Contar valores dentro de una matriz
# Cuando una matriz contiene valores que representan estados, se puede recorrer y utilizar una condición para contar cuántas veces aparece un determinado valor.

asistencia = [
    [1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0]
]

for indice, fila in enumerate(asistencia, start=1):
    asistencias = 0
    for valor in fila:
        if valor == 1:
            asistencias += 1
    print(f"Asistencias de la fila {indice}: {asistencias}")