"""
Tests para el módulo de Variables y tipos de datos primitivos.

Cada test tiene un docstring que describe el comportamiento esperado.
El alumno debe leer el test, entender qué pide y luego implementar
la función en ejercicios/variables.py hasta que el test pase.
"""

import sys
sys.path.insert(0, "../ejercicios")

from ejercicios.variables import (
    crear_variables_primitivas,
    es_entero,
    es_float,
    a_entero,
    a_float,
    a_string,
    es_entero_par,
    sumar_dos_numeros,
    division_entera,
    resto_division,
    comparar_mayores_o_iguales,
    concatenar_nombre_y_apellido,
    plantilla_presentacion,
    calcular_imc,
    clasificar_imc,
)


class TestCrearVariablesPrimitivas:
    def test_crea_variables_definidas(self):
        """Debe crear variables de tipos int, float, str y bool a nivel del módulo."""
        namespace = {}
        crear_variables_primitivas()
        exec(open("../ejercicios/variables.py").read(), namespace)
        assert "int" in namespace or any(isinstance(v, int) for v in namespace.values() if not v.__class__.__name__.startswith("_"))
        assert any(isinstance(v, float) for v in namespace.values() if not v.__class__.__name__.startswith("_"))
        assert any(isinstance(v, str) for v in namespace.values() if not v.__class__.__name__.startswith("_"))
        assert any(isinstance(v, bool) for v in namespace.values() if not v.__class__.__name__.startswith("_"))


class TestEsEntero:
    def test_entero_devuelve_true(self):
        """Debe retornar True cuando el valor es de tipo int."""
        assert es_entero(42) is True

    def test_float_devuelve_false(self):
        """Debe retornar False cuando el valor es de tipo float."""
        assert es_entero(3.14) is False

    def test_string_devuelve_false(self):
        """Debe retornar False cuando el valor es de tipo str."""
        assert es_entero("42") is False

    def test_booleano_devuelve_false(self):
        """Debe retornar False cuando el valor es de tipo bool."""
        assert es_entero(True) is False


class TestEsFloat:
    def test_float_devuelve_true(self):
        """Debe retornar True cuando el valor es de tipo float."""
        assert es_float(3.14) is True

    def test_int_devuelve_false(self):
        """Debe retornar False cuando el valor es de tipo int."""
        assert es_float(42) is False

    def test_string_devuelve_false(self):
        """Debe retornar False cuando el valor es de tipo str."""
        assert es_float("3.14") is False


class TestAEntero:
    def test_string_a_entero(self):
        """Debe convertir el string '10' a entero 10."""
        assert a_entero("10") == 10

    def test_float_a_entero(self):
        """Debe convertir el float 3.7 a entero 3 (trunca)."""
        assert a_entero(3.7) == 3

    def test_entero_pasa(self):
        """Un int debe seguir siendo int."""
        assert a_entero(5) == 5


class TestAFloat:
    def test_string_a_float(self):
        """Debe convertir el string '2.5' a float 2.5."""
        assert a_float("2.5") == 2.5

    def test_entero_a_float(self):
        """Debe convertir el entero 7 a float 7.0."""
        assert a_float(7) == 7.0

    def test_string_entero_a_float(self):
        """Debe convertir el string '3' a float 3.0."""
        assert a_float("3") == 3.0


class TestAString:
    def test_entero_a_string(self):
        """Debe convertir el entero 100 a string '100'."""
        assert a_string(100) == "100"

    def test_float_a_string(self):
        """Debe convertir el float 3.14 a string '3.14'."""
        assert a_string(3.14) == "3.14"

    def test_booleano_a_string(self):
        """Debe convertir el booleano True a string 'True'."""
        assert a_string(True) == "True"


class TestEsEnteroPar:
    def test_numero_par(self):
        """Debe retornar True para el número 4."""
        assert es_entero_par(4) is True

    def test_numero_impar(self):
        """Debe retornar False para el número 7."""
        assert es_entero_par(7) is False

    def test_cero_es_par(self):
        """El cero (0) debe ser considerado par."""
        assert es_entero_par(0) is True

    def test_negativo_par(self):
        """Debe retornar True para -6 (negativo par)."""
        assert es_entero_par(-6) is True


