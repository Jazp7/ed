# ==========================================================================
# SOLUCIÓN DE CASOS DE USO REALES CON PATRONES ESTRUCTURALES
# ==========================================================================

print("=" * 60)
print("CASO 1: SISTEMA DE HISTORIAL (PATRÓN LIFO)")
print("=" * 60)

# --------------------------------------------------------------------------
# JUSTIFICACIÓN DEL PATRÓN LIFO (Last In, First Out)
# --------------------------------------------------------------------------
# Se eligió LIFO porque el problema requiere un comportamiento de "pila":
# la última acción realizada debe ser la primera en revertirse.
# Una lista de Python funciona perfectamente como pila usando append() y pop().
# Esto simula el botón "Deshacer" (Undo) de cualquier editor de texto.
# --------------------------------------------------------------------------

class EditorTextoSimple:
    def __init__(self):
        self.contenido = ""
        self.historial = []  # Pila LIFO para almacenar estados anteriores

    def escribir(self, texto):
        """Guarda el estado actual antes de modificarlo (Push a la pila)"""
        self.historial.append(self.contenido) 
        self.contenido += texto
        print(f"✍️  Escrito: '{texto}' | Contenido actual: '{self.contenido}'")

    def deshacer(self):
        """Recupera el último estado guardado (Pop de la pila - LIFO)"""
        if not self.historial:
            print("⚠️  No hay más acciones para deshacer.")
            return
        
        ultimo_estado = self.historial.pop()  # Saca el ÚLTIMO elemento ingresado
        self.contenido = ultimo_estado
        print(f"↩️  Deshecho. Contenido restaurado: '{self.contenido}'")

# --- Prueba del Caso 1 ---
editor = EditorTextoSimple()
editor.escribir("Hola ")
editor.escribir("Mundo")
editor.escribir(" cruel")
editor.deshacer()  # Debe eliminar " cruel" (el último en entrar)
editor.deshacer()  # Debe eliminar "Mundo"


print("\n" + "=" * 60)
print("CASO 2: VALIDADOR DE ACCESO POR ROLES (ÁLGEBRA DE SETS)")
print("=" * 60)

# --------------------------------------------------------------------------
# JUSTIFICACIÓN DEL ÁLGEBRA DE SETS
# --------------------------------------------------------------------------
# Se eligieron Sets porque necesitamos verificar pertenencia y unicidad.
# Los roles de usuario no se repiten y el orden no importa.
# Usamos la INTERSECCIÓN (&) para validar si el usuario tiene AL MENOS
# uno de los roles permitidos. Esto es mucho más eficiente (O(1)) que 
# buscar en una lista, especialmente con muchos permisos.
# --------------------------------------------------------------------------

def verificar_acceso(usuario_roles: set, ruta_requerida: str):
    """
    Valida si un usuario puede acceder a una ruta basándose en sus roles.
    Usa álgebra de sets para encontrar coincidencias.
    """
    
    # Base de datos de permisos (Set de tuplas o diccionario de sets)
    PERMISOS_SISTEMA = {
        "/admin/dashboard": {"admin", "superuser"},
        "/perfil/editar":    {"admin", "editor", "usuario"},
        "/reportes/ver":     {"analista", "admin"},
        "/publico/info":     {"invitado", "usuario", "admin", "editor", "analista"}
    }

    if ruta_requerida not in PERMISOS_SISTEMA:
        return f"❌ Ruta '{ruta_requerida}' no existe."

    roles_permitidos = PERMISOS_SISTEMA[ruta_requerida]
    
    # OPERACIÓN CLAVE: Intersección de Sets
    # Devuelve los elementos comunes entre los roles del usuario y los permitidos
    roles_validos = usuario_roles & roles_permitidos 

    if roles_validos:
        return (f"✅ ACCESO CONCEDIDO a '{ruta_requerida}'. "
                f"Role(s) válido(s): {roles_validos}")
    else:
        return (f" ACCESO DENEGADO a '{ruta_requerida}'. "
                f"Roles del usuario: {usuario_roles} | Requeridos: {roles_permitidos}")

# --- Prueba del Caso 2 ---
usuario_a = {"editor", "usuario"}
usuario_b = {"invitado"}
usuario_c = {"admin"}

print(verificar_acceso(usuario_a, "/perfil/editar")) # Debe conceder (tiene 'editor' y 'usuario')
print(verificar_acceso(usuario_b, "/reportes/ver"))   # Debe denegar (no tiene 'analista' ni 'admin')
print(verificar_acceso(usuario_c, "/admin/dashboard"))# Debe conceder (tiene 'admin')
print(verificar_acceso(usuario_a, "/admin/dashboard"))# Debe denegar (no tiene 'admin' ni 'superuser')