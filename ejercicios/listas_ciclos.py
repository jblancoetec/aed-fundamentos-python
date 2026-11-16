"""
Módulo de ejercicios: Listas, ciclos, listas paralelas y listas de listas (matrices).

Todos los ejercicios tienen una dificultad media-elevada y están basados en las
guías y evaluaciones de Algoritmos y Estructuras de Datos (AED) y Taller de
Algoritmos y Programación (TAP).
"""


# ---------------------------------------------------------------------------
# Sección 1: Recorridos con ciclos, indexación y secuencias
# ---------------------------------------------------------------------------


def buscar_indice_caracter(texto, caracter):
    """Busca la primera aparición de un carácter dentro de un string.

    Recorre la cadena por índice y retorna la posición (0-based) de la primera
    coincidencia exacta (distingue mayúsculas, minúsculas y tildes).

    Args:
        texto (str): cadena de texto donde buscar.
        caracter (str): carácter de longitud 1 a localizar.

    Returns:
        int: primer índice donde aparece caracter, o -1 si no se encuentra
             o si caracter no tiene longitud 1.
    """
    pass


def obtener_indices_validos(secuencia):
    """Calcula todos los índices válidos (positivos y negativos) de una secuencia.

    Args:
        secuencia (list | str): lista o cadena de texto.

    Returns:
        tuple[list[int], list[int]]: tupla (indices_positivos, indices_negativos)
            donde indices_positivos va de 0 a len(secuencia) - 1, e
            indices_negativos va de -len(secuencia) a -1.
            Si la secuencia está vacía, retorna ([], []).
    """
    pass


def seleccionar_colores_pintureria(colores, indice_primero, indice_segundo):
    """Selecciona dos colores de una carta de pinturería validando los índices.

    Acepta tanto índices positivos (0 a n-1) como negativos (-n a -1).

    Args:
        colores (list[str]): lista de colores disponibles.
        indice_primero (int): índice del primer color elegido.
        indice_segundo (int): índice del segundo color elegido.

    Returns:
        str: "Pedido de pintura: {color1} y {color2}" si ambos índices son válidos
             y la lista no está vacía; o "Error: índice fuera de rango" en caso
             contrario.
    """
    pass


def generar_secuencia_descendente_filtrada(inicio, fin, paso, divisor):
    """Genera números descendiendo desde inicio hasta fin y filtra los negativos múltiplos de divisor.

    Recorre desde inicio hasta fin (inclusive) restando paso en cada iteración,
    y conserva únicamente los números que sean estrictamente negativos (< 0) y
    divisibles por divisor.

    Args:
        inicio (int): valor inicial del recorrido (debe ser >= fin).
        fin (int): valor límite inferior del recorrido (inclusive).
        paso (int): cantidad positiva que se descuenta en cada paso (> 0).
        divisor (int): número distinto de 0 por el cual deben ser múltiplos.

    Returns:
        list[int]: lista de enteros negativos múltiplos de divisor en orden de aparición.
                   Si paso <= 0, divisor == 0 o inicio < fin, retorna [].
    """
    pass


def generar_impares_en_rango(inicio, fin):
    """Genera todos los números impares entre inicio y fin (ambos inclusive).

    Si inicio <= fin, la secuencia es ascendente.
    Si inicio > fin, la secuencia es descendente.

    Args:
        inicio (int): extremo inicial del rango.
        fin (int): extremo final del rango.

    Returns:
        list[int]: lista de números impares en el orden correspondiente.
    """
    pass


def invertir_lista_con_indices(elementos):
    """Retorna una nueva lista con los elementos en orden inverso, sin modificar la original.

    Args:
        elementos (list): lista de elementos (por ejemplo, artículos ordenados por precio).

    Returns:
        list: nueva lista con los elementos desde el último hasta el primero.
    """
    pass


# ---------------------------------------------------------------------------
# Sección 2: Filtrado, conteo y manipulación de listas simples
# ---------------------------------------------------------------------------


