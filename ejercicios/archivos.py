"""
Módulo de ejercicios: Rutas, archivos de texto (modos r, w, a) y archivos CSV.

Todos los ejercicios tienen una dificultad media-elevada y están basados en las
guías y evaluaciones de Algoritmos y Estructuras de Datos (AED).
"""


# ---------------------------------------------------------------------------
# Sección 1: Rutas de archivos (absolutas y relativas)
# ---------------------------------------------------------------------------


def clasificar_y_descomponer_ruta(ruta_archivo):
    """Analiza una ruta de archivo e identifica si es absoluta o relativa y sus partes.

    Reglas:
    - Es absoluta si luego de .strip() comienza con "/".
    - "carpetas" contiene todo el camino previo al último "/" (sin "/" al final),
      o "" si no hay ninguna carpeta en la ruta.
    - "archivo" es el nombre final luego del último "/".
    - "extension" es el texto después del último "." dentro de "archivo" (en minúsculas),
      o "" si el archivo no tiene punto.

    Args:
        ruta_archivo (str): ruta a analizar (ej: "/home/etec/Documentos/TIC-80/Juego.tic").

    Returns:
        dict: {
            "es_absoluta": bool,
            "carpetas": str,
            "archivo": str,
            "extension": str
        }
    """
    pass


def obtener_ruta_relativa(carpeta_proyecto, ruta_absoluta):
    """Calcula la ruta relativa de un archivo respecto de la carpeta base del proyecto.

    Por ejemplo:
    carpeta_proyecto = "/home/etec/Documentos/CentroMedico/"
    ruta_absoluta = "/home/etec/Documentos/CentroMedico/Ingresos/Guardia/pacientes.csv"
    -> "Ingresos/Guardia/pacientes.csv"

    Args:
        carpeta_proyecto (str): ruta absoluta del directorio base.
        ruta_absoluta (str): ruta absoluta completa hacia el archivo.

    Returns:
        str | None: ruta relativa sin "/" inicial, o None si ruta_absoluta no está
                    dentro de carpeta_proyecto.
    """
    pass


def construir_ruta_absoluta(carpeta_proyecto, ruta_relativa):
    """Construye la ruta absoluta uniendo la carpeta del proyecto y la ruta relativa.

    Debe evitar barras "/" duplicadas en la unión, incluso si carpeta_proyecto
    termina con "/" y ruta_relativa comienza con "/".

    Args:
        carpeta_proyecto (str): directorio base (ej: "/home/etec/Documentos/Escuela/").
        ruta_relativa (str): camino relativo (ej: "Notas/4B/arquitectura.csv" o "/Notas/4B/arquitectura.csv").

    Returns:
        str: ruta absoluta normalizada con una única "/" entre segmentos.
    """
    pass


# ---------------------------------------------------------------------------
# Sección 2: Lectura y escritura de archivos de texto (modos r, w, a)
# ---------------------------------------------------------------------------


def leer_mensaje_multilinea(ruta_archivo):
    """Lee un archivo de texto de múltiples renglones ignorando líneas en blanco.

    Elimina el salto de línea final y espacios laterales de cada renglón, y
    descarta los renglones que queden vacíos.

    Args:
        ruta_archivo (str): ruta al archivo de texto (ej: correo.txt o creditos.txt).

    Returns:
        dict: {
            "lineas": list[str],
            "cantidad_lineas": int,
            "texto_completo": str (líneas limpias unidas por "\\n")
        }
    """
    pass


def leer_cumpleanios_alternados(ruta_archivo):
    """Lee un archivo que alterna un renglón con el nombre y otro con la fecha de cumpleaños.

    Si al final queda un renglón suelto sin su par de fecha, se ignora.

    Args:
        ruta_archivo (str): ruta al archivo de cumpleaños.

    Returns:
        list[str]: lista de mensajes con formato
                   "El {fecha} es el cumpleaños de {nombre}".
    """
    pass


def leer_alarmas_alternadas(ruta_archivo):
    """Lee un archivo que alterna la hora de una alarma y su mensaje de recordatorio.

    Args:
        ruta_archivo (str): ruta al archivo de alarmas.

    Returns:
        list[dict]: lista de diccionarios con formato:
                    {"hora": str, "mensaje": str, "recordatorio": "Recordatorio: {mensaje} a las {hora}"}
    """
    pass


def registrar_medicion_meteorologica(ruta_archivo, temperatura, humedad):
    """Agrega una nueva medición meteorológica al archivo y retorna el historial completo.

    Resuelve el problema clásico de modos de apertura:
    1) Abre el archivo en modo "a" (append) y escribe:
       "Temp {temperatura}C, humedad {humedad}%\\n"
    2) Luego abre el archivo en modo "r" (lectura) y retorna todas las líneas
       no vacías sin el salto de línea final.

    Args:
        ruta_archivo (str): ruta al archivo de registro meteorológico.
        temperatura (float | int): temperatura del día en grados Celsius.
        humedad (float | int): porcentaje de humedad del día.

    Returns:
        list[str]: todas las mediciones registradas en el archivo (incluyendo la nueva).
    """
    pass


