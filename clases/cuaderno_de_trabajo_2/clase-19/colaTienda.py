colaTienda = [] # Creamos una cola vacía porque
# Esta iniciando a abrir la tienda

# Operación ENQUEUE
# Tienda Rosita
colaTienda.append("Ana")
colaTienda.append("Carlos")
colaTienda.append("Luis")

print("Clientes de la tienda:", colaTienda)

# Operación Peek
# Consultar quien es el primer cliente
print("Siguiente cliente: ", colaTienda[0])

# Operación SIZE
# Consulta cuantos clientes hay
print("Clientes en espera: ", len(colaTienda))

# Operación DEQUEUE
# Atender el primer cliente
cliente = colaTienda.pop(0)
print("Cliente atendido", cliente)

# Mostrar los clientes que siguen:
print("Los clientes de la cola son: ", colaTienda)

# Operación REAR
# Consultar quién esta al final
print("El último cliente: ", colaTienda[-1])

# Test: hacer operación DEQUEUE
# Probar operación IS EMPTY
colaTienda.pop()
colaTienda.pop()

# Operación IS EMPTY
# Comprueba si todavía hay elementos (clientes)
if not colaTienda:
    print("No hay clientes esperando")
else:
    print("Todavía hay clientes esperando")
