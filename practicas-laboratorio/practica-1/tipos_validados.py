# tipos_validados.py
# Cada clase representa un tipo de dato con reglas propias.
# La validación ocurre en __init__ para evitar que existan objetos inválidos.


# ──────────────────────────────────────────────
# 1. EmailValido
# Regla: debe contener exactamente un "@" y tener dominio con "."
# Evita: direcciones sin @, sin dominio o con múltiples arrobas
# ─────────────────────────────────────────────
class EmailValido:
    def __init__(self, valor: str):
        if not isinstance(valor, str) or "@" not in valor:
            raise ValueError("El email debe ser una cadena y contener '@'.")
        partes = valor.split("@")
        if len(partes) != 2 or not partes[0] or "." not in partes[1]:
            raise ValueError("Formato de email inválido: falta usuario o dominio válido.")
        self.valor = valor

    def __repr__(self):
        return f"EmailValido('{self.valor}')"


# ──────────────────────────────────────────────
# 2. EdadValida
# Regla: debe ser un entero entre 0 y 150
# Evita: edades negativas, decimales o mayores a 150 años
# ──────────────────────────────────────────────
class EdadValida:
    def __init__(self, valor: int):
        if not isinstance(valor, int) or isinstance(valor, bool):
            raise TypeError("La edad debe ser un número entero.")
        if valor < 0 or valor > 150:
            raise ValueError("La edad debe estar entre 0 y 150 años.")
        self.valor = valor

    def __repr__(self):
        return f"EdadValida({self.valor})"


# ──────────────────────────────────────────────
# 3. TelefonoMexicano
# Regla: debe tener exactamente 10 dígitos (formato mexicano)
# Evita: números con letras, menos/más de 10 dígitos o caracteres especiales
# ─────────────────────────────────────────────
class TelefonoMexicano:
    def __init__(self, valor: str):
        digitos = valor.replace(" ", "").replace("-", "")
        if not digitos.isdigit() or len(digitos) != 10:
            raise ValueError(
                "El teléfono debe contener exactamente 10 dígitos numéricos."
            )
        self.valor = digitos

    def __repr__(self):
        return f"TelefonoMexicano('{self.valor}')"


# ──────────────────────────────────────────────
# 4. Porcentaje
# Regla: debe ser un número (int/float) entre 0 y 100
# Evita: valores fuera del rango porcentual o tipos no numéricos
# ──────────────────────────────────────────────
class Porcentaje:
    def __init__(self, valor: float):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise TypeError("El porcentaje debe ser un número.")
        if valor < 0 or valor > 100:
            raise ValueError("El porcentaje debe estar entre 0 y 100.")
        self.valor = float(valor)

    def __repr__(self):
        return f"Porcentaje({self.valor}%)"


# ──────────────────────────────────────────────
# 5. ClaveSegura
# Regla: mínimo 8 caracteres, al menos 1 mayúscula, 1 minúscula y 1 dígito
# Evita: contraseñas débiles, cortas o sin variedad de caracteres
# ──────────────────────────────────────────────
class ClaveSegura:
    def __init__(self, valor: str):
        if not isinstance(valor, str):
            raise TypeError("La clave debe ser una cadena de texto.")
        if len(valor) < 8:
            raise ValueError("La clave debe tener al menos 8 caracteres.")
        if not any(c.isupper() for c in valor):
            raise ValueError("La clave debe contener al menos una letra mayúscula.")
        if not any(c.islower() for c in valor):
            raise ValueError("La clave debe contener al menos una letra minúscula.")
        if not any(c.isdigit() for c in valor):
            raise ValueError("La clave debe contener al menos un dígito.")
        self.valor = valor

    def __repr__(self):
        return f"ClaveSegura('{'*' * len(self.valor)}')"


# ══════════════════════════════════════════════
# EJEMPLOS DE USO: caso válido e inválido por clase
# ══════════════════════════════════════════════

if __name__ == "__main__":

    # --- EmailValido ---
    try:
        correo_ok = EmailValido("usuario@dominio.com")
        print(f"✓ {correo_ok}")
    except (ValueError, TypeError) as e:
        print(f"✗ {e}")

    try:
        correo_mal = EmailValido("sin-arroba-dominio")
        print(f"✓ {correo_mal}")
    except (ValueError, TypeError) as e:
        print(f"✗ {e}")  # Rechazado: no contiene "@"

    # --- EdadValida ---
    try:
        edad_ok = EdadValida(25)
        print(f"✓ {edad_ok}")
    except (ValueError, TypeError) as e:
        print(f" {e}")

    try:
        edad_mal = EdadValida(-5)
        print(f"✓ {edad_mal}")
    except (ValueError, TypeError) as e:
        print(f"✗ {e}")  # Rechazado: edad negativa

    # --- TelefonoMexicano ---
    try:
        tel_ok = TelefonoMexicano("55-1234-5678")
        print(f"✓ {tel_ok}")
    except (ValueError, TypeError) as e:
        print(f"✗ {e}")

    try:
        tel_mal = TelefonoMexicano("123")
        print(f"✓ {tel_mal}")
    except (ValueError, TypeError) as e:
        print(f"✗ {e}")  # Rechazado: solo 3 dígitos

    # --- Porcentaje ---
    try:
        pct_ok = Porcentaje(75.5)
        print(f"✓ {pct_ok}")
    except (ValueError, TypeError) as e:
        print(f"✗ {e}")

    try:
        pct_mal = Porcentaje(150)
        print(f"✓ {pct_mal}")
    except (ValueError, TypeError) as e:
        print(f"✗ {e}")  # Rechazado: mayor a 100

    # --- ClaveSegura ---
    try:
        clave_ok = ClaveSegura("MiClave1")
        print(f"✓ {clave_ok}")
    except (ValueError, TypeError) as e:
        print(f"✗ {e}")

    try:
        clave_mal = ClaveSegura("debil")
        print(f"✓ {clave_mal}")
    except (ValueError, TypeError) as e:
        print(f"✗ {e}")  # Rechazado: muy corta y sin mayúsculas/dígitos