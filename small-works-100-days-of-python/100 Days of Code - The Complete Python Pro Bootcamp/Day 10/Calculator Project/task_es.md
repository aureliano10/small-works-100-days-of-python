El objetivo es construir un programa de calculadora.

### Demo
https://appbrewery.github.io/python-day10-demo/


### Guardar funciones como un valor en una variable
Puedes guardar una referencia a una función como un valor para una variable.
p.ej.
```
def add(n1, n2):
    return n1 + n2
    
    
mi_cálculo_favorito = add
mi_cálculo_favorito(3, 5)  # Devolverá 8
```
En el archivo de inicio, verás un diccionario que referencia cada una de las operaciones matemáticas que nuestra calculadora puede realizar. Pruébalo y mira si puedes hacer que realice suma, resta, multiplicación y división.

### PAUSA 1 
TAREA: Escribe las otras 3 funciones - restar, multiplicar y dividir.

### PAUSA 2
TAREA: Agrega estas 4 funciones a un diccionario como valores. Claves = "`+`", "`-`", "`*`", "`/`"

### PAUSA 3
TAREA: Utiliza las operaciones del diccionario para efectuar los cálculos. Multiplica 4 * 8 utilizando el diccionario.


### Funcionalidad del programa
- El programa pide al usuario que escriba el primer número.
- El programa pide al usuario que escriba un operador matemático (una opción entre "`+`", "`-`", "`*`" o "`/`")
- El programa pide al usuario que escriba el segundo número.
- El programa calcula el resultado con base en el operador matemático seleccionado.
- El programa pregunta si el usuario desea continuar trabajando con el resultado anterior.
- Si la respuesta es sí, el programa vuelve a utilizar el resultado anterior como el primer número y luego repite el proceso de cálculo.
- Si la respuesta es no, el programa solicita al usuario que escriba el primer número de nuevo y borra toda memoria de los cálculos anteriores.
- Agregar el logo de art.py

<div class="hint">
  Intenta dibujar un diagrama de flujo para planificar tu programa.
</div>

<div class="hint">
    Para llamar a la multiplicación desde el diccionario de operaciones, escribirías tu código de esta forma:

<code>resultado = operations["*"](n1= 5, n2= 3)</code>

El resultado sería entonces igual a 15.
</div>
