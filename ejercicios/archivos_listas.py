"""
Modulo de ejercicios: Lectura de archivos y tratamiento con listas.

Los ejercicios siguen una progresion de dificultad:

Nivel 1 - Lectura basica de archivos de texto plano.
Nivel 2 - Lectura de archivos CSV con un solo registro (encabezado + 1 fila):
           lectura cruda, acceso por indice, acceso por nombre, conversion
           de tipos, validacion de campos y formato del registro.
Nivel 3 - Lectura de archivos CSV con varios registros (listas y diccionarios).
Nivel 4 - Filtros, busquedas y agregaciones sobre el contenido del CSV.
"""


def leer_primera_linea(ruta):
    """Lee y retorna la primera linea de un archivo de texto, sin el salto de linea final.

    Args:
        ruta (str): ruta al archivo de texto.

    Returns:
        str: contenido de la primera linea (sin el "\\n" final).
             Si el archivo esta vacio, retorna "".
    """
    pass


def leer_lineas(ruta):
    """Lee todas las lineas de un archivo y las retorna como una lista de strings.

    Cada linea se entrega sin el salto de linea final ("\\n").
    El orden de la lista coincide con el orden del archivo.

    Args:
        ruta (str): ruta al archivo de texto.

    Returns:
        list[str]: lista con cada linea del archivo, en orden.
    """
    pass


def contar_lineas(ruta):
    """Cuenta la cantidad de lineas (registros) de un archivo de texto.

    Una linea es cualquier secuencia terminada en "\\n". La ultima linea
    del archivo se cuenta aunque no termine en "\\n". Un archivo vacio
    retorna 0.

    Args:
        ruta (str): ruta al archivo de texto.

    Returns:
        int: cantidad de lineas del archivo.
    """
    pass


def leer_csv_primera_fila(ruta):
    """Lee un archivo CSV con encabezado y una unica fila de datos.

    Ignora la primera linea (encabezado) y retorna los campos de la
    segunda linea (los datos) ya separados por coma.

    Args:
        ruta (str): ruta al archivo CSV.

    Returns:
        list[str]: valores de la unica fila de datos.
    """
    pass


def leer_csv_primera_fila_como_dict(ruta):
    """Lee un CSV con encabezado y una unica fila, retornando un diccionario.

    Combina la primera linea (encabezado) con la segunda linea (datos)
    para formar un dict de la forma {campo: valor}.

    Args:
        ruta (str): ruta al archivo CSV.

    Returns:
        dict[str, str]: pares campo:valor de la unica fila de datos.
    """
    pass


def obtener_campo_por_indice(ruta, indice):
    """Retorna el valor de un campo de la unica fila, accediendo por su posicion.

    La primera columna (indice 0) es el primer campo del encabezado.

    Args:
        ruta (str): ruta al archivo CSV.
        indice (int): posicion (0-based) del campo a obtener.

    Returns:
        str: valor del campo en la posicion indicada.
    """
    pass


def obtener_campo_por_nombre(ruta, nombre_campo):
    """Retorna el valor de un campo de la unica fila, accediendo por nombre.

    Busca el nombre en el encabezado y devuelve el valor correspondiente
    de la fila de datos.

    Args:
        ruta (str): ruta al archivo CSV.
        nombre_campo (str): nombre del encabezado a buscar.

    Returns:
        str: valor del campo cuyo encabezado coincide con nombre_campo.
    """
    pass


def contar_campos_csv(ruta):
    """Cuenta cuantos campos (columnas) tiene la fila de datos.

    No incluye el encabezado en el conteo: equivale al numero de columnas
    declaradas en la primera linea del archivo.

    Args:
        ruta (str): ruta al archivo CSV.

    Returns:
        int: cantidad de campos del registro.
    """
    pass


def obtener_encabezados_csv(ruta):
    """Retorna la lista de nombres de las columnas (encabezado) del CSV.

    Args:
        ruta (str): ruta al archivo CSV.

    Returns:
        list[str]: lista con los nombres de las columnas en orden.
    """
    pass


def convertir_campo_a_int(ruta, nombre_campo):
    """Retorna el valor de un campo convertido a entero.

    Args:
        ruta (str): ruta al archivo CSV.
        nombre_campo (str): nombre del campo cuyo valor se convertira a int.

    Returns:
        int: valor del campo convertido a entero.
    """
    pass


def convertir_campo_a_float(ruta, nombre_campo):
    """Retorna el valor de un campo convertido a numero decimal (float).

    Args:
        ruta (str): ruta al archivo CSV.
        nombre_campo (str): nombre del campo cuyo valor se convertira a float.

    Returns:
        float: valor del campo convertido a float.
    """
    pass


