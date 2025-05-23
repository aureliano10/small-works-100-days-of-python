### Generadores de números pseudoaleatorios
Las computadoras no son aleatorias, porque están construidas con circuitos y conmutadores. Sin embargo, el azar es muy importante al desarrollar software, especialmente videojuegos. Sería muy aburrido si cada movimiento en un videojuego estuviera predefinido.

Por esta razón, algunos científicos de la computación inventaron los generadores de números pseudoaleatorios. ej. https://es.wikipedia.org/wiki/Mersenne_Twister

Si deseas aprender más sobre los generadores de números pseudoaleatorios, te recomiendo ver este video de Khan Academy: https://www.youtube.com/watch?v=GtOt7EBNEwQ&ab_channel=KhanAcademyLabs

### El módulo random en Python
Lee la documentación aquí:
https://docs.python.org/3/library/random.html

Para usarlo, primero necesitas importarlo:

`import random`

### Números enteros aleatorios dentro de un rango

```
import random
rand_num = random.randint(1, 10)

#Esto generará un número entero aleatorio entre 1 y 10 (incluidos).
```

### Módulos en Python
Python nos permite colocar código en diferentes archivos e importar ese código cuando sea necesario. Esto significa que podemos organizar y modularizar mejor nuestro código.

Puedes crear un nuevo módulo simplemente creando un nuevo archivo `.py`, y luego puedes importar variables o funciones de ese archivo usando la palabra clave `import`.

### Números decimales aleatorios
Puedes generar un número aleatorio entre 0.0 (inclusive) y 1.0 (no inclusive) usando el siguiente código del módulo random:

```
import random
rand_num_0_to_1 = random.random()
```
También se puede representar así:

`0.0 <= random.random() < 1.0`

Puedes ampliar el rango de los números aleatorios generados por este método utilizando multiplicación.

ej. `random.random() * 5`

Generará un número aleatorio entre 0 y 5.

Otra forma de generar números decimales aleatorios es usar la función `uniform()`.

```
import random
random_float = random.uniform(1, 10)
#Esto generará un número decimal aleatorio entre 1 y 10. 
```
Este método puede incluir o no el límite superior dependiendo de cómo se redondea el número decimal. 
Por lo tanto, la mejor representación sería:

`a <= random.uniform(a,b) <= b`

Dependiendo de si quieres incluir el límite superior, puedes elegir entre usar `random.random()` o `random.uniform()`.

### PAUSA 1 - Cara o Cruz
Crea un programa para lanzar una moneda usando lo que has aprendido sobre randomización en Python. El programa debe imprimir aleatoriamente "Cara" o "Cruz" cada vez que se ejecute.

<div class="hint">
  Necesitarás pensar en lo que has aprendido sobre las declaraciones condicionales en Python.
</div>