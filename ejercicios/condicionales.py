"""
Módulo de ejercicios: Estructuras de control - Condicionales.
"""


def es_par_o_impar(n):
    """Determina si un número es par o impar.

    Args:
        n (int): número a evaluar

    Returns:
        str: "par" si n es divisible por 2, "impar" en caso contrario.
    """
    pass


def clasificar_nota(nota):
    """Clasifica una nota numérica en una categoría.

    Args:
        nota (float): nota del examen (0 a 10)

    Returns:
        str: categoría según la nota:
            - "Promocionado" si nota >= 7
            - "Aprobado" si 4 <= nota < 7
            - "Recupatorio" si nota < 4
    """
    pass


def maximo_de_tres(a, b, c):
    """Retorna el mayor de tres números.

    Args:
        a: primer número
        b: segundo número
        c: tercer número

    Returns:
        el mayor valor entre a, b y c.
    """
    pass


def minimo_de_tres(a, b, c):
    """Retorna el menor de tres números.

    Args:
        a: primer número
        b: segundo número
        c: tercer número

    Returns:
        el menor valor entre a, b y c.
    """
    pass


def es_bisiesto(year):
    """Determina si un año es bisiesto.

    Args:
        year (int): año a evaluar

    Returns:
        bool: True si el año es bisiesto, False en caso contrario.
              Un año es bisiesto si es divisible por 4,
              excepto los divisible por 100 que no sean divisible por 400.
    """
    pass


def calcular_precio_final(precio_base, categoria):
    """Aplica un descuento según la categoría del cliente.

    Args:
        precio_base (float): precio sin descuentos
        categoria (str): categoría del cliente ("general", "estudiante", "jubilado")

    Returns:
        float: precio final con el descuento aplicado:
            - "general": sin descuento
            - "estudiante": 20% de descuento
            - "jubilado": 30% de descuento
    """
    pass


def calculadora_simple(a, operacion, b):
    """Realiza una operación aritmética simple entre dos números.

    Args:
        a (float): primer operando
        operacion (str): operación a realizar ("+", "-", "*", "/")
        b (float): segundo operando

    Returns:
        float: resultado de la operación.
        Si la operación es "/" y b es 0, retornar "Error: división por cero".
    """
    pass


def fizzbuzz(n):
    """Implementa el clásico problema FizzBuzz.

    Args:
        n (int): número a evaluar

    Returns:
        str: "Fizz" si n es divisible por 3,
             "Buzz" si n es divisible por 5,
             "FizzBuzz" si n es divisible por ambos,
             o el número mismo convertido a string en caso contrario.
    """
    pass


def describir_numero(n):
    """Describe características de un número entero.

    Args:
        n (int): número a describir

    Returns:
        str: descripción con formato:
            - "Positivo y par" si n > 0 y es par
            - "Positivo e impar" si n > 0 y es impar
            - "Negativo y par" si n < 0 y es par
            - "Negativo e impar" si n < 0 y es impar
            - "Cero" si n == 0
    """
    pass


def acceso_usuario(edad, tiene_identificacion):
    """Determina si un usuario puede acceder.

    Args:
        edad (int): edad del usuario
        tiene_identificacion (bool): si tiene documento

    Returns:
        bool: True si edad >= 18 y tiene_identificacion es True, False en caso contrario.
    """
    pass


def dia_de_la_semana(numero):
    """Convierte un número (1-7) al nombre del día de la semana.

    Args:
        numero (int): número del 1 al 7

    Returns:
        str: nombre del día ("Lunes" a "Domingo").
             Si el número está fuera de rango, retornar "Día inválido".
    """
    pass