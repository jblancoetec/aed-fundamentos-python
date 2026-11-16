"""
Tests para el módulo de Funciones.

Cada test tiene un docstring que describe el comportamiento esperado.
El alumno debe leer el test, entender qué pide y luego implementar
la función en ejercicios/funciones.py hasta que el test pase.
"""

import sys
sys.path.insert(0, "../ejercicios")

from ejercicios.funciones import (
    saludar,
    saludar_persona,
    sumar,
    restar,
    multiplicar,
    dividir,
    es_positivo,
    es_multiplo_de_tres,
    obtener_mensaje_estado,
    sumar_hasta_limite,
    aplicar_descuento,
    repetir_texto,
    sumar_todos,
    promediar,
    construir_usuario,
    validar_edad_y_rol,
)


class TestSaludar:
    def test_imprime_hola(self, capsys):
        """saludar() debe hacer print de '¡Hola!'."""
        saludar()
        captured = capsys.readouterr()
        assert captured.out.strip() == "¡Hola!"


class TestSaludarPersona:
    def test_imprime_saludo_personalizado(self, capsys):
        """saludar_persona('Ana') debe hacer print de '¡Hola, Ana!'."""
        saludar_persona("Ana")
        captured = capsys.readouterr()
        assert captured.out.strip() == "¡Hola, Ana!"

    def test_imprime_otro_nombre(self, capsys):
        """saludar_persona('Pedro') debe hacer print de '¡Hola, Pedro!'."""
        saludar_persona("Pedro")
        captured = capsys.readouterr()
        assert captured.out.strip() == "¡Hola, Pedro!"


class TestSumar:
    def test_suma_positivos(self):
        """sumar(3, 5) debe retornar 8."""
        assert sumar(3, 5) == 8

    def test_suma_negativos(self):
        """sumar(-2, -4) debe retornar -6."""
        assert sumar(-2, -4) == -6

    def test_suma_con_zero(self):
        """sumar(10, 0) debe retornar 10."""
        assert sumar(10, 0) == 10

    def test_suma_decimales(self):
        """sumar(1.5, 2.5) debe retornar 4.0."""
        assert sumar(1.5, 2.5) == 4.0


class TestRestar:
    def test_resta_positivos(self):
        """restar(10, 3) debe retornar 7."""
        assert restar(10, 3) == 7

    def test_resta_negativo(self):
        """restar(5, -2) debe retornar 7."""
        assert restar(5, -2) == 7

    def test_resta_da_negativo(self):
        """restar(3, 8) debe retornar -5."""
        assert restar(3, 8) == -5


class TestMultiplicar:
    def test_multiplicar_positivos(self):
        """multiplicar(4, 5) debe retornar 20."""
        assert multiplicar(4, 5) == 20

    def test_multiplicar_por_cero(self):
        """multiplicar(7, 0) debe retornar 0."""
        assert multiplicar(7, 0) == 0

    def test_multiplicar_negativos(self):
        """multiplicar(-3, 4) debe retornar -12."""
        assert multiplicar(-3, 4) == -12


class TestDividir:
    def test_division_normal(self):
        """dividir(10, 2) debe retornar 5.0."""
        assert dividir(10, 2) == 5.0

    def test_division_decimal(self):
        """dividir(7, 2) debe retornar 3.5."""
        assert dividir(7, 2) == 3.5

    def test_division_por_cero(self):
        """dividir(5, 0) debe retornar None."""
        assert dividir(5, 0) is None


class TestEsPositivo:
    def test_positivo_true(self):
        """es_positivo(5) debe retornar True."""
        assert es_positivo(5) is True

    def test_cero_false(self):
        """es_positivo(0) debe retornar False."""
        assert es_positivo(0) is False

    def test_negativo_false(self):
        """es_positivo(-3) debe retornar False."""
        assert es_positivo(-3) is False


class TestEsMultiploDeTres:
    def test_multiplo_de_tres_true(self):
        """es_multiplo_de_tres(9) debe retornar True."""
        assert es_multiplo_de_tres(9) is True

    def test_no_multiplo_false(self):
        """es_multiplo_de_tres(10) debe retornar False."""
        assert es_multiplo_de_tres(10) is False

    def test_tres_es_multiplo(self):
        """es_multiplo_de_tres(3) debe retornar True."""
        assert es_multiplo_de_tres(3) is True

    def test_cero_es_multiplo(self):
        """es_multiplo_de_tres(0) debe retornar True."""
        assert es_multiplo_de_tres(0) is True


class TestObtenerMensajeEstado:
    def test_estado_ok(self):
        """es_correcto=True, mensaje_base='Procesado' debe retornar '[OK] Procesado'."""
        assert obtener_mensaje_estado(True, "Procesado") == "[OK] Procesado"

    def test_estado_error(self):
        """es_correcto=False, mensaje_base='No encontrado' debe retornar '[ERROR] No encontrado'."""
        assert obtener_mensaje_estado(False, "No encontrado") == "[ERROR] No encontrado"


