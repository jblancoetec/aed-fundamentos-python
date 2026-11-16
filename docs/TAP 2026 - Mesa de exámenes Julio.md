# Evaluación de Taller de Algoritmos y Programación

1\) Leer el siguiente código, y escribir al final lo que el usuario verá
en la consola, teniendo en cuenta los **print** usados:

def f(x):

x = x + 3

print(x)

x = 2

print(x)

x = 9

print(x)

f(x)

x = x \* 2

print(x)

2\) Subrayar todas las variables que existan en el siguiente código, y
finalmente completar cuántas variables locales y globales son:

def cobrarBoleto(precio):

nuevoSaldo = saldo -- precio

print(f\"Boleto cobrado: \${precio}\")

return nuevoSaldo

nombre = input(\"¡Buen día! Ingrese su nombre: \")

respuestaSaldo = input(f\"{nombre}, ingrese su saldo (con coma): \$\")

saldo = float(respuestaSaldo)

puedePagarBoleto = saldo \> 900

if puedePagarBoleto:

saldo = cobrarBoleto(900)

print(f\"{nombre}, su saldo restante es \${saldo}\")

else:

print(f\"{nombre}, \${saldo} no alcanza para el boleto\")

El programa tiene \_\_\_\_\_ variables globales, y \_\_\_\_\_ variables
locales.

3\) Dada la siguiente comparación:

vida \>= 10 and vida \< 33

Anotar el resultado de la comparación cuando la variable **vida**
vale\...

- 9

- 10

- 11

- 32

- 33

- 34

4\) Escribir qué mensaje verá el usuario al ejecutar el siguiente
código:

def dividir(numA, numB):

resultado = numA / numB

print(f\"{numA} / {numB} = {resultado}\")

numero1 = 10

numero2 = 2

dividir(numero2,numero1)

5\) El siguiente código contiene un error. Subrayar y explicar cuál es,
y finalmente explicar cómo se podría resolver. No hace falta escribir el
código corregido.

def dividirPorTres(num):

resultado = num / 3

return resultado

miNumero = 12

dividirPorTres(miNumero)

print(f\"{miNumero} dividido por tres da {resultado}\"

6\) Completar la línea en blanco del siguiente código para que funcione
correctamente.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

numeroAlAzar = randint(1,100)

ataqueImpacta = numeroAlAzar \<= 75

if ataqueImpacta:

print(\"¡El ataque impacta al enemigo!\")

else:

print(\"El ataque falló\...\")

7\) Se quiere escribir un código para ver si llueve, y no salir hasta
que pare. Completar la línea en blanco para que el código funcione
correctamente.

estaLloviendo = input(\"¿Está lloviendo? (si/no): \")

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

print(\"Mejor esperemos un rato más\...\")

estaLloviendo = input(\"Y ahora, ¿sigue lloviendo? (si/no): \")

print(\"Qué bien, ahora podemos salir a la calle.)

8\) Anotar el valor que resulta de ejecutar cada una de las siguientes
líneas de código:

- \"árbol\" != \"arbol\"

- \"murcielago\" in \"u\"

- \"CARRIL\" == \"Carril\"

- \" \" in \"¡buenos días!\"

- \"e\" in \"abrojo\"º

- \"ae\" in \"abecedario\"

9\) Leer el siguiente código, y escribir al final todo lo que el usuario
verá en la consola, teniendo en cuenta los **print** usados:

palabra = \"libro\"

if palabra\[2\] == \"i\":

print(\"Primera comparación: Es una I\")

else:

print(\"Primera comparación: No es una I\")

if palabra\[-2\] == \"r\":

print(\"Segunda comparación: Es una R\")

else:

print(\"Segunda comparación: No es una R\")

10\) Escribir todos los índices válidos que puedan usarse para acceder a
cada uno de los caracteres del string **\"ETEC 2026\"**.

11\) Escribir un código corto que, usando un for, recorra y muestre uno
por uno los caracteres que estén guardados en una variable llamada
**nombreCompleto**. No hace falta asignar la variable, sólo usarla, y el
programa deberá funcionar sin importar el largo del string almacenado.

12\) Escribir un código corto que, usando una repetición, muestre cien
veces una sola frase del estribillo de una canción.

13\) Imaginando que existe una variable **diaElegido**, donde el usuario
ingresará un día de la semana a elección, escribir una comparación que
resulte en True cuando esa variable corresponda a un día de semana
laboral en minúsculas y sin tildes.

14\) Se tiene la función **mget(x,y)**, que dada una coordenada X e Y
devuelve el identificador numérico del tile que está en esa posición del
mapa. Las coordenadas del avatar están guardadas en las variables
**ninjaX** y **ninjaY**. Escribir un fragmento de código donde el
programa verifique si el ninja se encuentra encima del tile de meta,
cuyo ID de tile es el **48**, y en caso afirmativo muestre un **print**
avisando que el ninja logró alcanzar la meta.