def filtrar_y_contar_bioma(niveles, bioma_buscado):
    """Cuenta cuántas veces aparece un bioma en el mapa y en qué posiciones.

    La comparación ignora mayúsculas/minúsculas y espacios laterales.

    Args:
        niveles (list[str]): lista de nombres de biomas en el mapa.
        bioma_buscado (str): nombre del bioma a contabilizar.

    Returns:
        tuple[int, list[int]]: tupla (cantidad_apariciones, lista_de_indices).
    """
    pass


def reporte_ventas_satisfactorias(ventas, venta_minima):
    """Evalúa cuántas ventas superan estrictamente la venta mínima esperada.

    Args:
        ventas (list[float | int]): montos de las ventas realizadas.
        venta_minima (float | int): umbral que debe superarse (> venta_minima).

    Returns:
        str: resumen con formato "{satisfactorias}/{total} ventas satisfactorias".
    """
    pass


def reporte_notas_desaprobadas(notas, nota_minima=7.0):
    """Calcula la cantidad, el porcentaje y el mensaje de notas desaprobadas.

    Una nota está desaprobada si es estrictamente menor a nota_minima (< nota_minima).

    Args:
        notas (list[float | int]): lista de calificaciones.
        nota_minima (float): nota mínima para aprobar (default 7.0).

    Returns:
        tuple[int, float, str]: tupla (desaprobados, porcentaje, mensaje) donde:
            - desaprobados (int): cantidad de notas menores a nota_minima.
            - porcentaje (float): porcentaje sobre el total redondeado a 2 decimales
              (0.0 si la lista está vacía).
            - mensaje (str): "{desaprobados}/{total} notas desaprobadas".
    """
    pass


def depurar_alturas_pacientes(alturas, indice_a_quitar, valor_a_quitar):
    """Realiza dos bajas sobre una copia de la lista de alturas de pacientes.

    1) Si indice_a_quitar es un índice válido (positivo o negativo) de la lista,
       elimina el elemento en esa posición (como pop).
    2) Luego, si valor_a_quitar está presente en la lista restante, elimina su
       primera aparición (como remove).

    No debe modificar la lista recibida por parámetro.

    Args:
        alturas (list[float]): lista original de alturas.
        indice_a_quitar (int): posición a eliminar en primer lugar.
        valor_a_quitar (float): valor a eliminar en segundo lugar.

    Returns:
        list[float]: nueva lista resultante luego de aplicar ambas operaciones.
    """
    pass


def actualizar_lista_compras(lista_actual, nuevos_articulos, articulos_cancelados):
    """Actualiza una lista de compras agregando nuevos ítems y quitando cancelados.

    1) Parte de una copia de lista_actual (limpiando espacios laterales de cada ítem).
    2) Agrega al final cada artículo de nuevos_articulos (limpio con strip) siempre
       que no sea una cadena vacía y no esté ya presente en la lista.
    3) Elimina todos los artículos que figuren en articulos_cancelados (comparando
       sin distinguir mayúsculas/minúsculas).

    Args:
        lista_actual (list[str]): artículos inicialmente cargados.
        nuevos_articulos (list[str]): artículos a incorporar.
        articulos_cancelados (list[str]): artículos a dar de baja.

    Returns:
        list[str]: lista de compras actualizada preservando el orden.
    """
    pass


# ---------------------------------------------------------------------------
# Sección 3: Listas paralelas
# ---------------------------------------------------------------------------


def consultar_precio_articulo(articulos, precios, nombre_articulo):
    """Busca el precio de un artículo en dos listas paralelas.

    La búsqueda del nombre ignora mayúsculas/minúsculas y espacios laterales.

    Args:
        articulos (list[str]): nombres de los artículos en venta.
        precios (list[float | int]): precios correspondientes a cada artículo.
        nombre_articulo (str): artículo cuyo precio se desea conocer.

    Returns:
        float | int | None: el precio del artículo, o None si no existe.
    """
    pass


