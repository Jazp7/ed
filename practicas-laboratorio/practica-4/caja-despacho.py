from collections import deque

# ==========================================================================
# SIMULACIÓN: SISTEMA INTEGRAL DE CAJA Y DESPACHO
# ==========================================================================

print("=" * 60)
print(" INICIANDO SIMULACIÓN DE CAJA Y DESPACHO")
print("=" * 60)

# --------------------------------------------------------------------------
# 1. CONFIGURACIÓN INICIAL DE ESTRUCTURAS
# --------------------------------------------------------------------------

# FIFO: Usamos deque porque es eficiente para sacar elementos por la izquierda (popleft)
# Simula la fila física de clientes esperando ser atendidos.
fila_caja = deque(["Cliente_Ana", "Cliente_Carlos", "Cliente_Luis"])

# SETS: Conjunto de membresías válidas en el sistema.
# Usamos set porque la búsqueda es O(1) y no permite duplicados.
membresias_vigentes = {"GOLD_001", "SILVER_023", "PLATINUM_99", "BRONCE_55"}

# SET: Para registrar cupones ya usados en esta sesión y evitar fraude/repetición.
cupones_usados_sesion: set[str] = set()

print(f"Estado inicial Fila (FIFO): {list(fila_caja)}")
print(f" Membresías activas: {membresias_vigentes}")
print(f"Cupones usados hasta ahora: {cupones_usados_sesion}")
print("-" * 60)


# --------------------------------------------------------------------------
# 2. FUNCIÓN DE ATENCIÓN (Lógica Central)
# --------------------------------------------------------------------------
def atender_cliente():
    """
    Procesa al siguiente cliente de la fila.
    Implementa: FIFO para la cola, LIFO para productos, Sets para validación.
    """
    
    # --- PASO A: FIFO (Atención en orden de llegada) ---
    # Validación crítica: ¿Hay alguien en la fila?
    if not fila_caja:
        print("ALERTA: La caja está vacía. No hay clientes para atender.")
        return

    # popleft() saca al PRIMERO que llegó (FIFO estricto)
    cliente_actual = fila_caja.popleft() 
    print(f"\nAtendiendo a: {cliente_actual}")

    # --- PASO B: LIFO (Bolsa de Productos) ---
    # El cliente pone productos en su bolsa (orden de compra).
    # El cajero registra/desempaca desde el último que metió (LIFO).
    bolsa_productos = ["Leche", "Pan", "Huevos", "Cereal"] 
    print(f"   Productos en bolsa (orden de entrada): {bolsa_productos}")
    
    print("   Registrando productos (LIFO - del último al primero):")
    while bolsa_productos:
        producto = bolsa_productos.pop() # pop() sin argumentos saca el ÚLTIMO (LIFO)
        print(f"      Escaneado: {producto}")

    # --- PASO C: SETS (Validación de Membresía y Cupones) ---
    
    # 1. Validar Membresía
    # Supongamos que el cliente presenta un código.
    codigo_cliente = "SILVER_023" 
    
    if codigo_cliente in membresias_vigentes:
        print(f"   Membresía '{codigo_cliente}' VÁLIDA. Descuento aplicado.")
    else:
        print(f"    Membresía '{codigo_cliente}' NO VIGENTE.")

    # 2. Validar Cupón (Evitar repetición en sesión)
    cupon_ofrecido = "DESCUENTO_VERANO"
    
    if cupon_ofrecido in cupones_usados_sesion:
        print(f"   Cupón '{cupon_ofrecido}' RECHAZADO: Ya fue usado en esta sesión.")
    else:
        # Si es válido, lo aplicamos y lo registramos en el set
        print(f"    Cupón '{cupon_ofrecido}' ACEPTADO.")
        cupones_usados_sesion.add(cupon_ofrecido) # Add al set para bloquearlo futuro

    print(f"   {cliente_actual} ha sido despachado exitosamente.")


# ==========================================================================
# EJECUCIÓN DE LA SIMULACIÓN
# ==========================================================================

# Atender a los 3 clientes iniciales
atender_cliente()
atender_cliente()
atender_cliente()

# Intentar atender un cuarto cliente cuando la fila ya está vacía
# (Esto prueba la validación de fila vacía requerida en el enunciado)
print("\n" + "-" * 60)
atender_cliente() 

# Mostrar estado final de los sets
print("\n" + "=" * 60)
print("ESTADO FINAL DEL SISTEMA")
print(f" Fila restante: {list(fila_caja)}")
print(f"Historial de cupones usados (Set): {cupones_usados_sesion}")