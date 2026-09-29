# ==========================================================================
# RETO: SIMPLIFICACIÓN Y OPERACIONES CON LAMBDA
# Estructuras de Datos - Práctica de Laboratorio 05
# Basado en los conceptos y ejercicios del cuaderno practica05.ipynb
# ==========================================================================

import sys

# Configuración de codificación para evitar errores de salida en consolas Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

"""
Este programa resuelve de forma integral los requerimientos establecidos en el
reto de la Práctica de Laboratorio 05 ("Simplificación y Operaciones con Lambda"),
tomando como base los conceptos enseñados en 'practica05.ipynb':

1. REFACTORIZACIÓN DE FUNCIONES CONVENCIONALES (DEF -> LAMBDA):
   - Conversión de 3 funciones tradicionales 'def' a expresiones 'lambda' equivalentes
     en una sola línea:
     a) Cálculo de descuentos comerciales sobre precios.
     b) Conversión de unidades de temperatura (Celsius <-> Fahrenheit).
     c) Formateo y estandarización de nombres completos.

2. VALIDACIONES CON OPERADORES TERNARIOS:
   - Expresiones lambda que devuelven respuestas booleanas o de estado descriptivo
     empleando la sintaxis ternaria: (valor_si_verdadero if condicion else valor_si_falso):
     a) Determinación de número positivo, negativo o cero.
     b) Determinación y validación de mayoría de edad (>= 18 años).
     c) Validación de suficiencia de fondos para compras.

3. PROCESAMIENTO EN LOTE (BATCH PROCESSING):
   - Aplicación de expresiones lambda dentro de bucles iterativos para transformar
     colecciones de valores numéricos:
     a) Aplicación de recargos por financiamiento/servicio a una lista de precios.
     b) Conversión masiva de divisas monetarias en lote.
     c) Conversión en lote de lecturas térmicas de sensores.

4. SISTEMA INTEGRADOR:
   - Clase que unifica los tres conceptos en un flujo real de procesamiento comercial.
"""


# ==========================================================================
# SECCIÓN 0: FUNDAMENTOS DEL CUADERNO DE TRABAJO (practica05.ipynb)
# ==========================================================================

def repasar_fundamentos_cuaderno():
    """
    Muestra y verifica los 4 ejemplos fundamentales del cuaderno de trabajo:
    1. Sintaxis básica def vs lambda (cálculo de IVA al 13%).
    2. Expresiones con múltiples argumentos (área de rectángulo y distancia).
    3. Condicionales en línea con operador ternario (evaluar estado y paridad).
    4. Aplicación rápida dentro de comprensiones y ciclos (formateo de códigos).
    """
    print("=" * 75)
    print("SECCIÓN 0: FUNDAMENTOS DEL CUADERNO DE TRABAJO (practica05.ipynb)")
    print("=" * 75)

    # 1. Sintaxis básica y comparación con def
    def calcular_iva(precio):
        return precio * 0.13

    calcular_iva_lambda = lambda precio: precio * 0.13

    print("\n--- 1. Sintaxis básica: def vs lambda (IVA 13%) ---")
    print(f"IVA normal (def) para $100:    ${calcular_iva(100):.2f}")
    print(f"IVA resumido (lambda) para $100: ${calcular_iva_lambda(100):.2f}")

    # 2. Múltiples argumentos
    area_rectangulo = lambda base, altura: base * altura
    distancia_total = lambda velocidad, tiempo: velocidad * tiempo

    print("\n--- 2. Múltiples argumentos ---")
    print(f"Área rectángulo (base=5, altura=8):       {area_rectangulo(5, 8)}")
    print(f"Distancia total (vel=60 km/h, t=2.5 hrs):  {distancia_total(60, 2.5)} km")

    # 3. Condicionales en línea (Operador Ternario)
    evaluar_estado = lambda nota: "Aprobado" if nota >= 6.0 else "Reprobado"
    es_par = lambda n: True if n % 2 == 0 else False

    print("\n--- 3. Operador Ternario en línea ---")
    print(f"Nota 7.5: {evaluar_estado(7.5)}")
    print(f"Nota 4.0: {evaluar_estado(4.0)}")
    print(f"¿Es 10 par?: {es_par(10)} | ¿Es 7 par?: {es_par(7)}")

    # 4. Aplicación dentro de comprensiones
    formatear_codigo = lambda prefijo, numero: f"{prefijo}-{numero:04d}"
    ids_generados = [formatear_codigo("USR", i) for i in range(1, 6)]
    print("\n--- 4. Comprensión de listas con lambda ---")
    print(f"Códigos de usuario generados: {ids_generados}")
    print("-" * 75)