def buscar_articulo_por_precio(articulos, precios, precio_buscado):
    """Retorna el nombre del primer artículo que tiene exactamente el precio buscado.

    Args:
        articulos (list[str]): nombres de los artículos en venta.
        precios (list[float | int]): precios correspondientes.
        precio_buscado (float | int): valor exacto a localizar.

    Returns:
        str | None: nombre del primer artículo que coincide, o None si no hay ninguno.
    """
    pass


def cobrar_expendedora_golosinas(articulos, precios, indice_articulo, dinero_depositado):
    """Simula la compra de una golosina en una máquina expendedora con listas paralelas.

    Reglas:
    - Solo se aceptan índices no negativos dentro del rango (0 <= indice_articulo < len).
      Si el índice es inválido, retorna:
      "Opción inválida. Se devuelven ${dinero_depositado}"
    - Si dinero_depositado >= precio del artículo, retorna:
      "Entregando {articulo}. Su vuelto es ${vuelto}"
    - Si dinero_depositado < precio del artículo, retorna:
      "No alcanza para {articulo} (${precio}). Se devuelven ${dinero_depositado}"

    Args:
        articulos (list[str]): nombres de las golosinas.
        precios (list[int | float]): precios de las golosinas.
        indice_articulo (int): número de opción elegida por el usuario.
        dinero_depositado (int | float): dinero ingresado en la máquina.

    Returns:
        str: mensaje resultante de la operación.
    """
    pass


def filtrar_articulos_accesibles(articulos, precios, presupuesto):
    """Obtiene los artículos cuyo precio no supera el presupuesto disponible.

    Args:
        articulos (list[str]): lista de nombres de artículos.
        precios (list[int | float]): lista paralela de precios.
        presupuesto (int | float): monto máximo disponible.

    Returns:
        list[str]: lista con formato "{articulo} (${precio})" para cada artículo
                   con precio <= presupuesto, respetando el orden original.
    """
    pass


# ---------------------------------------------------------------------------
# Sección 4: Listas de listas (matrices y tablas de registros)
# ---------------------------------------------------------------------------


def extraer_parametros_spr(enemigos, fila_x, col_x, fila_y, col_y, fila_id, col_id):
    """Extrae de una matriz de enemigos los valores (x, y, id_grafico) para invocar spr().

    Args:
        enemigos (list[list[int]]): matriz numérica con datos de enemigos.
        fila_x (int): fila para la posición horizontal.
        col_x (int): columna para la posición horizontal.
        fila_y (int): fila para la posición vertical.
        col_y (int): columna para la posición vertical.
        fila_id (int): fila para el identificador del gráfico.
        col_id (int): columna para el identificador del gráfico.

    Returns:
        tuple[int, int, int] | None: tupla (posicion_horizontal, posicion_vertical, grafico_id),
            o None si alguna coordenada está fuera de rango.
    """
    pass


def detectar_pokemones_debilitados_lista(pokemones_salvajes, vida_maxima=20):
    """Detecta los pokémon salvajes debilitados dentro de una lista de listas.

    Cada elemento de pokemones_salvajes tiene el formato: [nombre, tipos, vida].
    Un pokémon se considera debilitado si su vida es menor o igual a vida_maxima.

    Args:
        pokemones_salvajes (list[list]): lista de sublistas [nombre, tipos, vida].
        vida_maxima (int): umbral máximo de vida para considerarlo debilitado (default 20).

    Returns:
        list[str]: mensajes con formato
                   "¡Hay un {nombre} debilitado cerca! Le quedan {vida} puntos de vida"
                   en el orden en que aparecen.
    """
    pass


def detectar_animales_por_categoria(animales, categoria_buscada="insecto"):
    """Identifica los animales de una categoría específica en una lista de avistamientos.

    Cada sublista de animales tiene el formato: [nombre, especie, nivel_peligrosidad].
    La comparación de especie ignora mayúsculas/minúsculas.

    Args:
        animales (list[list]): lista de sublistas [nombre, especie, peligrosidad].
        categoria_buscada (str): especie a filtrar (default "insecto").

    Returns:
        list[str]: mensajes con formato
                   "¡Detectado un {especie}! Especie: {nombre}, nivel de peligrosidad: {peligrosidad}"
                   para cada coincidencia.
    """
    pass


