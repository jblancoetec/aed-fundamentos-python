"""
Módulo de ejercicios: Diccionarios y listas de diccionarios.

Todos los ejercicios tienen una dificultad media-elevada y están basados en las
guías y evaluaciones de Algoritmos y Estructuras de Datos (AED) y Taller de
Algoritmos y Programación (TAP).
"""


# ---------------------------------------------------------------------------
# Sección 1: Modelado, validación y transformación de diccionarios
# ---------------------------------------------------------------------------


def crear_ficha_animal(nombre, alimentacion, cantidad_patas, puede_volar, puede_nadar):
    """Construye la ficha enciclopédica de un animal validando y clasificando sus datos.

    Reglas:
    - Si nombre o alimentacion quedan vacíos tras .strip(), o si cantidad_patas < 0,
      retorna None.
    - Determina el campo "locomocion" según puede_volar y puede_nadar:
        * True y True   -> "aérea y acuática"
        * True y False  -> "aérea"
        * False y True  -> "acuática"
        * False y False -> "terrestre"

    Args:
        nombre (str): nombre del animal.
        alimentacion (str): tipo de alimentación ("carnívoro", "herbívoro", etc.).
        cantidad_patas (int): cantidad de patas (>= 0).
        puede_volar (bool): indica si vuela.
        puede_nadar (bool): indica si nada.

    Returns:
        dict | None: diccionario con las claves "nombre", "alimentacion",
                     "cantidad_patas", "puede_volar", "puede_nadar" y "locomocion",
                     o None si los datos son inválidos.
    """
    pass


def agregar_atributo_enemigo(enemigo, clave, valor):
    """Agrega o actualiza un atributo directamente en el diccionario de un enemigo.

    Además, si el diccionario posee las claves "vida" y "defensa",
    calcula y guarda la clave "poder_total" como round(vida + defensa * 2, 2).
    Si clave es un string vacío (tras strip), no agrega esa clave pero igual
    actualiza "poder_total" en el diccionario si corresponde y lo retorna.

    Args:
        enemigo (dict): diccionario del enemigo (ej: {"nombre": "Ninja", "vida": 15, "defensa": 3.5}).
        clave (str): nombre del nuevo atributo.
        valor: valor del atributo a incorporar.

    Returns:
        dict: el mismo diccionario del enemigo actualizado.
    """
    pass


def aplicar_ataque_a_enemigo(enemigo, danio_bruto):
    """Aplica un ataque directamente sobre el diccionario de un enemigo considerando su defensa.

    El daño efectivo es max(0.0, danio_bruto - enemigo["defensa"]).
    La nueva vida es max(0.0, round(enemigo["vida"] - danio_efectivo, 2)).
    Modifica y retorna el diccionario del enemigo para que incluya:
    - sus claves previas (con "vida" actualizada),
    - "danio_recibido": round(danio_efectivo, 2),
    - "derrotado": True si la nueva vida es 0, False en caso contrario.

    Args:
        enemigo (dict): diccionario con al menos "nombre", "vida" y "defensa".
        danio_bruto (float | int): puntos de ataque antes de restar defensa.

    Returns:
        dict: el mismo diccionario del enemigo con su estado tras el ataque.
    """
    pass


def evaluar_asistencia_estudiante(registro, porcentaje_regular=75.0):
    """Evalúa la condición de asistencia de un estudiante a partir de su registro.

    El diccionario de entrada tiene las claves "Nombre", "Apellido", "Presentes", "Ausentes"
    (donde Presentes y Ausentes pueden venir como int o str numérico).

    Args:
        registro (dict): datos crudos de asistencia del estudiante.
        porcentaje_regular (float): porcentaje mínimo para ser "Regular" (default 75.0).

    Returns:
        dict: diccionario con:
            - "nombre_completo": "{Nombre} {Apellido}"
            - "presentes": int
            - "ausentes": int
            - "total_clases": int (presentes + ausentes)
            - "porcentaje_asistencia": float redondeado a 2 decimales (0.0 si total_clases == 0)
            - "condicion": "Regular" si porcentaje_asistencia >= porcentaje_regular, sino "Libre"
    """
    pass


def formatear_horario_materia(registro_materia):
    """Formatea los datos de cursada de una materia y calcula su duración en minutos.

    El diccionario tiene las claves: "Materia", "Hora entrada", "Hora salida", "Profesor".
    Las horas tienen formato "HH:MM" (24 hs).

    Args:
        registro_materia (dict[str, str]): datos de la materia.

    Returns:
        dict: diccionario con:
            - "resumen": "Materia: {Materia} Ingreso: {Hora entrada} Egreso: {Hora salida} Profesor/a: {Profesor}"
            - "duracion_minutos": int con la diferencia en minutos entre salida y entrada.
    """
    pass


