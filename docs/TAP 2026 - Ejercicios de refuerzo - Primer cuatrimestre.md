# 1. Variables - Asignación y tipos de datos

## Ejercicio 1.1

Crear dos variables numéricas con valores a elección, y luego mostrarlas
en prints separados.

## Ejercicio 1.2

Crear dos variables de texto para el nombre y el apellido de una
persona, y luego mostrarlas juntas en dos prints de la siguiente forma:

- Un print mostrando el nombre primero, y después el apellido

- Otro print mostrando el apellido primero, y después el nombre

## Ejercicio 1.3

Leyendo el siguiente código, calcular qué se mostrará en cada print.

cargaSube = 200

print(cargaSube)

cargaSube = 100

print(cargaSube)

cargaSube = cargaSube + 50

print(cargaSube)

## Ejercicio 1.4

Para cargar datos en una enciclopedia de animales, se necesita completar
las siguientes variables. Prestemos especial atención al nombre de la
variable para elegir un tipo de dato que quede bien representado por su
nombre.

nombre =

alimentacion =

cantidadDePatas =

puedeVolar =

puedeNadar =

## Ejercicio 1.5

Identificar el tipo de dato de los siguientes valores, e inventar un
nombre de variable creativo para almacenar a cada uno. **Consejo:**
Evitemos usar nombres de variable demasiado genéricos como numero,
texto, o mensaje.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ = 15

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ = \"esqueleto guerrero\"

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ = 0.50

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ = False

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ = -100

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ = \"Lugano\"

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ = 214

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ = True

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ = 49508310

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ = 3.141592

# 2. Operadores aritméticos

## Ejercicio 2.1

Armar un código que calcule las siguientes operaciones aritméticas, e
identificar cuál operación es cada una:

4 + 9

15 / 3

-5 + 2

9 \*\* 2

-23 -- 9

14 // 3

14 \* 3

14 % 3

3 / 4

# 3. Comparaciones

## Ejercicio 3.1

Sin escribir código, identificar el resultado de las siguientes
comparaciones:

45 \< 0

\"oro\" == \"oró\"

9.81 \> 9.8

\"diccionario\" == \"diccionario\"

3 != -3

80 \< 80

\"Carlos\" == \"CARLOS\"

80 \>= 80

3.14 \< 4

\"rojo\" != \"bordó\"

## Ejercicio 3.2

Dada la comparación edad \> 18, identificar el resultado cuando edad
valga:

- 90

- 3

- 17

- 18

- 19

## Ejercicio 3.3

Dada la comparación precio \<= 1500, identificar el resultado cuando
precio valga:

- 150

- 2300

- 1499

- 1500

- 1501

# 4. Operadores lógicos

## Ejercicio 4.1

Dadas las siguientes operaciones lógicas con and, or y not, identificar
qué valor booleano producirán:

- True or True

- False and True

- False or False or False or True or False

- True and True and True and False and True

- not True

- not False

- not False and True

- False or not True

- 5 \> 3 and 20 \<= 20

- -5 \< 0 or 100 \> 9

- \"árbol\" == \"arbol\"

- \"contraseña\" != \"CoNtRaSeÑa\"

- \"porque\" == \"por que\"

- \"\" != \"lechuga\"

- 40 != 400 and \"casa\" != \"CASA\"

## Ejercicio 4.2

Sin escribir código, anotar el resultado de las siguientes comparaciones
lógicas:

Dada la condición x \>= 0 and x \< 240, cuando x vale\...

- -1

- 0

- 1

- 239

- 240

- 241

Dada la condición edad \< 16 or edad \> 18, cuando edad vale\...

- 15

- 16

- 17

- 18

- 19

Dada la condición nivel \>= 50 and nivel \<= 100, si nivel vale\...

- 49

- 50

- 51

- 99

- 100

- 101

## Ejercicio 4.3

Nos trajeron un código que supuestamente debería detectar enemigos entre
nivel 20 y 25, pero hay algún error en la comparación que hace que
siempre devuelva False. Analicemos el código para encontrar el error,
anotando por qué siempre devuelve False, y finalmente resolvamos el
error para que la comparación funcione.

