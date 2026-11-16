# Apunte: Fundamentos de Python

## 1. Variables y tipos de datos primitivos

### 1.1 ¿Qué es una variable?

Una variable es un espacio en memoria que almacena un valor. En Python se crea asignando un valor a un nombre.

```python
edad = 25
nombre = "Ana"
```

El nombre de la variable debe ser descriptivo, usar minúsculas y separadores `_` (snake_case).

### 1.2 Tipos de datos primitivos

Python tiene los siguientes tipos built-in principales:

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| `int` | Números enteros | `42`, `-7`, `0` |
| `float` | Números decimales | `3.14`, `-0.5`, `2.0` |
| `str` | Cadenas de texto | `"Hola"`, `'Mundo'` |
| `bool` | Valores booleanos | `True`, `False` |

### 1.3 Verificar el tipo de un valor

Para saber qué tipo tiene una variable se usa la función `type()`.

```python
x = 10
print(type(x))  # <class 'int'>

y = 3.14
print(type(y))  # <class 'float'>
```

Para hacer comprobaciones booleanas sobre el tipo:

```python
es_entero = isinstance(42, int)        # True
es_float = isinstance(3.14, float)     # True
```

### 1.4 Conversión entre tipos

Python permite convertir explícitamente entre tipos:

```python
int("10")      # "10" -> 10
float("2.5")   # "2.5" -> 2.5
str(100)       # 100 -> "100"
int(3.7)       # 3.7 -> 3 (trunca, no redondea)
float(5)       # 5 -> 5.0
```

> **Nota**: Las conversiones pueden fallar si el valor no es compatible. Por ejemplo, `int("hola")` lanza un `ValueError`.

### 1.5 Operaciones aritméticas

```python
a + b    # Suma
a - b    # Resta
a * b    # Multiplicación
a / b    # División (siempre retorna float)
a // b   # División entera (trunca decimales)
a % b    # Resto de la división entera
a ** b   # Potencia (a elevado a b)
```

```python
17 // 4   # 4
17 % 4    # 1
2 ** 3    # 8
```

### 1.6 Operadores de comparación

Retornan un valor `bool`:

```python
a == b   # Igual a
a != b   # Distinto de
a > b    # Mayor que
a < b    # Menor que
a >= b   # Mayor o igual que
a <= b   # Menor o igual que
```

### 1.7 Booleanos y operadores lógicos

Los valores booleanos en Python son `True` y `False`.

```python
True and False   # False
True or False    # True
not True         # False
```

Los operadores de comparación generan booleanos:

```python
5 > 3            # True
10 == 10         # True
4 % 2 == 0       # True (4 es par)
```

### 1.8 Strings (cadenas de texto)

Las cadenas se definen con comillas simples o dobles:

```python
nombre = "Ana"
apellido = 'García'
```

**Concatenación y f-strings:**

```python
nombre_completo = nombre + " " + apellido  # "Ana García"
presentacion = f"Hola, soy {nombre}, tengo {edad} años"
```

La f-string (formatted string literal) permite interpolar valores dentro del texto usando `{}`.

**Métodos útiles:**

```python
"hola".upper()           # "HOLA"
"Hola".lower()           # "hola"
"  espacio  ".strip()    # "espacio"
"abc".replace("a", "x")  # "xbc"
len("python")            # 6
```

---

## 2. Estructuras de control: Condicionales

Las condicionales permiten ejecutar código solo cuando se cumple una condición.

### 2.1 La sentencia `if`

```python
if condición:
    # código que se ejecuta si la condición es True
```

```python
edad = 18
if edad >= 18:
    print("Puede entrar")
```

### 2.2 `if` / `else`

```python
if condición:
    # se ejecuta si es True
else:
    # se ejecuta si es False
```

```python
if edad >= 18:
    print("Acceso permitido")
else:
    print("Acceso denegado")
```

### 2.3 `if` / `elif` / `else`

Cuando hay múltiples condiciones:

```python
if nota >= 7:
    print("Promocionado")
elif nota >= 4:
    print("Aprobado")
else:
    print("Recupatorio")
```

Se evalúan en orden. Una vez que una condición se cumple, se ejecutan ese bloque y se ignoran los demás.

### 2.4 Condiciones compuestas

Se pueden combinar booleanos con `and`, `or` y `not`:

```python
if edad >= 18 and tiene_identificacion:
    print("Acceso concedido")
```

```python
if es_admin or es_moderador:
    print("Puede editar")
```

```python
if not es_invitado:
    print("Contenido premium")
```

### 2.5 El operador ternario

Permite escribir un `if`/`else` en una sola línea:

```python
mensaje = "Mayor" if edad >= 18 else "Menor"
```

### 2.6 Consideraciones sobre booleanos en Python

Python considera "falsy" (evaluable como `False`) a estos valores:

- `None`
- `False`
- `0` (int), `0.0` (float)
- `""` (string vacío)
- `[]`, `{}`, `()` (colecciones vacías)

Todo lo demás es "truthy": `1`, `"hola"`, `[0]`, etc.

---

## 3. Funciones

Una función es un bloque de código reutilizable que realiza una tarea específica.

### 3.1 Definición básica

```python
def nombre_de_la_funcion():
    # cuerpo de la función
    print("Hola")
```

Para ejecutarla se llama por su nombre:

```python
nombre_de_la_funcion()
```

### 3.2 Parámetros y argumentos

Los **parámetros** son las variables en la definición. Los **argumentos** son los valores que se pasan al llamar la función.

```python
def saludar(nombre):          # 'nombre' es el parámetro
    print(f"Hola, {nombre}")

saludar("Ana")                # "Ana" es el argumento
```

Se pueden definir múltiples parámetros:

```python
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)       # resultado = 8
```

### 3.3 Retorno de resultados

La sentencia `return` devuelve un valor al caller. Si no se coloca `return`, la función retorna `None`.

```python
def sumar(a, b):
    return a + b

resultado = sumar(10, 5)      # resultado = 15
```

**Return anticipado:** se puede salir de la función antes:

```python
def dividir(a, b):
    if b == 0:
        return None
    return a / b
```

**Múltiples valores de retorno:** las funciones pueden retornar tuplas.

```python
def obtener_estado(valido, mensaje):
    return (valido, mensaje)

es_valido, msg = obtener_estado(True, "OK")
```

### 3.4 Valores por defecto

Los parámetros pueden tener un valor default:

```python
def aplicar_descuento(precio, descuento=10):
    return precio * (100 - descuento) / 100

aplicar_descuento(100)         # 90.0 (10% off)
aplicar_descuento(100, 20)     # 80.0 (20% off)
```

Los parámetros con default deben ir después de los que no lo tienen.

### 3.5 Argumentos variables: `*args`

Cuando no se sabe cuántos argumentos se van a pasar:

```python
def sumar_todos(*args):
    total = 0
    for numero in args:
        total += numero
    return total

sumar_todos(1, 2, 3)           # 6
sumar_todos(10, 20)            # 30
sumar_todos()                  # 0
```

`args` es una tupla con todos los argumentos posicionales.

### 3.6 Argumentos por nombre: `**kwargs`

Permite recibir pares clave-valor arbitrarios:

```python
def construir_usuario(nombre, **kwargs):
    return {"nombre": nombre, **kwargs}

construir_usuario("Ana", edad=25, ciudad="Córdoba")
# {"nombre": "Ana", "edad": 25, "ciudad": "Córdoba"}
```

`kwargs` es un diccionario.

### 3.7 Documentación de funciones

Se recomienda usar docstrings para describir qué hace la función:

```python
def calcular_imc(peso_kg, altura_m):
    """
    Calcula el índice de masa corporal (IMC).

    Args:
        peso_kg (float): peso en kilogramos
        altura_m (float): altura en metros

    Returns:
        float: el IMC redondeado a 2 decimales.
    """
    imc = peso_kg / (altura_m ** 2)
    return round(imc, 2)
```

---

## Resumen rápido

| Concepto | Sintaxis clave |
|----------|---------------|
| Variable | `x = 10` |
| Conversión | `int()`, `float()`, `str()` |
| Condicional | `if / elif / else` |
| Comparación | `==`, `!=`, `>`, `<`, `>=`, `<=` |
| Función simple | `def f(): pass` |
| Función con args | `def f(a, b): return a + b` |
| Valor default | `def f(x=10): pass` |
| `*args` | `def f(*args):` para muchos argumentos posicionales |
| `**kwargs` | `def f(**kwargs):` para muchos argumentos por nombre |