# ==========================================================================
# REQUERIMIENTO 1: REFACTORIZACIÓN DE FUNCIONES CONVENCIONALES
# ==========================================================================

# --------------------------------------------------------------------------
# CASO 1: CÁLCULO DE DESCUENTOS COMERCIALES
# --------------------------------------------------------------------------
# Función tradicional con 'def':
def calcular_precio_descuento_def(precio: float, porcentaje_descuento: float) -> float:
    """Calcula el precio final tras aplicar un porcentaje de descuento."""
    monto_descuento = precio * (porcentaje_descuento / 100)
    precio_final = precio - monto_descuento
    return round(precio_final, 2)

# Versión refactorizada a una sola línea usando 'lambda':
calcular_precio_descuento_lambda = lambda precio, porcentaje: round(precio * (1 - (porcentaje / 100)), 2)

# Función auxiliar lambda para obtener únicamente el monto descontado:
calcular_ahorro_lambda = lambda precio, porcentaje: round(precio * (porcentaje / 100), 2)


# --------------------------------------------------------------------------
# CASO 2: CONVERSIÓN DE TEMPERATURA (CELSIUS A FAHRENHEIT)
# --------------------------------------------------------------------------
# Fórmula matemática: F = (C * 9/5) + 32
# Función tradicional con 'def':
def celsius_a_fahrenheit_def(celsius: float) -> float:
    """Convierte grados Celsius a Fahrenheit usando fórmula tradicional."""
    resultado = (celsius * 9 / 5) + 32
    return round(resultado, 2)

# Versión refactorizada a una sola línea usando 'lambda':
celsius_a_fahrenheit_lambda = lambda c: round((c * 9 / 5) + 32, 2)

# Expresión complementaria: Fahrenheit a Celsius: C = (F - 32) * 5/9
fahrenheit_a_celsius_lambda = lambda f: round((f - 32) * 5 / 9, 2)


# --------------------------------------------------------------------------
# CASO 3: FORMATEO Y ESTANDARIZACIÓN DE NOMBRES
# --------------------------------------------------------------------------
# Función tradicional con 'def':
def formatear_nombre_def(nombre: str, apellido: str) -> str:
    """Limpia espacios en blanco y da formato estándar: 'APELLIDO, Nombre'."""
    nombre_limpio = nombre.strip().title()
    apellido_limpio = apellido.strip().upper()
    return f"{apellido_limpio}, {nombre_limpio}"

# Versión refactorizada a una sola línea usando 'lambda':
formatear_nombre_lambda = lambda nombre, apellido: f"{apellido.strip().upper()}, {nombre.strip().title()}"

# Expresión complementaria: Formato directo 'Nombre Apellido' capitalizado:
capitalizar_completo_lambda = lambda nombre_completo: " ".join(nombre_completo.strip().title().split())


