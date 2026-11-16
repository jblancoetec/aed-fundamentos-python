# Evaluación de Taller de Algoritmos y Programación

1\) Se tiene la siguiente documentación de una función:

> random.randint(a,b) -\> int
>
> Retorna un número al azar entre A y B (inclusive).

Completar el espacio en el siguiente código para que funcione
correctamente.

from random import randint

respuesta1 = input(\"Elegi el número mínimo: \")

num1 = int(respuesta1)

respuesta2 = input(\"Elegi el número máximo: \")

num2 = int(respuesta2)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

print(f\"El número generado al azar es: {numeroGenerado}\")

2\) Hay un error en el siguiente código. Subrayar la línea donde ocurra
el error. Luego, escribir abajo por qué es un error, y cómo se debería
reescribir esa línea para que el programa funcione correctamente.

from math import sqrt

def calcularHipotenusa(a,b):

h = math.sqrt(a\*\*2 + b\*\*2)

return h

respuesta1 = input(\"Ingresá el largo de un cateto: \")

cateto1 = float(respuesta1)

respuesta2 = input(\"Ingresá el largo del otro cateto: \")

cateto2 = float(respuesta2)

hipotenusa = calcularHipotenusa(cateto1,cateto2)

print(f\"La hipotenusa del triángulo con esos catetos mide
{hipotenusa}\")

3\) Al lado de cada una de las siguientes invocaciones, escribir si se
trata de una función que retorna un valor, o un procedimiento que no
tiene valor de retorno.

print()

map()

input()

btnp()

float()

4\) Subrayar todas las variables globales del siguiente código, y anotar
cuántas son en total:

def calcularSuperficieCirculo(r):

s = 2 \* 3.1415 \* r

> return s

def calcularVolumenCilindro(rad,h):

sup = calcularSuperficieCirculo(rad)

v = sup \* h

return v

respuesta1 = input(\"Ingresá el radio del cilindro: \")

radio = float(respuesta1)

respuesta2 = input(\"Ingresá la segunda nota: \")

altura = float(respuesta2)

volumen = calcularVolumenCilindro(nota1,nota2)

print(f\"El promedio de las tres notas es {promedio}\")

El programa tiene \_\_\_\_\_ variables globales.

5\) Se intentó invocar spr en TIC-80, pero por un error de escritura se
produjo un resultado inesperado. Indicar qué se verá en el juego al
ejecutar spr:

perroX = 21

perroY = 107

perroId = 92

def TIC():

spr(perroY, perroId, perroX)

Se verá el gráfico número: \_\_\_\_\_\_\_

En la posición horizontal: \_\_\_\_\_\_\_

Y la posición vertical: \_\_\_\_\_\_\_

6\) Dada la siguiente función, identificar el tipo de dato de cada uno
de sus parámetros o argumentos, y también el de su valor de retorno.
Luego, escribir una línea de código de ejemplo de cómo se invocaría la
función con datos inventados (no con variables, sino con datos como -1,
3.14, True o \"Hola\").

def funcion(a,b):

print(\"A continuación, entregamos el diploma a {a}\")

if b == True:

> t = f\"Técnica {a}\"

else:

> t = f\"Técnico {a}\"

return t

[Tipo de variable]{.underline} (a):

[Tipo de variable]{.underline} (b):

[Tipo de valor de retorno]{.underline} (t):

[Ejemplo de invocación:]{.underline}
funcion(\_\_\_\_\_\_\_\_\_\_\_,\_\_\_\_\_\_\_\_\_\_\_)
