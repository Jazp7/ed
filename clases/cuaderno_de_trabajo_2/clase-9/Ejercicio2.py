#Ubicación de dispositivos
#Una empresa de tecnología registra la ubicación de sus dispositivos mediante coordenadas.

dispositivo1 = ("PC001", "Servidor Principal", (150, 300), "Activo")
dispositivo2 = ("PC002", "Roter Central", (420, 180), "Activo")
dispositivo3 = ("PC003", "Switch de Distribución", (200, 500), "Inactivo")

print("===== INFORMACIÓN DISPOSITIVO 1 =====")
print(f"Código: {dispositivo1[0]}")
print(f"Nombre: {dispositivo1[1]}")
print(f"Coordernada X: {dispositivo1[2][0]}")
print(f"Coordenada Y: {dispositivo1[2][1]}")
print(f"Estado: {dispositivo1[3]}\n")

dispositivos = (dispositivo1, dispositivo2, dispositivo3)

coordenada_y_disp2 = dispositivos[1][2][1]
print(f"Coorndenada Y del segundo dispositivo: {coordenada_y_disp2}")