def demostrar_requerimiento_1():
    """Ejecuta y compara sistemáticamente las 3 funciones tradicionales vs sus lambdas."""
    print("\n" + "=" * 75)
    print("REQUERIMIENTO 1: REFACTORIZACIÓN DE FUNCIONES CONVENCIONALES (DEF -> LAMBDA)")
    print("=" * 75)
    print("\n--- Demostración y Validación Cruzada: def vs lambda ---")

    # 1. Pruebas de Descuento
    pruebas_descuento = [(100.0, 15.0), (250.0, 20.0), (49.99, 10.0), (1200.0, 35.0)]
    print("\n[Caso 1: Cálculo de Descuentos]")
    print(f"{'Precio Base':>12} | {'% Desc':>8} | {'def (Normal)':>14} | {'lambda (1 línea)':>16} | {'¿Idénticos?':>11}")
    print("-" * 72)
    for precio, desc in pruebas_descuento:
        res_def = calcular_precio_descuento_def(precio, desc)
        res_lam = calcular_precio_descuento_lambda(precio, desc)
        coinciden = "SI (OK)" if res_def == res_lam else "NO"
        ahorro = calcular_ahorro_lambda(precio, desc)
        print(f"${precio:>11.2f} | {desc:>7.1f}% | ${res_def:>13.2f} | ${res_lam:>15.2f} | {coinciden:>11} (Ahorro: ${ahorro:.2f})")

    # 2. Pruebas de Temperatura
    pruebas_temp = [-10.0, 0.0, 20.0, 37.0, 100.0]
    print("\n[Caso 2: Conversión de Temperatura (Celsius a Fahrenheit)]")
    print(f"{'Celsius (°C)':>14} | {'def (Normal)':>14} | {'lambda (1 línea)':>16} | {'Inverso (°C)':>14} | {'¿Idénticos?':>11}")
    print("-" * 78)
    for c in pruebas_temp:
        f_def = celsius_a_fahrenheit_def(c)
        f_lam = celsius_a_fahrenheit_lambda(c)
        c_inverso = fahrenheit_a_celsius_lambda(f_lam)
        coinciden = "SI (OK)" if f_def == f_lam else "NO"
        print(f"{c:>13.1f}° | {f_def:>13.1f}°F | {f_lam:>15.1f}°F | {c_inverso:>13.1f}°C | {coinciden:>11}")

    # 3. Pruebas de Formateo de Nombres
    pruebas_nombres = [
        ("  juan carlos ", " perez  martinez "),
        ("maria", "gomez"),
        (" aristides ", "zelaya "),
        ("ANA  LUCIA", "hernandez-soto")
    ]
    print("\n[Caso 3: Formateo de Nombres]")
    print(f"{'Nombre y Apellido Original':<35} | {'def':<25} | {'lambda':<25}")
    print("-" * 90)
    for nom, ape in pruebas_nombres:
        nom_def = formatear_nombre_def(nom, ape)
        nom_lam = formatear_nombre_lambda(nom, ape)
        print(f"'{nom} {ape}'"[:35].ljust(35) + f" | {nom_def:<25} | {nom_lam:<25}")


# ==========================================================================
# REQUERIMIENTO 2: VALIDACIONES CON OPERADORES TERNARIOS
# ==========================================================================

"""
El operador ternario en Python permite evaluar condiciones en una sola expresión:
    valor_si_verdadero if condicion else valor_si_falso

Cuando se requieren más de 2 estados, es posible encadenar operadores ternarios:
    estado_1 if cond_1 else (estado_2 if cond_2 else estado_3)
"""

# --------------------------------------------------------------------------
# A. EVALUACIÓN DE NÚMEROS: POSITIVO / NEGATIVO / CERO
# --------------------------------------------------------------------------
# 1. Validación Booleana: ¿Es positivo el número?
es_positivo = lambda n: True if n > 0 else False

# 2. Validación de Estado Descriptivo (ternario anidado para 3 estados):
determinar_signo = lambda n: "Positivo" if n > 0 else ("Negativo" if n < 0 else "Cero / Neutro")

# 3. Validación de paridad con operador ternario:
clasificar_paridad = lambda n: "Par" if n % 2 == 0 else "Impar"


# --------------------------------------------------------------------------
# B. VALIDACIÓN DE MAYORÍA DE EDAD
# --------------------------------------------------------------------------
UMBRAL_MAYORIA_EDAD = 18

# 1. Validación Booleana directa:
es_mayor_edad = lambda edad: True if edad >= UMBRAL_MAYORIA_EDAD else False

# 2. Validación de Estado Descriptivo:
clasificar_mayoria_edad = lambda edad: "Mayor de edad" if edad >= UMBRAL_MAYORIA_EDAD else "Menor de edad"

# 3. Validación de Categoría Etaria (ternario encadenado multinivel):
categorizar_etapa_vida = lambda edad: (
    "Adulto Mayor" if edad >= 60 else (
        "Adulto" if edad >= 18 else (
            "Adolescente" if edad >= 12 else "Infante"
        )
    )
)


