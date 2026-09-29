# ==========================================================================
# RETO: SISTEMA DE MONITOREO E INVENTARIO HASH
# Estructuras de Datos - Practica de Laboratorio 05
# Basado en los conceptos de Hash Maps y Diccionarios de practica06.ipynb
# ==========================================================================

import sys

# Configuracion de codificacion para evitar problemas en consolas Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

"""
Este programa implementa un Sistema Integral de Monitoreo e Inventario basado
en tablas Hash (Diccionarios de Python), resolviendo los 3 requerimientos del reto:

1. MAPEO DE REGISTROS:
   - Estructura de inventario donde las claves son codigos SKU unicos (acceso O(1)).
   - Los valores son diccionarios internos con atributos: nombre, precio, existencia y categoria.
   - Operaciones de insercion, actualizacion, consulta segura (.get) y eliminacion (.pop).

2. CONTADOR DE OCURRENCIAS:
   - Procesamiento de registros de eventos y transacciones.
   - Calculo de frecuencias utilizando exclusivamente el patron .get(clave, 0) + 1.
   - Sin librerias externas (sin Counter, sin defaultdict).

3. AGRUPAMIENTO POR CATEGORIA:
   - Mapeo agrupado: diccionario donde cada clave es una categoria y su valor
     asociado es una lista dinamica de productos pertenecientes a ella.
"""


# ==========================================================================
# 1. REQUERIMIENTO 1: MAPEO DE REGISTROS (INVENTARIO SKU)
# ==========================================================================

print("=" * 70)
print("REQUERIMIENTO 1: MAPEO DE REGISTROS (ESTRUCTURA DE INVENTARIO HASH)")
print("=" * 70)

# Estructura principal:
# Clave: Codigo SKU (str)
# Valor: Diccionario interno con {nombre, precio, existencia, categoria}
inventario_sku: dict[str, dict] = {
    "SKU-1001": {
        "nombre": "Teclado Mecanico RGB",
        "precio": 59.99,
        "existencia": 25,
        "categoria": "Perifericos"
    },
    "SKU-1002": {
        "nombre": "Mouse Optico Inalambrico",
        "precio": 24.50,
        "existencia": 40,
        "categoria": "Perifericos"
    },
    "SKU-1003": {
        "nombre": "Monitor Gamer 24\" IPS 144Hz",
        "precio": 175.00,
        "existencia": 12,
        "categoria": "Pantallas"
    },
    "SKU-1004": {
        "nombre": "Auriculares HyperX Cloud II",
        "precio": 69.99,
        "existencia": 18,
        "categoria": "Audio"
    },
    "SKU-1005": {
        "nombre": "Disco SSD NVMe 1TB M.2",
        "precio": 89.90,
        "existencia": 30,
        "categoria": "Almacenamiento"
    },
    "SKU-1006": {
        "nombre": "Monitor Curvo 27\" QHD",
        "precio": 260.00,
        "existencia": 8,
        "categoria": "Pantallas"
    }
}


def mostrar_inventario(inventario: dict[str, dict], titulo: str = "Catalogo de Inventario Actual"):
    """Imprime el catalogo de productos con formato tabular ordenado."""
    print(f"\n--- {titulo} ---")
    encabezado = f"{'SKU':<10} | {'Producto':<30} | {'Categoria':<15} | {'Precio ($)':>10} | {'Stock':>7}"
    print(encabezado)
    print("-" * len(encabezado))
    for sku, datos in inventario.items():
        print(f"{sku:<10} | {datos['nombre']:<30} | {datos['categoria']:<15} | {datos['precio']:>10.2f} | {datos['existencia']:>7}")
    print("-" * len(encabezado))


# Mostramos el inventario inicial
mostrar_inventario(inventario_sku, "Inventario Inicial Registrado")

# A. Acceso directo vs Acceso seguro con .get() (segun visto en practica06.ipynb)
print("\n[Operacion 1: Consultas de Productos]")
sku_busqueda = "SKU-1002"
print(f"Busqueda directa ({sku_busqueda}):", inventario_sku[sku_busqueda]["nombre"])

sku_inexistente = "SKU-9999"
# Uso de .get() para evitar KeyError y proveer valor por defecto
resultado_seguro = inventario_sku.get(sku_inexistente, "Producto no encontrado en inventario")
print(f"Busqueda segura con .get() ({sku_inexistente}): {resultado_seguro}")