def registrar_compra_en_archivo(ruta_archivo, articulo, cantidad):
    """Registra una compra en modo append y calcula el total histórico de unidades compradas.

    Cada línea del archivo tiene el formato "{articulo} x{cantidad}\\n".
    Si articulo limpio es "" o cantidad <= 0, no escribe nada en el archivo y solo
    calcula el total actual si el archivo existe (o 0 si no existe).

    Args:
        ruta_archivo (str): ruta al archivo Compras.txt.
        articulo (str): nombre del producto comprado.
        cantidad (int): cantidad de unidades compradas.

    Returns:
        int: suma total de unidades (todas las cantidades luego de 'x') en el archivo.
    """
    pass


def sobrescribir_resumen_ventas(ruta_archivo, ventas, venta_minima):
    """Escribe en modo 'w' un reporte con las ventas que superan el mínimo y el resumen final.

    En el archivo se debe escribir:
    - Una línea "Venta aprobada: ${venta}\\n" por cada venta > venta_minima.
    - Una última línea "{satisfactorias}/{total} ventas satisfactorias\\n".

    Args:
        ruta_archivo (str): ruta donde se guardará el resumen.
        ventas (list[float | int]): lista de ventas.
        venta_minima (float | int): monto mínimo a superar.

    Returns:
        int: cantidad de ventas satisfactorias escritas.
    """
    pass


# ---------------------------------------------------------------------------
# Sección 3: Lectura y formateo de archivos CSV de evaluaciones AED
# ---------------------------------------------------------------------------


def formatear_asistencia_csv(ruta_archivo):
    """Lee un CSV de asistencia (Nombre,Apellido,Presentes,Ausentes) y formatea cada fila.

    Ignora el encabezado y elimina los saltos de línea.

    Args:
        ruta_archivo (str): ruta al archivo CSV.

    Returns:
        list[str]: líneas con formato
                   "Nombre: {Nombre} Apellido: {Apellido} Presentes: {Presentes} Ausentes: {Ausentes}".
    """
    pass


def formatear_materias_csv(ruta_archivo):
    """Lee un CSV de horarios de materias (Materia,Hora entrada,Hora salida,Profesor) y lo formatea.

    Ignora el encabezado y elimina los saltos de línea.

    Args:
        ruta_archivo (str): ruta al archivo CSV.

    Returns:
        list[str]: líneas con formato
                   "Materia: {Materia} Ingreso: {Hora entrada} Egreso: {Hora salida} Profesor/a: {Profesor}".
    """
    pass


def formatear_horarios_trabajo_csv(ruta_archivo):
    """Lee un CSV de fichadas laborales (Fecha,Nombre,Hora entrada,Hora salida) y lo formatea.

    Args:
        ruta_archivo (str): ruta al archivo CSV.

    Returns:
        list[str]: líneas con formato
                   "Fecha: {Fecha} Nombre: {Nombre} Entrada: {Hora entrada} Salida: {Hora salida}".
    """
    pass


def formatear_agenda_csv(ruta_archivo):
    """Lee un CSV de agenda (Nombre,Apellido,Localidad,Telefono) y formatea cada contacto.

    Args:
        ruta_archivo (str): ruta al archivo CSV.

    Returns:
        list[str]: líneas con formato
                   "Nombre: {Nombre} Apellido: {Apellido} Localidad: {Localidad} Telefono: {Telefono}".
    """
    pass


def leer_csv_como_matriz(ruta_archivo):
    """Lee un archivo CSV completo y lo retorna como una matriz (lista de listas de strings).

    Incluye el encabezado como primera sublista. Ignora líneas completamente vacías.

    Args:
        ruta_archivo (str): ruta al archivo CSV.

    Returns:
        list[list[str]]: matriz con los campos de cada fila limpios de saltos de línea.
    """
    pass


def leer_csv_como_diccionarios(ruta_archivo):
    """Lee un archivo CSV con encabezado y retorna una lista de diccionarios.

    Args:
        ruta_archivo (str): ruta al archivo CSV.

    Returns:
        list[dict[str, str]]: un diccionario {columna: valor} por cada fila de datos.
    """
    pass


# ---------------------------------------------------------------------------
# Sección 4: Procesamiento avanzado, filtros, agregaciones y escritura de CSV
# ---------------------------------------------------------------------------


def filtrar_csv_por_rango_numerico(ruta_archivo, nombre_columna, minimo, maximo):
    """Filtra las filas de un CSV cuyo valor numérico en nombre_columna está entre minimo y maximo.

    La comparación es inclusiva: minimo <= float(valor) <= maximo.

    Args:
        ruta_archivo (str): ruta al archivo CSV.
        nombre_columna (str): nombre del campo numérico en el encabezado.
        minimo (float | int): valor mínimo aceptado.
        maximo (float | int): valor máximo aceptado.

    Returns:
        list[dict[str, str]]: registros que cumplen la condición.
    """
    pass


