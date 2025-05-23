### Múltiples Entradas
Puedes tener múltiples entradas en las funciones. Todo lo que necesitas hacer es separarlas con una coma `,`.

### PAUSA 1
Crea una función con múltiples entradas

<div class="hint">
  <code>
def greet(name, greeting):

    ____print(f"{greeting} {name}")
    
greet("Angela", "¡Hola!")
</code>
</div>

### PAUSA 2
Modifica la función para que imprima los valores esperados.
```
def greet_with(name, location)
    Hola name
    ¿Cómo es en location?
```

### Argumentos Posicionales
Por defecto, cuando creas una función en Python, mantendrá el orden de los argumentos en la definición de la función.

por ejemplo, En la función de abajo, el primer argumento que entra siempre se imprimirá antes que el segundo. `a = 2, b = 1`

```
def my_function(a, b)
  print(a)
  print(b)
  
 my_function(2, 1)
 #Se imprimirá:
 # 2
 # 1
```

### Argumentos de Palabras Clave
Puedes utilizar palabras clave cuando provees los argumentos al llamar a una función para que haya menos confusión acerca de qué valor se asigna a qué parámetro de entrada.

### PAUSA 3 
Llama a la función `greet_with()` utilizando argumentos de palabras clave.

<div class="hint">
  <code>
greet_with(location="Londres", name="Angela")
</code>
</div>