# B. Modificacion de atributos (Actualizacion de existencias y precio)
print("\n[Operacion 2: Modificacion y Actualizacion]")
print(f"Stock anterior de SKU-1001: {inventario_sku['SKU-1001']['existencia']} unidades")
inventario_sku["SKU-1001"]["existencia"] += 10  # Ingresaron 10 unidades
inventario_sku["SKU-1001"]["precio"] = 54.99     # Descuento promocional
print(f"Stock actualizado de SKU-1001: {inventario_sku['SKU-1001']['existencia']} unidades | Nuevo Precio: ${inventario_sku['SKU-1001']['precio']}")

# C. Insercion de un nuevo registro
print("\n[Operacion 3: Insercion de Nuevo Producto]")
nuevo_sku = "SKU-1007"
inventario_sku[nuevo_sku] = {
    "nombre": "Microfono Condensador USB",
    "precio": 42.00,
    "existencia": 15,
    "categoria": "Audio"
}
print(f"Nuevo producto insertado con clave '{nuevo_sku}': {inventario_sku[nuevo_sku]['nombre']}")

# D. Eliminacion segura con .pop()
print("\n[Operacion 4: Eliminacion Segura con .pop()]")
sku_eliminar = "SKU-1006"
producto_eliminado = inventario_sku.pop(sku_eliminar, None)
if producto_eliminado:
    print(f"Producto eliminado ({sku_eliminar}): {producto_eliminado['nombre']} (Stock liberado: {producto_eliminado['existencia']})")
else:
    print(f"El producto {sku_eliminar} no existia.")

# Estado tras modificaciones
mostrar_inventario(inventario_sku, "Inventario Tras Operaciones")


# ==========================================================================
# 2. REQUERIMIENTO 2: CONTADOR DE OCURRENCIAS (MONITOREO HASH MAP)
# ==========================================================================

print("\n" + "=" * 70)
print("REQUERIMIENTO 2: CONTADOR DE OCURRENCIAS (.get() CON VALORES POR DEFECTO)")
print("=" * 70)

# A. Log de eventos del sistema de monitoreo
registro_eventos_sistema = [
    "LOGIN_SUCCESS", "VENTA", "LOGIN_SUCCESS", "FALLO_AUTH",
    "CONSULTA_STOCK", "VENTA", "VENTA", "REPOSICION",
    "CONSULTA_STOCK", "LOGIN_SUCCESS", "FALLO_AUTH", "VENTA",
    "VENTA", "CONSULTA_STOCK", "LOGIN_FAIL", "VENTA"
]

# B. Lista de transacciones de ventas por SKU
registro_transacciones_sku = [
    "SKU-1001", "SKU-1002", "SKU-1001", "SKU-1005", "SKU-1001",
    "SKU-1003", "SKU-1002", "SKU-1001", "SKU-1005", "SKU-1004",
    "SKU-1007", "SKU-1002", "SKU-1001", "SKU-1004", "SKU-1001"
]


def contar_frecuencias(lista_elementos: list) -> dict:
    """
    Calcula la frecuencia de cada elemento en una coleccion utilizando
    unicamente diccionarios estandar y el metodo .get() con valor por defecto.
    
    Complejidad Temporal: O(n) donde n es el numero de elementos.
    Complejidad Espacial: O(k) donde k es el numero de elementos unicos.
    
    Patron visto en practica06.ipynb:
        conteo[elem] = conteo.get(elem, 0) + 1
    """
    frecuencias: dict = {}
    for elemento in lista_elementos:
        frecuencias[elemento] = frecuencias.get(elemento, 0) + 1
    return frecuencias


# Conteo 1: Frecuencia de Eventos del Sistema
conteo_eventos = contar_frecuencias(registro_eventos_sistema)

print("\n--- Monitoreo de Eventos del Sistema (Logs) ---")
print(f"Total de registros procesados: {len(registro_eventos_sistema)}")
print(f"Diccionario Hash de frecuencias:\n{conteo_eventos}\n")

print(f"{'Tipo de Evento':<20} | {'Frecuencia':>10} | {'Grafico de Frecuencia'}")
print("-" * 55)
for evento, freq in sorted(conteo_eventos.items(), key=lambda item: item[1], reverse=True):
    barra = "#" * freq
    print(f"{evento:<20} | {freq:>10} | {barra}")

# Conteo 2: Frecuencia de Ventas por SKU
conteo_ventas_sku = contar_frecuencias(registro_transacciones_sku)