class TestSumarDosNumeros:
    def test_suma_positivos(self):
        """Debe retornar 15 para 10 + 5."""
        assert sumar_dos_numeros(10, 5) == 15

    def test_suma_negativos(self):
        """Debe retornar -3 para -1 + -2."""
        assert sumar_dos_numeros(-1, -2) == -3

    def test_suma_con_decimales(self):
        """Debe retornar 7.5 para 3.2 + 4.3."""
        assert sumar_dos_numeros(3.2, 4.3) == 7.5


class TestDivisionEntera:
    def test_division_normal(self):
        """Debe retornar 4 para 17 // 4."""
        assert division_entera(17, 4) == 4

    def test_division_exacta(self):
        """Debe retornar 5 para 25 // 5."""
        assert division_entera(25, 5) == 5

    def test_division_negativo(self):
        """Debe retornar -3 para -10 // 3."""
        assert division_entera(-10, 3) == -3


class TestRestoDivision:
    def test_resto_normal(self):
        """Debe retornar 1 para 17 % 4."""
        assert resto_division(17, 4) == 1

    def test_resto_exacto(self):
        """Debe retornar 0 para 20 % 5."""
        assert resto_division(20, 5) == 0

    def test_resto_negativo(self):
        """Debe retornar 2 para -10 % 3."""
        assert resto_division(-10, 3) == 2


class TestCompararMayoresOIguales:
    def test_mayor_o_igual_true(self):
        """Debe retornar True cuando a=10 y b=5."""
        assert comparar_mayores_o_iguales(10, 5) is True

    def test_igual_devuelve_true(self):
        """Debe retornar True cuando a=7 y b=7."""
        assert comparar_mayores_o_iguales(7, 7) is True

    def test_menor_devuelve_false(self):
        """Debe retornar False cuando a=3 y b=8."""
        assert comparar_mayores_o_iguales(3, 8) is False


class TestConcatenarNombreYApellido:
    def test_concatena_correctamente(self):
        """Debe retornar 'Juan Pérez' para 'Juan' y 'Pérez'."""
        assert concatenar_nombre_y_apellido("Juan", "Pérez") == "Juan Pérez"

    def test_nombre_corto(self):
        """Debe retornar 'Ana García' para 'Ana' y 'García'."""
        assert concatenar_nombre_y_apellido("Ana", "García") == "Ana García"


class TestPlantillaPresentacion:
    def test_presentacion_formato(self):
        """El resultado debe seguir el formato esperado."""
        resultado = plantilla_presentacion("María", 28, "Córdoba")
        assert resultado == "Hola, soy María, tengo 28 años y vivo en Córdoba."

    def test_presentacion_otro_ejemplo(self):
        """Debe funcionar con otros datos."""
        resultado = plantilla_presentacion("Pedro", 45, "Mendoza")
        assert resultado == "Hola, soy Pedro, tengo 45 años y vivo en Mendoza."


class TestCalcularIMC:
    def test_imc_normal(self):
        """Para peso=70kg y altura=1.75m debe retornar aproximadamente 22.86."""
        resultado = calcular_imc(70, 1.75)
        assert round(resultado, 2) == 22.86

    def test_imc_sobrepeso(self):
        """Para peso=90kg y altura=1.70m debe retornar aproximadamente 31.14."""
        resultado = calcular_imc(90, 1.70)
        assert round(resultado, 2) == 31.14


class TestClasificarIMC:
    def test_bajo_peso(self):
        """IMC menor a 18.5 debe retornar 'Bajo peso'."""
        assert clasificar_imc(17.0) == "Bajo peso"

    def test_normal(self):
        """IMC entre 18.5 y 25 debe retornar 'Normal'."""
        assert clasificar_imc(22.0) == "Normal"

    def test_sobrepeso(self):
        """IMC entre 25 y 30 debe retornar 'Sobrepeso'."""
        assert clasificar_imc(27.0) == "Sobrepeso"

    def test_obesidad(self):
        """IMC de 30 o más debe retornar 'Obesidad'."""
        assert clasificar_imc(32.0) == "Obesidad"