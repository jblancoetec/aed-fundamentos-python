# Evaluación de Algoritmos y Estructuras de Datos

Teoría

1\) ¿Cuál es la diferencia entre abrir un archivo en modo \"w\" y
abrirlo en modo \"a\"?

2\) ¿Con qué dos instrucciones se pueden borrar datos de una lista (no
lista de listas) que se llame alturaDePacientes? Escribir código que
declare esa lista con cuatro elementos a elección, y luego saque dos
datos que quieras de esa lista, usando una instrucción de borrado
distinta en cada caso.

3\) Para abrir archivos podemos especificar sus rutas absolutas o
relativas. ¿Cuál es la diferencia entre ambas? Dar dos ejemplos de rutas
de cada tipo.

4\) ¿Importa el orden en el que declaramos los datos en una lista? ¿Por
qué?

5\) ¿Cuál es la principal diferencia entre guardar información en
variables de un programa, y guardar esa misma información en un archivo?

6a) Enumerar las funciones que conozcas que sólo puedan usarse al abrir
un archivo en modo \"r\".

6b) Enumerar las funciones que conozcas que sólo puedan usarse al abrir
un archivo en modo \"w\" o \"a\".

7a) ¿Qué paso tenemos que hacer antes de poder leer o escribir los datos
de un archivo?

7b) ¿Qué paso conviene hacer cuando ya se terminó de leer o escribir lo
que necesitamos de un archivo?

8\) Explicá en tus palabras qué valor calcula el siguiente código, y con
qué criterio se hace el cálculo (aunque la lista no está declarada,
considerar que existe):

ventaMinima = 10000

ventasSatisfactorias = 0

for venta in ventas:

if venta \> ventaMinima:

ventasSatisfactorias = ventasSatisfactorias + 1

print(f\"{ventasSatisfactorias}/{len(ventas)} ventas satisfactorias\")

9\) ¿Con qué instrucción podemos agregar datos a una lista (no lista de
listas) que se llame listaDeCompras? Escribir código que declare la
lista primero con al menos dos datos, y luego agregue un nuevo dato a
elección a esa lista. Cuidado, que los datos que guardes en la lista
deberán tener sentido con el nombre de la variable.

10a) Escribí el código que haría falta para, usando la instrucción
while, recorrer e imprimir uno por uno todos los elementos de una lista
(no lista de listas) llamada estudiantes. Nótese que no hace falta
declarar la lista, y que contiene una cantidad desconocida de elementos
(el programa deberá funcionar bien sin importar el largo de la lista).

10b) Escribí el código que haría falta para, usando la instrucción for,
recorrer e imprimir uno por uno todos los elementos de una lista (no
lista de listas) llamada pedidos. Nótese que no hace falta declarar la
lista, y que contiene una cantidad desconocida de elementos (el programa
deberá funcionar bien sin importar el largo de la lista).

Práctica

1\) Completar el espacio en blanco para que el siguiente código
funcione, teniendo en cuenta que el archivo contiene un mensaje largo
con varios renglones.