def buscar_registros_por_patron_csv(ruta_archivo, nombre_columna, patron):
    """Busca todos los registros de un CSV donde la columna indicada contenga el patrón.

    La búsqueda por subcadena ignora mayúsculas y minúsculas.

    Args:
        ruta_archivo (str): ruta al archivo CSV.
        nombre_columna (str): nombre de la columna donde buscar.
        patron (str): subcadena a localizar.

    Returns:
        list[dict[str, str]]: lista de diccionarios que coinciden con el patrón.
    """
    pass


def estadisticas_columna_csv(ruta_archivo, nombre_columna):
    """Calcula suma, promedio, máximo, mínimo y cantidad sobre una columna numérica de un CSV.

    Args:
        ruta_archivo (str): ruta al archivo CSV.
        nombre_columna (str): columna cuyos valores se convertirán a float.

    Returns:
        dict | None: {
            "suma": float (redondeado a 2 decimales),
            "promedio": float (redondeado a 2 decimales),
            "maximo": float,
            "minimo": float,
            "cantidad": int
        }, o None si no hay filas de datos o la columna no existe.
    """
    pass


def calcular_asistencia_curso_csv(ruta_archivo, porcentaje_minimo=75.0):
    """Procesa un CSV de asistencia y clasifica a los alumnos en regulares y libres.

    El CSV tiene las columnas: Nombre,Apellido,Presentes,Ausentes.
    El porcentaje de cada alumno es Presentes / (Presentes + Ausentes) * 100.

    Args:
        ruta_archivo (str): ruta al archivo CSV de asistencia.
        porcentaje_minimo (float): umbral para condición regular (default 75.0).

    Returns:
        dict: {
            "regulares": list[str] ("{Nombre} {Apellido}"),
            "libres": list[str] ("{Nombre} {Apellido}"),
            "promedio_asistencia": float (promedio de porcentajes redondeado a 2 decimales)
        }
    """
    pass


def agrupar_csv_por_columna(ruta_archivo, columna_clave):
    """Agrupa todos los registros de un CSV en un diccionario según el valor de una columna.

    Args:
        ruta_archivo (str): ruta al archivo CSV.
        columna_clave (str): nombre de la columna por la cual agrupar.

    Returns:
        dict[str, list[dict[str, str]]]: diccionario {valor_columna: [registros]}.
    """
    pass


def exportar_diccionarios_a_csv(ruta_destino, encabezados, registros):
    """Escribe una lista de diccionarios en un archivo CSV respetando el orden de encabezados.

    Args:
        ruta_destino (str): ruta donde se creará/sobrescribirá el CSV.
        encabezados (list[str]): nombres de las columnas en orden.
        registros (list[dict]): datos a volcar en el archivo.

    Returns:
        int: cantidad de filas de datos escritas (sin contar el encabezado).
    """
    pass


def actualizar_stock_csv(ruta_origen, ruta_destino, cambios_stock):
    """Lee un CSV de inventario, aplica variaciones de stock y guarda el resultado en ruta_destino.

    El CSV tiene columnas: componente,categoria,cantidad.
    cambios_stock es un dict {nombre_componente: variacion_int} (puede ser positiva o negativa).
    La cantidad resultante nunca puede ser menor a 0 (si da negativa, queda en 0).

    Args:
        ruta_origen (str): ruta del CSV original.
        ruta_destino (str): ruta donde escribir el CSV actualizado.
        cambios_stock (dict[str, int]): ajustes a aplicar por nombre de componente.

    Returns:
        list[dict[str, str]]: registros actualizados tal como quedaron guardados (cantidad como str).
    """
    pass


def generar_reporte_aprobados_csv(ruta_notas_csv, ruta_reporte_txt, nota_aprobacion=7.0):
    """Lee un CSV de notas y escribe un archivo de texto con el listado de aprobados.

    El CSV tiene columnas: nombre,materia,nota.
    En ruta_reporte_txt debe escribir:
    - Una línea "{nombre} aprobó {materia} con {nota}\\n" por cada fila con float(nota) >= nota_aprobacion.
    - Una última línea "Total aprobados: {aprobados}/{total}\\n".

    Args:
        ruta_notas_csv (str): ruta al CSV de entrada.
        ruta_reporte_txt (str): ruta al archivo de texto de salida.
        nota_aprobacion (float): nota mínima para aprobar (default 7.0).

    Returns:
        int: cantidad de estudiantes aprobados.
    """
    pass


def consolidar_archivos_csv(lista_rutas_origen, ruta_destino):
    """Une varios archivos CSV que comparten la misma estructura en un único archivo CSV.

    Escribe el encabezado una sola vez al comienzo de ruta_destino y a continuación
    todas las filas de datos de cada archivo en el orden recibido.

    Args:
        lista_rutas_origen (list[str]): rutas de los archivos CSV a combinar.
        ruta_destino (str): ruta del archivo CSV consolidado.

    Returns:
        int: cantidad total de filas de datos escritas en el archivo destino.
    """
    pass
