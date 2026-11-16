"""
Módulo de ejercicios: Funciones.
"""


def saludar():
    """Imprime un saludo por pantalla.

    No tiene argumentos ni retorno.
    Solo debe hacer print("¡Hola!").
    """
    pass


def saludar_persona(nombre):
    """Imprime un saludo personalizado.

    Args:
        nombre (str): nombre de la persona a saludar

    No tiene retorno, solo print.
    """
    pass


def sumar(a, b):
    """Suma dos números y retorna el resultado.

    Args:
        a: primer número
        b: segundo número

    Returns:
        float: la suma de a y b.
    """
    pass


def restar(a, b):
    """Resta dos números y retorna el resultado.

    Args:
        a: primer número
        b: segundo número

    Returns:
        float: la resta de a y b (a - b).
    """
    pass


def multiplicar(a, b):
    """Multiplica dos números y retorna el resultado.

    Args:
        a: primer número
        b: segundo número

    Returns:
        float: el producto de a y b.
    """
    pass


def dividir(a, b):
    """Divide dos números y retorna el resultado.

    Args:
        a: dividendo
        b: divisor

    Returns:
        float: el cociente de a / b.
        Si b es 0, retorna None.
    """
    pass


def es_positivo(n):
    """Determina si un número es positivo.

    Args:
        n: número a evaluar

    Returns:
        bool: True si n > 0, False en caso contrario.
    """
    pass


def es_multiplo_de_tres(n):
    """Determina si un número es múltiplo de 3.

    Args:
        n (int): número a evaluar

    Returns:
        bool: True si n es divisible por 3, False en caso contrario.
    """
    pass


def obtener_mensaje_estado(es_correcto, mensaje_base):
    """Retorna un mensaje con estado según un valor booleano.

    Args:
        es_correcto (bool): indica si el estado es exitoso
        mensaje_base (str): mensaje base para el estado

    Returns:
        str: mensaje con formato "[OK] {mensaje_base}" si es_correcto,
             o "[ERROR] {mensaje_base}" si no lo es.
    """
    pass


def sumar_hasta_limite(inicio, limite):
    """Suma números consecutivos desde inicio hasta limite (inclusive).

    Args:
        inicio (int): número inicial de la suma
        limite (int): número máximo a incluir en la suma

    Returns:
        int: la suma de todos los enteros desde inicio hasta limite.
    """
    pass


def aplicar_descuento(precio, descuento=10):
    """Aplica un descuento a un precio.

    Args:
        precio (float): precio original
        descuento (float): porcentaje de descuento (default 10)

    Returns:
        float: el precio con el descuento aplicado.
    """
    pass


def repetir_texto(texto, veces=2):
    """Repite un texto un número de veces.

    Args:
        texto (str): texto a repetir
        veces (int): cantidad de repeticiones (default 2)

    Returns:
        str: el texto repetido, separado por espacios.
    """
    pass


def sumar_todos(*args):
    """Suma todos los argumentos pasados.

    Args:
        *args: cantidad variable de números

    Returns:
        float: la suma de todos los argumentos.
        Si no se pasan argumentos, retorna 0.
    """
    pass


def promediar(*args):
    """Calcula el promedio de los argumentos pasados.

    Args:
        *args: cantidad variable de números

    Returns:
        float: el promedio de los argumentos.
        Si no se pasan argumentos, retorna None.
    """
    pass


def construir_usuario(nombre, **kwargs):
    """Construye un diccionario con datos de un usuario.

    Args:
        nombre (str): nombre del usuario
        **kwargs: pares clave-valor adicionales (ej: edad=25, ciudad="BsAs")

    Returns:
        dict: diccionario con 'nombre' y todas las clave-valor de kwargs.
    """
    pass


def validar_edad_y_rol(edad, rol):
    """Valida que la edad y el rol sean aceptables.

    Args:
        edad (int): edad del usuario
        rol (str): rol del usuario ("admin", "usuario", "invitado")

    Returns:
        tuple: (bool, str) donde el bool indica si la validación pasó
               y el string es el mensaje explicativo.
               - (True, "Válido") si edad >= 18 y rol es válido
               - (False, "Edad mínima: 18") si edad < 18
               - (False, "Rol inválido") si rol no es uno de los permitidos
    """
    pass