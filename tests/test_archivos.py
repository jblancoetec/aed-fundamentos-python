"""
Tests para el módulo de Rutas, archivos de texto y archivos CSV.

Cada test tiene un docstring que describe el comportamiento esperado.
El alumno debe leer el test, entender qué pide y luego implementar
la función en ejercicios/archivos.py hasta que el test pase.
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, "../ejercicios")

from ejercicios.archivos import (
    clasificar_y_descomponer_ruta,
    obtener_ruta_relativa,
    construir_ruta_absoluta,
    leer_mensaje_multilinea,
    leer_cumpleanios_alternados,
    leer_alarmas_alternadas,
    registrar_medicion_meteorologica,
    registrar_compra_en_archivo,
    sobrescribir_resumen_ventas,
    formatear_asistencia_csv,
    formatear_materias_csv,
    formatear_horarios_trabajo_csv,
    formatear_agenda_csv,
    leer_csv_como_matriz,
    leer_csv_como_diccionarios,
    filtrar_csv_por_rango_numerico,
    buscar_registros_por_patron_csv,
    estadisticas_columna_csv,
    calcular_asistencia_curso_csv,
    agrupar_csv_por_columna,
    exportar_diccionarios_a_csv,
    actualizar_stock_csv,
    generar_reporte_aprobados_csv,
    consolidar_archivos_csv,
)


DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


def ruta(nombre):
    return os.path.join(DATA_DIR, nombre)


# ---------------------------------------------------------------------------
# Sección 1: Rutas de archivos (absolutas y relativas)
# ---------------------------------------------------------------------------


class TestClasificarYDescomponerRuta:
    def test_ruta_absoluta_con_carpetas(self):
        """Descompone '/home/etec/Documentos/TIC-80/JuegoPollito.tic'."""
        assert clasificar_y_descomponer_ruta(
            "/home/etec/Documentos/TIC-80/JuegoPollito.tic"
        ) == {
            "es_absoluta": True,
            "carpetas": "/home/etec/Documentos/TIC-80",
            "archivo": "JuegoPollito.tic",
            "extension": "tic",
        }

    def test_ruta_relativa_con_y_sin_subcarpeta(self):
        """Descompone 'Fotos/Bosque.png' y 'Resumen.txt'."""
        assert clasificar_y_descomponer_ruta("Fotos/Bosque.png") == {
            "es_absoluta": False,
            "carpetas": "Fotos",
            "archivo": "Bosque.png",
            "extension": "png",
        }
        assert clasificar_y_descomponer_ruta("Resumen.txt") == {
            "es_absoluta": False,
            "carpetas": "",
            "archivo": "Resumen.txt",
            "extension": "txt",
        }


class TestObtenerRutaRelativa:
    def test_ejemplos_evaluacion_tercer_bimestre(self):
        """Verifica los casos de CentroMedico y Trabajos de las evaluaciones de AED."""
        assert (
            obtener_ruta_relativa(
                "/home/etec/Documentos/CentroMedico/",
                "/home/etec/Documentos/CentroMedico/Ingresos/Guardia/pacientes.csv",
            )
            == "Ingresos/Guardia/pacientes.csv"
        )
        assert (
            obtener_ruta_relativa(
                "/home/etec/Documentos/Trabajos",
                "/home/etec/Documentos/Trabajos/Arquitectura/PCs/componentes.csv",
            )
            == "Arquitectura/PCs/componentes.csv"
        )

    def test_ruta_fuera_del_proyecto_retorna_none(self):
        """Si la ruta absoluta no pertenece a la carpeta del proyecto, retorna None."""
        assert (
            obtener_ruta_relativa(
                "/home/etec/Documentos/Escuela/",
                "/home/etec/Descargas/notas.csv",
            )
            is None
        )


class TestConstruirRutaAbsoluta:
    def test_une_sin_duplicar_barras(self):
        """Debe unir carpeta y ruta relativa tanto si empieza con '/' como si no."""
        assert (
            construir_ruta_absoluta(
                "/home/etec/Documentos/Escuela/", "/Notas/4B/arquitectura.csv"
            )
            == "/home/etec/Documentos/Escuela/Notas/4B/arquitectura.csv"
        )
        assert (
            construir_ruta_absoluta(
                "/home/etec/Documentos/Deposito", "Inventarios/entorno214.csv"
            )
            == "/home/etec/Documentos/Deposito/Inventarios/entorno214.csv"
        )


# ---------------------------------------------------------------------------
# Sección 2: Lectura y escritura de archivos de texto (modos r, w, a)
# ---------------------------------------------------------------------------


class TestLeerMensajeMultilinea:
    def test_lee_correo_ignorando_renglones_vacios(self):
        """correo.txt tiene 4 líneas con texto y 1 línea en blanco que debe ignorarse."""
        resultado = leer_mensaje_multilinea(ruta("correo.txt"))
        assert resultado["cantidad_lineas"] == 4
        assert resultado["lineas"][0] == "Hola equipo,"
        assert resultado["lineas"][-1] == "Coordinación de AED"
        assert "\n\n" not in resultado["texto_completo"]


class TestLeerCumpleaniosAlternados:
    def test_lee_pares_nombre_y_fecha(self):
        """Debe combinar cada par de renglones en 'El {fecha} es el cumpleaños de {nombre}'."""
        assert leer_cumpleanios_alternados(ruta("cumpleanios.txt")) == [
            "El 14 de junio es el cumpleaños de Ana Gómez",
            "El 22 de junio es el cumpleaños de Bartolo Sotomayor",
            "El 30 de junio es el cumpleaños de Cosme Fulanito",
        ]


class TestLeerAlarmasAlternadas:
    def test_lee_pares_hora_y_mensaje(self):
        """Debe retornar la lista de diccionarios de alarmas con hora, mensaje y recordatorio."""
        resultado = leer_alarmas_alternadas(ruta("alarmas.txt"))
        assert len(resultado) == 3
        assert resultado[0] == {
            "hora": "07:30",
            "mensaje": "Despertarse para ir a la ETEC",
            "recordatorio": "Recordatorio: Despertarse para ir a la ETEC a las 07:30",
        }
        assert resultado[-1]["hora"] == "17:20"


class TestRegistrarMedicionMeteorologica:
    def test_agrega_en_modo_append_y_lee_historial(self, tmp_path):
        """Debe conservar mediciones previas al agregar nuevas y retornar todas las líneas."""
        archivo = tmp_path / "RegistroMeteorologico.txt"
        hist1 = registrar_medicion_meteorologica(str(archivo), 18.5, 60)
        assert hist1 == ["Temp 18.5C, humedad 60%"]

        hist2 = registrar_medicion_meteorologica(str(archivo), 22.0, 55)
        assert hist2 == [
            "Temp 18.5C, humedad 60%",
            "Temp 22.0C, humedad 55%",
        ]


class TestRegistrarCompraEnArchivo:
    def test_acumula_unidades_compradas(self, tmp_path):
        """Debe escribir '{articulo} x{cantidad}' y retornar la suma total de unidades."""
        archivo = tmp_path / "Compras.txt"
        assert registrar_compra_en_archivo(str(archivo), "Cuaderno", 3) == 3
        assert registrar_compra_en_archivo(str(archivo), "Lapicera", 5) == 8
        assert registrar_compra_en_archivo(str(archivo), "Goma", 0) == 8
        assert registrar_compra_en_archivo(str(archivo), "   ", 4) == 8


class TestSobrescribirResumenVentas:
    def test_escribe_solo_ventas_aprobadas_y_resumen(self, tmp_path):
        """Debe sobrescribir el archivo en modo 'w' con las ventas > venta_minima."""
        archivo = tmp_path / "resumen_ventas.txt"
        cantidad = sobrescribir_resumen_ventas(
            str(archivo), [8000, 12000, 15000, 10000], 10000
        )
        assert cantidad == 2
        lineas = archivo.read_text(encoding="utf-8").splitlines()
        assert lineas == [
            "Venta aprobada: $12000",
            "Venta aprobada: $15000",
            "2/4 ventas satisfactorias",
        ]


# ---------------------------------------------------------------------------
# Sección 3: Lectura y formateo de archivos CSV de evaluaciones AED
# ---------------------------------------------------------------------------


class TestFormatearAsistenciaCsv:
    def test_formatea_presentes_csv(self):
        """Verifica el formato de Presentes1eroC.csv de la evaluación del jueves."""
        lineas = formatear_asistencia_csv(ruta("presentes.csv"))
        assert len(lineas) == 5
        assert (
            lineas[0]
            == "Nombre: Analía Apellido: Álvarez Presentes: 7 Ausentes: 1"
        )
        assert (
            lineas[2]
            == "Nombre: Cosme Apellido: Fulanito Presentes: 8 Ausentes: 0"
        )


class TestFormatearMateriasCsv:
    def test_formatea_materias_csv(self):
        """Verifica el formato de MateriasJueves4B.csv de la evaluación del jueves."""
        lineas = formatear_materias_csv(ruta("materias.csv"))
        assert len(lineas) == 4
        assert (
            lineas[0]
            == "Materia: Algoritmos y Estructuras de Datos Ingreso: 13:10 Egreso: 17:20 Profesor/a: Impelluso"
        )


class TestFormatearHorariosTrabajoCsv:
    def test_formatea_horarios_trabajo_csv(self):
        """Verifica el formato de HorariosDeTrabajo.csv de la evaluación del viernes."""
        lineas = formatear_horarios_trabajo_csv(ruta("horarios_trabajo.csv"))
        assert len(lineas) == 4
        assert (
            lineas[0]
            == "Fecha: 26/09/2026 Nombre: Cosme Fulanito Entrada: 10:10 Salida: 13:10"
        )


class TestFormatearAgendaCsv:
    def test_formatea_agenda_csv(self):
        """Verifica el formato de Agenda.csv de la evaluación del viernes."""
        lineas = formatear_agenda_csv(ruta("agenda.csv"))
        assert len(lineas) == 4
        assert (
            lineas[0]
            == "Nombre: Cosme Apellido: Fulanito Localidad: La Tablada Telefono: 1135249400"
        )


class TestLeerCsvComoMatriz:
    def test_matriz_incluye_encabezado_y_filas(self):
        """varios.csv debe producir una matriz de 6 filas (1 encabezado + 5 datos)."""
        matriz = leer_csv_como_matriz(ruta("varios.csv"))
        assert len(matriz) == 6
        assert matriz[0] == ["nombre", "edad", "ciudad"]
        assert matriz[1] == ["Ana", "25", "Rosario"]
        assert matriz[-1] == ["Sofia", "28", "BsAs"]


class TestLeerCsvComoDiccionarios:
    def test_convierte_a_lista_de_diccionarios(self):
        """Cada fila de datos debe convertirse en un diccionario con las claves del encabezado."""
        registros = leer_csv_como_diccionarios(ruta("varios.csv"))
        assert len(registros) == 5
        assert registros[0] == {"nombre": "Ana", "edad": "25", "ciudad": "Rosario"}
        assert registros[-1] == {"nombre": "Sofia", "edad": "28", "ciudad": "BsAs"}


# ---------------------------------------------------------------------------
# Sección 4: Procesamiento avanzado, filtros, agregaciones y escritura de CSV
# ---------------------------------------------------------------------------


class TestFiltrarCsvPorRangoNumerico:
    def test_filtra_notas_entre_7_y_9(self):
        """En notas.csv, entre 7.0 y 9.0 están Ana (8.5) y Sofia (7.0)."""
        filtrados = filtrar_csv_por_rango_numerico(ruta("notas.csv"), "nota", 7.0, 9.0)
        assert [r["nombre"] for r in filtrados] == ["Ana", "Sofia"]

    def test_filtra_edades_entre_25_y_35(self):
        """En varios.csv, entre 25 y 35 años están Ana (25), Luis (35) y Sofia (28)."""
        filtrados = filtrar_csv_por_rango_numerico(ruta("varios.csv"), "edad", 25, 35)
        assert [r["nombre"] for r in filtrados] == ["Ana", "Luis", "Sofia"]


class TestBuscarRegistrosPorPatronCsv:
    def test_busca_subcadena_ignorando_mayusculas(self):
        """Buscar 'algoritmos' en materias.csv debe encontrar las 2 materias de programación."""
        encontrados = buscar_registros_por_patron_csv(
            ruta("materias.csv"), "Materia", "algoritmos"
        )
        assert len(encontrados) == 2
        assert encontrados[0]["Profesor"] == "Impelluso"
        assert encontrados[1]["Profesor"] == "Blanco"


class TestEstadisticasColumnaCsv:
    def test_estadisticas_de_notas_y_edades(self):
        """Calcula suma, promedio, máximo, mínimo y cantidad sobre notas.csv y varios.csv."""
        assert estadisticas_columna_csv(ruta("notas.csv"), "nota") == {
            "suma": 35.5,
            "promedio": 7.1,
            "maximo": 9.5,
            "minimo": 4.5,
            "cantidad": 5,
        }
        assert estadisticas_columna_csv(ruta("varios.csv"), "edad") == {
            "suma": 150.0,
            "promedio": 30.0,
            "maximo": 40.0,
            "minimo": 22.0,
            "cantidad": 5,
        }
        assert estadisticas_columna_csv(ruta("notas.csv"), "inexistente") is None


class TestCalcularAsistenciaCursoCsv:
    def test_clasifica_regulares_y_libres_en_presentes_csv(self):
        """En presentes.csv: Analía (87.5%), Cosme (100%) y Diana (75%) son regulares; Bartolo (62.5%) y Esteban (50%) libres."""
        resultado = calcular_asistencia_curso_csv(ruta("presentes.csv"), 75.0)
        assert resultado == {
            "regulares": ["Analía Álvarez", "Cosme Fulanito", "Diana Gómez"],
            "libres": ["Bartolo Sotomayor", "Esteban Quito"],
            "promedio_asistencia": 75.0,
        }


class TestAgruparCsvPorColumna:
    def test_agrupa_agenda_por_localidad(self):
        """En agenda.csv hay 2 contactos de La Tablada, 1 de Lugano y 1 de Mataderos."""
        grupos = agrupar_csv_por_columna(ruta("agenda.csv"), "Localidad")
        assert set(grupos.keys()) == {"La Tablada", "Lugano", "Mataderos"}
        assert len(grupos["La Tablada"]) == 2
        assert grupos["Lugano"][0]["Nombre"] == "Ana"


class TestExportarDiccionariosACsv:
    def test_escribe_csv_y_se_puede_releer(self, tmp_path):
        """Debe escribir encabezado y filas respetando el orden de columnas."""
        destino = tmp_path / "salida.csv"
        encabezados = ["jugador", "puntaje", "dificultad"]
        datos = [
            {"dificultad": "difícil", "jugador": "Ana", "puntaje": 4500},
            {"dificultad": "fácil", "jugador": "Cosme", "puntaje": 3200},
        ]
        escritos = exportar_diccionarios_a_csv(str(destino), encabezados, datos)
        assert escritos == 2
        lineas = destino.read_text(encoding="utf-8").splitlines()
        assert lineas == [
            "jugador,puntaje,dificultad",
            "Ana,4500,difícil",
            "Cosme,3200,fácil",
        ]


class TestActualizarStockCsv:
    def test_aplica_cambios_sin_bajar_de_cero(self, tmp_path):
        """Actualiza cantidades de inventario.csv y guarda el nuevo CSV en destino."""
        destino = tmp_path / "inventario_actualizado.csv"
        cambios = {
            "Teclado mecánico": -5,
            "Memoria RAM 16GB": 3,
            "Monitor 24 pulgadas": -10,
        }
        actualizados = actualizar_stock_csv(
            ruta("inventario.csv"), str(destino), cambios
        )
        cantidades = {r["componente"]: r["cantidad"] for r in actualizados}
        assert cantidades["Teclado mecánico"] == "7"
        assert cantidades["Memoria RAM 16GB"] == "8"
        assert cantidades["Monitor 24 pulgadas"] == "0"
        assert cantidades["Mouse inalámbrico"] == "8"
        assert destino.exists()


class TestGenerarReporteAprobadosCsv:
    def test_escribe_reporte_de_aprobados(self, tmp_path):
        """En notas.csv aprueban con >= 7.0 Ana (8.5), Maria (9.5) y Sofia (7.0)."""
        salida = tmp_path / "aprobados.txt"
        aprobados = generar_reporte_aprobados_csv(
            ruta("notas.csv"), str(salida), nota_aprobacion=7.0
        )
        assert aprobados == 3
        lineas = salida.read_text(encoding="utf-8").splitlines()
        assert lineas == [
            "Ana aprobó Matemática con 8.5",
            "Maria aprobó Matemática con 9.5",
            "Sofia aprobó Matemática con 7.0",
            "Total aprobados: 3/5",
        ]


class TestConsolidarArchivosCsv:
    def test_consolida_una_linea_y_varios_sin_duplicar_encabezado(self, tmp_path):
        """Unir una_linea.csv (1 fila) y varios.csv (5 filas) debe escribir 6 filas de datos."""
        destino = tmp_path / "consolidado.csv"
        total = consolidar_archivos_csv(
            [ruta("una_linea.csv"), ruta("varios.csv")], str(destino)
        )
        assert total == 6
        matriz = leer_csv_como_matriz(str(destino))
        assert len(matriz) == 7
        assert matriz[0] == ["nombre", "edad", "ciudad"]
        assert matriz[1] == ["Juan", "30", "Córdoba"]
        assert matriz[2] == ["Ana", "25", "Rosario"]
        assert matriz[-1] == ["Sofia", "28", "BsAs"]
