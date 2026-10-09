"""Soluciones de las actividades de árboles binarios de la práctica 8."""

from ejemplos import Nodo, buscar_valor, contar_nodos, postorden, preorden


def ejercicio_1_arbol_genealogico():
    print("Ejercicio 1: Árbol genealógico familiar")

    abuelo = Nodo("Roberto")
    abuelo.izq = Nodo("Carlos")
    abuelo.der = Nodo("Lucía")
    abuelo.izq.izq = Nodo("Mateo")
    abuelo.izq.der = Nodo("Sofía")
    abuelo.der.izq = Nodo("Diego")
    abuelo.der.der = Nodo("Valentina")

    print(f"Abuelo: {abuelo.valor}")
    print(f"Hijos: {abuelo.izq.valor} y {abuelo.der.valor}")
    print(
        f"Hijos de {abuelo.izq.valor}: "
        f"{abuelo.izq.izq.valor} y {abuelo.izq.der.valor}"
    )
    print(
        f"Hijos de {abuelo.der.valor}: "
        f"{abuelo.der.izq.valor} y {abuelo.der.der.valor}"
    )


def ejercicio_2_menu_decisiones():
    print("\nEjercicio 2: Menú interactivo de decisiones")

    raiz = Nodo("¿El equipo puede conectarse a Internet?")
    raiz.izq = Nodo("Sí: comprobar la velocidad de conexión")
    raiz.der = Nodo("No: reiniciar el módem o router")
    raiz.izq.izq = Nodo("Conexión estable: cerrar el caso")
    raiz.izq.der = Nodo("Conexión lenta: revisar la señal Wi-Fi")
    raiz.der.izq = Nodo("Conexión restablecida: cerrar el caso")
    raiz.der.der = Nodo("Sin conexión: contactar al proveedor")

    print("Recorrido en preorden (evaluación desde la raíz):")
    preorden(raiz)
    print("\nRecorrido en postorden (cierre desde las hojas):")
    postorden(raiz)
    print()


def contar_hojas(nodo):
    if nodo is None:
        return 0
    if nodo.izq is None and nodo.der is None:
        return 1
    return contar_hojas(nodo.izq) + contar_hojas(nodo.der)


def es_hoja_con_valor(nodo, valor):
    if nodo is None:
        return False
    if nodo.valor == valor:
        return nodo.izq is None and nodo.der is None
    return es_hoja_con_valor(nodo.izq, valor) or es_hoja_con_valor(
        nodo.der, valor
    )


def ejercicio_3_auditoria_carpetas():
    print("\nEjercicio 3: Reporte de auditoría de carpetas")

    raiz = Nodo("Sistema")
    raiz.izq = Nodo("Documentos")
    raiz.der = Nodo("Multimedia")
    raiz.izq.izq = Nodo("Personal")
    raiz.izq.der = Nodo("Estudios")
    raiz.der.izq = Nodo("Fotos")
    raiz.der.der = Nodo("Musica")
    raiz.izq.izq.izq = Nodo("identidad.pdf")
    raiz.izq.izq.der = Nodo("curriculum.pdf")
    raiz.izq.der.izq = Nodo("notas.txt")
    raiz.izq.der.der = Nodo("trabajos.pdf")
    raiz.der.izq.izq = Nodo("vacaciones.jpg")
    raiz.der.izq.der = Nodo("familia.jpg")
    raiz.der.der.izq = Nodo("lista.m3u")
    raiz.der.der.der = Nodo("cancion.mp3")

    print(f"Total de carpetas y archivos: {contar_nodos(raiz)}")
    print(f"Total de archivos finales (hojas): {contar_hojas(raiz)}")

    nombre_archivo = input("Ingrese el nombre del archivo que desea buscar: ").strip()
    if not nombre_archivo:
        print("Error: el nombre del archivo no puede estar vacío.")
    elif buscar_valor(raiz, nombre_archivo) and es_hoja_con_valor(
        raiz, nombre_archivo
    ):
        print(f"El archivo '{nombre_archivo}' existe en la estructura.")
    elif buscar_valor(raiz, nombre_archivo):
        print(f"'{nombre_archivo}' existe en la estructura, pero es una carpeta.")
    else:
        print(f"El archivo '{nombre_archivo}' no existe en la estructura.")


def main():
    ejercicio_1_arbol_genealogico()
    ejercicio_2_menu_decisiones()
    ejercicio_3_auditoria_carpetas()


if __name__ == "__main__":
    main()