print("\n--- Frecuencia de Ventas por Codigo SKU ---")
print(f"{'SKU':<10} | {'Nombre del Producto':<30} | {'Ventas':>8}")
print("-" * 54)
for sku, ventas in sorted(conteo_ventas_sku.items(), key=lambda item: item[1], reverse=True):
    nombre = inventario_sku.get(sku, {}).get("nombre", "Desconocido")
    print(f"{sku:<10} | {nombre:<30} | {ventas:>8}")


# ==========================================================================
# 3. REQUERIMIENTO 3: AGRUPAMIENTO POR CATEGORIA
# ==========================================================================

print("\n" + "=" * 70)
print("REQUERIMIENTO 3: AGRUPAMIENTO POR CATEGORIA (MAPEO CON COLECCIONES)")
print("=" * 70)

# Lista de elementos para clasificar
lista_productos_catalogo = [
    {"sku": "SKU-1001", "nombre": "Teclado Mecanico RGB", "categoria": "Perifericos"},
    {"sku": "SKU-1002", "nombre": "Mouse Optico Inalambrico", "categoria": "Perifericos"},
    {"sku": "SKU-1003", "nombre": "Monitor Gamer 24\" IPS 144Hz", "categoria": "Pantallas"},
    {"sku": "SKU-1004", "nombre": "Auriculares HyperX Cloud II", "categoria": "Audio"},
    {"sku": "SKU-1005", "nombre": "Disco SSD NVMe 1TB M.2", "categoria": "Almacenamiento"},
    {"sku": "SKU-1007", "nombre": "Microfono Condensador USB", "categoria": "Audio"},
    {"sku": "SKU-1008", "nombre": "Memoria RAM DDR5 32GB", "categoria": "Almacenamiento"},
    {"sku": "SKU-1009", "nombre": "Webcam 4K Streaming Pro", "categoria": "Perifericos"},
    {"sku": "SKU-1010", "nombre": "Monitor Ultrawide 34\"", "categoria": "Pantallas"}
]


def agrupar_por_categoria(elementos: list[dict], clave_cat: str = "categoria", clave_val: str = "nombre") -> dict[str, list]:
    """
    Agrupa una lista de elementos en un diccionario donde:
      - Clave: Categoria
      - Valor: Lista de elementos pertenecientes a dicha categoria.
      
    Implementa el patron de Mapeo Agrupado ensenado en practica06.ipynb:
        categoria -> [elemento1, elemento2, ...]
    """
    agrupacion: dict[str, list] = {}
    
    for item in elementos:
        categoria = item[clave_cat]
        valor = item[clave_val]
        
        # Si la categoria no existe en el diccionario, se inicializa como lista vacia
        if categoria not in agrupacion:
            agrupacion[categoria] = []
        
        # Agregamos el elemento a la lista asociada a su categoria
        agrupacion[categoria].append(valor)
        
    return agrupacion


# Generamos el agrupamiento
productos_por_categoria = agrupar_por_categoria(lista_productos_catalogo)

print("\n--- Clasificacion de Productos por Categoria ---")
print(f"Diccionario estructurado con listas:\n{productos_por_categoria}\n")

for categoria, productos in productos_por_categoria.items():
    print(f" Categoria: {categoria.upper()} ({len(productos)} productos)")
    for prod in productos:
        print(f"   * {prod}")
    print()

# Demostracion: Anadir dinamicamente un elemento a una categoria existente
print("[Operacion Dinamica: Agregar producto a categoria existente]")
categoria_destino = "Perifericos"
nuevo_periferico = "Pad Mouse XXL RGB"
productos_por_categoria[categoria_destino].append(nuevo_periferico)
print(f"Producto '{nuevo_periferico}' anadido a '{categoria_destino}'.")
print(f"Nueva lista de {categoria_destino}: {productos_por_categoria[categoria_destino]}")


# ==========================================================================
# 4. SISTEMA INTEGRADO: MONITOREO E INVENTARIO HASH
# ==========================================================================

print("\n" + "=" * 70)
print("SISTEMA INTEGRADO: MONITOREO E INVENTARIO HASH (DEMOSTRACION COMPLETA)")
print("=" * 70)

