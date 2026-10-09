# Ejemplos de nodos, recorridos y operaciones en árboles binarios.


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None


def preorden(nodo):
    if nodo is not None:
        print(nodo.valor, end=" ")
        preorden(nodo.izq)
        preorden(nodo.der)


def inorden(nodo):
    if nodo is not None:
        inorden(nodo.izq)
        print(nodo.valor, end=" ")
        inorden(nodo.der)


def postorden(nodo):
    if nodo is not None:
        postorden(nodo.izq)
        postorden(nodo.der)
        print(nodo.valor, end=" ")


def contar_nodos(nodo):
    if nodo is None:
        return 0
    return 1 + contar_nodos(nodo.izq) + contar_nodos(nodo.der)


def buscar_valor(nodo, objetivo):
    if nodo is None:
        return False
    if nodo.valor == objetivo:
        return True
    return buscar_valor(nodo.izq, objetivo) or buscar_valor(nodo.der, objetivo)


def mostrar_ejemplos():
    raiz = Nodo("A")
    raiz.izq = Nodo("B")
    raiz.der = Nodo("C")
    raiz.izq.izq = Nodo("D")
    raiz.izq.der = Nodo("E")

    print("Construcción manual del árbol:")
    print(raiz.valor)
    print(raiz.izq.valor, raiz.der.valor)
    print(raiz.izq.izq.valor, raiz.izq.der.valor)

    print("\nRecorridos:")
    print("Preorden:", end=" ")
    preorden(raiz)
    print()
    print("Inorden:", end=" ")
    inorden(raiz)
    print()
    print("Postorden:", end=" ")
    postorden(raiz)
    print()

    print(f"\nCantidad de nodos: {contar_nodos(raiz)}")
    print(f"¿Está el valor E?: {buscar_valor(raiz, 'E')}")
    print(f"¿Está el valor Z?: {buscar_valor(raiz, 'Z')}")


if __name__ == "__main__":
    mostrar_ejemplos()
