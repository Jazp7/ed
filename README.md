# Estructuras de Datos (ED)

Este repositorio contiene los códigos, ejercicios y tareas desarrollados en la asignatura de Estructuras de Datos.

---

## Contenido de las clases

- **clase-3**: Ejercicios y códigos correspondientes a la clase 3.
- **clase-4**: Ejercicios y códigos correspondientes a la clase 4.

---

## Estructura del proyecto

Cada clase se organiza como un proyecto independiente para seguir las buenas prácticas de aislamiento de dependencias y entornos. Dentro de la carpeta de cada clase encontrarás:

- Archivos `.py` - Código fuente de la clase.
- `pyproject.toml` - Definición del proyecto y dependencias manejadas con **uv**.
- `uv.lock` - Control de versiones exactas de las dependencias.
- `.python-version` - Versión de Python especificada para el entorno.

---

## Uso de `.gitignore`

Se incluye un archivo `.gitignore` en la raíz del repositorio para evitar subir el entorno virtual (`.venv/`), archivos de caché de Python (`__pycache__/`), verificadores de tipos (`.mypy_cache/`) y otros archivos temporales. Esto ayuda a mantener el repositorio liviano y evita subir archivos pesados e innecesarios al servidor remoto de GitHub.

---

## Instalación y ejecución

Debido a que los entornos virtuales (`.venv/`) no se incluyen en el repositorio, se deben instalar o sincronizar las dependencias localmente en cada clase.

> ℹ️ **Nota sobre `uv`:** Para utilizar los comandos `uv sync` y `uv run`, se debe tener instalado **uv** en el sistema. Puedes consultar las instrucciones de instalación en el sitio oficial de [docs.astral.sh/uv](https://docs.astral.sh/uv/).

### Pasos para ejecutar una clase:

1. **Navegar a la carpeta de la clase:**
   ```bash
   cd clase-3
   ```

2. **Instalar / sincronizar dependencias:**
   Si utilizas **uv** (recomendado):
   ```bash
   uv sync
   ```
   Si utilizas `pip` tradicional con un entorno virtual:
   ```bash
   python -m venv .venv
   # En Windows: .venv\Scripts\activate
   # En Linux/macOS: source .venv/bin/activate
   ```

3. **Ejecución del código:**
   - **Utilizando `uv` (Recomendado):**
     ```bash
     uv run 01-print.py
     ```
   - **Utilizando Python estándar:**
     ```bash
     python 01-print.py
     ```
     o en Linux/macOS:
     ```bash
     python3 01-print.py
     ```