def calcular_horas_trabajadas(registro_horario):
    """Calcula el tiempo trabajado a partir de un registro de entrada y salida.

    El registro contiene: "Fecha", "Nombre", "Hora entrada", "Hora salida" (en formato "HH:MM").

    Args:
        registro_horario (dict[str, str]): registro de asistencia laboral.

    Returns:
        dict: diccionario con:
            - "fecha": str
            - "nombre": str
            - "minutos_trabajados": int
            - "horas_trabajadas": float (minutos / 60 redondeado a 2 decimales)
    """
    pass


def normalizar_contacto_agenda(registro_agenda):
    """Normaliza y valida un contacto proveniente de una agenda.

    El diccionario de entrada tiene: "Nombre", "Apellido", "Localidad", "Telefono".
    Reglas:
    - Limpia espacios laterales de todos los campos.
    - En el teléfono, elimina guiones "-" y espacios internos " ".
    - El teléfono se considera válido si tras limpiarlo contiene únicamente dígitos
      y su longitud es de al menos 8 caracteres.

    Args:
        registro_agenda (dict[str, str]): contacto crudo.

    Returns:
        dict: diccionario con:
            - "nombre_completo": "{Apellido}, {Nombre}"
            - "localidad": str
            - "telefono": str (limpio)
            - "valido": bool
    """
    pass


def procesar_operacion_sube(cuenta_sube, tipo_operacion, monto):
    """Procesa una recarga o el cobro de un boleto directamente sobre una tarjeta SUBE.

    Opera modificando el diccionario recibido y retornándolo:
    - Si monto <= 0: la operación falla con mensaje "Monto inválido".
    - Si tipo_operacion == "recarga": suma el monto al saldo, mantiene "viajes_realizados"
      y guarda mensaje "Recarga acreditada. Saldo: ${nuevo_saldo}".
    - Si tipo_operacion == "viaje":
        * Si saldo >= monto: descuenta monto, incrementa "viajes_realizados" en 1 y
          guarda mensaje "Viaje cobrado. Saldo restante: ${nuevo_saldo}".
        * Si saldo < monto: no modifica saldo ni viajes, operación falla con mensaje
          "Saldo insuficiente".
    - Cualquier otro tipo_operacion falla con mensaje "Operación desconocida".

    Args:
        cuenta_sube (dict): {"titular": str, "saldo": float, "viajes_realizados": int}.
        tipo_operacion (str): "recarga" o "viaje".
        monto (float | int): importe de la operación.

    Returns:
        dict: el diccionario cuenta_sube actualizado con {"titular": str,
              "saldo": float (redondeado a 2 dec), "viajes_realizados": int,
              "exito": bool, "mensaje": str}.
    """
    pass


# ---------------------------------------------------------------------------
# Sección 2: Búsqueda y filtrado sobre listas de diccionarios
# ---------------------------------------------------------------------------


def detectar_pokemones_debilitados_dict(pokemones_salvajes, vida_maxima=12):
    """Reporta los pokémon debilitados a partir de una lista de diccionarios.

    Cada diccionario tiene las claves: "nombre", "tipos", "vida".
    Se considera debilitado cuando vida <= vida_maxima.

    Args:
        pokemones_salvajes (list[dict]): lista de pokémon en el área.
        vida_maxima (int): puntos de vida máximos para considerarlo debilitado (default 12).

    Returns:
        list[str]: cada elemento tiene las 3 líneas unidas por "\\n":
                   "¡Hay un {nombre} debilitado cerca!\\nLe quedan {vida} puntos de vida\\nY sus tipos son {tipos}"
    """
    pass


def filtrar_pokemones_por_tipo(pokemones_salvajes, tipo_buscado):
    """Filtra los pokémon que poseen un tipo determinado (simple o compuesto).

    El campo "tipos" puede contener un único tipo (ej: "bicho") o dos separados
    por barra (ej: "roca/tierra"). La comparación ignora mayúsculas/minúsculas.

    Args:
        pokemones_salvajes (list[dict]): lista de diccionarios de pokémon.
        tipo_buscado (str): tipo elemental a buscar (ej: "tierra", "eléctrico").

    Returns:
        list[str]: lista con los nombres de los pokémon que poseen ese tipo,
                   en orden de aparición.
    """
    pass


def resumen_tipos_pokemones(pokemones_salvajes):
    """Cuenta cuántos pokémon hay de cada tipo individual en el área.

    Si un pokémon tiene "tipos": "roca/tierra", suma 1 tanto a "roca" como a "tierra"
    (normalizados en minúsculas).

    Args:
        pokemones_salvajes (list[dict]): lista de diccionarios con clave "tipos".

    Returns:
        dict[str, int]: diccionario {tipo_en_minusculas: cantidad}.
    """
    pass