# --------------------------------------------------------------------------
# C. VALIDACIÓN COMERCIAL Y REGLAS DE NEGOCIO
# --------------------------------------------------------------------------
# 1. Validación de suficiencia de saldo para compras:
validar_fondos = lambda saldo, costo: (
    "Aprobada: Fondos suficientes" if saldo >= costo
    else f"Rechazada: Fondos insuficientes (Faltan ${costo - saldo:.2f})"
)

# 2. Validación de límite crediticio o sobregiro:
es_transaccion_valida = lambda saldo, costo: True if saldo >= costo else False


def demostrar_requerimiento_2():
    """Prueba exhaustiva de las expresiones lambda condicionales."""
    print("\n" + "=" * 75)
    print("REQUERIMIENTO 2: VALIDACIONES CON OPERADORES TERNARIOS (RESPUESTAS BOOLEANAS Y DE ESTADO)")
    print("=" * 75)
    print("\n--- Demostración de Evaluaciones con Operador Ternario ---")

    # Pruebas de Signo Numérico
    valores_numericos = [-15.5, -3, 0, 0.0, 4.2, 18, -0.01]
    print("\n[Validación 1: Signo y Paridad de Números]")
    print(f"{'Número':>10} | {'es_positivo (bool)':>19} | {'determinar_signo (estado)':>26} | {'Par/Impar':>10}")
    print("-" * 74)
    for num in valores_numericos:
        b_pos = es_positivo(num)
        estado = determinar_signo(num)
        # Paridad tiene sentido estricto para números enteros
        paridad = clasificar_paridad(int(num)) if isinstance(num, int) or num.is_integer() else "N/A (Real)"
        print(f"{num:>10.2f} | {str(b_pos):>19} | {estado:>26} | {paridad:>10}")

    # Pruebas de Mayoría de Edad
    edades_prueba = [5, 11, 12, 15, 17, 18, 19, 35, 60, 78]
    print("\n[Validación 2: Verificación de Mayoría de Edad y Etapas]")
    print(f"{'Edad':>6} | {'es_mayor_edad (bool)':>21} | {'Estado Legal':>16} | {'Categoría Etaria':>18}")
    print("-" * 68)
    for edad in edades_prueba:
        mayor_bool = es_mayor_edad(edad)
        estado_legal = clasificar_mayoria_edad(edad)
        categoria = categorizar_etapa_vida(edad)
        print(f"{edad:>6} | {str(mayor_bool):>21} | {estado_legal:>16} | {categoria:>18}")

    # Pruebas de Fondos Comerciales
    casos_compra = [
        (100.0, 45.0),
        (50.0, 50.0),
        (25.0, 89.90),
        (300.0, 299.99),
        (0.0, 15.0)
    ]
    print("\n[Validación 3: Verificación de Fondos y Transacciones]")
    print(f"{'Saldo':>10} | {'Costo Total':>12} | {'Válido':>8} | {'Mensaje del Sistema'}")
    print("-" * 75)
    for saldo, costo in casos_compra:
        valido = "SI" if es_transaccion_valida(saldo, costo) else "NO"
        mensaje = validar_fondos(saldo, costo)
        print(f"${saldo:>9.2f} | ${costo:>11.2f} | {valido:>8} | {mensaje}")


# ==========================================================================
# REQUERIMIENTO 3: PROCESAMIENTO EN LOTE (BATCH PROCESSING CON BUCLES)
# ==========================================================================

# --------------------------------------------------------------------------
# LAMBDAS PARA TRANSFORMACIÓN EN LOTE
# --------------------------------------------------------------------------
# 1. Aplicación de recargo porcentual por servicio, financiamiento o método de pago
aplicar_recargo_lambda = lambda precio, tasa_recargo: round(precio * (1 + (tasa_recargo / 100)), 2)

# 2. Cálculo del incremento neto por recargo
calcular_monto_recargo_lambda = lambda precio, tasa_recargo: round(precio * (tasa_recargo / 100), 2)

# 3. Conversión de divisas (ej. USD a Euros con tasa de cambio)
convertir_divisa_lambda = lambda monto, tasa_cambio: round(monto * tasa_cambio, 2)

