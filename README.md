# Estructuras de Datos (ED) - Ciclo II / 2026

Este repositorio contiene los códigos, notas, ejercicios y tareas desarrolladas en la asignatura de **Estructuras de Datos**. El proyecto se encuentra organizado en cuadernos de trabajo temáticos, prácticas de laboratorio y tareas complementarias.

---

## 📂 Estructura General del Repositorio

```text
ED/
├── clases/
│   ├── cuaderno_de_trabajo_1/     # Fundamentos de Python y tipos primitivos
│   └── cuaderno_de_trabajo_2/     # Estructuras de datos, TADs y control de flujo
├── practicas-laboratorio/         # Guías y proyectos de laboratorio (1 a 6)
└── tareas/                        # Ejercicios asignados complementarios
```

---

## 📚 Contenido de las Clases

### 📘 Cuaderno de Trabajo No. 1: Fundamentos de Python

Abarca las clases iniciales de introducción al lenguaje, tipos primitivos y manipulación numérica:

* **[clase-3](file:///C:/Users/arist/Desktop/Ciclo%20II%20-%202026/ED/clases/cuaderno_de_trabajo_1/clase-3)**: Sintaxis básica, variables y salida por consola (`01-print.py`).
* **[clase-4](file:///C:/Users/arist/Desktop/Ciclo%20II%20-%202026/ED/clases/cuaderno_de_trabajo_1/clase-4)**: Tipos de datos en memoria (`sys.getsizeof`), enteros, flotantes, booleanos y cadenas formateadas (`02-tipos-datos.py`).
* **[clase-5](file:///C:/Users/arist/Desktop/Ciclo%20II%20-%202026/ED/clases/cuaderno_de_trabajo_1/clase-5)**: Operadores matemáticos, potencia, módulo e interacción por consola (`03-numeros.py`).

---

### 📗 Cuaderno de Trabajo No. 2: Estructuras de Datos y TADs

Contiene el estudio de las colecciones nativas de Python, estructuras lineales (Pilas y Colas), modularización y control de flujo:

| Clase | Tema Principal | Archivos Destacados |
| :--- | :--- | :--- |
| **[clase-7](file:///C:/Users/arist/Desktop/Ciclo%20II%20-%202026/ED/clases/cuaderno_de_trabajo_2/clase-7)** | **Listas y Slicing** | `listas.py`, `lista-ejercicio.py`, `indice.py` |
| **[clase-9](file:///C:/Users/arist/Desktop/Ciclo%20II%20-%202026/ED/clases/cuaderno_de_trabajo_2/clase-9)** | **Tuplas** | `tupla.py`, `Ejercicio1.py` (Servidor), `Ejercicio2.py` (Coordenadas) |
| **[clase-10](file:///C:/Users/arist/Desktop/Ciclo%20II%20-%202026/ED/clases/cuaderno_de_trabajo_2/clase-10)** | **Conjuntos (`Sets`)** | `set.py` (Mutabilidad y operaciones de conjuntos: $\cup, \cap, -, \Delta$) |
| **[clase-11](file:///C:/Users/arist/Desktop/Ciclo%20II%20-%202026/ED/clases/cuaderno_de_trabajo_2/clase-11)** | **Diccionarios** | `diccionario.py`, `ejemplo1.py`, `ejemplo2.py` |
| **[clase-12](file:///C:/Users/arist/Desktop/Ciclo%20II%20-%202026/ED/clases/cuaderno_de_trabajo_2/clase-12)** | **Pilas (Introducción)** | `clase.py` (Estructura LIFO mediante listas nativas) |
| **[clase-13](file:///C:/Users/arist/Desktop/Ciclo%20II%20-%202026/ED/clases/cuaderno_de_trabajo_2/clase-13)** | **Pilas (Operaciones)** | `pila.py` (`append`, `pop`, inspección de estados) |
| **[clase-15](file:///C:/Users/arist/Desktop/Ciclo%20II%20-%202026/ED/clases/cuaderno_de_trabajo_2/clase-15)** | **Funciones** | `funciones.py` (Declaración con `def`, parámetros y retornos) |
| **[clase-16](file:///C:/Users/arist/Desktop/Ciclo%20II%20-%202026/ED/clases/cuaderno_de_trabajo_2/clase-16)** | **Modularización de TADs** | `def.py` (`push`/`pop`), `pila.py`, `sistemadeaceleracion.py` |
| **[clase-18](file:///C:/Users/arist/Desktop/Ciclo%20II%20-%202026/ED/clases/cuaderno_de_trabajo_2/clase-18)** | **Control de Flujo** | `if-else.py`, `elif.py`, `for.py`, `for-range.py`, `while.py` |
| **[clase-19](file:///C:/Users/arist/Desktop/Ciclo%20II%20-%202026/ED/clases/cuaderno_de_trabajo_2/clase-19)** | **Colas (FIFO) y Simulación** | `cola.py`, `colaTienda.py`, `sistema-banco.py` (Menú de turnos) |
| **[clase-20](file:///C:/Users/arist/Desktop/Ciclo%20II%20-%202026/ED/clases/cuaderno_de_trabajo_2/clase-20)** | **Continuación Sistema de Banco** | `clase-20.md` (Desarrollo continuo de `sistema-banco.py`) |

---

## 🛠️ Instalación y Entorno de Ejecución

El proyecto gestiona dependencias y versiones de Python mediante [uv](https://docs.astral.sh/uv/) en la carpeta `clases/`.

### 1. Requisitos
* Python 3.13+
* [uv](https://docs.astral.sh/uv/) (Recomendado) o `python` estándar.

### 2. Ejecutar un archivo de clase

#### Opción A: Con `uv` (Recomendado)
Desde la carpeta `clases/`:
```bash
cd clases
uv run cuaderno_de_trabajo_2/clase-19/sistema-banco.py
```

#### Opción B: Con Python tradicional
Desde la raíz del repositorio:
```bash
python clases/cuaderno_de_trabajo_2/clase-19/sistema-banco.py
```
*(En Linux/macOS: `python3 clases/cuaderno_de_trabajo_2/clase-19/sistema-banco.py`)*

---

## 📋 Control de Versiones e Higiene del Repositorio

El archivo [.gitignore](file:///C:/Users/arist/Desktop/Ciclo%20II%20-%202026/ED/.gitignore) previene el rastreo de:
* Entornos virtuales (`.venv/`, `env/`).
* Archivos de caché (`__pycache__/`, `*.pyc`).
* Metadatos de linters y typecheckers (`.mypy_cache/`, `.pytest_cache/`).
* Archivos de respaldo temporal de editores (`*.un~`, `*~`, `.DS_Store`).
