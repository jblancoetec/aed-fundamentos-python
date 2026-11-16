A continuación, se provee una lista de ejercicios adicionales para
practicar y reforzar los temas vistos en clase para quienes necesiten
practicarlos más. Los ejercicios van en orden de dificultad creciente.

# 1. Acceso por índices

## Ejercicio 1.1

Dada la siguiente lista de colores:

colores = \[\"gris\", \"azul\", \"violeta\", \"verde\", \"rojo\",
\"naranja\", \"marrón\"\]

Escribir el código para acceder a\...

a\) El primer color de la lista

b\) El color violeta

c\) El anteúltimo color

Aparte, escribir qué aparecería en pantalla con los siguientes print:

d\) print(colores\[5\])

e\) print(colores\[-5\])

f\) print(colores\[7\])

## Ejercicio 1.2

Con la misma lista de colores, armar un programa que acceda a ella para
imprimir todos los colores, usando un print por color. **Consejo:** Para
practicar mejor los índices, resolver el ejercicio sin usar
repeticiones.

## Ejercicio 1.3

Con la misma lista de colores, armar un programa que los imprima de
atrás para adelante, usando un print por color. **Consejo:** Para
practicar mejor los índices, resolver el ejercicio sin usar
repeticiones.

## Ejercicio 1.4

Siguiendo con la lista de colores del ejercicio 1, se pide armar un
programa para una pinturería. En el programa, queremos que el usuario
pueda ingresar el índice de dos colores que quiera pedir, y el programa
le muestre en un único print los colores de pintura que corresponden en
el mismo orden que los haya ingresado.

# 2. Recorrido de números con while

Los siguientes ejercicios deberán resolverse usando while.

## Ejercicio 2.1

Crear un programa que use un while para recorrer los números del 0 al
99, y los imprima uno por uno usando print.

## Ejercicio 2.2

Crear un programa que use un while para recorrer los números del 150 al
250, y los imprima uno por uno usando print.

## Ejercicio 2.3

Crear un programa que use un while para recorrer todos los números
impares del 31 al 91, y los imprima uno por uno usando print.

## Ejercicio 2.4

Crear un programa que use un while para recorrer todos los números del 0
al --44 (empezando desde el cero), y los imprima uno por uno usando
print.

## Ejercicio 2.5

Crear un programa que use un while para recorrer todos los números del
100 al -120, yendo de cinco en cinco (ej: 100, 95, 90, 85, etc.)

# 3. Recorrido de listas con while

## Ejercicio 3.1

Dada la siguiente lista de biomas en un mapa de Minecraft, armar un
programa que use un while para recorrer todos los índices, y muestre el
nombre de cada bioma en orden.

niveles = \[\"Pradera\", \"Bosque\", \"Bosque\", \"Pantano\",
\"Bosque\", \"Montaña\", \"Pradera\", \"Playa\", \"Bosque\",
\"Pradera\", \"Playa\"\]

## Ejercicio 3.2

Data la siguiente lista de artículos ordenados por precio, armar un
programa que use un while para recorrer la lista en orden inverso,
mostrando los artículos de menor a mayor precio.

Armar dos versiones de este código:

a\) Recorriendo la lista con índices positivos.

b\) Recorriendo la lista con índices negativos.

