# Evaluación de Taller de Algoritmos y Programación

Teoría

1a) ¿Cómo funciona el operador lógico and? ¿Qué resultado da True and
False?

1b) ¿Cómo funciona el operador lógico or? ¿Qué resultado da True or
False?

2\) ¿Para qué sirve declarar una variable como global adentro de un
procedimiento o función?

[Para que cualquier cambio del valor adentro del procedimiento persista
al salir de él.]{.mark}

3\) ¿Para qué sirven los parámetros de un procedimiento o función?

[Para pasarle valores que use localmente, sin tener que referenciar a
variables globales directamente.]{.mark}

4\) ¿Qué es importante a la hora de elegir el nombre de un procedimiento
o función que definamos? Escribí al menos dos ejemplos de nombres que te
parezcan correctos para funciones o procedimientos.

[Que el nombre sea claro en qué tipo de dato almacena, y qué
significa.]{.mark}

[Ej: tieneLaLlave, naveX]{.mark}

5\) ¿Cuál es la diferencia entre hacer 5 / 2. y 5 // 2 en código de
Python? Anotar el resultado y cuál operación es la que se está
realizando en cada caso.

[5 / 2 = 2.5, pero 5 // 2 = 2. / calcula la división con coma, y // la
división entera]{.mark}

6\) Si queremos verificar que una variable llamada x esté entre los
valores 0 y 240, ¿cómo escribirías un único if para que haga esa
verificación?

[x \>= 0 and x \<=240, o bien 0 \<= x \<= 240]{.mark}

7\) ¿Cómo reconoce Python cuando el código está adentro o afuera de un
if, def, u otra estructura similar?

[Por la indentación (espacios o tabs).]{.mark}

8\) ¿Cuántos elif pueden haber después de un if?

[Cero o más]{.mark}

9\) ¿Cuántos else pueden haber después de un if?

[Uno o ninguno]{.mark}

10\) ¿Cuántos tipos de datos conocés? Describí cada uno, y, por cada
tipo de dato, escribí al menos dos ejemplos de valores que podrían
guardarse en él

[Números enteros: -5; 901]{.mark}

[Números con coma: 3.14; 9.81]{.mark}

[Texto: Contiene letras, números y símbolos para formar texto.
\"¡Hola!\"; \"Hora: 19:30\"]{.mark}

[Booleano: Contiene un valor de verdadero o falso. True; False]{.mark}

11\) ¿Cuál es la diferencia entre un solo igual (=) y dos juntos (==)?
¿Para qué sirve cada uno?

[Un igual asigna datos a la variable a su izquierda, y dos iguales
compara si los datos a ambos lados son iguales.]{.mark}

12a) ¿Para qué sirve la instrucción return adentro de una función?

[Para que la función genere un valor que pueda ser usado afuera de
ella]{.mark}

12b) ¿Qué es indispensable hacer con el valor de retorno de la función
para poder usarlo después?

[Deberá ser asignado a alguna variable, usado para operaciones o
comparaciones, etc.]{.mark}

13a) ¿Por qué se genera un error cuando intentamos sumar un número a un
dato que recibimos de un input()?

[Porque input devuelve un string, que no se puede sumar con un
número.]{.mark}

13b) ¿Cómo podemos resolver ese error?

[Habrá que convertir el string a entero (si se puede) antes de hacer la
suma.]{.mark}

14\) ¿Para qué sirven las variables en el código?

[Para guardar datos y poder usarlos más adelante.]{.mark}

Práctica

1\) Leer el siguiente código, y escribir al final lo que el usuario verá
en la consola, teniendo en cuenta los print usados:

x = 5

print(x) [5]{.mark}

x = 4

print(x) [4]{.mark}

x = x - 3

print(x) [1]{.mark}

2\) Leer el siguiente código, y escribir al final lo que el usuario verá
en la consola, teniendo en cuenta los print usados:

x = 11

print(x) [11]{.mark}

print(y) [ERROR: variable y no definida]{.mark}

y = x \* 5

3\) Anotar al lado de las siguientes variables el tipo de dato que
almacenan:

vidaZombi = 24 [int]{.mark}

esRecreo = \"True\" [str]{.mark}

altura = 1.57 [float]{.mark}

tesoro = \"diamante\" [str]{.mark}

estaLloviendo = False [bool]{.mark}

4\) Subrayar todas las variables del siguiente código, y anotar cuántas
son en total:

[correoGuardado]{.mark} = \"cfulanito@gmail.com\"

[claveGuardada]{.mark} = \"Cosme1748\"

