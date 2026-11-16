# Evaluación de Taller de Algoritmos y Programación

Teoría

1a) ¿Cómo funciona el operador lógico and? ¿Qué resultado da True and
False?

1b) ¿Cómo funciona el operador lógico or? ¿Qué resultado da True or
False?

2\) ¿Para qué sirve declarar una variable como global adentro de un
procedimiento o función?

3\) ¿Para qué sirven los parámetros de un procedimiento o función?

4\) ¿Qué es importante a la hora de elegir el nombre de un procedimiento
o función que definamos? Escribí al menos dos ejemplos de nombres que te
parezcan correctos para funciones o procedimientos.

5\) ¿Cuál es la diferencia entre hacer 5 / 2. y 5 // 2 en código de
Python? Anotar el resultado y cuál operación es la que se está
realizando en cada caso.

6\) Si queremos verificar que una variable llamada x esté entre los
valores 0 y 240, ¿cómo escribirías un único if para que haga esa
verificación?

7\) ¿Cómo reconoce Python cuando el código está adentro o afuera de un
if, def, u otra estructura similar?

8\) ¿Cuántos elif pueden haber después de un if?

9\) ¿Cuántos else pueden haber después de un if?

10\) ¿Cuántos tipos de datos conocés? Describí cada uno, y, por cada
tipo de dato, escribí al menos dos ejemplos de valores que podrían
guardarse en él

11\) ¿Cuál es la diferencia entre un solo igual (=) y dos juntos (==)?
¿Para qué sirve cada uno?

12a) ¿Para qué sirve la instrucción return adentro de una función?

12b) ¿Qué es indispensable hacer con el valor de retorno de la función
para poder usarlo después?

13a) ¿Por qué se genera un error cuando intentamos sumar un número a un
dato que recibimos de un input()?

13b) ¿Cómo podemos resolver ese error?

14\) ¿Para qué sirven las variables en el código?

Práctica

1\) Leer el siguiente código, y escribir al final lo que el usuario verá
en la consola, teniendo en cuenta los print usados:

x = 5

print(x)

x = 4

print(x)

x = x - 3

print(x)

2\) Leer el siguiente código, y escribir al final lo que el usuario verá
en la consola, teniendo en cuenta los print usados:

x = 11

print(x)

print(y)

y = x \* 5

3\) Anotar al lado de las siguientes variables el tipo de dato que
almacenan:

vidaZombi = 24

esRecreo = \"True\"

altura = 1.57

tesoro = \"diamante\"

estaLloviendo = False

4\) Subrayar todas las variables del siguiente código, y anotar cuántas
son en total:

correoGuardado = \"cfulanito@gmail.com\"

claveGuardada = \"Cosme1748\"

correoIngresado = input(\"Correo: \")

claveIngresada = input(\"Clave: \")

correoCorrecto = correoGuardado == correoIngresado

claveCorrecta = claveGuardada == claveIngresada

if correoCorrecto and claveCorrecta:

print(f\"Sesión iniciada como {correoIngresado}\")

else:

print(\"Verifique sus datos e intente nuevamente.\")

El programa tiene \_\_\_\_\_ variables:

5\) Dada la siguiente comparación:

puntaje \> 2000

Identificar el resultado de la comparación si puntaje vale\...

- 1999

- 2000

- 2001

6\) Dado el siguiente código:

if edad \< 16:

print(\"Aún no puedes votar\")

elif edad \< 18:

print(\"Puedes votar si quieres\")

elif edad \< 70:

print(\"Es obligatorio que votes\")

else:

print(\"A tu edad, votar ya no es obligatorio\")

Identificar qué se imprimirá si edad vale\...

- 16

- 33

7\) Dado el siguiente código:

def procedimientoMisterioso():

print(\"Lluvioso\")

def otroProcedimientoMisterioso():

print(\"Despejado\")

print(\"Nublado\")

otroProcedimientoMisterioso()

print(\"Tormentoso\")

Escribir aquí debajo todo lo que se imprimirá al ejecutarlo.

8\) Dado el siguiente código:

def restar(numA, numB):

resultado = numA -- numB

print(f\"{numA} - {numB} = {resultado}\")

numero1 = 6

numero2 = 7

restar(numero2,numero1)

Escribir qué mensaje se imprimirá al ejecutarlo.

9\) El siguiente código contiene un error. Detectar y explicar cuál es,
y finalmente explicar cómo se podría resolver el error (no hace falta
escribir el código corregido).

def elevarAlCuadrado(num):

resultado = num \*\* 2

return resultado

miNumero = 4

elevarAlCuadrado(miNumero)

print(f\"{miNumero} al cuadrado da {resultado}\"

10\) Dado el siguiente código:

cargaEnSube = 100.0

costoDelBoleto = 0.50

def cobrarBoleto():

global cargaEnSube

cargaDescontada= cargaEnSube -- costoDelBoleto

cargaEnSube = cargaDescontada

respuestaCarga = input(\"Ingrese su saldo (con coma): \$\")

cargaEnSube = float(respuestaCarga)

cobrarBoleto()

print(f\"Viaje cobrado. Saldo restante: \${cargaEnSube}\")

a\) Identificar y agrupar cuáles variables son locales, y cuáles son
globales:

- Variables locales:

- Variables globales:

b\) Anotar a continuación todo lo que verá el usuario cuando se ejecute
el código. Pista: No sólo se trata de los print.

# Evaluación de Taller de Algoritmos y Programación

Teoría

1\) ¿Para qué sirven las variables en un código?

2\) ¿Para qué sirven los parámetros de un procedimiento o función?

3\) ¿Cómo reconoce Python cuando el código está adentro o afuera de un
if, def, u otra estructura similar?

4\) ¿Cuál es la diferencia entre un solo igual (=) y dos juntos (==)?
¿Para qué sirve cada uno?

5\) ¿Para qué sirve declarar una variable como global adentro de un
procedimiento o función?

6a) ¿Por qué se genera un error cuando intentamos sumar un número a un
dato que recibimos de un input()?

6b) ¿Cómo podemos resolver ese error?

7a) ¿Para qué sirve la instrucción return adentro de una función?

