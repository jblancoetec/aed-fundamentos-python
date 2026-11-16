"""
Tests para el módulo de Estructuras de control - Condicionales.

Cada test tiene un docstring que describe el comportamiento esperado.
El alumno debe leer el test, entender qué pide y luego implementar
la función en ejercicios/condicionales.py hasta que el test pase.
"""

import sys
sys.path.insert(0, "../ejercicios")

from ejercicios.condicionales import (
    es_par_o_impar,
    clasificar_nota,
    maximo_de_tres,
    minimo_de_tres,
    es_bisiesto,
    calcular_precio_final,
    calculadora_simple,
    fizzbuzz,
    describir_numero,
    acceso_usuario,
    dia_de_la_semana,
)


class TestEsParOImpar:
    def test_numero_par(self):
        """Debe retornar 'par' para n=4."""
        assert es_par_o_impar(4) == "par"

    def test_numero_impar(self):
        """Debe retornar 'impar' para n=7."""
        assert es_par_o_impar(7) == "impar"

    def test_cero_es_par(self):
        """Debe retornar 'par' para n=0."""
        assert es_par_o_impar(0) == "par"

    def test_negativo_par(self):
        """Debe retornar 'par' para n=-6."""
        assert es_par_o_impar(-6) == "par"

    def test_negativo_impar(self):
        """Debe retornar 'impar' para n=-3."""
        assert es_par_o_impar(-3) == "impar"


class TestClasificarNota:
    def test_promocionado(self):
        """Nota 8.0 debe retornar 'Promocionado'."""
        assert clasificar_nota(8.0) == "Promocionado"

    def test_promocionado_exacto(self):
        """Nota 7.0 debe retornar 'Promocionado'."""
        assert clasificar_nota(7.0) == "Promocionado"

    def test_aprobado(self):
        """Nota 5.5 debe retornar 'Aprobado'."""
        assert clasificar_nota(5.5) == "Aprobado"

    def test_aprobado_limite_inferior(self):
        """Nota 4.0 debe retornar 'Aprobado'."""
        assert clasificar_nota(4.0) == "Aprobado"

    def test_recupatorio(self):
        """Nota 3.5 debe retornar 'Recupatorio'."""
        assert clasificar_nota(3.5) == "Recupatorio"

    def test_recupatorio_limite(self):
        """Nota 3.99 debe retornar 'Recupatorio'."""
        assert clasificar_nota(3.99) == "Recupatorio"


class TestMaximoDeTres:
    def test_primero_es_maximo(self):
        """Debe retornar 10 cuando a=10, b=5, c=3."""
        assert maximo_de_tres(10, 5, 3) == 10

    def test_segundo_es_maximo(self):
        """Debe retornar 15 cuando a=8, b=15, c=12."""
        assert maximo_de_tres(8, 15, 12) == 15

    def test_tercero_es_maximo(self):
        """Debe retornar 20 cuando a=5, b=9, c=20."""
        assert maximo_de_tres(5, 9, 20) == 20

    def test_todos_iguales(self):
        """Debe retornar 7 cuando todos son 7."""
        assert maximo_de_tres(7, 7, 7) == 7

    def test_negativos(self):
        """Debe retornar -1 cuando a=-5, b=-1, c=-3."""
        assert maximo_de_tres(-5, -1, -3) == -1


class TestMinimoDeTres:
    def test_primero_es_minimo(self):
        """Debe retornar 2 cuando a=2, b=8, c=12."""
        assert minimo_de_tres(2, 8, 12) == 2

    def test_segundo_es_minimo(self):
        """Debe retornar 3 cuando a=10, b=3, c=7."""
        assert minimo_de_tres(10, 3, 7) == 3

    def test_tercero_es_minimo(self):
        """Debe retornar 1 cuando a=5, b=9, c=1."""
        assert minimo_de_tres(5, 9, 1) == 1


class TestEsBisiesto:
    def test_año_bisiesto_divisible_por_4(self):
        """2020 es divisible por 4 y no por 100, debe ser bisiesto."""
        assert es_bisiesto(2020) is True

    def test_año_no_bisiesto(self):
        """2019 no es divisible por 4, no es bisiesto."""
        assert es_bisiesto(2019) is False

    def test_sieglo_no_bisiesto(self):
        """1900 es divisible por 100 pero no por 400, no es bisiesto."""
        assert es_bisiesto(1900) is False

    def test_sieglo_bisiesto(self):
        """2000 es divisible por 400, es bisiesto."""
        assert es_bisiesto(2000) is True

    def test_año_400(self):
        """1600 es divisible por 400, es bisiesto."""
        assert es_bisiesto(1600) is True

    def test_año_100_no_bisiesto(self):
        """2100 no es divisible por 400, no es bisiesto."""
        assert es_bisiesto(2100) is False


