"""
Tests para el modulo de Lectura de archivos y tratamiento con listas.

Cada test tiene un docstring que describe el comportamiento esperado.
El alumno debe leer el test, entender que pide y luego implementar
la funcion en ejercicios/archivos_listas.py hasta que el test pase.

Los datos de prueba viven en tests/data/ y se acceden por nombre:
    - una_linea.csv: CSV con encabezado + 1 fila de datos.
    - varios.csv:    CSV con encabezado + 5 filas de datos.
    - notas.csv:     CSV con encabezado + 5 filas (columna numerica).
    - frases.txt:    Archivo de texto plano con 3 lineas.
"""

import os
import sys

sys.path.insert(0, "../ejercicios")

from ejercicios.archivos_listas import (
    leer_primera_linea,
    leer_lineas,
    contar_lineas,
    leer_csv_primera_fila,
    leer_csv_primera_fila_como_dict,
    leer_csv_como_matriz,
    leer_csv_como_lista_diccionarios,
    obtener_columna_csv,
    filtrar_csv_por_columna,
    contar_coincidencias_csv,
    buscar_registro_por_patron,
    sumar_columna_numerica_csv,
    promedio_columna_numerica_csv,
    maximo_columna_numerica_csv,
)


DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


def ruta(nombre):
    return os.path.join(DATA_DIR, nombre)


# ---------------------------------------------------------------------------
# Nivel 1: Lectura basica de archivos de texto plano
# ---------------------------------------------------------------------------


class TestLeerPrimeraLinea:
    def test_retorna_primera_linea_sin_salto(self):
        """Debe retornar 'Hola mundo' (sin '\\n') como primera linea de frases.txt."""
        assert leer_primera_linea(ruta("frases.txt")) == "Hola mundo"

    def test_no_retorna_linea_vacia_al_final(self):
        """El resultado no debe terminar en '\\n' aunque el archivo si lo tenga."""
        resultado = leer_primera_linea(ruta("frases.txt"))
        assert not resultado.endswith("\n")


class TestLeerLineas:
    def test_retorna_tres_lineas(self):
        """frases.txt tiene 3 lineas, debe retornar una lista de 3 elementos."""
        resultado = leer_lineas(ruta("frases.txt"))
        assert resultado == ["Hola mundo", "Python es genial", "Aprender a programar"]

    def test_lineas_no_tienen_salto_final(self):
        """Cada elemento de la lista retornada no debe terminar en '\\n'."""
        resultado = leer_lineas(ruta("frases.txt"))
        for linea in resultado:
            assert not linea.endswith("\n")

    def test_orden_correcto(self):
        """La primera linea retornada debe ser 'Hola mundo' y la tercera 'Aprender a programar'."""
        resultado = leer_lineas(ruta("frases.txt"))
        assert resultado[0] == "Hola mundo"
        assert resultado[-1] == "Aprender a programar"


class TestContarLineas:
    def test_frases_tiene_tres_lineas(self):
        """frases.txt tiene exactamente 3 lineas."""
        assert contar_lineas(ruta("frases.txt")) == 3

    def test_csv_varios_tiene_seis_lineas(self):
        """varios.csv tiene 1 encabezado + 5 filas = 6 lineas."""
        assert contar_lineas(ruta("varios.csv")) == 6

    def test_csv_una_linea_tiene_dos_lineas(self):
        """una_linea.csv tiene 1 encabezado + 1 fila = 2 lineas."""
        assert contar_lineas(ruta("una_linea.csv")) == 2


# ---------------------------------------------------------------------------
# Nivel 2: CSV con un solo registro
# ---------------------------------------------------------------------------


class TestLeerCsvPrimeraFila:
    def test_retorna_lista_de_campos(self):
        """Debe retornar ['Juan', '30', 'Córdoba'] para una_linea.csv."""
        assert leer_csv_primera_fila(ruta("una_linea.csv")) == ["Juan", "30", "Córdoba"]

    def test_no_incluye_encabezado(self):
        """El primer elemento retornado debe ser un dato ('Juan'), no un encabezado ('nombre')."""
        resultado = leer_csv_primera_fila(ruta("una_linea.csv"))
        assert "nombre" not in resultado
        assert resultado[0] == "Juan"