archivoCorreo = open(\"Correo.txt\",\"r\")

contenidoCorreo =
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

print(f\"Ha recibido el siguiente mensaje: {contenidoCorreo}\")

archivo.close()

2\) Completar los espacios en blanco para que el siguiente código
funcione, dado un archivo que contiene, alternados, un renglón con el
nombre de una persona y otro con la fecha de su cumpleaños.

archivoCumpleaños = open(\"Calendario/CumpleañoJunio.txt\",\"r\")

nombre = \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

fechaCompleta = \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

print(f\"El {fechaCompleta} es el cumpleaños de {nombre}\")

archivoCumpleaños.close()

3\) Subrayar el error en el siguiente código, y describir abajo por qué
es un error. registroMeteorologico = open(\"RegistroMeteorologico.txt\",
\"r\")

medicionesAnteriores= registroMeteorologico.read()

print(\"Mediciones registradas hasta ahora:\\n{medicionesAnteriores})

temperatura = float(input(\"Ingrese la temperatura de hoy: \"))

humedadDeHoy = float(input(\"Ingrese la humedad de hoy: \"))

registroMeteorologico.write(\"Temp {temperatura}C, humedad
{humedad}%\\n\")

registroMeteorologico.close()

4\) ¿Qué índices válidos (que no den un error fuera de rango) pueden
usarse para acceder a los datos de la siguiente lista?

mochila = \[\"cuaderno\", \"cartuchera\", \"SUBE\", \"pañuelos\"\]

5\) ¿Qué índices válidos (que no den un error fuera de rango) pueden
usarse para acceder individualmente a cada dato de la siguiente lista?

dniEstudiantes = \[ \[\"Ana Gómez\", 48031048\], \[\"Bartolo
Sotomayor\", 47905106\], \[\"Cosme Fulanito\", 99431080\] \]

6\) En un juego, se quiere programar una habilidad para detectar pokémon
debilitados que estén cargados en la lista de pokémon salvajes del área.
Para este ejemplo, un pokémon se considerará debilitado cuando tengan
veinte puntos de vida o menos.

Los datos de cada pokémon son: nombre, tipos, vida.

Completar los espacios en el siguiente código para que reporte a los
pokémon atrapables al usar la habilidad.

pokemonesSalvajes = \[ \[\"Golem\", \"roca/tierra\", 54\],

\[\"Caterpie\", \"bicho\", 11\],

\[\"Ditto\", \"normal\", 21\],

\[\"Alakazam\",\"psíquico\", 37\],

\[\"Raichu\", \"eléctrico\", 2\] \]

for pokemonSalvaje in pokemonesSalvajes:

if \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_:

print(f\"¡Hay un {\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_} debilitado
cerca! Le

quedan {\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_} puntos de vida)

7\) ¿Cómo armarías una lista de listas para guardar las especificaciones
técnicas de computadoras? Aclará tres datos con tipos distintos (no
pueden ser, por ejemplo, tres strings) que haría falta almacenar, qué
tipo de dato es cada uno, y declará una lista de ejemplo con los datos
de tres computadoras con distintas especificaciones.

8\) ¿Cómo armarías una lista de listas que guarde información de temas
musicales disponibles en un sistema de compra online? Aclará tres datos
con tipos distintos (no pueden ser, por ejemplo, tres strings) que haría
falta almacenar, qué tipo de dato es cada uno, y declará una lista de
ejemplo con los datos de tres temas distintos. **Nota:** No hace falta
que los datos sean reales ni exactos.

# Evaluación de Algoritmos y Estructuras de Datos

Teoría

1a) Enumerar las funciones que conozcas que sólo puedan usarse al abrir
un archivo en modo \"r\".

1b) Enumerar las funciones que conozcas que sólo puedan usarse al abrir
un archivo en modo \"w\" o \"a\".

2\) ¿Con qué instrucción podemos agregar datos a una lista (no lista de
listas) que se llame listaDeCompras? Escribir código que declare la
lista primero con al menos dos datos, y luego agregue un nuevo dato a
elección a esa lista. Cuidado, que los datos que guardes en la lista
deberán tener sentido con el nombre de la variable.

3a) ¿Qué paso tenemos que hacer antes de poder leer o escribir los datos
de un archivo?

3b) ¿Qué paso conviene hacer cuando ya se terminó de leer o escribir lo
que necesitamos de un archivo?

4\) ¿Cuál es la principal diferencia entre guardar información en
variables de un programa, y guardar esa misma información en un archivo?

5\) ¿Importa el orden en el que declaramos los datos en una lista? ¿Por
qué?

6\) Para abrir archivos podemos especificar sus rutas absolutas o
relativas. ¿Cuál es la diferencia entre ambas? Dar dos ejemplos de rutas
de cada tipo.

7\) ¿Cuál es la diferencia entre abrir un archivo en modo \"w\" y
abrirlo en modo \"a\"?

8\) ¿Con qué dos instrucciones se pueden borrar datos de una lista (no
lista de listas) que se llame alturaDePacientes? Escribir código que
declare esa lista con cuatro elementos a elección, y luego saque dos
datos que quieras de esa lista, usando una instrucción de borrado
distinta en cada caso.

9a) Escribí el código que haría falta para, usando la instrucción while,
recorrer e imprimir uno por uno todos los elementos de una lista (no
lista de listas) llamada estudiantes. Nótese que no hace falta declarar
la lista, y que contiene una cantidad desconocida de elementos (el
programa deberá funcionar bien sin importar el largo de la lista).

9b) Escribí el código que haría falta para, usando la instrucción for,
recorrer e imprimir uno por uno todos los elementos de una lista (no
lista de listas) llamada pedidos. Nótese que no hace falta declarar la
lista, y que contiene una cantidad desconocida de elementos (el programa
deberá funcionar bien sin importar el largo de la lista).

10\) Explicá en tus palabras qué valor calcula el siguiente código, y
con qué criterio se hace el cálculo (aunque la lista no está declarada,
considerar que existe):