nivel \< 20 and nivel \> 25

## Ejercicio 4.4

Nos trajeron un código que debería detectar si alguien puede participar
en un torneo para participantes entre 13 y 19 años, pero hay algún error
en la comparación que hace que siempre devuelva True. Analicemos el
código para encontrar el error, anotando por qué siempre devuelve False,
y finalmente resolvamos el error para que la comparación funcione.

edad \>= 13 or edad \<= 19

# 5. Ejecución condicional - if

## Ejercicio 5.1

Razonar cuáles mensajes verá el usuario al ejecutar el siguiente código.

llueve = True

print(\"¡Buenos días!\")

if llueve:

print(\"Acordate de llevar paraguas.\")

## Ejercicio 5.2

Razonar cuáles mensajes se imprimirán al ejecutar el siguiente código.

edad = 17

print(\"¡Bienvenido al cine! Su entrada, por favor.\")

if edad \>= 18:

print(\"Muchas gracias, disfrute la función.\")

else:

print(\"Lo siento, pero esta película no es apta para menores.\")

## Ejercicio 5.3

Primero, leer el siguiente código:

if divisor != 0:

resultado = dividendo / divisor

print(f\"{dividendo} / {divisor} = {resultado}\")

else:

print(\"¡No se puede dividir por cero!\")

Finalmente, responder qué se imprimirá cuando:

a\) dividendo = 7

divisor = 0

b\) dividendo = 27

divisor = 9

# 6. Procedimientos sin parámetros

## Ejercicio 6.1 (parte 1)

Se nos pidió armar un sistema de menú para un restaurante. Crear un
programa que, **sin usar procedimientos**, de primero la bienvenida al
restaurante, y luego muestre tres categorías de productos (ej:
ensaladas, postres y bebidas). Al principio de cada categoría se deberá
avisar al usuario de qué categoría se trata, y dentro de cada categoría
se deberán listar cuatro artículos (doce en total).

## Ejercicio 6.1 (parte 2)

Siguiendo con el sistema del restaurante, nos piden separar las tres
categorías en procedimientos aparte. El programa principal deberá dar la
bienvenida, y luego invocar el procedimiento de cada categoría.

## Ejercicio 6.1 (parte 3)

Usando de base el código del ejercicio anterior, se quiere que el
usuario pueda elegir qué categoría mostrar. Cambiar el programa
principal para que solicite al usuario la categoría que quiera ver, y
muestre sólo la categoría elegida. Si se ingresa una categoría inválida,
se deberá avisar al usuario de su error sin mostrar ningún producto.

## Ejercicio 6.1 (parte 4)

Siguiendo con el código del restaurante, ahora el cliente nos pidió una
cuarta opción: ver el menú completo. El procedimiento para ver el menú
completo **no podrá usar prints**.

**Pista:** Podemos llamar a un procedimiento desde adentro de otro
procedimiento.

## Ejercicio 6.2

Armar un procedimiento que, sin usar parámetros, pida al usuario su
temperatura corporal y le avise si tiene fiebre o no. Para el ejercicio,
se considerará que una persona tiene fiebre si su temperatura supera los
36.9 grados Celsius.

Finalmente, nos avisaron que el programa deberá, al ejecutarse, tomar la
temperatura de tres personas en total, ni más ni menos.

## Ejercicio 6.3

Anotar qué se mostrará en cada print del siguiente código:

x = 9

print(x)

def f():

x = 5

print(x)

f()

print(x)

## Ejercicio 6.4

Anotar qué se mostrará en cada print del siguiente código:

y = 17

print(y)

def f():

global y

y = y - 3

print(y)

f()

print(y)

# 7. Procedimientos con parámetros

Los primeros ejercicios nos pedirán dar ejemplos de cómo invocarlos. A
continuación, veamos un ejemplo de qué se esperará como respuesta:

def saludar(aQuien):

print(f\"¡Hola {aQuien}!\")

Respuesta de ejemplo:

- Saludar recibe un parámetro, aQuien, que espera ser de tipo string. Si
  ponemos otro tipo de dato, igual funcionará porque no hace ninguna
  operación matemática ni de comparación con el parámetro.

- saludar(\"Leandro\") \--\> ¡Hola Leandro!

- saludar(\"estudiantes de la ETEC\") \--\> ¡Hola estudiantes de la
  ETEC!

- saludar(15) \--\> ¡Hola 15!

## Ejercicio 7.1

Dado el siguiente procedimiento, identificar de qué tipo es cada
parámetro, y luego dar dos ejemplos de cómo podría invocarse, y qué
generará el print interno en cada caso.

def repetirFrase(fraseARepetir, cantidadDeVeces):

fraseGenerada = fraseARepetir \* cantidadDeVeces

print(fraseGenerada)

## Ejercicio 7.2

Dado el siguiente procedimiento, identificar de qué tipo es cada
parámetro, y luego dar dos ejemplos de cómo podría invocarse, y qué
generará el print interno en cada caso.

def dejarEntrar(esVip, nombre):

if esVip:

print(f\"Buenos días {nombre}. Puede pasar al sector VIP\"

else:

print(f\"¡Hola {nombre}! Pase al sector común\"

## Ejercicio 7.3

Dado el siguiente procedimiento, identificar de qué tipo es cada
parámetro, y luego dar dos ejemplos de cómo podría invocarse, y qué
generará el print interno en cada caso.

def calcularPerimetroTriangulo(lado1, lado2, lado3):

perimetro = lado1 + lado2 + lado3

print(f\"El perímetro del triángulo es de {perimetro}\")

## Ejercicio 7.4

Dado el siguiente procedimiento, identificar de qué tipo es cada
parámetro, y luego dar dos ejemplos de cómo podría invocarse, y qué
generará el print interno en cada caso.

def entrarAlCine(nombre, edad, tieneEntrada):

if tieneEntrada:

if edad \>= 16:

print(f\"Pasá {nombre}. ¡Que disfrutes la función!\")

else:

print(f\"{nombre}, sos demasiado joven. Te devuelvo la plata\")

elif edad \< 16:

print(f\"{nombre}, sos demasiado joven. Por suerte no sacaste entrada\")

else:

print(f\"{nombre}, por favor sacá una entrada para pasar\")

## Ejercicio 7.1

Se quiere crear un procedimiento que, recibiendo el nombre de un
archivo, genere y muestre como se llamará la copia del archivo.
**Ejemplo:** Si se ingresa el archivo Ciudadania.txt, la copia se
llamará Copia de Ciudadania.txt

## Ejercicio 7.2

Se quiere crear un procedimiento que, recibiendo el nombre de una
persona, la salude de distinta forma:

- Si tiene el mismo nombre que nosotros, saludará comentando la
  coincidencia

- Si tiene un nombre distinto, le haga un saludo genérico

# 8. Funciones

## Ejercicio 8.1

Crear una función que, recibiendo una medida en centímetros, la devuelva
convertida a metros (con coma).

## Ejercicio 8.2

Crear una función que, recibiendo una medida en kilómetros, la devuelva
convertida a centímetros (con coma).

## Ejercicio 8.3

Crear una función que, recibiendo un número, devuelva:

- -1 si el número ingresado es negativo

- 1 si el número ingresado es positivo

- 0 si el número ingresado es cero

## Ejercicio 8.4

Un profe de matemática pidió crear una función en Python que pueda
calcular f(x) = 3x + 2. Escribir la función y, desde el programa
principal, invocarla y omprobar que funcione correctamente para los
valores x = -2, y también x = 5.

## Ejercicio 8.5

Armar una función que, recibiendo dos números, devuelva el mayor de los
dos.

## Ejercicio 8.6

Armar una función que, recibiendo dos números, devuelva el menor de los
dos.

## Ejercicio 8.7

Se quiere una función que, recibiendo cualquier usuario y clave,
devuelva un booleano avisando si se pudo iniciar sesión o no. Los datos
recibidos se compararán siempre contra el usuario \"ETEC\" y la clave
\"Lugano\" para verificar si son correctos o no.

Luego, armar un programa que pida un usuario y clave al usuario, los use
para invocar la función, y finalmente use el booleano de retorno para
mostrar al usuario distintos mensajes dependiendo si el inicio de sesión
fue exitoso o no.
