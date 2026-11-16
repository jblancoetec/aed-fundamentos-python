# Evaluación de Algoritmos y Estructuras de Datos

1\) ¿Qué ve el usuario cuando se ejecuta el siguiente código?

mensaje = \"Hoy aprendimos historia\"\
print(\"historia\" in mensaje)

2\) ¿Qué ve el usuario cuando se ejecuta el siguiente código?

texto = \"Algoritmos\"\
print(texto\[-3\])

3\) ¿Cuáles son las tres formas de abrir un archivo que vimos en clase?
Explicá en tus palabras qué particularidades tiene cada una de ellas.

4\) ¿Qué hace el siguiente código con el archivo?

archivo = open(\"datos.txt\", \"r\")\
contenido = archivo.read()

a)  Abre el archivo para leer, y lo cierra automáticamente después de
    leerlo

b)  Abre el archivo para leer, y lo deja abierto después de leerlo

c)  Abre el archivo para escribir y se genera un error, porque el modo
    de escritura no permite usar **read**

d)  Borra el contenido de **datos.txt** antes de leerlo, por lo que el
    read no recibe nada

5\) Completar el espacio en blanco para que el siguiente código
funcione, teniendo en cuenta que el archivo **Correo.txt** contiene un
mensaje largo, de varios renglones.

archivoCorreo = open(\"Correo.txt\",\"r\")

contenidoCorreo =
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

print(f\"Ha recibido el siguiente mensaje: {contenidoCorreo}\")

archivo.close()

6\) Completar los espacios en blanco para que el siguiente código
funcione, considerando que el archivo **Cumpleaños.txt** contiene,
alternados, un renglón con el nombre de una persona y otro con la fecha
de su cumpleaños.

archivoCumpleaños = open(\"Calendario/Cumpleaños.txt\",\"r\")

nombre = \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

fechaCompleta = \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

print(f\"El {fechaCompleta} es el cumpleaños de {nombre}\")

archivoCumpleaños.close()

7\) ¿Qué índices válidos (que no den un error fuera de rango) pueden
usarse para acceder a los datos de la siguiente lista?

mochila = \[\"cuaderno\", \"cartuchera\", \"SUBE\", \"pañuelos\"\]

8\) ¿Qué índices válidos (que no den un error fuera de rango) pueden
usarse para acceder individualmente a cada dato de la siguiente lista?

dniEstudiantes = \[ \[\"Ana Gómez\", 48031048\], \[\"Bartolo
Sotomayor\", 47905106\], \[\"Cosme Fulanito\", 99431080\] \]

9\) ¿Qué ve el usuario cuando se ejecuta el siguiente código?

frutas = \[\"manzana\", \"pera\", \"banana\"\]\
frutas.append(\"uva\")\
frutas.pop(2)\
print(frutas)\
print(len(frutas))\
print(frutas\[2\])

10\) ¿Qué números ve el usuario cuando se ejecuta el siguiente código?

for i in range(6, 0, -2):\
print(i)

11\) ¿Qué valor queda almacenado en la variable **resultado** después de
ejecutar el siguiente código?

def buscarCaracter(texto,caracter):\
for i in range(len(texto)):\
if texto \[i\] == caracter:\
return i\
return -1\
\
resultado = buscarCaracter(\"lanzazos\", \"z\"))

12\) ¿Por qué el orden en el que declaramos los datos en un diccionario
no es un problema comparado con cuando usamos listas?

13\) ¿Cómo podemos agregar un nuevo dato a un diccionario? Escribir una
única línea de código donde se agregue un nuevo dato que tenga sentido
al siguiente diccionario:

enemigo = { \"nombre\": \"Ninja\", \"vida\":15, \"defensa\":3.5 }

14\) En un juego, se quiere programar una habilidad para detectar
pokémon debilitados que estén cargados en la lista de pokémon salvajes
del área. Para este ejemplo, un pokémon se considerará debilitado cuando
tenga doce puntos de vida o menos.

Completar los espacios en el siguiente código para que reporte a los
pokémon atrapables al usar la habilidad.

pokemonesSalvajes = \[

{\"nombre\":\"Golem\" , \"tipos\":\"roca/tierra\", \"vida\":54},

{\"nombre\":\"Caterpie\", \"tipos\":\"bicho\" , \"vida\":11},

{\"nombre\":\"Ditto\" , \"tipos\":\"normal\" , \"vida\":21},

{\"nombre\":\"Alakazam\", \"tipos\":\"psíquico\" , \"vida\":13},

{\"nombre\":\"Raichu\" , \"tipos\":\"eléctrico\" , \"vida\": 2}

\]

for pokemon in pokemonesSalvajes:

if \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_:

print(f\"¡Hay un {\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_}
debilitado cerca!\")

print(f\"Le quedan
{\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_} puntos de vida\")

print(f\"Y sus tipos son
{\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_}\")
