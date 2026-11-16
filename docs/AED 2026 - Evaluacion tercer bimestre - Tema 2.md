# Evaluación de Algoritmos y Estructuras de Datos

1\) Se tiene un proyecto alojado en la carpeta

/home/etec/Documentos/Escuela/

Escribir la ruta absoluta de un archivo CSV cuando su ruta relativa es:

Notas/4B/arquitectura.csv

2\) Se tiene la siguiente función incompleta para mostr

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
