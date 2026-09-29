pila = []

pila.append("Iniciar Sesión") # append() para agregar elemento

pila.append("consultar perfil")
pila.append("ver amigos en comun")
pila.append("Hola Khe Ase??")

print("pila actual:")
print(pila)

#Desapilar un elemento
accion = pila.pop()

print("\n Accion retirada")
print(accion)

print("\n penultima Accion retirada")
print(pila)