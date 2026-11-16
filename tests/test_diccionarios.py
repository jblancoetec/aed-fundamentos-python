"""
Tests para el módulo de Diccionarios y listas de diccionarios.

Cada test tiene un docstring que describe el comportamiento esperado.
El alumno debe leer el test, entender qué pide y luego implementar
la función en ejercicios/diccionarios.py hasta que el test pase.
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, "../ejercicios")

from ejercicios.diccionarios import (
    crear_ficha_animal,
    agregar_atributo_enemigo,
    aplicar_ataque_a_enemigo,
    evaluar_asistencia_estudiante,
    formatear_horario_materia,
    calcular_horas_trabajadas,
    normalizar_contacto_agenda,
    procesar_operacion_sube,
    detectar_pokemones_debilitados_dict,
    filtrar_pokemones_por_tipo,
    resumen_tipos_pokemones,
    filtrar_contactos_por_localidad,
    buscar_temas_musicales,
    calcular_carrito_musica,
    filtrar_peliculas_recomendadas,
    agrupar_peliculas_por_decada,
    liquidar_jornada_empleados,
    combinar_listas_paralelas_en_inventario,
    procesar_pedido_quiosco,
    estadisticas_notas_por_materia,
    obtener_mejores_promedios,
    ranking_jugadores_por_dificultad,
    cruzar_estudiantes_y_cursos,
    auditar_componentes_pc,
)


# ---------------------------------------------------------------------------
# Sección 1: Modelado, validación y transformación de diccionarios
# ---------------------------------------------------------------------------


class TestCrearFichaAnimal:
    def test_ficha_pato_aerea_y_acuatica(self):
        """Un pato que vuela y nada debe tener locomoción 'aérea y acuática'."""
        ficha = crear_ficha_animal("  Pato criollo ", "omnívoro", 2, True, True)
        assert ficha == {
            "nombre": "Pato criollo",
            "alimentacion": "omnívoro",
            "cantidad_patas": 2,
            "puede_volar": True,
            "puede_nadar": True,
            "locomocion": "aérea y acuática",
        }

    def test_distintas_locomociones(self):
        """Verifica locomoción 'aérea', 'acuática' y 'terrestre'."""
        assert crear_ficha_animal("Águila", "carnívoro", 2, True, False)["locomocion"] == "aérea"
        assert crear_ficha_animal("Tiburón", "carnívoro", 0, False, True)["locomocion"] == "acuática"
        assert crear_ficha_animal("Puma", "carnívoro", 4, False, False)["locomocion"] == "terrestre"

    def test_datos_invalidos_retornan_none(self):
        """Nombre vacío, alimentación vacía o patas negativas deben retornar None."""
        assert crear_ficha_animal("   ", "herbívoro", 4, False, False) is None
        assert crear_ficha_animal("Vaca", "", 4, False, False) is None
        assert crear_ficha_animal("Araña", "insectívoro", -2, False, False) is None


class TestAgregarAtributoEnemigo:
    def test_agrega_atributo_y_calcula_poder_total(self):
        """Debe agregar el nuevo dato en el diccionario y calcular poder_total = vida + 2*defensa."""
        enemigo = {"nombre": "Ninja", "vida": 15, "defensa": 3.5}
        actualizado = agregar_atributo_enemigo(enemigo, "arma", "katana")
        assert actualizado == {
            "nombre": "Ninja",
            "vida": 15,
            "defensa": 3.5,
            "arma": "katana",
            "poder_total": 22.0,
        }
        assert enemigo["arma"] == "katana"

    def test_clave_vacia_no_se_agrega(self):
        """Si la clave está vacía, no la agrega pero sí calcula poder_total."""
        enemigo = {"nombre": "Ninja", "vida": 10, "defensa": 2.0}
        assert agregar_atributo_enemigo(enemigo, "   ", 100) == {
            "nombre": "Ninja",
            "vida": 10,
            "defensa": 2.0,
            "poder_total": 14.0,
        }


class TestAplicarAtaqueAEnemigo:
    def test_ataque_parcial_con_defensa(self):
        """Con vida 15, defensa 3.5 y ataque 10, recibe 6.5 de daño y queda con 8.5 de vida."""
        enemigo = {"nombre": "Ninja", "vida": 15, "defensa": 3.5}
        resultado = aplicar_ataque_a_enemigo(enemigo, 10)
        assert resultado == {
            "nombre": "Ninja",
            "vida": 8.5,
            "defensa": 3.5,
            "danio_recibido": 6.5,
            "derrotado": False,
        }
        assert enemigo["vida"] == 8.5

    def test_ataque_menor_a_defensa_y_ataque_letal(self):
        """Si el ataque no supera la defensa el daño es 0; si supera la vida queda en 0 y derrotado=True."""
        enemigo = {"nombre": "Esqueleto", "vida": 10, "defensa": 5.0}
        sin_danio = aplicar_ataque_a_enemigo(enemigo, 3)
        assert sin_danio["vida"] == 10
        assert sin_danio["danio_recibido"] == 0.0
        assert sin_danio["derrotado"] is False

        letal = aplicar_ataque_a_enemigo(enemigo, 25)
        assert letal["vida"] == 0.0
        assert letal["danio_recibido"] == 20.0
        assert letal["derrotado"] is True


class TestEvaluarAsistenciaEstudiante:
    def test_estudiante_regular_y_libre(self):
        """Analía con 7 presentes y 1 ausente tiene 87.5% (Regular); con 5 y 3 tiene 62.5% (Libre)."""
        reg = {"Nombre": "Analía", "Apellido": "Álvarez", "Presentes": "7", "Ausentes": "1"}
        assert evaluar_asistencia_estudiante(reg) == {
            "nombre_completo": "Analía Álvarez",
            "presentes": 7,
            "ausentes": 1,
            "total_clases": 8,
            "porcentaje_asistencia": 87.5,
            "condicion": "Regular",
        }
        reg_libre = {"Nombre": "Bartolo", "Apellido": "Sotomayor", "Presentes": 5, "Ausentes": 3}
        assert evaluar_asistencia_estudiante(reg_libre)["condicion"] == "Libre"


class TestFormatearHorarioMateria:
    def test_calcula_duracion_y_resumen(self):
        """De 13:10 a 17:20 hay 250 minutos (4 horas y 10 minutos)."""
        materia = {
            "Materia": "Algoritmos y Estructuras de Datos",
            "Hora entrada": "13:10",
            "Hora salida": "17:20",
            "Profesor": "Impelluso",
        }
        assert formatear_horario_materia(materia) == {
            "resumen": (
                "Materia: Algoritmos y Estructuras de Datos "
                "Ingreso: 13:10 Egreso: 17:20 Profesor/a: Impelluso"
            ),
            "duracion_minutos": 250,
        }


class TestCalcularHorasTrabajadas:
    def test_jornada_cosme_fulanito(self):
        """De 10:10 a 13:10 son 180 minutos (3.0 horas)."""
        registro = {
            "Fecha": "26/09/2026",
            "Nombre": "Cosme Fulanito",
            "Hora entrada": "10:10",
            "Hora salida": "13:10",
        }
        assert calcular_horas_trabajadas(registro) == {
            "fecha": "26/09/2026",
            "nombre": "Cosme Fulanito",
            "minutos_trabajados": 180,
            "horas_trabajadas": 3.0,
        }


class TestNormalizarContactoAgenda:
    def test_contacto_valido_e_invalido(self):
        """Debe limpiar guiones/espacios del teléfono y validar que tenga >= 8 dígitos."""
        contacto = {
            "Nombre": " Cosme ",
            "Apellido": " Fulanito ",
            "Localidad": " La Tablada ",
            "Telefono": "11-3524-9400",
        }
        assert normalizar_contacto_agenda(contacto) == {
            "nombre_completo": "Fulanito, Cosme",
            "localidad": "La Tablada",
            "telefono": "1135249400",
            "valido": True,
        }
        invalido = {
            "Nombre": "Ana",
            "Apellido": "Gómez",
            "Localidad": "Lugano",
            "Telefono": "1234-ABCD",
        }
        assert normalizar_contacto_agenda(invalido)["valido"] is False


class TestProcesarOperacionSube:
    def test_recarga_y_viaje_exitoso(self):
        """Verifica acreditación de recarga y descuento de boleto en SUBE."""
        cuenta = {"titular": "Cosme", "saldo": 500.0, "viajes_realizados": 2}
        recargada = procesar_operacion_sube(cuenta, "recarga", 2000.0)
        assert recargada == {
            "titular": "Cosme",
            "saldo": 2500.0,
            "viajes_realizados": 2,
            "exito": True,
            "mensaje": "Recarga acreditada. Saldo: $2500.0",
        }
        viaje = procesar_operacion_sube(recargada, "viaje", 900.0)
        assert viaje == {
            "titular": "Cosme",
            "saldo": 1600.0,
            "viajes_realizados": 3,
            "exito": True,
            "mensaje": "Viaje cobrado. Saldo restante: $1600.0",
        }

    def test_saldo_insuficiente_y_monto_invalido(self):
        """Si no alcanza el saldo o el monto es <= 0, exito debe ser False."""
        cuenta = {"titular": "Ana", "saldo": 400.0, "viajes_realizados": 1}
        sin_saldo = procesar_operacion_sube(cuenta, "viaje", 900.0)
        assert sin_saldo["exito"] is False
        assert sin_saldo["mensaje"] == "Saldo insuficiente"
        assert sin_saldo["saldo"] == 400.0

        monto_neg = procesar_operacion_sube(cuenta, "recarga", -100)
        assert monto_neg["exito"] is False
        assert monto_neg["mensaje"] == "Monto inválido"


# ---------------------------------------------------------------------------
# Sección 2: Búsqueda y filtrado sobre listas de diccionarios
# ---------------------------------------------------------------------------


class TestDetectarPokemonesDebilitadosDict:
    def test_detecta_con_umbral_12_mesa_julio(self):
        """Con vida_maxima=12 (Mesa Julio), detecta a Caterpie (11) y Raichu (2), pero no Alakazam (13)."""
        pokemones = [
            {"nombre": "Golem", "tipos": "roca/tierra", "vida": 54},
            {"nombre": "Caterpie", "tipos": "bicho", "vida": 11},
            {"nombre": "Ditto", "tipos": "normal", "vida": 21},
            {"nombre": "Alakazam", "tipos": "psíquico", "vida": 13},
            {"nombre": "Raichu", "tipos": "eléctrico", "vida": 2},
        ]
        assert detectar_pokemones_debilitados_dict(pokemones) == [
            "¡Hay un Caterpie debilitado cerca!\nLe quedan 11 puntos de vida\nY sus tipos son bicho",
            "¡Hay un Raichu debilitado cerca!\nLe quedan 2 puntos de vida\nY sus tipos son eléctrico",
        ]


class TestFiltrarPokemonesPorTipo:
    def test_filtra_tipo_simple_y_compuesto(self):
        """Buscar 'tierra' debe encontrar a Golem ('roca/tierra') y Sandshrew ('tierra')."""
        pokemones = [
            {"nombre": "Golem", "tipos": "roca/tierra", "vida": 54},
            {"nombre": "Caterpie", "tipos": "bicho", "vida": 11},
            {"nombre": "Sandshrew", "tipos": "Tierra", "vida": 30},
        ]
        assert filtrar_pokemones_por_tipo(pokemones, "tierra") == [
            "Golem",
            "Sandshrew",
        ]


class TestResumenTiposPokemones:
    def test_cuenta_tipos_separando_barra(self):
        """Debe desglosar los tipos compuestos con '/' y contar cada uno en minúsculas."""
        pokemones = [
            {"nombre": "Golem", "tipos": "roca/tierra", "vida": 54},
            {"nombre": "Onix", "tipos": "Roca/Tierra", "vida": 35},
            {"nombre": "Caterpie", "tipos": "bicho", "vida": 11},
        ]
        assert resumen_tipos_pokemones(pokemones) == {
            "roca": 2,
            "tierra": 2,
            "bicho": 1,
        }


class TestFiltrarContactosPorLocalidad:
    def test_filtra_contactos_de_la_tablada(self):
        """Debe retornar los contactos de la localidad buscada ignorando mayúsculas."""
        agenda = [
            {"Nombre": "Cosme", "Apellido": "Fulanito", "Localidad": "La Tablada", "Telefono": "1135249400"},
            {"Nombre": "Ana", "Apellido": "Gómez", "Localidad": "Lugano", "Telefono": "1148031048"},
            {"Nombre": "Bartolo", "Apellido": "Sotomayor", "Localidad": "la tablada", "Telefono": "1147905106"},
        ]
        resultado = filtrar_contactos_por_localidad(agenda, "  LA TABLADA ")
        assert len(resultado) == 2
        assert resultado[0]["Nombre"] == "Cosme"
        assert resultado[1]["Nombre"] == "Bartolo"


class TestBuscarTemasMusicales:
    def test_aplica_filtros_combinados(self):
        """Debe filtrar por género, precio máximo y disponibilidad."""
        catalogo = [
            {"titulo": "Ciudad Mágica", "genero": "Rock", "duracion_seg": 210, "precio": 1200.0, "disponible": True},
            {"titulo": "Flaca", "genero": "Rock", "duracion_seg": 270, "precio": 1800.0, "disponible": True},
            {"titulo": "Adiós Nonino", "genero": "Tango", "duracion_seg": 480, "precio": 1500.0, "disponible": True},
            {"titulo": "Ji Ji Ji", "genero": "Rock", "duracion_seg": 330, "precio": 1100.0, "disponible": False},
        ]
        assert buscar_temas_musicales(catalogo, genero="rock", precio_maximo=1500.0) == [
            "Ciudad Mágica"
        ]
        assert buscar_temas_musicales(catalogo, genero="rock", solo_disponibles=False) == [
            "Ciudad Mágica",
            "Flaca",
            "Ji Ji Ji",
        ]


class TestCalcularCarritoMusica:
    def test_calcula_totales_y_separa_no_disponibles(self):
        """Suma precio y duración de disponibles sin duplicar pedidos repetidos."""
        catalogo = [
            {"titulo": "Tema A", "duracion_seg": 200, "precio": 1000.0, "disponible": True},
            {"titulo": "Tema B", "duracion_seg": 180, "precio": 1500.5, "disponible": True},
            {"titulo": "Tema C", "duracion_seg": 240, "precio": 900.0, "disponible": False},
        ]
        pedidos = ["Tema A", "Tema C", "Tema A", "Inexistente", "Tema B"]
        assert calcular_carrito_musica(catalogo, pedidos) == {
            "comprados": ["Tema A", "Tema B"],
            "no_disponibles": ["Tema C", "Inexistente"],
            "total_pagar": 2500.5,
            "duracion_total_seg": 380,
        }


class TestFiltrarPeliculasRecomendadas:
    def test_filtra_por_puntaje_anio_y_atp(self):
        """Verifica filtrado con y sin restricción ATP."""
        peliculas = [
            {"titulo": "El Viaje de Chihiro", "anio": 2001, "puntaje": 8.6, "atp": True},
            {"titulo": "Relatos Salvajes", "anio": 2014, "puntaje": 8.1, "atp": False},
            {"titulo": "Toy Story", "anio": 1995, "puntaje": 8.3, "atp": True},
        ]
        assert filtrar_peliculas_recomendadas(peliculas, 8.0, 2000, solo_atp=False) == [
            "El Viaje de Chihiro",
            "Relatos Salvajes",
        ]
        assert filtrar_peliculas_recomendadas(peliculas, 8.0, 2000, solo_atp=True) == [
            "El Viaje de Chihiro"
        ]


class TestAgruparPeliculasPorDecada:
    def test_agrupa_correctamente_por_decada(self):
        """1995 y 1999 van a '1990s'; 2001 va a '2000s'."""
        peliculas = [
            {"titulo": "Toy Story", "anio": 1995},
            {"titulo": "Matrix", "anio": 1999},
            {"titulo": "Shrek", "anio": 2001},
        ]
        assert agrupar_peliculas_por_decada(peliculas) == {
            "1990s": ["Toy Story", "Matrix"],
            "2000s": ["Shrek"],
        }


# ---------------------------------------------------------------------------
# Sección 3: Agregaciones, cruces de datos y reportes con diccionarios
# ---------------------------------------------------------------------------


class TestLiquidarJornadaEmpleados:
    def test_acumula_horas_y_pagos_por_empleado(self):
        """Cosme trabaja 3h el 26/09 y 5h el 27/09 = 8.0h ($40000 a $5000/h)."""
        registros = [
            {"Fecha": "26/09/2026", "Nombre": "Cosme Fulanito", "Hora entrada": "10:10", "Hora salida": "13:10"},
            {"Fecha": "26/09/2026", "Nombre": "Ana Gómez", "Hora entrada": "08:30", "Hora salida": "12:30"},
            {"Fecha": "27/09/2026", "Nombre": "Cosme Fulanito", "Hora entrada": "09:00", "Hora salida": "14:00"},
        ]
        assert liquidar_jornada_empleados(registros, 5000) == {
            "Cosme Fulanito": {"horas": 8.0, "pago": 40000.0},
            "Ana Gómez": {"horas": 4.0, "pago": 20000.0},
        }


class TestCombinarListasParalelasEnInventario:
    def test_combina_y_descarta_invalidos(self):
        """Solo incluye ítems con precio > 0 y stock >= 0, calculando valor_total."""
        articulos = ["alfajor", "mentitas", "error_precio", "error_stock"]
        precios = [1500, 900, 0, 500]
        stocks = [10, 5, 8, -1]
        assert combinar_listas_paralelas_en_inventario(articulos, precios, stocks) == [
            {"articulo": "alfajor", "precio": 1500.0, "stock": 10, "valor_total": 15000.0},
            {"articulo": "mentitas", "precio": 900.0, "stock": 5, "valor_total": 4500.0},
        ]


class TestProcesarPedidoQuiosco:
    def test_descuenta_stock_y_separa_rechazados(self):
        """Entrega solo lo que tiene stock suficiente y actualiza el stock en el inventario."""
        inventario = {
            "alfajor": {"precio": 1500.0, "stock": 4},
            "mentitas": {"precio": 900.0, "stock": 2},
        }
        pedido = {"alfajor": 3, "mentitas": 5, "chocolate": 1}
        resultado = procesar_pedido_quiosco(inventario, pedido)
        assert resultado == {
            "total": 4500.0,
            "entregados": ["alfajor"],
            "rechazados": ["mentitas", "chocolate"],
            "inventario_actualizado": {
                "alfajor": {"precio": 1500.0, "stock": 1},
                "mentitas": {"precio": 900.0, "stock": 2},
            },
        }
        assert inventario["alfajor"]["stock"] == 1


class TestEstadisticasNotasPorMateria:
    def test_estadisticas_por_materia(self):
        """Calcula promedio, máxima, mínima, aprobados y desaprobados por materia."""
        notas = [
            {"nombre": "Ana", "materia": "AED", "nota": "8.5"},
            {"nombre": "Pedro", "materia": "AED", "nota": "5.5"},
            {"nombre": "María", "materia": "AED", "nota": 10.0},
            {"nombre": "Ana", "materia": "TAP", "nota": 7.0},
        ]
        assert estadisticas_notas_por_materia(notas) == {
            "AED": {
                "promedio": 8.0,
                "maxima": 10.0,
                "minima": 5.5,
                "aprobados": 2,
                "desaprobados": 1,
            },
            "TAP": {
                "promedio": 7.0,
                "maxima": 7.0,
                "minima": 7.0,
                "aprobados": 1,
                "desaprobados": 0,
            },
        }


class TestObtenerMejoresPromedios:
    def test_filtra_estudiantes_con_promedio_suficiente(self):
        """Ana tiene promedio 8.0 (2 materias) y Pedro 5.5 (1 materia)."""
        notas = [
            {"nombre": "Ana", "materia": "AED", "nota": 9.0},
            {"nombre": "Pedro", "materia": "AED", "nota": 5.5},
            {"nombre": "Ana", "materia": "TAP", "nota": 7.0},
        ]
        assert obtener_mejores_promedios(notas, 7.0) == [
            {"nombre": "Ana", "promedio": 8.0, "cantidad_materias": 2}
        ]


class TestRankingJugadoresPorDificultad:
    def test_resume_mejor_jugador_y_promedio(self):
        """Agrupa partidas por dificultad e identifica récord y promedio."""
        partidas = [
            {"jugador": "Ana", "puntaje": 4000, "dificultad": "difícil"},
            {"jugador": "Bartolo", "puntaje": 6000, "dificultad": "difícil"},
            {"jugador": "Cosme", "puntaje": 2500, "dificultad": "fácil"},
        ]
        assert ranking_jugadores_por_dificultad(partidas) == {
            "difícil": {
                "mejor_jugador": "Bartolo",
                "mejor_puntaje": 6000,
                "promedio_puntaje": 5000.0,
                "partidas_jugadas": 2,
            },
            "fácil": {
                "mejor_jugador": "Cosme",
                "mejor_puntaje": 2500,
                "promedio_puntaje": 2500.0,
                "partidas_jugadas": 1,
            },
        }


class TestCruzarEstudiantesYCursos:
    def test_unifica_dni_y_curso_por_nombre(self):
        """Une los datos de los estudiantes que figuran en ambos listados."""
        dnis = [
            {"nombre": "Ana Gómez", "dni": 48031048},
            {"nombre": "Bartolo Sotomayor", "dni": 47905106},
            {"nombre": "Cosme Fulanito", "dni": 99431080},
        ]
        cursos = [
            {"nombre": "Cosme Fulanito", "anio": 3, "division": "D"},
            {"nombre": "Ana Gómez", "anio": 4, "division": "B"},
        ]
        assert cruzar_estudiantes_y_cursos(dnis, cursos) == [
            {"nombre": "Ana Gómez", "dni": 48031048, "curso": "4B"},
            {"nombre": "Cosme Fulanito", "dni": 99431080, "curso": "3D"},
        ]


class TestAuditarComponentesPc:
    def test_audita_operativos_y_faltantes(self):
        """Cuenta operativos por categoría y detecta los que tienen stock operativo < stock_minimo."""
        componentes = [
            {"componente": "Teclado mecánico", "categoria": "periferico", "cantidad": 12, "estado": "operativo"},
            {"componente": "Monitor 24", "categoria": "pantalla", "cantidad": 3, "estado": "operativo"},
            {"componente": "Fuente ATX", "categoria": "hardware", "cantidad": 8, "estado": "en reparación"},
            {"componente": "Mouse óptico", "categoria": "periferico", "cantidad": 6, "estado": "operativo"},
        ]
        assert auditar_componentes_pc(componentes, stock_minimo=5) == {
            "faltantes": ["Monitor 24", "Fuente ATX"],
            "total_operativos": 21,
            "por_categoria": {"periferico": 18, "pantalla": 3},
        }