[correoIngresado]{.mark} = input(\"Correo: \")

[claveIngresada]{.mark} = input(\"Clave: \")

[correoCorrecto]{.mark} = correoGuardado == correoIngresado

[claveCorrecta]{.mark} = claveGuardada == claveIngresada

if correoCorrecto and claveCorrecta:

print(f\"Sesión iniciada como {correoIngresado}\")

else:

print(\"Verifique sus datos e intente nuevamente.\")

El programa tiene \_\_[6]{.mark}\_\_ variables:

5\) Dada la siguiente comparación:

puntaje \> 2000

Identificar el resultado de la comparación si puntaje vale\...

- 1999 [False]{.mark}

- 2000 [False]{.mark}

- 2001 [True]{.mark}

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

- 16 [Puedes votar si quieres]{.mark}

- 33 [Es obligatorio que votes]{.mark}

7\) Dado el siguiente código:

def procedimientoMisterioso():

print(\"Lluvioso\")

def otroProcedimientoMisterioso():

print(\"Despejado\")

print(\"Nublado\")

otroProcedimientoMisterioso()

print(\"Tormentoso\")

Escribir aquí debajo todo lo que se imprimirá al ejecutarlo.

[Nublado]{.mark}

[Despejado]{.mark}

[Tormentoso]{.mark}

8\) Dado el siguiente código:

def restar(numA, numB):

resultado = numA -- numB

print(f\"{numA} - {numB} = {resultado}\")

numero1 = 6

numero2 = 7

restar(numero2,numero1)

Escribir qué mensaje se imprimirá al ejecutarlo.

[7 - 6 = 1]{.mark}

9\) El siguiente código contiene un error. Detectar y explicar cuál es,
y finalmente explicar cómo se podría resolver el error (no hace falta
escribir el código corregido).

def elevarAlCuadrado(num):

resultado = num \*\* 2

return resultado

miNumero = 4

elevarAlCuadrado(miNumero)

print(f\"{miNumero} al cuadrado da [{resultado}]{.mark}\"

[El error es que se intenta usar la variable resultado, que sólo existe
adentro de la función. Faltó asignar el valor de retorno a una variable,
y usarla en el print.]{.mark}

10\) Dado el siguiente código:

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

[cargaDescontada]{.mark}

- Variables globales:

[cargaEnSube, costoDelBoleto, respuestaCarga]{.mark}

b\) Anotar a continuación todo lo que verá el usuario cuando se ejecute
el código. Pista: No sólo se trata de los print.

[Ingrese su saldo (con coma): \$10]{.mark}

[Viaje cobrado. Saldo restante: \$9.5]{.mark}

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

print(x) [2]{.mark}

x = 9

print(x) [9]{.mark}

x = x \* 2

print(x) [18]{.mark}

2\) Leer el siguiente código, y escribir al final lo que el usuario verá
en la consola, teniendo en cuenta los print usados:

x = 9

print(x) [9]{.mark}

print(y) [ERROR: Uso de variable sin declarar: y]{.mark}

y = x / 3

3\) Anotar al lado de las siguientes variables el tipo de dato que
almacenan:

misionRealizada = True [bool]{.mark}

gravedad = 9.81 [float]{.mark}

contraseña = \"1234\" [string]{.mark}

nivel = 15 [int]{.mark}

mes = \"junio\" [string]{.mark}

4\) Subrayar todas las variables del siguiente código, y anotar cuántas
son en total:

[nombre]{.mark} = input(\"¡Buen día! Ingrese su nombre: \")

[respuestaEdad]{.mark} = input(\"Ahora, ingrese su edad: \")

[edad]{.mark} = int(respuestaEdad)

[esMayorDeEdad]{.mark} = edad \>= 18

if esMayorDeEdad:

print(f\"Muy bien {nombre}, aquí tiene el menú y la carta de vinos\")

else:

print(f\"Muy bien {nombre}, aquí tiene el menú\")

El programa tiene \_\_[4]{.mark}\_\_ variables.

5\) Dada la siguiente comparación:

vida \<= 10

Identificar el resultado de la comparación si puntaje vale\...

- 9 [True]{.mark}

- 10 [True]{.mark}

- 11 [False]{.mark}

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

- 3 [¡Está re cerca! Vayamos caminando]{.mark}

- 19 [Queda algo lejos, vayamos en colectivo]{.mark}

7\) Dado el siguiente código:

def procedimientoMisterioso():

print(\"Zapatillas\")

def otroProcedimientoMisterioso():

print(\"Campera\")

print(\"Remera\")

print(\"Pantalones\")

procedimientoMisterioso()

Escribir aquí debajo todo lo que se verá al ejecutarlo.

[Remera]{.mark}

[Pantalones]{.mark}

[Zapatillas]{.mark}

8\) Dado el siguiente código:

def dividir(numA, numB):

resultado = numA / numB

print(f\"{numA} / {numB} = {resultado}\")

numero1 = 2

numero2 = 4

restar(numero2,numero1)

Escribir qué mensaje se imprimirá al ejecutarlo.

[4 / 2 = 2.0]{.mark}

9\) El siguiente código contiene un error. Detectar y explicar cuál es,
y finalmente explicar cómo se podría resolver el error (no hace falta
escribir el código corregido).

def dividirPorCuatro(num):

resultado = num / 4

return resultado

miNumero = 12

numeroRecibido = dividirPorCuatro(miNumero)

print(f\"{[num]{.mark}} dividido por cuatro da {numeroRecibido}\"

[Se intentó usar la variable num, que sólo existe en la función. En vez
de num, en el print debería haberse usado miNumero.]{.mark}

10\) Dado el siguiente código:

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

[cargaNueva]{.mark}

- Variables globales:

[respuestaCarga, cargaEnSube, recargaPendiente]{.mark}

b\) Anotar a continuación todo lo que verá el usuario cuando se ejecute
el código. Pista: No sólo se trata de los print.

[Ingrese su saldo (con coma): \$500]{.mark}

[Recarga acreditada. Saldo: \$2500.0]{.mark}