class TestCalcularPrecioFinal:
    def test_categoria_general_sin_descuento(self):
        """Categoria 'general' no tiene descuento."""
        assert calcular_precio_final(100, "general") == 100.0

    def test_categoria_estudiante_20_descuento(self):
        """Categoria 'estudiante' tiene 20% de descuento sobre 100 = 80."""
        assert calcular_precio_final(100, "estudiante") == 80.0

    def test_categoria_jubilado_30_descuento(self):
        """Categoria 'jubilado' tiene 30% de descuento sobre 100 = 70."""
        assert calcular_precio_final(100, "jubilado") == 70.0

    def test_precio_decimal_con_descuento(self):
        """Debe funcionar con precios decimales."""
        resultado = calcular_precio_final(50.0, "estudiante")
        assert resultado == 40.0


class TestCalculadoraSimple:
    def test_suma(self):
        """10 + 5 debe retornar 15."""
        assert calculadora_simple(10, "+", 5) == 15

    def test_resta(self):
        """10 - 4 debe retornar 6."""
        assert calculadora_simple(10, "-", 4) == 6

    def test_multiplicacion(self):
        """3 * 7 debe retornar 21."""
        assert calculadora_simple(3, "*", 7) == 21

    def test_division(self):
        """20 / 4 debe retornar 5.0."""
        assert calculadora_simple(20, "/", 4) == 5.0

    def test_division_decimal(self):
        """7 / 2 debe retornar 3.5."""
        assert calculadora_simple(7, "/", 2) == 3.5

    def test_division_por_cero(self):
        """10 / 0 debe retornar 'Error: división por cero'."""
        assert calculadora_simple(10, "/", 0) == "Error: división por cero"


class TestFizzbuzz:
    def test_multiplo_de_3_devuelve_fizz(self):
        """9 es divisible por 3 pero no por 5, debe retornar 'Fizz'."""
        assert fizzbuzz(9) == "Fizz"

    def test_multiplo_de_5_devuelve_buzz(self):
        """10 es divisible por 5 pero no por 3, debe retornar 'Buzz'."""
        assert fizzbuzz(10) == "Buzz"

    def test_multiplo_de_ambos_devuelve_fizzbuzz(self):
        """15 es divisible por 3 y por 5, debe retornar 'FizzBuzz'."""
        assert fizzbuzz(15) == "FizzBuzz"

    def test_no_multiplo_devuelve_numero(self):
        """7 no es divisible por 3 ni por 5, debe retornar '7'."""
        assert fizzbuzz(7) == "7"

    def test_uno_devuelve_uno(self):
        """1 debe retornar '1'."""
        assert fizzbuzz(1) == "1"

    def test_30_devuelve_fizzbuzz(self):
        """30 es divisible por ambos, debe retornar 'FizzBuzz'."""
        assert fizzbuzz(30) == "FizzBuzz"


class TestDescribirNumero:
    def test_positivo_par(self):
        """4 es positivo y par -> 'Positivo y par'."""
        assert describir_numero(4) == "Positivo y par"

    def test_positivo_impar(self):
        """7 es positivo e impar -> 'Positivo e impar'."""
        assert describir_numero(7) == "Positivo e impar"

    def test_negativo_par(self):
        """-6 es negativo y par -> 'Negativo y par'."""
        assert describir_numero(-6) == "Negativo y par"

    def test_negativo_impar(self):
        """-3 es negativo e impar -> 'Negativo e impar'."""
        assert describir_numero(-3) == "Negativo e impar"

    def test_cero(self):
        """0 debe retornar 'Cero'."""
        assert describir_numero(0) == "Cero"


class TestAccesoUsuario:
    def test_adulto_con_id_true(self):
        """edad=20 y tiene_identificacion=True debe retornar True."""
        assert acceso_usuario(20, True) is True

    def test_adulto_sin_id_false(self):
        """edad=20 y tiene_identificacion=False debe retornar False."""
        assert acceso_usuario(20, False) is False

    def test_menor_con_id_false(self):
        """edad=16 y tiene_identificacion=True debe retornar False."""
        assert acceso_usuario(16, True) is False

    def test_menor_sin_id_false(self):
        """edad=16 y tiene_identificacion=False debe retornar False."""
        assert acceso_usuario(16, False) is False

    def test_exactly_18_con_id_true(self):
        """edad=18 y tiene_identificacion=True debe retornar True."""
        assert acceso_usuario(18, True) is True


class TestDiaDeLaSemana:
    def test_lunes(self):
        """1 debe retornar 'Lunes'."""
        assert dia_de_la_semana(1) == "Lunes"

    def test_miercoles(self):
        """3 debe retornar 'Miércoles'."""
        assert dia_de_la_semana(3) == "Miércoles"

    def test_viernes(self):
        """5 debe retornar 'Viernes'."""
        assert dia_de_la_semana(5) == "Viernes"

    def test_domingo(self):
        """7 debe retornar 'Domingo'."""
        assert dia_de_la_semana(7) == "Domingo"

    def test_dia_invalido_0(self):
        """0 debe retornar 'Día inválido'."""
        assert dia_de_la_semana(0) == "Día inválido"

    def test_dia_invalido_mayor_a_7(self):
        """8 debe retornar 'Día inválido'."""
        assert dia_de_la_semana(8) == "Día inválido"

    def test_dia_invalido_negativo(self):
        """-1 debe retornar 'Día inválido'."""
        assert dia_de_la_semana(-1) == "Día inválido"