def filtrar_contactos_por_localidad(agenda, localidad_buscada):
    """Obtiene los contactos de una localidad específica.

    La comparación de localidad ignora mayúsculas/minúsculas y espacios laterales.

    Args:
        agenda (list[dict]): lista de diccionarios con claves "Nombre", "Apellido",
                             "Localidad", "Telefono".
        localidad_buscada (str): nombre de la localidad a filtrar.

    Returns:
        list[dict]: lista de contactos que pertenecen a esa localidad.
    """
    pass


def buscar_temas_musicales(catalogo, genero=None, precio_maximo=None, solo_disponibles=True):
    """Busca temas musicales en una tienda online aplicando múltiples filtros.

    Cada tema del catálogo es un dict:
    {"titulo": str, "genero": str, "duracion_seg": int, "precio": float, "disponible": bool}.

    Args:
        catalogo (list[dict]): lista de temas musicales.
        genero (str | None): si se especifica, filtra por ese género (case-insensitive).
        precio_maximo (float | None): si se especifica, filtra con precio <= precio_maximo.
        solo_disponibles (bool): si es True, exige disponible == True.

    Returns:
        list[str]: títulos de los temas que cumplen todos los criterios activos.
    """
    pass


def calcular_carrito_musica(catalogo, titulos_pedidos):
    """Procesa la compra de una lista de temas musicales contra el catálogo.

    Un tema puede comprarse si existe en el catálogo (comparación exacta de título)
    y tiene "disponible": True. No debe comprarse dos veces el mismo título si
    aparece repetido en titulos_pedidos.

    Args:
        catalogo (list[dict]): temas con "titulo", "duracion_seg", "precio", "disponible".
        titulos_pedidos (list[str]): títulos solicitados por el cliente.

    Returns:
        dict: {
            "comprados": list[str],
            "no_disponibles": list[str],
            "total_pagar": float (redondeado a 2 decimales),
            "duracion_total_seg": int
        }
    """
    pass


def filtrar_peliculas_recomendadas(peliculas, puntaje_minimo, anio_minimo, solo_atp=False):
    """Filtra películas que cumplan con puntaje, año de estreno y calificación ATP.

    Cada película es un dict: {"titulo": str, "anio": int, "puntaje": float, "atp": bool}.

    Args:
        peliculas (list[dict]): catálogo de películas.
        puntaje_minimo (float): puntaje mínimo requerido (>=).
        anio_minimo (int): año de estreno mínimo requerido (>=).
        solo_atp (bool): si es True, solo incluye películas con "atp" == True.

    Returns:
        list[str]: lista de títulos que cumplen las condiciones.
    """
    pass


def agrupar_peliculas_por_decada(peliculas):
    """Agrupa los títulos de las películas según su década de estreno.

    Por ejemplo, un estreno de 1994 pertenece a la clave "1990s", y uno de 2023 a "2020s".

    Args:
        peliculas (list[dict]): lista de dicts con al menos "titulo" (str) y "anio" (int).

    Returns:
        dict[str, list[str]]: diccionario {decada: [titulos]} respetando el orden de aparición.
    """
    pass


# ---------------------------------------------------------------------------
# Sección 3: Agregaciones, cruces de datos y reportes con diccionarios
# ---------------------------------------------------------------------------


def liquidar_jornada_empleados(registros_horarios, valor_hora):
    """Acumula las horas trabajadas por empleado y calcula su liquidación en pesos.

    Cada registro tiene "Fecha", "Nombre", "Hora entrada", "Hora salida" ("HH:MM").

    Args:
        registros_horarios (list[dict]): lista de fichadas de empleados.
        valor_hora (float | int): monto abonado por cada hora trabajada.

    Returns:
        dict[str, dict]: diccionario {nombre: {"horas": float, "pago": float}}
                         con ambos valores redondeados a 2 decimales.
    """
    pass


def combinar_listas_paralelas_en_inventario(articulos, precios, stocks):
    """Convierte tres listas paralelas en una lista de diccionarios de inventario.

    Solo incluye aquellos productos donde precio > 0 y stock >= 0.
    Si las listas tienen distinta longitud, procesa hasta la longitud de la más corta.

    Args:
        articulos (list[str]): nombres de los artículos.
        precios (list[float | int]): precios unitarios.
        stocks (list[int]): cantidades disponibles.

    Returns:
        list[dict]: lista de dicts con claves:
                    "articulo", "precio" (float), "stock" (int),
                    "valor_total" (float redondeado a 2 decimales = precio * stock).
    """
    pass


