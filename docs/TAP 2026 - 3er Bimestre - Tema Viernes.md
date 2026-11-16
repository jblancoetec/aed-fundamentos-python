# Evaluación de Taller de Algoritmos y Programación

1\) Se tiene la siguiente documentación de una función:

> random.randint(a,b) -\> int
>
> Retorna un número al azar entre A y B (inclusive).

Completar el espacio en el siguiente código para que funcione
correctamente.

import random

respuestaMax = input(\"Elegi el número máximo: \")

numMax = int(respuestaMax)

respuestaMin = input(\"Elegi el número mínimo: \")

numMin = int(respuestaMin)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

print(f\"El número generado al azar es: {numeroGenerado}\")

2\) Hay un error en el siguiente código. Subrayar la línea donde ocurra
el error. Luego, escribir abajo por qué es un error, y cómo se debería
reescribir esa línea para que el programa funcione correctamente.

from math import pi

def calcularPerimetro(r):

per = 2 \* r \* math.pi

return per

respuesta = input(\"Ingresá el radio de la circunferencia: \")

radio = float(respuesta)

perimetro = calcularPerimetro(radio)

print(f\"El perímetro de la circunferencia mide {perimetro}\")

3\) Al lado de cada una de las siguientes invocaciones, escribir si se
trata de una función que retorna un valor, o un procedimiento que no
tiene valor de retorno.

float()

print()

mget()

input()

map()

4\) Subrayar todas las variables globales del siguiente código, y anotar
cuántas son en total:

def calcularVolumenCubo(b,h,p):

s = b \* h \* p

> return s

respuesta1 = input(\"Ingresá la primer nota: \")

base = float(respuesta1)

respuesta2 = input(\"Ingresá la segunda nota: \")

altura = float(respuesta2)

respuesta3 = input(\"Ingresá la tercer nota: \")

profundidad = float(respuesta3)

volumen = calcularVolumenCubo(base,altura,profundidad)

print(f\"El volumen del cubo es {volumen}\")

El programa tiene \_\_\_\_\_ variables globales.

5\) Se intentó invocar spr en TIC-80, pero por un error de escritura se
produjo un resultado inesperado. Indicar qué se verá en el juego al
ejecutar spr:

perroX = 44

perroY = 11

perroId = 66

def TIC():

spr(perroXY perroId, perroY)

Se verá el gráfico número: \_\_\_\_\_\_\_

En la posición horizontal: \_\_\_\_\_\_\_

Y la posición vertical: \_\_\_\_\_\_\_

6\) Dada la siguiente función, identificar el tipo de dato de cada uno
de sus parámetros o argumentos, y también el de su valor de retorno.
Luego, escribir una línea de código de ejemplo de cómo se invocaría la
función con datos inventados (no con variables, sino con datos como -1,
3.14, True o \"Hola\").

def funcion(a,b):

print(f\"Sr/a {a}, le damos la bienvenida al sistema de depósito\")

print(f\"Su saldo actual es de \${b}\")

r = input(\"Ingrese la cantidad de dinero a depositar: \$\")

d = float(r)

s = d + b

return s

[Tipo de variable]{.underline} (a):

[Tipo de variable]{.underline} (b):

[Tipo de valor de retorno]{.underline} (t):

[Ejemplo de invocación:]{.underline}
funcion(\_\_\_\_\_\_\_\_\_\_\_,\_\_\_\_\_\_\_\_\_\_\_)