# 4. Cálculo de precio total con impuesto y descuento simultáneo
calcular_total_complejo_lambda = lambda base, iva_pct, desc_pct: round(
    (base * (1 - (desc_pct / 100))) * (1 + (iva_pct / 100)), 2
)


def procesar_lote_precios_con_bucle(precios: list[float], tasa_recargo: float) -> list[dict]:
    """
    Transforma una colección de precios aplicando una expresión lambda
    dentro de un bucle 'for' tradicional.
    
    Registra para cada elemento:
      - Precio base original
      - Monto monetario del recargo
      - Precio final ajustado
    """
    resultados_lote: list[dict] = []
    
    # Bucle iterativo tradicional que aplica la lambda elemento por elemento
    for p in precios:
        monto_recargo = calcular_monto_recargo_lambda(p, tasa_recargo)
        precio_final = aplicar_recargo_lambda(p, tasa_recargo)
        
        resultados_lote.append({
            "precio_base": p,
            "monto_recargo": monto_recargo,
            "precio_final": precio_final
        })
        
    return resultados_lote


def procesar_lote_temperaturas_con_bucle(temperaturas_c: list[float]) -> list[tuple[float, float]]:
    """
    Transforma una lista de mediciones térmicas de °C a °F utilizando
    la lambda dentro de un bucle acumulador.
    """
    resultados: list[tuple[float, float]] = []
    for temp in temperaturas_c:
        temp_f = celsius_a_fahrenheit_lambda(temp)
        resultados.append((temp, temp_f))
    return resultados


def demostrar_requerimiento_3():
    """Ejecuta los ejercicios de transformación en lote con métricas y formateo."""
    print("\n" + "=" * 75)
    print("REQUERIMIENTO 3: PROCESAMIENTO EN LOTE (BATCH PROCESSING CON BUCLES Y LAMBDA)")
    print("=" * 75)
    print("\n--- Demostración 1: Aplicación de Recargos a Lista de Precios ---")

    lista_precios_originales = [15.50, 42.00, 99.99, 150.00, 8.25, 275.50, 499.00]
    PORCENTAJE_RECARGO = 8.5  # 8.5% por financiamiento en cuotas

    print(f"Colección inicial de precios: {lista_precios_originales}")
    print(f"Recargo comercial a aplicar: {PORCENTAJE_RECARGO}%\n")

    # Procesamiento con bucle
    lote_procesado = procesar_lote_precios_con_bucle(lista_precios_originales, PORCENTAJE_RECARGO)

    encabezado = f"{'Item':<6} | {'Precio Base':>12} | {'Recargo (+8.5%)':>16} | {'Precio Final':>14}"
    print(encabezado)
    print("-" * len(encabezado))

    total_base = 0.0
    total_recargo = 0.0
    total_final = 0.0

    for idx, item in enumerate(lote_procesado, start=1):
        total_base += item["precio_base"]
        total_recargo += item["monto_recargo"]
        total_final += item["precio_final"]
        print(f"#{idx:<5} | ${item['precio_base']:>11.2f} | ${item['monto_recargo']:>15.2f} | ${item['precio_final']:>13.2f}")

    print("-" * len(encabezado))
    print(f"{'TOTAL':<6} | ${total_base:>11.2f} | ${total_recargo:>15.2f} | ${total_final:>13.2f}")

    # Equivalente con List Comprehension (técnica también vista en practica05.ipynb)
    precios_finales_comprension = [aplicar_recargo_lambda(p, PORCENTAJE_RECARGO) for p in lista_precios_originales]
    print(f"\nVerificación por List Comprehension:\n{precios_finales_comprension}")

    print("\n--- Demostración 2: Conversión Masiva de Moneda (USD a EUR) en Lote ---")
    TASA_CAMBIO_EUR = 0.92  # 1 USD = 0.92 EUR
    montos_usd = [10.0, 25.0, 50.0, 100.0, 250.0, 500.0, 1200.0]

    montos_eur = []
    # Bucle de transformación
    for monto in montos_usd:
        eur = convertir_divisa_lambda(monto, TASA_CAMBIO_EUR)
        montos_eur.append(eur)

    print(f"{'Monto USD ($)':>14} | {'Tasa':>6} | {'Monto EUR (€)':>14}")
    print("-" * 40)
    for u, e in zip(montos_usd, montos_eur):
        print(f"${u:>13.2f} | {TASA_CAMBIO_EUR:>6.2f} | €{e:>13.2f}")

    print("\n--- Demostración 3: Conversión de Lecturas de Sensores en Lote ---")
    sensores_celsius = [-5.0, 0.0, 12.5, 21.0, 28.4, 36.6, 42.0]
    sensores_transformados = procesar_lote_temperaturas_con_bucle(sensores_celsius)

    print(f"{'Sensor':<8} | {'Temp (°C)':>10} | {'Temp (°F)':>10}")
    print("-" * 34)
    for i, (c, f) in enumerate(sensores_transformados, start=1):
        print(f"S-{i:03d}   | {c:>9.1f}° | {f:>9.1f}°")