def campo_existe_csv(ruta, nombre_campo):
    """Verifica si un nombre de columna aparece en el encabezado del CSV.

    Args:
        ruta (str): ruta al archivo CSV.
        nombre_campo (str): nombre de columna a buscar.

    Returns:
        bool: True si nombre_campo esta en el encabezado, False en caso contrario.
    """
    pass


def formato_registro_csv(ruta):
    """Retorna el unico registro del CSV como una cadena formateada.

    El formato es "clave=valor, clave=valor, ...", donde cada par
    clave=valor corresponde a un campo del registro.

    Args:
        ruta (str): ruta al archivo CSV.

    Returns:
        str: representacion del registro en formato "clave=valor".
    """
    pass


def leer_csv_como_matriz(ruta):
    """Lee un archivo CSV completo y lo retorna como una matriz (lista de listas).

    La primera sublista corresponde al encabezado y las siguientes a
    cada fila de datos. No se omite ninguna linea.

    Args:
        ruta (str): ruta al archivo CSV.

    Returns:
        list[list[str]]: cada linea del CSV como una lista de campos.
    """
    pass


def leer_csv_como_lista_diccionarios(ruta):
    """Lee un CSV con varias filas y lo retorna como una lista de diccionarios.

    La primera linea del archivo es el encabezado; cada fila siguiente
    produce un diccionario {campo: valor}.

    Args:
        ruta (str): ruta al archivo CSV.

    Returns:
        list[dict[str, str]]: una entrada por cada fila de datos.
    """
    pass


def obtener_columna_csv(ruta, indice_columna):
    """Lee un CSV y retorna todos los valores de una columna (excluyendo el encabezado).

    Args:
        ruta (str): ruta al archivo CSV.
        indice_columna (int): indice (0-based) de la columna a extraer.

    Returns:
        list[str]: valores de la columna en el orden de aparicion en el archivo.
    """
    pass


def filtrar_csv_por_columna(ruta, indice_columna, valor):
    """Retorna las filas de un CSV cuya columna indicada tiene el valor dado.

    Args:
        ruta (str): ruta al archivo CSV.
        indice_columna (int): indice (0-based) de la columna a filtrar.
        valor (str): valor exacto que debe tener esa columna.

    Returns:
        list[dict[str, str]]: filas completas (como dict) que cumplen el filtro.
    """
    pass


def contar_coincidencias_csv(ruta, indice_columna, valor):
    """Cuenta cuantas filas de un CSV tienen un valor especifico en una columna.

    Args:
        ruta (str): ruta al archivo CSV.
        indice_columna (int): indice (0-based) de la columna a evaluar.
        valor (str): valor exacto a buscar.

    Returns:
        int: cantidad de filas que cumplen.
    """
    pass


def buscar_registro_por_patron(ruta, indice_columna, patron):
    """Retorna el primer registro de un CSV cuya columna contenga el patron dado.

    La comparacion es por subcadena (case-sensitive): un valor de la columna
    "contiene" al patron si patron aparece como substring dentro del valor.

    Args:
        ruta (str): ruta al archivo CSV.
        indice_columna (int): indice (0-based) de la columna donde buscar.
        patron (str): texto a buscar como subcadena.

    Returns:
        dict[str, str] | None: el primer registro que cumple (como dict),
        o None si no hay coincidencias.
    """
    pass


def sumar_columna_numerica_csv(ruta, indice_columna):
    """Suma todos los valores numericos de una columna de un CSV (sin encabezado).

    Args:
        ruta (str): ruta al archivo CSV.
        indice_columna (int): indice (0-based) de la columna a sumar.

    Returns:
        float: suma de los valores convertidos a float.
    """
    pass


def promedio_columna_numerica_csv(ruta, indice_columna):
    """Calcula el promedio de los valores numericos de una columna de un CSV.

    Args:
        ruta (str): ruta al archivo CSV.
        indice_columna (int): indice (0-based) de la columna a promediar.

    Returns:
        float: promedio (suma / cantidad) redondeado a 2 decimales.
    """
    pass


def maximo_columna_numerica_csv(ruta, indice_columna):
    """Retorna el valor maximo de una columna numerica de un CSV.

    Args:
        ruta (str): ruta al archivo CSV.
        indice_columna (int): indice (0-based) de la columna.

    Returns:
        float: valor maximo encontrado en la columna.
    """
    pass
