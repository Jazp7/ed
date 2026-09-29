#Sistema de configuración de servidor.
#===== CONFIGURACIÓN DEL SISTEMA =====
#Aplicación: Sistema Académico
configuracion = ("Sistema Académico", "1.0.0", "localhost", 8080, "producción")
print("===== CONFIGURACIÓN DEL SISTEMA =====")
print(f"Aplicacion: {configuracion[0]}")
print(f"Version: {configuracion[1]}")
print(f"Servidor: {configuracion[2]}")
print(f"Puerto: {configuracion[3]}")
print(f"Modo: {configuracion[4]}\n")

print(f"Version: {configuracion[1]}")
print(f"Servidor: {configuracion[2]}")
print(f"Puerto: {configuracion[3]}\n")

print(f"Longitud: {len(configuracion)}")