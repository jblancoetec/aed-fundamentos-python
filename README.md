# Práctico: Fundamentos de Python

## Objetivos de aprendizaje

- Comprender y utilizar variables y tipos de datos primitivos.
- Aplicar estructuras de control condicionales para tomar decisiones.
- Definir funciones con argumentos, valores por defecto y retorno de resultados.
- Leer archivos de texto y CSV, y procesar su contenido con listas.

## Metodología: TDD (Test-Driven Development)

El flujo de trabajo es el siguiente:

1. **Lee el test** en `tests/`. Cada test tiene un docstring que describe el comportamiento esperado.
2. **Ejecuta los tests** y verifica que fallen.
3. **Implementa** la función en `ejercicios/` hasta que los tests pasen.
4. **No modifiques los tests**. Si un test falla, tu código es el que debe corregirse.

## Estructura del proyecto

```
fundamentos-python/
├── ejercicios/          # Tu código va acá
│   ├── variables.py
│   ├── condicionales.py
│   ├── funciones.py
│   └── archivos_listas.py
├── tests/               # Tests que no debes modificar
│   ├── test_variables.py
│   ├── test_condicionales.py
│   ├── test_funciones.py
│   ├── test_archivos_listas.py
│   └── data/            # Archivos de prueba (CSV y texto)
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
pytest tests/test_variables.py
pytest tests/test_condicionales.py
pytest tests/test_funciones.py
pytest tests/test_archivos_listas.py
```

## Progreso sugerido

- **Semana 1**: Variables y tipos de datos
- **Semana 2**: Condicionales
- **Semana 3+**: Funciones
- **Semana 4+**: Archivos y listas (Nivel 1 → Nivel 4, ver comentarios en `ejercicios/archivos_listas.py`)

## Normas del práctico

- No editen los archivos dentro de `tests/`.
- Los archivos en `ejercicios/` tienen stubs (funciones vacías). Reemplazar `pass` por la implementación.
- Ante la duda sobre el comportamiento de un test, lean el docstring del test.
- Los desafíos son opcionales pero recomendados.