class TestSumarHastaLimite:
    def test_suma_desde_1_hasta_5(self):
        """sumar_hasta_limite(1, 5) debe retornar 15 (1+2+3+4+5)."""
        assert sumar_hasta_limite(1, 5) == 15

    def test_suma_desde_3_hasta_7(self):
        """sumar_hasta_limite(3, 7) debe retornar 25 (3+4+5+6+7)."""
        assert sumar_hasta_limite(3, 7) == 25

    def test_limite_igual_inicio(self):
        """sumar_hasta_limite(4, 4) debe retornar 4."""
        assert sumar_hasta_limite(4, 4) == 4

    def test_suma_negativos(self):
        """sumar_hasta_limite(-2, 2) debe retornar 0."""
        assert sumar_hasta_limite(-2, 2) == 0


class TestAplicarDescuento:
    def test_descuento_default_10(self):
        """aplicar_descuento(100) debe retornar 90.0 (10% off)."""
        assert aplicar_descuento(100) == 90.0

    def test_descuento_custom_20(self):
        """aplicar_descuento(100, 20) debe retornar 80.0 (20% off)."""
        assert aplicar_descuento(100, 20) == 80.0

    def test_descuento_0(self):
        """aplicar_descuento(50, 0) debe retornar 50.0 (sin descuento)."""
        assert aplicar_descuento(50, 0) == 50.0

    def test_descuento_50(self):
        """aplicar_descuento(200, 50) debe retornar 100.0."""
        assert aplicar_descuento(200, 50) == 100.0


class TestRepetirTexto:
    def test_repetir_default_2_veces(self):
        """repetir_texto('hola') debe retornar 'hola hola'."""
        assert repetir_texto("hola") == "hola hola"

    def test_repetir_3_veces(self):
        """repetir_texto('chao', 3) debe retornar 'chao chao chao'."""
        assert repetir_texto("chao", 3) == "chao chao chao"

    def test_repetir_1_vez(self):
        """repetir_texto('uno', 1) debe retornar 'uno'."""
        assert repetir_texto("uno", 1) == "uno"


class TestSumarTodos:
    def test_suma_tres_numeros(self):
        """sumar_todos(1, 2, 3) debe retornar 6."""
        assert sumar_todos(1, 2, 3) == 6

    def test_suma_dos_numeros(self):
        """sumar_todos(10, 5) debe retornar 15."""
        assert sumar_todos(10, 5) == 15

    def test_suma_un_numero(self):
        """sumar_todos(42) debe retornar 42."""
        assert sumar_todos(42) == 42

    def test_sin_argumentos_retorna_cero(self):
        """sumar_todos() debe retornar 0."""
        assert sumar_todos() == 0


class TestPromediar:
    def test_promedio_tres_numeros(self):
        """promediar(2, 4, 6) debe retornar 4.0."""
        assert promediar(2, 4, 6) == 4.0

    def test_promedio_dos_numeros(self):
        """promediar(5, 15) debe retornar 10.0."""
        assert promediar(5, 15) == 10.0

    def test_promedio_un_numero(self):
        """promediar(8) debe retornar 8.0."""
        assert promediar(8) == 8.0

    def test_sin_argumentos_retorna_none(self):
        """promediar() debe retornar None."""
        assert promediar() is None


class TestConstruirUsuario:
    def test_solo_nombre(self):
        """construir_usuario('Ana') debe retornar {'nombre': 'Ana'}."""
        assert construir_usuario("Ana") == {"nombre": "Ana"}

    def test_con_kwargs(self):
        """construir_usuario('Juan', edad=30, ciudad='BsAs') debe retornar el diccionario con las 3 claves."""
        resultado = construir_usuario("Juan", edad=30, ciudad="BsAs")
        assert resultado == {"nombre": "Juan", "edad": 30, "ciudad": "BsAs"}

    def test_multiple_kwargs(self):
        """construir_usuario con kwargs variados debe incluirlos todos."""
        resultado = construir_usuario("Pedro", edad=25, rol="admin", activo=True)
        assert resultado == {"nombre": "Pedro", "edad": 25, "rol": "admin", "activo": True}


class TestValidarEdadYRol:
    def test_valido_todos_ok(self):
        """edad=20 y rol='admin' debe retornar (True, 'Válido')."""
        assert validar_edad_y_rol(20, "admin") == (True, "Válido")

    def test_edad_invalida(self):
        """edad=16 y rol='admin' debe retornar (False, 'Edad mínima: 18')."""
        assert validar_edad_y_rol(16, "admin") == (False, "Edad mínima: 18")

    def test_rol_invalido(self):
        """edad=25 y rol='unknown' debe retornar (False, 'Rol inválido')."""
        assert validar_edad_y_rol(25, "unknown") == (False, "Rol inválido")

    def test_exactly_18_valido(self):
        """edad=18 y rol='usuario' debe retornar (True, 'Válido')."""
        assert validar_edad_y_rol(18, "usuario") == (True, "Válido")

    def test_rol_invitado_valido(self):
        """edad=30 y rol='invitado' debe retornar (True, 'Válido')."""
        assert validar_edad_y_rol(30, "invitado") == (True, "Válido")