class TestLeerCsvPrimeraFilaComoDict:
    def test_retorna_diccionario_con_campos(self):
        """Debe retornar {'nombre': 'Juan', 'edad': '30', 'ciudad': 'Córdoba'}."""
        resultado = leer_csv_primera_fila_como_dict(ruta("una_linea.csv"))
        assert resultado == {"nombre": "Juan", "edad": "30", "ciudad": "Córdoba"}

    def test_claves_son_los_encabezados(self):
        """Las claves del dict deben coincidir con la primera linea (encabezado)."""
        resultado = leer_csv_primera_fila_como_dict(ruta("una_linea.csv"))
        assert set(resultado.keys()) == {"nombre", "edad", "ciudad"}


# ---------------------------------------------------------------------------
# Nivel 3: CSV con varios registros
# ---------------------------------------------------------------------------


class TestLeerCsvComoMatriz:
    def test_matriz_incluye_encabezado(self):
        """La primera sublista debe ser ['nombre', 'edad', 'ciudad']."""
        resultado = leer_csv_como_matriz(ruta("varios.csv"))
        assert resultado[0] == ["nombre", "edad", "ciudad"]

    def test_matriz_tiene_seis_filas(self):
        """varios.csv: 1 encabezado + 5 datos = 6 filas en la matriz."""
        resultado = leer_csv_como_matriz(ruta("varios.csv"))
        assert len(resultado) == 6

    def test_primera_fila_datos(self):
        """La segunda sublista (primera fila de datos) debe ser ['Ana', '25', 'Rosario']."""
        resultado = leer_csv_como_matriz(ruta("varios.csv"))
        assert resultado[1] == ["Ana", "25", "Rosario"]

    def test_ultima_fila_datos(self):
        """La ultima sublista debe ser ['Sofia', '28', 'BsAs']."""
        resultado = leer_csv_como_matriz(ruta("varios.csv"))
        assert resultado[-1] == ["Sofia", "28", "BsAs"]


class TestLeerCsvComoListaDiccionarios:
    def test_cantidad_de_registros(self):
        """varios.csv tiene 5 filas de datos -> 5 diccionarios."""
        resultado = leer_csv_como_lista_diccionarios(ruta("varios.csv"))
        assert len(resultado) == 5

    def test_primer_registro_completo(self):
        """El primer dict debe corresponder a Ana de Rosario."""
        resultado = leer_csv_como_lista_diccionarios(ruta("varios.csv"))
        assert resultado[0] == {"nombre": "Ana", "edad": "25", "ciudad": "Rosario"}

    def test_ultimo_registro_completo(self):
        """El ultimo dict debe corresponder a Sofia de BsAs."""
        resultado = leer_csv_como_lista_diccionarios(ruta("varios.csv"))
        assert resultado[-1] == {"nombre": "Sofia", "edad": "28", "ciudad": "BsAs"}

    def test_todos_los_registros_tienen_mismas_claves(self):
        """Todos los diccionarios deben tener las mismas claves (las del encabezado)."""
        resultado = leer_csv_como_lista_diccionarios(ruta("varios.csv"))
        claves_esperadas = {"nombre", "edad", "ciudad"}
        for registro in resultado:
            assert set(registro.keys()) == claves_esperadas


class TestObtenerColumnaCsv:
    def test_columna_nombres(self):
        """La columna 0 (nombre) debe ser ['Ana', 'Pedro', 'Maria', 'Luis', 'Sofia']."""
        assert obtener_columna_csv(ruta("varios.csv"), 0) == [
            "Ana", "Pedro", "Maria", "Luis", "Sofia"
        ]

    def test_columna_ciudades(self):
        """La columna 2 (ciudad) debe incluir Rosario, Mendoza, Salta, Córdoba y BsAs en orden."""
        assert obtener_columna_csv(ruta("varios.csv"), 2) == [
            "Rosario", "Mendoza", "Salta", "Córdoba", "BsAs"
        ]

    def test_excluye_encabezado(self):
        """El primer valor retornado no debe ser 'nombre' (encabezado de la columna 0)."""
        assert obtener_columna_csv(ruta("varios.csv"), 0)[0] != "nombre"