# ==========================================================================
# SECCIÓN 4: CASO INTEGRAL - MOTOR DE PROCESAMIENTO COMERCIAL CON LAMBDA
# ==========================================================================

class SistemaComercialLambda:
    """
    Sistema integral que demuestra la aplicación práctica y organizada de
    todas las operaciones con lambda aprendidas en el laboratorio:
    - Generación y formateo de códigos de orden con f-strings.
    - Estandarización de clientes con formatear_nombre_lambda.
    - Validación de clientes mediante operadores ternarios (mayoría de edad y saldo).
    - Transformación y procesamiento de listas de artículos en lote (recargos y descuentos).
    """

    def __init__(self, nombre_tienda: str, tasa_iva: float = 13.0):
        self.nombre_tienda = nombre_tienda
        self.tasa_iva = tasa_iva
        self.contador_ordenes = 0
        # Expresión lambda para generar códigos de factura únicos
        self.generar_id_factura = lambda num: f"FAC-{num:05d}"

    def procesar_orden(
        self,
        cliente_nombre: str,
        cliente_apellido: str,
        cliente_edad: int,
        saldo_disponible: float,
        articulos_precios: list[float],
        porcentaje_descuento: float = 0.0,
        porcentaje_recargo_pago: float = 0.0
    ) -> dict:
        """Procesa una transacción completa aplicando la suite de expresiones lambda."""
        self.contador_ordenes += 1
        id_factura = self.generar_id_factura(self.contador_ordenes)
        
        # 1. Formateo de nombres con lambda
        nombre_titular = formatear_nombre_lambda(cliente_nombre, cliente_apellido)
        
        # 2. Validación de edad con ternario
        es_adulto = es_mayor_edad(cliente_edad)
        categoria_edad = clasificar_mayoria_edad(cliente_edad)
        
        # Si no es mayor de edad, no puede celebrar contratos comerciales a plazos
        if not es_adulto and porcentaje_recargo_pago > 0:
            return {
                "id_factura": id_factura,
                "cliente": nombre_titular,
                "estado": "RECHAZADA",
                "motivo": f"El cliente es {categoria_edad} ({cliente_edad} años). Requiere tutor legal para compras a crédito."
            }

        # 3. Procesamiento en lote de los precios de los artículos
        # Aplicamos descuento unitario si aplica
        precios_con_descuento: list[float] = []
        for p in articulos_precios:
            p_desc = calcular_precio_descuento_lambda(p, porcentaje_descuento)
            precios_con_descuento.append(p_desc)
            
        subtotal_base = sum(precios_con_descuento)

        # Aplicamos recargo por método de pago si aplica (financiamiento)
        subtotal_con_recargo = aplicar_recargo_lambda(subtotal_base, porcentaje_recargo_pago)
        
        # Calculamos impuesto sobre el valor agregado (IVA)
        monto_iva = round(subtotal_con_recargo * (self.tasa_iva / 100), 2)
        total_a_pagar = round(subtotal_con_recargo + monto_iva, 2)

        # 4. Validación de fondos con operador ternario
        aprobada = es_transaccion_valida(saldo_disponible, total_a_pagar)
        mensaje_estado = validar_fondos(saldo_disponible, total_a_pagar)

        return {
            "id_factura": id_factura,
            "cliente": nombre_titular,
            "edad": cliente_edad,
            "categoria_edad": categoria_edad,
            "cant_articulos": len(articulos_precios),
            "subtotal_base": subtotal_base,
            "recargo_aplicado": round(subtotal_con_recargo - subtotal_base, 2),
            "iva": monto_iva,
            "total_a_pagar": total_a_pagar,
            "saldo_cliente": saldo_disponible,
            "saldo_restante": round(saldo_disponible - total_a_pagar, 2) if aprobada else saldo_disponible,
            "estado": "APROBADA" if aprobada else "RECHAZADA",
            "diagnostico": mensaje_estado
        }


