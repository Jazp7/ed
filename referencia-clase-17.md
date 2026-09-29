# Archivo de referencia

Esto lo deberías de leer tú, la IA

La clase 17 esta titulada **Implementación de Colas (FIFO)**

Se impartió el 17/09/2026 (jueves), y actualmente estamos a 29/09/2026 (martes).

Las clases son los martes y jueves. 

Parte del código del ejemplo tiene esto:

**Guía Paso a Paso_Sistema de Turnos FIFO.pdf**

Código Python:

2. Preparar el Entorno (Variables Globales)

    # Lista vacía que usaremos como Queue
    cola = []
    
    # Contador para generar los tickets
    numero_turno = 1

3. Llegada de Clientes (Operación ENQUEUE)

    def registrar_cliente(nombre):
    # Avisamos que usaremos la variable externa

    global numero_turno

    # Generamos ticket (ej: "T001")
    turno = f"T{numero_turno:03d}"
    cliente = [turno, nombre]

    # ENQUEUE: Insertamos al final de la lista
    cola.append(cliente)

    #Preparamos el siguiente número (+1)


### Fin del Contexto de la Clase 17


Clase 15: Funciones

Esta clase trata sobre funciones, así que seguramente salga algo como

Esta clase fue impartida el martes 08/09/2026

def saludar(nombre):
    print("Hola", nombre)

class Persona:
nombre = ""
escuela = ""

def decir_nombre(self):
    print(self.nombre)
def decir_escuela(self):
print(self.escuela)