# ---------------------------------------------------------------------------
# Nivel 4: Filtros, busquedas y agregaciones
# ---------------------------------------------------------------------------


class TestFiltrarCsvPorColumna:
    def test_filtro_una_coincidencia(self):
        """Filtrar varios.csv por ciudad == 'Córdoba' debe retornar solo el registro de Luis."""
        resultado = filtrar_csv_por_columna(ruta("varios.csv"), 2, "Córdoba")
        assert resultado == [{"nombre": "Luis", "edad": "35", "ciudad": "Córdoba"}]

    def test_filtro_sin_coincidencias(self):
        """Filtrar por una ciudad inexistente debe retornar lista vacia."""
        resultado = filtrar_csv_por_columna(ruta("varios.csv"), 2, "Mar del Plata")
        assert resultado == []

    def test_filtro_devuelve_lista_de_dicts(self):
        """El resultado del filtro debe ser una lista de diccionarios (mismo formato que el archivo completo)."""
        resultado = filtrar_csv_por_columna(ruta("varios.csv"), 2, "Rosario")
        assert isinstance(resultado, list)
        assert len(resultado) == 1
        assert isinstance(resultado[0], dict)
        assert set(resultado[0].keys()) == {"nombre", "edad", "ciudad"}


class TestContarCoincidenciasCsv:
    def test_ciudad_cordoba_aparece_una_vez(self):
        """Solo Luis vive en Córdoba -> debe contar 1."""
        assert contar_coincidencias_csv(ruta("varios.csv"), 2, "Córdoba") == 1

    def test_ciudad_inexistente_cero(self):
        """Una ciudad que no esta en el archivo debe contar 0."""
        assert contar_coincidencias_csv(ruta("varios.csv"), 2, "Ushuaia") == 0


class TestBuscarRegistroPorPatron:
    def test_patron_subcadena_en_nombre(self):
        """El patron 'Mar' debe encontrar el registro de Maria (Maria contiene 'Mar')."""
        resultado = buscar_registro_por_patron(ruta("varios.csv"), 0, "Mar")
        assert resultado == {"nombre": "Maria", "edad": "22", "ciudad": "Salta"}

    def test_patron_sin_coincidencias_retorna_none(self):
        """Si ningun nombre contiene 'Z', debe retornar None."""
        resultado = buscar_registro_por_patron(ruta("varios.csv"), 0, "Z")
        assert resultado is None

    def test_patron_puede_ser_nombre_completo(self):
        """Pasar 'Pedro' como patron debe encontrar a Pedro (Pedro contiene 'Pedro')."""
        resultado = buscar_registro_por_patron(ruta("varios.csv"), 0, "Pedro")
        assert resultado == {"nombre": "Pedro", "edad": "40", "ciudad": "Mendoza"}


class TestSumarColumnaNumericaCsv:
    def test_suma_de_notas(self):
        """8.5 + 6.0 + 9.5 + 4.5 + 7.0 = 35.5."""
        assert sumar_columna_numerica_csv(ruta("notas.csv"), 2) == 35.5

    def test_suma_de_edades(self):
        """25 + 40 + 22 + 35 + 28 = 150 (columna edad en varios.csv)."""
        assert sumar_columna_numerica_csv(ruta("varios.csv"), 1) == 150.0


class TestPromedioColumnaNumericaCsv:
    def test_promedio_de_notas(self):
        """Promedio de [8.5, 6.0, 9.5, 4.5, 7.0] = 7.1."""
        assert promedio_columna_numerica_csv(ruta("notas.csv"), 2) == 7.1

    def test_promedio_redondeado_a_dos_decimales(self):
        """El resultado debe estar redondeado a 2 decimales."""
        resultado = promedio_columna_numerica_csv(ruta("notas.csv"), 2)
        assert round(resultado, 2) == resultado


class TestMaximoColumnaNumericaCsv:
    def test_maximo_de_notas(self):
        """La nota maxima en notas.csv es 9.5 (Maria)."""
        assert maximo_columna_numerica_csv(ruta("notas.csv"), 2) == 9.5

    def test_maximo_de_edades(self):
        """La edad maxima en varios.csv es 40 (Pedro)."""
        assert maximo_columna_numerica_csv(ruta("varios.csv"), 1) == 40.0
