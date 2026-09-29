# estructuras_datos.py
# Miniprograma demostrativo: Listas, Tuplas, Sets + FIFO/LIFO

print("=" * 50)
print("DEMOSTRACIÓN DE ESTRUCTURAS DE DATOS")
print("=" * 50)

# ──────────────────────────────────────────────
# 1. LISTA (Lista de reproducción musical)
# Uso: FIFO (First In, First Out) - Cola
# Justificación: Se necesita orden secuencial y mutabilidad.
# La primera canción añadida es la primera en reproducirse.
# ──────────────────────────────────────────────
print("\n1. LISTA DE REPRODUCCIÓN (FIFO / COLA)")
playlist = ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California"]
print(f"   Estado inicial: {playlist}")

# Simular reproducción (sacar del inicio -> FIFO)
siguiente_cancion = playlist.pop(0) 
print(f"   ▶ Reproduciendo (FIFO): '{siguiente_cancion}'")
print(f"   Restante: {playlist}")

# Agregar nueva canción al final
playlist.append("Smells Like Teen Spirit")
print(f"    Agregada al final: {playlist}")


# ─────────────────────────────────────────────
# 2. LISTA (Inventario básico de productos)
# Uso: LIFO (Last In, First Out) - Pila
# Justificación: Modela apilamiento físico. El último producto 
# ingresado al almacén es el primero en salir (ej. cajas apiladas).
# ──────────────────────────────────────────────
print("\n2. INVENTARIO DE PRODUCTOS (LIFO / PILA)")
inventario = ["Laptop A", "Monitor B", "Teclado C"]
print(f"   Estado inicial: {inventario}")

# Simular entrada de mercancía (apilar)
inventario.append("Mouse D")
print(f"   📦 Nuevo ingreso (Push): 'Mouse D'")

# Simular salida de mercancía (desapilar -> LIFO)
ultimo_producto = inventario.pop()
print(f"   📤 Salida más reciente (Pop): '{ultimo_producto}'")
print(f"   Inventario actual: {inventario}")


# ──────────────────────────────────────────────
# 3. TUPLA (Colección de videojuegos)
# Uso: Datos inmutables (Solo lectura)
# Justificación: Una colección "definitiva" o catálogo base no debe 
# modificarse accidentalmente. Garantiza integridad de datos.
# ─────────────────────────────────────────────
print("\n3. COLECCIÓN DE VIDEOJUEGOS (TUPLA)")
videojuegos = ("Zelda: TOTK", "Mario Odyssey", "Metroid Prime")
print(f"   Colección fija: {videojuegos}")
print(f"   Acceso por índice [0]: '{videojuegos[0]}'")
# videojuegos[0] = "Otro juego"  #  Esto lanzaría TypeError


# ──────────────────────────────────────────────
# 4. SET (Registro de cursos aprobados)
# Uso: Unicidad y pertenencia
# Justificación: No pueden existir duplicados (no apruebas twice el mismo curso).
# Permite verificar rápidamente si un curso ya está en el registro.
# ──────────────────────────────────────────────
print("\n4. REGISTRO DE CURSOS APROBADOS (SET)")
cursos_aprobados = {"Matemáticas", "Física", "Programación"}
print(f"   Cursos actuales: {cursos_aprobados}")

# Intentar agregar duplicado (el set lo ignora automáticamente)
cursos_aprobados.add("Matemáticas") 
print(f"   Intento agregar 'Matemáticas' again: {cursos_aprobados} (Sin cambios)")

# Agregar nuevo curso válido
cursos_aprobados.add("Ética")
print(f"   Nuevo curso agregado: {cursos_aprobados}")

# Verificación rápida (O(1))
if "Física" in cursos_aprobados:
    print("   ✅ 'Física' ya está registrada.")


# ──────────────────────────────────────────────
# 5. SET (Gestión de participantes de evento)
# Uso: Operaciones de conjuntos (Unión/Diferencia)
# Justificación: Ideal para gestionar asistencia sin duplicados
# y comparar listas (ej. quiénes faltaron).
# ─────────────────────────────────────────────
print("\n5. PARTICIPANTES DE EVENTO (SET)")
invitados = {"Ana", "Carlos", "Luis", "Maria"}
asistentes = {"Ana", "Luis", "Pedro"}  # Pedro no estaba invitado, Ana y Luis sí

# Quiénes asistieron siendo invitados válidos
presentes_validos = invitados & asistentes  # Intersección
print(f"   Invitados: {invitados}")
print(f"   Asistentes reales: {asistentes}")
print(f"   ✅ Presentes válidos (Intersección): {presentes_validos}")

# Quiénes faltaron (Diferencia)
ausentes = invitados - asistentes
print(f"   ❌ Ausentes (Diferencia): {ausentes}")

print("\n" + "=" * 50)
print("FIN DE LA DEMOSTRACIÓN")