# Evaluación de Taller de Algoritmos y Programación

1\) Se tiene la siguiente documentación de una función:

> random.randint(a,b) -\> int
>
> Retorna un número al azar entre A y B (inclusive).

Completar el espacio en el siguiente código para que funcione
correctamente.

import random

respuesta1 = input(\"Elegi el número mínimo: \")

num1 = int(respuesta1)

respuesta2 = input(\"Elegi el número máximo: \")

num2 = int(respuesta2)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

print(f\"El número generado al azar es: {numeroGenerado}\")

2\) Hay un error en el siguiente código. Subrayar la línea donde ocurra
el error. Luego, escribir abajo por qué es un error, y cómo se debería
reescribir esa línea para que el programa funcione correctamente.

import math

def calcularHipotenusa(a,b):

h = sqrt(a\*\*2 + b\*\*2)

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

cls()

mget()

float()

print()

input()

4\) Subrayar todas las variables globales del siguiente código, y anotar
cuántas son en total:

def calcularPromedio(numA, numB, numC):

tot = numA + numB + numC:

> return tot / 2

respuesta1 = input(\"Ingresá la primer nota: \")

nota1 = float(respuesta1)

respuesta2 = input(\"Ingresá la segunda nota: \")

nota2 = float(respuesta2)

respuesta3 = input(\"Ingresá la tercer nota: \")

nota3 = float(respuesta3)

promedio = calcularPromedio(nota1,nota2,nota3)

print(f\"El promedio de las tres notas es {promedio}\")

El programa tiene \_\_\_\_\_ variables globales.

5\) Se intentó invocar spr en TIC-80, pero por un error de escritura se
produjo un resultado inesperado. Indicar qué se verá en el juego al
ejecutar spr:

perroX = 84

perroY = 7

perroId = 43

def TIC():

spr(perroY, perroX, perroId)

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

> t = f\"Técnico {a}\"

else:

> t = f\"Técnica {a}\"

return t

[Tipo de variable]{.underline} (a):

[Tipo de variable]{.underline} (b):

[Tipo de valor de retorno]{.underline} (t):

[Ejemplo de invocación:]{.underline}
funcion(\_\_\_\_\_\_\_\_\_\_\_,\_\_\_\_\_\_\_\_\_\_\_)
