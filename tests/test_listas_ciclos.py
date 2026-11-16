"""
Tests para el módulo de Listas, ciclos, listas paralelas y listas de listas.

Cada test tiene un docstring que describe el comportamiento esperado.
El alumno debe leer el test, entender qué pide y luego implementar
la función en ejercicios/listas_ciclos.py hasta que el test pase.
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, "../ejercicios")

from ejercicios.listas_ciclos import (
    buscar_indice_caracter,
    obtener_indices_validos,
    seleccionar_colores_pintureria,
    generar_secuencia_descendente_filtrada,
    generar_impares_en_rango,
    invertir_lista_con_indices,
    filtrar_y_contar_bioma,
    reporte_ventas_satisfactorias,
    reporte_notas_desaprobadas,
    depurar_alturas_pacientes,
    actualizar_lista_compras,
    consultar_precio_articulo,
    buscar_articulo_por_precio,
    cobrar_expendedora_golosinas,
    filtrar_articulos_accesibles,
    extraer_parametros_spr,
    detectar_pokemones_debilitados_lista,
    detectar_animales_por_categoria,
    obtener_animal_mas_peligroso,
    formatear_tabla_puntajes,
    obtener_mejor_partida,
    buscar_estudiante_por_dni,
    agrupar_estudiantes_por_curso,
    filtrar_computadoras_por_requisitos,
)


# ---------------------------------------------------------------------------
# Sección 1: Recorridos con ciclos, indexación y secuencias
# ---------------------------------------------------------------------------


class TestBuscarIndiceCaracter:
    def test_encuentra_primera_aparicion_repetida(self):
        """En 'lanzazos', la primera 'z' está en el índice 3."""
        assert buscar_indice_caracter("lanzazos", "z") == 3

    def test_caracter_al_inicio_y_al_final(self):
        """Debe retornar 0 para el primer carácter y el último índice cuando está al final."""
        assert buscar_indice_caracter("Algoritmos", "A") == 0
        assert buscar_indice_caracter("libro", "o") == 4

    def test_caracter_inexistente_retorna_menos_uno(self):
        """Si el carácter no aparece en el texto, debe retornar -1."""
        assert buscar_indice_caracter("abrojo", "e") == -1

    def test_distingue_mayusculas_y_tildes(self):
        """La búsqueda es exacta: 'a' no coincide con 'á' ni con 'A'."""
        assert buscar_indice_caracter("árbol", "a") == -1
        assert buscar_indice_caracter("árbol", "á") == 0

    def test_caracter_invalido_retorna_menos_uno(self):
        """Si el segundo parámetro está vacío o tiene más de un carácter, retorna -1."""
        assert buscar_indice_caracter("abecedario", "") == -1
        assert buscar_indice_caracter("abecedario", "ab") == -1


class TestObtenerIndicesValidos:
    def test_indices_lista_cuatro_elementos(self):
        """Para una lista de 4 elementos debe retornar ([0, 1, 2, 3], [-4, -3, -2, -1])."""
        mochila = ["cuaderno", "cartuchera", "SUBE", "pañuelos"]
        assert obtener_indices_validos(mochila) == ([0, 1, 2, 3], [-4, -3, -2, -1])

    def test_indices_string_etec(self):
        """Para 'ETEC 2026' (9 caracteres) debe retornar positivos 0..8 y negativos -9..-1."""
        positivos, negativos = obtener_indices_validos("ETEC 2026")
        assert positivos == [0, 1, 2, 3, 4, 5, 6, 7, 8]
        assert negativos == [-9, -8, -7, -6, -5, -4, -3, -2, -1]

    def test_secuencia_vacia(self):
        """Para una secuencia vacía debe retornar ([], [])."""
        assert obtener_indices_validos([]) == ([], [])
        assert obtener_indices_validos("") == ([], [])


class TestSeleccionarColoresPintureria:
    def test_indices_positivos_validos(self):
        """Con índices 0 y 2 debe armar el pedido con 'gris' y 'violeta'."""
        colores = ["gris", "azul", "violeta", "verde", "rojo", "naranja", "marrón"]
        assert (
            seleccionar_colores_pintureria(colores, 0, 2)
            == "Pedido de pintura: gris y violeta"
        )

    def test_indices_negativos_validos(self):
        """Debe aceptar índices negativos dentro de rango (-1 es 'marrón', -2 es 'naranja')."""
        colores = ["gris", "azul", "violeta", "verde", "rojo", "naranja", "marrón"]
        assert (
            seleccionar_colores_pintureria(colores, -2, -1)
            == "Pedido de pintura: naranja y marrón"
        )

    def test_indice_fuera_de_rango_positivo_o_negativo(self):
        """Si alguno de los índices se sale de rango (ej: 7 o -8), retorna mensaje de error."""
        colores = ["gris", "azul", "violeta", "verde", "rojo", "naranja", "marrón"]
        assert (
            seleccionar_colores_pintureria(colores, 2, 7)
            == "Error: índice fuera de rango"
        )
        assert (
            seleccionar_colores_pintureria(colores, -8, 0)
            == "Error: índice fuera de rango"
        )

    def test_lista_vacia_retorna_error(self):
        """Si la lista de colores está vacía, cualquier índice está fuera de rango."""
        assert (
            seleccionar_colores_pintureria([], 0, 0)
            == "Error: índice fuera de rango"
        )


class TestGenerarSecuenciaDescendenteFiltrada:
    def test_de_100_a_menos_120_de_5_en_5_multiplos_de_3(self):
        """Recorriendo de 100 a -120 de 5 en 5, los negativos múltiplos de 3 van de -15 a -120."""
        resultado = generar_secuencia_descendente_filtrada(100, -120, 5, 3)
        assert resultado == [-15, -30, -45, -60, -75, -90, -105, -120]

    def test_rango_sin_negativos_retorna_vacio(self):
        """Si el recorrido nunca llega a valores negativos, debe retornar []."""
        assert generar_secuencia_descendente_filtrada(50, 0, 5, 3) == []

    def test_parametros_invalidos_retornan_vacio(self):
        """Si paso <= 0, divisor == 0 o inicio < fin, debe retornar []."""
        assert generar_secuencia_descendente_filtrada(10, -10, 0, 2) == []
        assert generar_secuencia_descendente_filtrada(10, -10, -5, 2) == []
        assert generar_secuencia_descendente_filtrada(10, -10, 2, 0) == []
        assert generar_secuencia_descendente_filtrada(-20, 10, 5, 3) == []


class TestGenerarImparesEnRango:
    def test_rango_ascendente_31_a_41(self):
        """Entre 31 y 41 inclusive debe retornar [31, 33, 35, 37, 39, 41]."""
        assert generar_impares_en_rango(31, 41) == [31, 33, 35, 37, 39, 41]

    def test_rango_con_extremos_pares(self):
        """Entre 10 y 16 debe retornar [11, 13, 15]."""
        assert generar_impares_en_rango(10, 16) == [11, 13, 15]

    def test_rango_descendente(self):
        """Si inicio > fin (ej: de 9 a -3), debe retornar los impares en orden descendente."""
        assert generar_impares_en_rango(9, -3) == [9, 7, 5, 3, 1, -1, -3]

    def test_mismo_numero_par_o_impar(self):
        """Si inicio == fin, retorna [n] si es impar o [] si es par."""
        assert generar_impares_en_rango(7, 7) == [7]
        assert generar_impares_en_rango(8, 8) == []


class TestInvertirListaConIndices:
    def test_invierte_articulos_por_precio(self):
        """Debe invertir el orden de los artículos sin modificar la lista original."""
        articulos = [
            "Cocina industrial a gas (Eskabe) $350.000",
            "Cocina a gas (Volcán) $205.000",
            "Anafe eléctrico doble (Gadnic) $160.000",
            "Anafe eléctrico simple (Gadnic) $90.000",
            "Anafe a garrafa (Eskabe) $87.000",
        ]
        copia_original = list(articulos)
        invertida = invertir_lista_con_indices(articulos)
        assert invertida[0] == "Anafe a garrafa (Eskabe) $87.000"
        assert invertida[-1] == "Cocina industrial a gas (Eskabe) $350.000"
        assert len(invertida) == 5
        assert articulos == copia_original

    def test_lista_vacia(self):
        """Invertir una lista vacía debe retornar []."""
        assert invertir_lista_con_indices([]) == []


# ---------------------------------------------------------------------------
# Sección 2: Filtrado, conteo y manipulación de listas simples
# ---------------------------------------------------------------------------


class TestFiltrarYContarBioma:
    def test_contar_bosques_en_mapa(self):
        """En la lista de niveles clásica, 'Bosque' aparece 4 veces en [1, 2, 4, 8]."""
        niveles = [
            "Pradera", "Bosque", "Bosque", "Pantano", "Bosque",
            "Montaña", "Pradera", "Playa", "Bosque", "Pradera", "Playa",
        ]
        assert filtrar_y_contar_bioma(niveles, "Bosque") == (4, [1, 2, 4, 8])

    def test_ignora_mayusculas_y_espacios(self):
        """Buscar '  pradera ' en minúsculas debe encontrar las 3 praderas en [0, 6, 9]."""
        niveles = [
            "Pradera", "Bosque", "Bosque", "Pantano", "Bosque",
            "Montaña", "Pradera", "Playa", "Bosque", "Pradera", "Playa",
        ]
        assert filtrar_y_contar_bioma(niveles, "  pradera ") == (3, [0, 6, 9])

    def test_bioma_inexistente(self):
        """Si el bioma no existe en el mapa, debe retornar (0, [])."""
        niveles = ["Pradera", "Bosque", "Pantano"]
        assert filtrar_y_contar_bioma(niveles, "Desierto") == (0, [])


class TestReporteVentasSatisfactorias:
    def test_ventas_superiores_al_minimo(self):
        """Solo las ventas estrictamente mayores a 10000 cuentan como satisfactorias."""
        ventas = [8500, 10000, 12500, 19000, 4300, 10001]
        assert (
            reporte_ventas_satisfactorias(ventas, 10000)
            == "3/6 ventas satisfactorias"
        )

    def test_lista_vacia_de_ventas(self):
        """Si no hubo ventas, el reporte debe ser '0/0 ventas satisfactorias'."""
        assert (
            reporte_ventas_satisfactorias([], 10000)
            == "0/0 ventas satisfactorias"
        )


class TestReporteNotasDesaprobadas:
    def test_calcula_cantidad_porcentaje_y_mensaje(self):
        """Con notas [8, 4, 6.5, 7, 9, 5] y mínima 7.0 hay 3 desaprobadas (50.0%)."""
        notas = [8, 4, 6.5, 7, 9, 5]
        assert reporte_notas_desaprobadas(notas) == (
            3,
            50.0,
            "3/6 notas desaprobadas",
        )

    def test_nota_minima_personalizada(self):
        """Con nota_minima=6.0 sobre [4, 6, 8], solo 4 está desaprobada (33.33%)."""
        assert reporte_notas_desaprobadas([4, 6, 8], nota_minima=6.0) == (
            1,
            33.33,
            "1/3 notas desaprobadas",
        )

    def test_sin_notas(self):
        """Para lista vacía debe retornar (0, 0.0, '0/0 notas desaprobadas')."""
        assert reporte_notas_desaprobadas([]) == (
            0,
            0.0,
            "0/0 notas desaprobadas",
        )


class TestDepurarAlturasPacientes:
    def test_quita_por_indice_y_luego_por_valor(self):
        """Debe quitar primero el índice indicado y luego la primera aparición del valor."""
        alturas = [1.65, 1.80, 1.72, 1.58]
        resultado = depurar_alturas_pacientes(alturas, 1, 1.58)
        assert resultado == [1.65, 1.72]
        assert alturas == [1.65, 1.80, 1.72, 1.58]

    def test_indice_fuera_de_rango_o_valor_inexistente(self):
        """Si el índice no es válido o el valor no está, ignora esa baja sin lanzar error."""
        alturas = [1.60, 1.70, 1.75]
        assert depurar_alturas_pacientes(alturas, 10, 1.70) == [1.60, 1.75]
        assert depurar_alturas_pacientes(alturas, -1, 1.99) == [1.60, 1.70]


class TestActualizarListaCompras:
    def test_agrega_nuevos_sin_duplicar_y_quita_cancelados(self):
        """Debe agregar nuevos válidos, evitar duplicados y eliminar los cancelados."""
        actual = ["leche", "pan", "huevos"]
        nuevos = ["  queso ", "pan", "", "   ", "manteca"]
        cancelados = ["HUEVOS", "gaseosa"]
        resultado = actualizar_lista_compras(actual, nuevos, cancelados)
        assert resultado == ["leche", "pan", "queso", "manteca"]
        assert actual == ["leche", "pan", "huevos"]


# ---------------------------------------------------------------------------
# Sección 3: Listas paralelas
# ---------------------------------------------------------------------------


class TestConsultarPrecioArticulo:
    def test_encuentra_precio_ignorando_mayusculas(self):
        """En el quiosco, 'mentitas' vale 900 y 'CHOCOLATE' vale 2300."""
        articulos = ["alfajor", "mentitas", "chocolate", "chicle"]
        precios = [1500, 900, 2300, 500]
        assert consultar_precio_articulo(articulos, precios, "mentitas") == 900
        assert consultar_precio_articulo(articulos, precios, "  CHOCOLATE ") == 2300

    def test_articulo_inexistente_retorna_none(self):
        """Si el artículo no está en la lista, debe retornar None."""
        articulos = ["alfajor", "mentitas"]
        precios = [1500, 900]
        assert consultar_precio_articulo(articulos, precios, "caramelo") is None


class TestBuscarArticuloPorPrecio:
    def test_encuentra_articulo_de_2300(self):
        """El artículo que vale 2300 es 'chocolate'."""
        articulos = ["alfajor", "mentitas", "chocolate", "chicle"]
        precios = [1500, 900, 2300, 500]
        assert buscar_articulo_por_precio(articulos, precios, 2300) == "chocolate"

    def test_precio_inexistente_retorna_none(self):
        """Si ningún artículo tiene ese precio, retorna None."""
        articulos = ["alfajor", "mentitas"]
        precios = [1500, 900]
        assert buscar_articulo_por_precio(articulos, precios, 9999) is None


class TestCobrarExpendedoraGolosinas:
    def test_compra_exitosa_con_vuelto(self):
        """Si deposita $2000 y pide el índice 0 ('alfajor' a $1500), recibe $500 de vuelto."""
        articulos = ["alfajor", "mentitas", "chocolate", "chicle"]
        precios = [1500, 900, 2300, 500]
        assert (
            cobrar_expendedora_golosinas(articulos, precios, 0, 2000)
            == "Entregando alfajor. Su vuelto es $500"
        )

    def test_dinero_insuficiente(self):
        """Si deposita $1000 y pide 'chocolate' ($2300), informa que no alcanza y devuelve $1000."""
        articulos = ["alfajor", "mentitas", "chocolate", "chicle"]
        precios = [1500, 900, 2300, 500]
        assert (
            cobrar_expendedora_golosinas(articulos, precios, 2, 1000)
            == "No alcanza para chocolate ($2300). Se devuelven $1000"
        )

    def test_indice_invalido_negativo_o_fuera_de_rango(self):
        """Si elige una opción negativa o fuera de rango, devuelve el dinero."""
        articulos = ["alfajor", "mentitas"]
        precios = [1500, 900]
        assert (
            cobrar_expendedora_golosinas(articulos, precios, 5, 1500)
            == "Opción inválida. Se devuelven $1500"
        )
        assert (
            cobrar_expendedora_golosinas(articulos, precios, -1, 1500)
            == "Opción inválida. Se devuelven $1500"
        )


class TestFiltrarArticulosAccesibles:
    def test_filtra_por_presupuesto(self):
        """Con presupuesto $1500 alcanza para alfajor ($1500), mentitas ($900) y chicle ($500)."""
        articulos = ["alfajor", "mentitas", "chocolate", "chicle"]
        precios = [1500, 900, 2300, 500]
        assert filtrar_articulos_accesibles(articulos, precios, 1500) == [
            "alfajor ($1500)",
            "mentitas ($900)",
            "chicle ($500)",
        ]


# ---------------------------------------------------------------------------
# Sección 4: Listas de listas (matrices y tablas de registros)
# ---------------------------------------------------------------------------


class TestExtraerParametrosSpr:
    def test_extraccion_matriz_enemigos_tema_1_y_2(self):
        """Verifica las lecturas de la matriz 3x3 de enemigos de la evaluación de AED."""
        enemigos = [
            [25, 10, 47],
            [110, 53, 120],
            [84, 106, 9],
        ]
        assert extraer_parametros_spr(enemigos, 0, 1, 1, 2, 2, 0) == (10, 120, 84)
        assert extraer_parametros_spr(enemigos, 2, 1, 0, 2, 1, 0) == (106, 47, 110)

    def test_coordenada_fuera_de_rango_retorna_none(self):
        """Si alguna fila o columna no existe en la matriz, retorna None."""
        enemigos = [[25, 10], [110, 53]]
        assert extraer_parametros_spr(enemigos, 0, 0, 3, 0, 1, 1) is None


class TestDetectarPokemonesDebilitadosLista:
    def test_detecta_caterpie_y_raichu_con_umbral_20(self):
        """Con vida_maxima=20, solo Caterpie (11) y Raichu (2) están debilitados (Ditto tiene 21)."""
        pokemones = [
            ["Golem", "roca/tierra", 54],
            ["Caterpie", "bicho", 11],
            ["Ditto", "normal", 21],
            ["Alakazam", "psíquico", 37],
            ["Raichu", "eléctrico", 2],
        ]
        assert detectar_pokemones_debilitados_lista(pokemones) == [
            "¡Hay un Caterpie debilitado cerca! Le quedan 11 puntos de vida",
            "¡Hay un Raichu debilitado cerca! Le quedan 2 puntos de vida",
        ]

    def test_incluye_limite_exacto(self):
        """Si un pokémon tiene exactamente vida_maxima puntos de vida, debe incluirse."""
        pokemones = [["Pikachu", "eléctrico", 20], ["Onix", "roca", 21]]
        assert detectar_pokemones_debilitados_lista(pokemones, 20) == [
            "¡Hay un Pikachu debilitado cerca! Le quedan 20 puntos de vida"
        ]


class TestDetectarAnimalesPorCategoria:
    def test_detecta_insectos_en_lista(self):
        """Debe reportar a la mantis y a la avispa con el formato de la evaluación."""
        animales = [
            ["oso pardo", "mamífero", 15],
            ["mantis", "insecto", 1],
            ["rana venenosa", "reptil", 9],
            ["tarántula", "arácnido", 4],
            ["avispa", "insecto", 7],
        ]
        assert detectar_animales_por_categoria(animales, "insecto") == [
            "¡Detectado un insecto! Especie: mantis, nivel de peligrosidad: 1",
            "¡Detectado un insecto! Especie: avispa, nivel de peligrosidad: 7",
        ]


class TestObtenerAnimalMasPeligroso:
    def test_mas_peligroso_general_y_filtrado(self):
        """General es 'oso pardo' (15); filtrando por 'insecto' es 'avispa' (7)."""
        animales = [
            ["oso pardo", "mamífero", 15],
            ["mantis", "insecto", 1],
            ["rana venenosa", "reptil", 9],
            ["avispa", "insecto", 7],
        ]
        assert obtener_animal_mas_peligroso(animales) == ["oso pardo", "mamífero", 15]
        assert obtener_animal_mas_peligroso(animales, "INSECTO") == [
            "avispa",
            "insecto",
            7,
        ]
        assert obtener_animal_mas_peligroso(animales, "ave") is None


class TestFormatearTablaPuntajes:
    def test_formatea_todas_y_filtradas_por_dificultad(self):
        """Debe numerar desde 1 y permitir filtrar por dificultad."""
        partidas = [
            [4500, "Ana", "difícil"],
            [3200, "Cosme", "fácil"],
            [5100, "Bartolo", "difícil"],
        ]
        assert formatear_tabla_puntajes(partidas) == [
            "1. Ana - 4500 pts (difícil)",
            "2. Cosme - 3200 pts (fácil)",
            "3. Bartolo - 5100 pts (difícil)",
        ]
        assert formatear_tabla_puntajes(partidas, "difícil") == [
            "1. Ana - 4500 pts (difícil)",
            "2. Bartolo - 5100 pts (difícil)",
        ]


class TestObtenerMejorPartida:
    def test_obtiene_mayor_puntaje(self):
        """Debe retornar la sublista de mayor puntaje general o por dificultad."""
        partidas = [
            [4500, "Ana", "difícil"],
            [6000, "Cosme", "fácil"],
            [5100, "Bartolo", "difícil"],
        ]
        assert obtener_mejor_partida(partidas) == [6000, "Cosme", "fácil"]
        assert obtener_mejor_partida(partidas, "difícil") == [
            5100,
            "Bartolo",
            "difícil",
        ]
        assert obtener_mejor_partida([], "fácil") is None


class TestBuscarEstudiantePorDni:
    def test_encuentra_estudiante_existente_e_inexistente(self):
        """Debe encontrar a Bartolo Sotomayor por su DNI o retornar None si no está."""
        dni_estudiantes = [
            ["Ana Gómez", 48031048],
            ["Bartolo Sotomayor", 47905106],
            ["Cosme Fulanito", 99431080],
        ]
        assert (
            buscar_estudiante_por_dni(dni_estudiantes, 47905106)
            == "Bartolo Sotomayor"
        )
        assert buscar_estudiante_por_dni(dni_estudiantes, 11111111) is None


class TestAgruparEstudiantesPorCurso:
    def test_filtra_por_anio_y_division(self):
        """Debe retornar solo los estudiantes que cursan en el año y división indicados."""
        cursos = [
            ["Ana Gómez", 4, "B"],
            ["Cosme Fulanito", 3, "D"],
            ["Laura Díaz", 4, "b"],
            ["Pedro Pérez", 4, "A"],
        ]
        assert agrupar_estudiantes_por_curso(cursos, 4, "B") == [
            "Ana Gómez",
            "Laura Díaz",
        ]
        assert agrupar_estudiantes_por_curso(cursos, 5, "A") == []


class TestFiltrarComputadorasPorRequisitos:
    def test_filtra_por_ram_precio_y_ssd(self):
        """Debe verificar RAM mínima, precio máximo y condición de SSD."""
        pcs = [
            ["Office Basic", 8, 450000.0, True],
            ["Gamer Pro", 16, 950000.0, True],
            ["Server HDD", 32, 800000.0, False],
            ["Workstation", 16, 780000.0, True],
        ]
        assert filtrar_computadoras_por_requisitos(pcs, 16, 900000.0, requiere_ssd=True) == [
            "Workstation"
        ]
        assert filtrar_computadoras_por_requisitos(pcs, 16, 900000.0, requiere_ssd=False) == [
            "Server HDD",
            "Workstation",
        ]
