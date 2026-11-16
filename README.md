# Práctico: Algoritmos y Estructuras de Datos en Python

## Objetivos de aprendizaje

- Recorrer, filtrar y transformar **listas**, **listas paralelas** y **listas de listas (matrices)** mediante ciclos `for` y `while`.
- Modelar, validar, consultar y agregar información utilizando **diccionarios** y **listas de diccionarios**.
- Manipular rutas absolutas y relativas, leer y escribir **archivos de texto** (modos `"r"`, `"w"` y `"a"`) y procesar **archivos CSV**.

## Metodología: TDD (Test-Driven Development)

El flujo de trabajo es el siguiente:

1. **Lee el test** en `tests/`. Cada test tiene un docstring que describe el comportamiento esperado.
2. **Ejecuta los tests** y verifica que fallen.
3. **Implementa** la función en `ejercicios/` hasta que los tests pasen.
4. **No modifiques los tests**. Si un test falla, tu código es el que debe corregirse.

## Estructura del proyecto

```
aed-fundamentos-python/
├── ejercicios/                  # Tu código va acá (24 ejercicios por módulo)
│   ├── listas_ciclos.py         # Ciclos, listas simples, listas paralelas y matrices
│   ├── diccionarios.py          # Diccionarios y listas de diccionarios
│   └── archivos.py              # Rutas, archivos de texto (r/w/a) y archivos CSV
├── tests/                       # Tests que no debes modificar
│   ├── test_listas_ciclos.py
│   ├── test_diccionarios.py
│   ├── test_archivos.py
│   └── data/                    # Archivos de prueba (CSV y texto)
├── APUNTE.md
├── pytest.ini
└── README.md
```

## Setup

```bash
pip install pytest
```

## Ejecución

```bash
pytest
```

Para ejecutar solo un módulo:

```bash
pytest tests/test_listas_ciclos.py
pytest tests/test_diccionarios.py
pytest tests/test_archivos.py
```

## Progreso sugerido

- **Módulo 1 (`ejercicios/listas_ciclos.py`)**: Indexación, ciclos, listas simples, listas paralelas y matrices.
- **Módulo 2 (`ejercicios/diccionarios.py`)**: Modelado de registros con diccionarios, búsquedas, filtros y agregaciones sobre listas de diccionarios.
- **Módulo 3 (`ejercicios/archivos.py`)**: Rutas absolutas/relativas, archivos de texto con formato y lectura/escritura de archivos CSV.

## Normas del práctico

- No editen los archivos dentro de `tests/`.
- Los archivos en `ejercicios/` tienen stubs (funciones vacías con `pass`). Reemplazar `pass` por la implementación.
- Ante la duda sobre el comportamiento de un ejercicio, lean tanto el docstring de la función como el docstring del test correspondiente.