def demostrar_caso_integral():
    """Simula una serie de órdenes comerciales para probar la clase integradora."""
    print("\n" + "=" * 75)
    print("SECCIÓN 4: CASO INTEGRAL (SISTEMA DE FACTURACIÓN Y PROCESAMIENTO CON LAMBDA)")
    print("=" * 75)
    sistema = SistemaComercialLambda(nombre_tienda="TechStore Central", tasa_iva=13.0)
    
    ordenes_a_procesar = [
        {
            "nombre": "  carlos alberto ",
            "apellido": " fuentes rivas",
            "edad": 28,
            "saldo": 300.0,
            "articulos": [35.0, 120.0, 45.50],
            "descuento": 10.0,  # 10% descuento
            "recargo": 5.0      # 5% recargo pago tarjeta
        },
        {
            "nombre": "sofia",
            "apellido": "navarro",
            "edad": 16,
            "saldo": 150.0,
            "articulos": [80.0, 25.0],
            "descuento": 0.0,
            "recargo": 10.0     # Intento de crédito siendo menor
        },
        {
            "nombre": "esteban",
            "apellido": "martinez",
            "edad": 45,
            "saldo": 50.0,
            "articulos": [120.0, 85.0],
            "descuento": 5.0,
            "recargo": 0.0      # Compra normal pero fondos insuficientes
        },
        {
            "nombre": "valeria andrea",
            "apellido": "castillo",
            "edad": 22,
            "saldo": 600.0,
            "articulos": [150.0, 210.0, 75.0],
            "descuento": 15.0,
            "recargo": 0.0
        }
    ]

    print("\n--- Ejecución de Órdenes Comerciales en Lote ---")
    for orden in ordenes_a_procesar:
        res = sistema.procesar_orden(
            cliente_nombre=orden["nombre"],
            cliente_apellido=orden["apellido"],
            cliente_edad=orden["edad"],
            saldo_disponible=orden["saldo"],
            articulos_precios=orden["articulos"],
            porcentaje_descuento=orden["descuento"],
            porcentaje_recargo_pago=orden["recargo"]
        )

        etiqueta_estado = "[APROBADA]" if res["estado"] == "APROBADA" else "[RECHAZADA]"
        print(f"\n{etiqueta_estado} Factura: {res['id_factura']} | Estado: {res['estado']}")
        print(f"   Cliente: {res['cliente']}")
        
        if res["estado"] == "APROBADA":
            print(f"   Artículos: {res['cant_articulos']} | Subtotal: ${res['subtotal_base']:.2f} | IVA (13%): ${res['iva']:.2f}")
            print(f"   Total Facturado: ${res['total_a_pagar']:.2f} | Saldo Restante: ${res['saldo_restante']:.2f}")
            print(f"   Diagnóstico: {res['diagnostico']}")
        else:
            motivo = res.get("motivo") or res.get("diagnostico")
            print(f"   Motivo de Rechazo: {motivo}")

    print("\n" + "=" * 75)
    print("FIN DE LA PRÁCTICA 5 - SIMPLIFICACIÓN Y OPERACIONES CON LAMBDA")
    print("=" * 75)


# ==========================================================================
# FUNCIÓN PRINCIPAL / ENTRY POINT
# ==========================================================================

def main():
    """Ejecuta todas las secciones de la práctica de forma secuencial."""
    repasar_fundamentos_cuaderno()
    demostrar_requerimiento_1()
    demostrar_requerimiento_2()
    demostrar_requerimiento_3()
    demostrar_caso_integral()


if __name__ == "__main__":
    main()