7b) ¿Qué es indispensable hacer con el valor de retorno de la función
para poder usarlo después?

8a) ¿Cómo funciona el operador lógico and? ¿Qué resultado da False and
True?

8b) ¿Cómo funciona el operador lógico or? ¿Qué resultado da False or
True?

9\) ¿Qué es importante a la hora de elegir el nombre de un procedimiento
o función que definamos? Escribí al menos dos ejemplos de nombres que te
parezcan correctos para funciones o procedimientos.

10\) ¿Cuántos elif pueden haber después de un if?

11\) Si queremos verificar que una variable llamada x esté entre los
valores 0 y 240, ¿cómo escribirías un único if para que haga esa
verificación?

12\) ¿Cuál es la diferencia entre hacer 5 / 2, y 5 // 2 en código de
Python? Anotar el resultado y cuál operación es la que se está
realizando en cada caso.

13\) ¿Cuántos tipos de datos conocés? Describí cada uno, y, por cada
tipo de dato, escribí al menos dos ejemplos de valores que podrían
guardarse en él

14\) ¿Cuántos else pueden haber después de un if?

Práctica

1\) Leer el siguiente código, y escribir al final lo que el usuario verá
en la consola, teniendo en cuenta los print usados:

x = 2

print(x)

x = 9

print(x)

x = x \* 2

print(x)

2\) Leer el siguiente código, y escribir al final lo que el usuario verá
en la consola, teniendo en cuenta los print usados:

x = 9

print(x)

print(y)

y = x / 3

3\) Anotar al lado de las siguientes variables el tipo de dato que
almacenan:

misionRealizada = True

gravedad = 9.81

contraseña = \"1234\"

nivel = 15

mes = \"junio\"

4\) Subrayar todas las variables del siguiente código, y anotar cuántas
son en total:

nombre = input(\"¡Buen día! Ingrese su nombre: \")

respuestaEdad = input(\"Ahora, ingrese su edad: \")

edad = int(respuestaEdad)

esMayorDeEdad = edad \>= 18

if esMayorDeEdad:

print(f\"Muy bien {nombre}, aquí tiene el menú y la carta de vinos\")

else:

print(f\"Muy bien {nombre}, aquí tiene el menú\")

El programa tiene \_\_\_\_\_ variables.

5\) Dada la siguiente comparación:

vida \<= 10

Identificar el resultado de la comparación si puntaje vale\...

- 9

- 10

- 11

6\) Dado el siguiente código:

if distancia \> 20:

print(\"Queda muy lejos, mejor no vamos\")

elif edad \> 10:

print(\"Queda algo lejos, vayamos en colectivo\")

elif edad \> 3:

print(\"Queda bastante cerca, vayamos en bicicleta\")

else:

print(\"¡Está re cerca! Vayamos caminando \")

Identificar qué se imprimirá si distancia vale\...

- 3

- 19

7\) Dado el siguiente código:

def procedimientoMisterioso():

print(\"Zapatillas\")

def otroProcedimientoMisterioso():

print(\"Campera\")

print(\"Remera\")

print(\"Pantalones\")

procedimientoMisterioso()

Escribir aquí debajo todo lo que se verá al ejecutarlo.

8\) Dado el siguiente código:

def dividir(numA, numB):

resultado = numA / numB

print(f\"{numA} / {numB} = {resultado}\")

numero1 = 2

numero2 = 4

restar(numero2,numero1)

Escribir qué mensaje se imprimirá al ejecutarlo.

9\) El siguiente código contiene un error. Detectar y explicar cuál es,
y finalmente explicar cómo se podría resolver el error (no hace falta
escribir el código corregido).

def dividirPorCuatro(num):

resultado = num / 4

return resultado

miNumero = 12

numeroRecibido = dividirPorCuatro(miNumero)

print(f\"{num} dividido por cuatro da {numeroRecibido}\"

10\) Dado el siguiente código:

cargaEnSube = 100.0

recargaPendiente = 2000.0

def acreditarRecarga():

global cargaEnSube

cargaNueva = cargaEnSube + recargaPendiente

cargaEnSube = cargaNueva

respuestaCarga = input(\"Ingrese su saldo (con coma): \$\")

cargaEnSube = float(respuestaCarga)

acreditarRecarga()

print(f\"Recarga acreditada. Saldo: \${cargaEnSube}\")

a\) Identificar y agrupar cuáles variables son locales, y cuáles son
globales:

- Variables locales:

- Variables globales:

b\) Anotar a continuación todo lo que verá el usuario cuando se ejecute
el código. Pista: No sólo se trata de los print.