articulos = \[\"Cocina industrial a gas (Eskabe) \$350.000\", \"Cocina a
gas (Volcán) \$205.000\", \"Anafe eléctrico doble (Gadnic) \$160.000\",
\"Anafe eléctrico simple (Gadnic) \$90.000\", \"Anafe a garrafa (Eskabe)
\$87.000\"\]

## Ejercicio 3.3

# 4. While con condiciones

## Ejercicio 4.1

Con el programa del [ejercicio 2.1](#ejercicio-2.1) como base, agregar
un if para que sólo se impriman los números pares. **Ayuda:** Podemos
decir que un número es par si, al dividirlo por dos, el resto de dicha
división es cero (ignoremos por ahora que el cero no debería ser par ni
impar).

## Ejercicio 4.2

Con el programa del [ejercicio 2.5](#ejercicio-2.5) como base, agregar
un if para que sólo se impriman los números que sean negativos y
múltiplos de tres. **Ayuda:** Podemos decir que un número es múltiplo de
tres si, al dividirlo por tres, el resto de dicha división es cero.

## Ejercicio 4.3 (parte 1)

Con el programa del [ejercicio 3.1](#ejercicio-3.1) como base, agregar
un if para que sólo se imprima el nombre del bioma cuando sea un bosque.

## Ejercicio 4.3 (parte 2)

Con el programa del ejercicio 4.3 (parte 1) como base, cambiar que en
vez de imprimir cada vez que encuentra un bioma de bosque en la lista,
use ese if para ir contando cuántas veces el bioma era de bosque, y al
final informe al usuario cuántos bosques se cruzó recorriendo la lista.
**Pista:** deberían ser cuatro.

## Ejercicio 4.3 (parte 3)

Con el programa del ejercicio 4.3 (parte 2) como base, cambiar el código
para que, en vez de contar los bosques, se pueda contar cualquier bioma
que ingrese el usuario (aunque, si ingresa un bioma que no está en la
lista o lo escribe mal, el programa lo va a encontrar cero veces).

## Ejercicio 4.4

Se tiene la siguiente lista de premios en una lotería:

premios = \[\"mouse inalámbrico\", \"teclado mecánico\", \"auriculares
con micrófono\", \"pen drive 8 gb\", \"LED rojo quemado\"\]

Armar un programa que elija al azar un premio, y le diga al usuario qué
se ganó.

# 5. Lista única

## Ejercicio 5.1 (parte 1)

Se quiere guardar los siguientes datos para una tabla de puntajes:

- Puntaje obtenido

- Nombre del jugador

- Dificultad (fácil o difícil)

Crear una lista única que contenga los datos de tres partidas jugadas.

## Ejercicio 5.1 (parte 2)

Con la lista ya creada, armar un programa que muestre la tabla de
puntajes, pero **sin usar repeticiones de ningún tipo**. Se deberá
acceder siempre con índices numéricos.

## Ejercicio 5.1 (parte 3)

Con la misma lista de la parte 1, mostrar la tabla de puntajes con una
repetición while.

## Ejercicio 5.1 (parte 4)

Con la misma lista de la parte 1, mostrar la tabla de puntajes usando
una repetición for y la función range().

## Ejercicio 5.1 (parte 5)

Con la misma lista de la parte 1, mostrar la tabla de puntajes usando
una repetición for, pero sin range().

## Ejercicio 5.2

# 6. Listas paralelas

## Ejercicio 6.1

Un quiosco quiere mostrar tiene en listas paralelas, almacenados el
nombre de las cosas que ofrece en una lista, y los precios de cada
artículo en la otra.

articulosEnVenta = \[ \"alfajor\", \"mentitas\", \"chocolate\",
\"chicle\" \]

precios = \[ 1500, 900, 2300, 500\]

Escribir el código para acceder a\...

a\) El precio de las mentitas

b\) El nombre del artículo que vale \$2300

c\) El nombre y el precio del último artículo

## Ejercicio 6.2

Con las listas paralelas del ejercicio anterior, armar un programa para
una expendedora de golosinas. El usuario deberá ingresar el número de
artículo (usando como número los índices de cada golosina), y el
programa deberá decirle cuánto cuesta esa golosina. Si el usuario
ingresa un índice inválido, será su culpa: en este ejercicio no hace
falta asegurarnos que no se salga de rango.

## Ejercicio 6.3

Para terminar el programa de la expendedora de golosinas, se quiere
hacerle unos cambios adicionales:

- Antes que nada, el usuario deberá responder cuánto dinero deposita en
  la máquina

- Luego, se le pedirá como siempre el número de artículo a comprar, y el
  programa le mostrará el precio del artículo

- Finalmente, el programa intentará cobrarle al usuario el artículo que
  quiere comprar:

  - Si le alcanza el dinero que depositó, deberá decirle que le entrega
    la golosina elegida, y avisarle cuánto dinero le quedó de vuelto

  - Si no le alcanza el dinero depositado, el programa le debe decir que
    no le alcanza para comprar la golosina, y avisarle que le devuelve
    todo el dinero
