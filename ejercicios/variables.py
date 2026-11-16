"""
Módulo de ejercicios: Variables y tipos de datos primitivos.
"""


def crear_variables_primitivas():
    """Crea una variable de cada tipo primitivo: int, float, str, bool.
    No necesita argumentos ni retorno.
    Solo define las variables a nivel del modulo (ej: a = 10).
    """
    pass


def es_entero(valor):
    """Determina si un valor es un número entero (tipo int).

    Args:
        valor: cualquier valor

    Returns:
        bool: True si el valor es de tipo int, False en caso contrario.
    """
    pass


def es_float(valor):
    """Determina si un valor es un número decimal (tipo float).

    Args:
        valor: cualquier valor

    Returns:
        bool: True si el valor es de tipo float, False en caso contrario.
    """
    pass


def a_entero(valor):
    """Convierte un valor a entero (int).

    Args:
        valor: cualquier valor convertible a entero

    Returns:
        int: el valor convertido a entero.
    """
    pass


def a_float(valor):
    """Convierte un valor a decimal (float).

    Args:
        valor: cualquier valor convertible a decimal

    Returns:
        float: el valor convertido a float.
    """
    pass


def a_string(valor):
    """Convierte un valor a texto (str).

    Args:
        valor: cualquier valor

    Returns:
        str: el valor convertido a string.
    """
    pass


def es_entero_par(n):
    """Determina si un número entero es par.

    Args:
        n (int): número a evaluar

    Returns:
        bool: True si n es par, False si es impar.
    """
    pass


def sumar_dos_numeros(a, b):
    """Suma dos números y retorna el resultado.

    Args:
        a: primer número
        b: segundo número

    Returns:
        float: la suma de a y b.
    """
    pass


def division_entera(a, b):
    """Calcula la división entera entre dos números.

    Args:
        a (int): dividendo
        b (int): divisor (no puede ser cero)

    Returns:
        int: el resultado de la división entera.
    """
    pass


def resto_division(a, b):
    """Calcula el resto de la división entera entre dos números.

    Args:
        a (int): dividendo
        b (int): divisor (no puede ser cero)

    Returns:
        int: el resto de a // b.
    """
    pass


def comparar_mayores_o_iguales(a, b):
    """Determina si a es mayor o igual que b.

    Args:
        a: primer número
        b: segundo número

    Returns:
        bool: True si a >= b, False en caso contrario.
    """
    pass


def concatenar_nombre_y_apellido(nombre, apellido):
    """Une el nombre y apellido con un espacio en el medio.

    Args:
        nombre (str): nombre de pila
        apellido (str): apellido

    Returns:
        str: nombre completo con formato "Nombre Apellido".
    """
    pass


def plantilla_presentacion(nombre, edad, ciudad):
    """Genera una presentación en una frase.

    Args:
        nombre (str): nombre de la persona
        edad (int): edad de la persona
        ciudad (str): ciudad de residencia

    Returns:
        str: frase con formato "Hola, soy {nombre}, tengo {edad} años y vivo en {ciudad}."
    """
    pass


def calcular_imc(peso_kg, altura_m):
    """Calcula el índice de masa corporal (IMC).

    Args:
        peso_kg (float): peso en kilogramos
        altura_m (float): altura en metros

    Returns:
        float: el IMC (peso / altura^2), redondeado a 2 decimales.
    """
    pass


def clasificar_imc(imc):
    """Clasifica el IMC en una categoría.

    Args:
        imc (float): valor del índice de masa corporal

    Returns:
        str: categoría del IMC:
            - "Bajo peso" si imc < 18.5
            - "Normal" si 18.5 <= imc < 25
            - "Sobrepeso" si 25 <= imc < 30
            - "Obesidad" si imc >= 30
    """
    pass