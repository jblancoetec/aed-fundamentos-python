# Evaluación de Taller de Algoritmos y Programación

1\) Se tiene la siguiente documentación de una función:

> random.randint(a,b) -\> int
>
> Retorna un número al azar entre A y B (inclusive).

Completar el espacio en el siguiente código para que funcione
correctamente.

from random import randint

respuestaMax = input(\"Elegi el número máximo: \")

numMax = int(respuestaMax)

respuestaMin = input(\"Elegi el número mínimo: \")

numMin = int(respuestaMin)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

print(f\"El número generado al azar es: {numeroGenerado}\")

2\) Hay un error en el siguiente código. Subrayar la línea donde ocurra
el error. Luego, escribir abajo por qué es un error, y cómo se debería
reescribir esa línea para que el programa funcione correctamente.

import math

def calcularPerimetro(r):

per = 2 \* r \* pi

return per

respuesta = input(\"Ingresá el radio de la circunferencia: \")

radio = float(respuesta)

perimetro = calcularPerimetro(radio)

print(f\"El perímetro de la circunferencia mide {perimetro}\")

3\) Al lado de cada una de las siguientes invocaciones, escribir si se
trata de una función que retorna un valor, o un procedimiento que no
tiene valor de retorno.

int()

input()

print()

spr()

btn()

4\) Subrayar todas las variables globales del siguiente código, y anotar
cuántas son en total:

def calcularMayor(numA, numB):

if numA \> numB:

> return numA
>
> else:
>
> return numB

respuesta1 = input(\"Elegi el número mínimo: \")

num1 = int(respuesta1)

respuesta2 = input(\"Elegi el número máximo: \")

num2 = int(respuesta2)

mayor = calcularMayor(num1,num2)

print(f\"Entre {num1} y {num2}, el número mayor es {mayor}\")

El programa tiene \_\_\_\_\_ variables globales.

5\) Se intentó invocar spr en TIC-80, pero por un error de escritura se
produjo un resultado inesperado. Indicar qué se verá en el juego al
ejecutar spr:

perroX = 10

perroY = 50

perroId = 64

def TIC():

spr(perroX, perroY, perroId)

Se verá el gráfico número: \_\_\_\_\_\_\_

En la posición horizontal: \_\_\_\_\_\_\_

Y la posición vertical: \_\_\_\_\_\_\_

6\) Dada la siguiente función, identificar el tipo de dato de cada uno
de sus parámetros o argumentos, y también el de su valor de retorno.
Luego, escribir una línea de código de ejemplo de cómo se invocaría la
función con datos inventados (no con variables, sino con datos como -1,
3.14, True o \"Hola\").

def funcion(a,b):

print(f\"Sr/a {a}, le damos la bienvenida al sistema de pago
automático\")

print(f\"Su total a pagar es de \${b}\")

r = input(\"Ingrese la cantidad de dinero a depositar: \$\")

d = float(r)

s = d -- b

return s

[Tipo de variable]{.underline} (a):

[Tipo de variable]{.underline} (b):

[Tipo de valor de retorno]{.underline} (s):

[Ejemplo de invocación:]{.underline}
funcion(\_\_\_\_\_\_\_\_\_\_\_,\_\_\_\_\_\_\_\_\_\_\_)
