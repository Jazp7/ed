def push(pila, elemento): #Creando una funcion llamada push()
    pila.append(elemento)


def pop(pila): #Creamos pop para retirar elementos
    return pila.pop()

#Creamos una pila vacia
pila = []
push(pila, "A")
push(pila, "B")
push(pila, "C")

print("Elementos de la pila: ", pila)

elemento = pop(pila)
print("El ultimo elemento es: ", elemento)