notaMinima = 7

desaprobados = 0

for nota in notas:

if nota \< notaMinima:

desaprobados = desaprobados + 1

print(f\"{desaprobados}/{len(notas)} notas desaprobadas\")

Práctica

1\) Completar los espacios en blanco para que el siguiente código
funcione, teniendo en cuenta que el archivo contiene, alternados, un
renglón con la hora de la alarma y otro con el mensaje descriptivo de
recordatorio.

archivoAlarma = open(\"Alarma01.txt\",\"r\")

horaAlarma = \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

mensajeAlarma = \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

print(f\"Recordatorio: {mensajeAlarma} a las {horaAlarma}\")

archivoAlarma.close()

2\) Completar el espacio en blanco para que el siguiente código
funcione, teniendo en cuenta que el archivo contiene una lista de
créditos larga con varios renglones.

archivoCreditos = open(\"Archivos/Créditos.txt\",\"r\")

contenidoCreditos = \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

print(f\"Este programa fue desarrollado por: {contenidoCreditos}\")

archivoCreditos.close()

3\) Subrayar el error en el siguiente código, y describir abajo por qué
es un error.

archivoCompras = open(\"Compras.txt\", \"a\")

comprasAnteriores = archivoCompras.read()

print(\"Compras registradas hasta ahora:\\n{comprasAnteriores})

articulo = input(\"Ingrese el artículo a comprado: \")

cantidad = int(input(\"Ingrese la cantidad comprada: \"))

archivoCompras.write(f\"{articulo} x{cantidad}\\n\")

archivoCompras.close()

4\) ¿Qué índices válidos (que no den un error fuera de rango) pueden
usarse para acceder a los datos de la siguiente lista?

cartuchera = \[\"resaltador amarillo\", \"lapiz 2B\", \"birome azul\",
\"goma de borrar\", \"clip\"\]

5\) ¿Qué índices válidos (que no den un error fuera de rango) pueden
usarse para acceder a los datos de la siguiente lista?

cursosEstudiantes = \[ \[\"Ana Gómez\", 4, \"B\"\], \[\"Cosme
Fulanito\", 3, \"D\"\] \]

6\) En un juego de avistamiento de animales, se quiere programar una
habilidad que identifique y muestre los datos de todos los animales de
categoría \"insecto\" que estén cargados en la lista de animales
presentes en el área.

Los datos del animal son: nombre, especie, nivel de peligrosidad.

Completar los espacios en el siguiente código para que reporte a los
animales correctos al usar la habilidad.

animales = \[ \[\"oso pardo\", \"mamífero\", 15\],

\[\"mantis\", \"insecto\", 1\],

\[\"rana venenosa\", \"reptil\", 9\],

\[\"tarántula\", \"arácnido\", 4\],

\[\"avispa\", \"insecto\", 7\] \]

for animal in animales:

if \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_:

print(f\"¡Detectado un insecto! Especie: {\_\_\_\_\_\_\_\_\_\_\_\_\_\_},

nivel de peligrosidad: {\_\_\_\_\_\_\_\_\_\_\_\_\_\_})

7\) ¿Cómo armarías una lista de listas para guardar información de
películas? Aclará al menos tres datos de distintos tipos (no pueden ser,
por ejemplo, tres strings) que haría falta almacenar, qué tipo de dato
es cada uno, y declará una lista de ejemplo con los datos de tres
películas distintas. **Nota:** No hace falta que los datos sean reales
ni exactos.

8\) ¿Cómo armarías una lista de listas que guarde información para una
agenda de contactos de celular? Aclará al menos tres datos de distintos
tipos (no pueden ser, por ejemplo, tres strings) que haría falta
almacenar, qué tipo de dato es cada uno, y declará una lista de ejemplo
con los datos de tres contactos distintos.

# Preguntas teóricas sin mezclar

1\) ¿Cuál es la principal diferencia entre guardar información en
variables de un programa, y guardar esa misma información en un archivo?

2\) Para abrir archivos podemos especificar sus rutas absolutas o
relativas. ¿Cuál es la diferencia entre ambas? Dar dos ejemplos de rutas
de cada tipo.

3a) ¿Qué paso tenemos que hacer antes de poder leer o escribir los datos
de un archivo?

3b) ¿Qué paso conviene hacer cuando ya se terminó de leer o escribir lo
que necesitamos de un archivo?

4a) Enumerar las funciones que conozcas que sólo puedan usarse al abrir
un archivo en modo \"r\".

4b) Enumerar las funciones que conozcas que sólo puedan usarse al abrir
un archivo en modo \"w\" o \"a\".

5\) ¿Cuál es la diferencia entre abrir un archivo en modo \"w\" y
abrirlo en modo \"a\"?

6\) ¿Importa el orden en el que declaramos los datos en una lista? ¿Por
qué?

7a) Escribí el código que haría falta para, usando la instrucción while,
recorrer e imprimir uno por uno todos los elementos de una lista (no
lista de listas) llamada estudiantes. Nótese que no hace falta declarar
la lista, y que contiene una cantidad desconocida de elementos (el
programa deberá funcionar bien sin importar el largo de la lista).

7b) Escribí el código que haría falta para, usando la instrucción for,
recorrer e imprimir uno por uno todos los elementos de una lista (no
lista de listas) llamada pedidos. Nótese que no hace falta declarar la
lista, y que contiene una cantidad desconocida de elementos (el programa
deberá funcionar bien sin importar el largo de la lista).

8\) ¿Con qué instrucción podemos agregar datos a una lista (no lista de
listas) que se llame listaDeCompras? Escribir código que declare la
lista primero con al menos dos datos, y luego agregue un nuevo dato a
elección a esa lista. Cuidado, que los datos que guardes en la lista
deberán tener sentido con el nombre de la variable.

9\) ¿Con qué dos instrucciones se pueden borrar datos de una lista (no
lista de listas) que se llame alturaDePacientes? Escribir código que
declare esa lista con cuatro elementos a elección, y luego saque dos
datos que quieras de esa lista, usando una instrucción de borrado
distinta en cada caso.

10\) Explicá en tus palabras qué valor calcula el siguiente código, y
con qué criterio se hace el cálculo (aunque la lista no está declarada,
considerar que existe):

ventaMinima = 10000

ventasSatisfactorias = 0

for venta in ventas:

if venta \> ventaMinima:

ventasSatisfactorias = ventasSatisfactorias + 1

print(f\"{ventasSatisfactorias}/{len(ventas)} ventas satisfactorias\")