class SistemaMonitoreoInventarioHash:
    """
    Clase integradora que combina el Mapeo de Registros por SKU,
    el Monitoreo de Eventos con conteo de frecuencias mediante .get(),
    y el Agrupamiento dinamico por Categorias.
    """
    
    def __init__(self):
        # Diccionario principal de inventario (SKU -> Atributos)
        self.inventario: dict[str, dict] = {}
        # Lista historica de eventos/transacciones
        self.logs_eventos: list[str] = []
        
    def registrar_producto(self, sku: str, nombre: str, precio: float, existencia: int, categoria: str) -> None:
        """Registra o actualiza un producto indexado por su SKU."""
        self.inventario[sku] = {
            "nombre": nombre,
            "precio": precio,
            "existencia": existencia,
            "categoria": categoria
        }
        self.registrar_evento(f"ALTA_PRODUCTO:{sku}")
        
    def registrar_evento(self, tipo_evento: str) -> None:
        """Registra un evento en la bitacora del sistema."""
        self.logs_eventos.append(tipo_evento)
        
    def procesar_venta(self, sku: str, cantidad: int = 1) -> bool:
        """Procesa la venta de un SKU verificando existencias de forma segura."""
        producto = self.inventario.get(sku)
        if not producto:
            self.registrar_evento("ERROR_SKU_NO_EXISTE")
            print(f"[!] Error de venta: El SKU '{sku}' no existe en inventario.")
            return False
            
        if producto["existencia"] < cantidad:
            self.registrar_evento("ERROR_STOCK_INSUFICIENTE")
            print(f"[!] Stock insuficiente para {producto['nombre']}. Disponibles: {producto['existencia']}")
            return False
            
        producto["existencia"] -= cantidad
        self.registrar_evento("VENTA_EXITOSA")
        self.registrar_evento(f"TRANSACCION_SKU:{sku}")
        print(f"[+] Venta procesada: {cantidad}x {producto['nombre']} | Quedan: {producto['existencia']}")
        return True

    def obtener_resumen_frecuencias(self) -> dict[str, int]:
        """Calcula las frecuencias de eventos usando .get()."""
        conteo: dict[str, int] = {}
        for ev in self.logs_eventos:
            conteo[ev] = conteo.get(ev, 0) + 1
        return conteo

    def agrupar_catalogo_por_categoria(self) -> dict[str, list[dict]]:
        """Agrupa el inventario actual por categorias con todos sus datos."""
        agrupados: dict[str, list[dict]] = {}
        for sku, datos in self.inventario.items():
            cat = datos["categoria"]
            if cat not in agrupados:
                agrupados[cat] = []
            agrupados[cat].append({"sku": sku, **datos})
        return agrupados

    def reporte_general(self) -> None:
        """Genera un informe integral del sistema hash."""
        print("\n" + "=" * 55)
        print("          REPORTE GENERAL DEL SISTEMA")
        print("=" * 55)
        print(f"Total de SKUs registrados: {len(self.inventario)}")
        print(f"Total de eventos en log: {len(self.logs_eventos)}")
        
        print("\n--- Frecuencia de Eventos Registrados (.get) ---")
        for ev, count in self.obtener_resumen_frecuencias().items():
            print(f"   * {ev:<25} -> {count} ocurrencia(s)")
            
        print("\n--- Inventario Agrupado por Categorias ---")
        for cat, items in self.agrupar_catalogo_por_categoria().items():
            print(f"   [{cat} - {len(items)} items]")
            for item in items:
                print(f"      - {item['sku']}: {item['nombre']} (${item['precio']:.2f}, Stock: {item['existencia']})")
        print("=" * 55)


# Demostracion del sistema integrado
sistema = SistemaMonitoreoInventarioHash()

# Registros iniciales
sistema.registrar_producto("SKU-A1", "Camara Web HD", 29.99, 10, "Video")
sistema.registrar_producto("SKU-A2", "Foco LED RGB Inteligente", 12.50, 25, "Iluminacion")
sistema.registrar_producto("SKU-A3", "Tira LED 5 Metros", 18.00, 15, "Iluminacion")
sistema.registrar_producto("SKU-A4", "Tripode Ajustable", 21.00, 8, "Video")

# Simulacion de transacciones y eventos
print("\n--- Ejecutando Transacciones de Prueba ---")
sistema.procesar_venta("SKU-A1", 2)
sistema.procesar_venta("SKU-A2", 5)
sistema.procesar_venta("SKU-A1", 1)
sistema.procesar_venta("SKU-A999", 1) # SKU inexistente
sistema.procesar_venta("SKU-A4", 10)  # Stock insuficiente

# Reporte final
sistema.reporte_general()