def obtener_animal_mas_peligroso(animales, especie_filtro=None):
    """Encuentra el animal con mayor nivel de peligrosidad, opcionalmente filtrado por especie.

    Cada sublista tiene el formato: [nombre, especie, peligrosidad].
    Si hay empate, conserva el primero que apareció.

    Args:
        animales (list[list]): lista de sublistas [nombre, especie, peligrosidad].
        especie_filtro (str | None): si no es None, solo evalúa animales de esa especie
                                     (ignorando mayúsculas/minúsculas).

    Returns:
        list | None: la sublista [nombre, especie, peligrosidad] del animal más peligroso,
                     o None si ningún animal cumple el filtro.
    """
    pass


def formatear_tabla_puntajes(partidas, dificultad_filtro=None):
    """Formatea una tabla de puntajes almacenada como lista de listas.

    Cada sublista de partidas tiene el formato: [puntaje, nombre_jugador, dificultad].
    Si dificultad_filtro no es None, solo incluye las partidas de esa dificultad
    (comparando sin distinguir mayúsculas/minúsculas).
    La numeración del puesto comienza en 1 sobre las partidas filtradas.

    Args:
        partidas (list[list]): lista de sublistas [puntaje, jugador, dificultad].
        dificultad_filtro (str | None): dificultad a filtrar ("fácil", "difícil", etc.) o None.

    Returns:
        list[str]: líneas con formato "{puesto}. {jugador} - {puntaje} pts ({dificultad})".
    """
    pass


def obtener_mejor_partida(partidas, dificultad_filtro=None):
    """Obtiene la partida con el puntaje más alto de la tabla.

    Cada sublista tiene el formato: [puntaje, nombre_jugador, dificultad].

    Args:
        partidas (list[list]): lista de sublistas [puntaje, jugador, dificultad].
        dificultad_filtro (str | None): si se indica, filtra primero por esa dificultad.

    Returns:
        list | None: sublista [puntaje, jugador, dificultad] de mayor puntaje,
                     o None si no hay partidas que coincidan.
    """
    pass


def buscar_estudiante_por_dni(dni_estudiantes, dni_buscado):
    """Busca el nombre de un estudiante a partir de su DNI en una lista de listas.

    Cada sublista de dni_estudiantes tiene el formato: [nombre_completo, dni].

    Args:
        dni_estudiantes (list[list]): lista de pares [nombre, dni].
        dni_buscado (int): número de documento a buscar.

    Returns:
        str | None: nombre del estudiante correspondiente, o None si no se encuentra.
    """
    pass


def agrupar_estudiantes_por_curso(cursos_estudiantes, anio, division):
    """Obtiene los nombres de todos los estudiantes que pertenecen a un año y división.

    Cada sublista de cursos_estudiantes tiene el formato: [nombre, anio, division].
    La comparación de división ignora mayúsculas/minúsculas.

    Args:
        cursos_estudiantes (list[list]): lista de sublistas [nombre, anio, division].
        anio (int): año de cursada (ej: 4).
        division (str): letra de división (ej: "B").

    Returns:
        list[str]: nombres de los estudiantes de ese curso en orden de aparición.
    """
    pass


def filtrar_computadoras_por_requisitos(computadoras, ram_minima_gb, precio_maximo, requiere_ssd=True):
    """Filtra especificaciones técnicas de computadoras almacenadas en una lista de listas.

    Cada sublista de computadoras tiene el formato:
    [modelo (str), ram_gb (int), precio (float), tiene_ssd (bool)].

    Args:
        computadoras (list[list]): lista de especificaciones de PCs.
        ram_minima_gb (int): memoria RAM mínima requerida (>=).
        precio_maximo (float): presupuesto máximo permitido (<=).
        requiere_ssd (bool): si es True, solo acepta equipos con tiene_ssd == True;
                             si es False, acepta con o sin SSD.

    Returns:
        list[str]: nombres de los modelos que cumplen todos los requisitos.
    """
    pass