def procesar_pedido_quiosco(inventario, pedido):
    """Procesa un pedido de varios artículos descontando stock directamente sobre el inventario.

    El inventario tiene formato: {articulo: {"precio": float, "stock": int}}.
    El pedido tiene formato: {articulo: cantidad_pedida}.
    Un ítem del pedido se entrega solo si el artículo existe en inventario,
    cantidad_pedida > 0 y stock >= cantidad_pedida; en caso contrario se agrega a "rechazados".

    Args:
        inventario (dict[str, dict]): inventario de artículos a actualizar.
        pedido (dict[str, int]): cantidades solicitadas por artículo.

    Returns:
        dict: {
            "total": float (redondeado a 2 decimales),
            "entregados": list[str],
            "rechazados": list[str],
            "inventario_actualizado": dict (el inventario con los stocks descontados)
        }
    """
    pass


def estadisticas_notas_por_materia(registros_notas, nota_aprobacion=7.0):
    """Agrupa las calificaciones por materia y calcula sus indicadores estadísticos.

    Cada registro tiene: {"nombre": str, "materia": str, "nota": float | str}.

    Args:
        registros_notas (list[dict]): filas de notas de los estudiantes.
        nota_aprobacion (float): nota mínima para aprobar (default 7.0).

    Returns:
        dict[str, dict]: por cada materia retorna:
            {
                "promedio": float (redondeado a 2 decimales),
                "maxima": float,
                "minima": float,
                "aprobados": int (nota >= nota_aprobacion),
                "desaprobados": int (nota < nota_aprobacion)
            }
    """
    pass


def obtener_mejores_promedios(registros_notas, promedio_minimo=7.0):
    """Calcula el promedio general de cada estudiante y filtra los que alcanzan el mínimo.

    Cada registro tiene: {"nombre": str, "materia": str, "nota": float | str}.

    Args:
        registros_notas (list[dict]): calificaciones de estudiantes en distintas materias.
        promedio_minimo (float): promedio mínimo para ser incluido (default 7.0).

    Returns:
        list[dict]: lista de diccionarios en orden de aparición del estudiante:
                    [{"nombre": str, "promedio": float (2 dec), "cantidad_materias": int}]
                    solo para quienes tengan promedio >= promedio_minimo.
    """
    pass


def ranking_jugadores_por_dificultad(partidas_dict):
    """Resume las estadísticas de una tabla de puntajes agrupando por dificultad.

    Cada elemento de partidas_dict es: {"jugador": str, "puntaje": int, "dificultad": str}.

    Args:
        partidas_dict (list[dict]): historial de partidas jugadas.

    Returns:
        dict[str, dict]: por cada dificultad retorna:
            {
                "mejor_jugador": str (en caso de empate, el primero),
                "mejor_puntaje": int,
                "promedio_puntaje": float (redondeado a 2 decimales),
                "partidas_jugadas": int
            }
    """
    pass


def cruzar_estudiantes_y_cursos(dni_estudiantes, cursos_estudiantes):
    """Unifica dos listas de diccionarios de estudiantes a través de su nombre.

    - dni_estudiantes contiene dicts: {"nombre": str, "dni": int}
    - cursos_estudiantes contiene dicts: {"nombre": str, "anio": int, "division": str}

    Solo incluye a los estudiantes que aparecen en ambas listas.

    Args:
        dni_estudiantes (list[dict]): registros con nombre y DNI.
        cursos_estudiantes (list[dict]): registros con nombre, año y división.

    Returns:
        list[dict]:[{"nombre": str, "dni": int, "curso": "{anio}{division}"}]
                   en el orden de dni_estudiantes.
    """
    pass


def auditar_componentes_pc(componentes, stock_minimo):
    """Audita el inventario de componentes de PC del depósito escolar.

    Cada componente es un dict:
    {"componente": str, "categoria": str, "cantidad": int, "estado": str}.
    - Solo se contabilizan en "total_operativos" y "por_categoria" aquellos con
      estado == "operativo" (case-insensitive).
    - Un componente operativo se incluye en "faltantes" si su cantidad < stock_minimo.
    - Los componentes cuyo estado no sea "operativo" también se incluyen en "faltantes"
      si no hay otro registro operativo suficiente, o directamente si están en la lista
      con cantidad operativa < stock_minimo (evaluar cada fila: si estado != "operativo"
      su cantidad operativa efectiva es 0, por lo que si stock_minimo > 0 entra en "faltantes").

    Args:
        componentes (list[dict]): inventario del laboratorio.
        stock_minimo (int): cantidad operativa mínima requerida por ítem.

    Returns:
        dict: {
            "faltantes": list[str],
            "total_operativos": int,
            "por_categoria": dict[str, int]
        }
    """
    pass
