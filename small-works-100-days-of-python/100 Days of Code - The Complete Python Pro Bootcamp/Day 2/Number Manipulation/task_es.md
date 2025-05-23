### Redondeando hacia abajo un número
Puedes redondear hacia abajo un número o eliminar todos los decimales utilizando la función `int()`, que convierte un número de punto flotante (con decimales) en un número entero.

`int(3.738492) # Se convierte en 3` 

### Redondeando un número
Sin embargo, si quieres redondear un número decimal al entero más cercano, utilizando el método matemático tradicional, donde cualquier número mayor a .5 se redondea hacia arriba y cualquier número menor se redondea hacia abajo, puedes utilizar la función `round()` de Python.

`round(3.738492) # Se convierte en 4`

`round(3.14159) # Se convierte en 3`

`round(3.14159, 2) # Se convierte en 3.14`

### Operadores de asignación
Los operadores de asignación, como el operador de asignación de suma `+=`, sumarán el número a la derecha al valor original de la variable a la izquierda y asignarán el nuevo valor a la variable.

`+=`

`-=`

`*=`

`/=`

### f-Strings
En Python, podemos usar f-strings para insertar una variable o una expresión dentro de una cadena de texto.

`age = 12`

`print(f"Soy {age} años viejo")`

`# Mostrará: Soy 12 años viejo.`