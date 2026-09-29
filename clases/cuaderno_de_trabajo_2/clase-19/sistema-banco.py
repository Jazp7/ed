# Sistema de un banco
# Banco los manguitos

cola: list = [] # Cola vacía que será ocupada globalmente

numero_turno = 1 # Variable global para contabilizar los clientes

def registrar_cliente(nombre):
    global numero_turno

    # Generar el código de turno
    # T = Letra que significa turno
    # :03d mínimo de dígitos para rellenar son 3
    # Ejemplo: T001

    turno = f"T{numero_turno:03d}"
    cliente = [turno, nombre]
    cola.append(cliente)
    numero_turno += 1

    # Imprimamos resultado
    print("\nCliente registrado correctamente.")
    print("Turno asignado: ", turno)
    print("Cliente: ", nombre)

def ver_siguiente():
    if cola:
        siguiente = cola[0]
        print("Próximo Cliente: ")
        print("Turno del cliente: ", siguiente[0])
        print("Cliente siguiente: ", siguiente[1])
    else:
        print("\nNo hay clientes en espera.")


def atender_cliente():
    if cola:
        cliente = cola.pop(0)
        print(" --- Llamamos al cliente ---")
        print("Turno: ", cliente[0])
        print("Cliente: ", cliente[1])

    else:
        print("\nNo hay clientes que atender. =)")

def mostrar_cola():
    if not cola:
        print("No hay clientes esperando.")
    else:
        for cliente in cola:
            print(cliente[0], " - ", cliente[1])

        # Para saber cuantos clientes esperan
        print("\nCantidad de clientes que esperan: ", len(cola))

        # Para saber quién es el último cliente
        print("Último turno: ", cola[-1][0])


while True:
    # Vista de menú:
    print("\n")
    print(" Banco Los Manguitos")
    print(" -- Menú de Turnos --")
    print("1. Registrar clientes")
    print("2. Ver próximos clientes")
    print("3. Llamar al cliente")
    print("4. Mostrar todos los clientes")
    print("5. Salir")

    opcion = input("Seleccione una opción (número): ")

    if opcion == "1":
        nombre = input(" Ingrese su nombre: ")
        registrar_cliente(nombre)

    elif opcion == "2":
        ver_siguiente()

    elif opcion == "3":
        atender_cliente()

    elif opcion == "4":
        mostrar_cola()

    elif opcion == "5":
        print("\n Sistema finalizado")
        break

    else:
        print("\n La opción seleccionada no existe")
