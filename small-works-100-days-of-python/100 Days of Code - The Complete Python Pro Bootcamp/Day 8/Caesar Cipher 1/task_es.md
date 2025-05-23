Vas a construir un programa de cifrado y descifrado utilizando el [cifrado de César](https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar).

### Demostración
https://appbrewery.github.io/python-day8-demo/

### POR HACER-1: 
Crea una función llamada `encrypt()` que toma `original_text` y `shift_amount` como 2 entradas.

### POR HACER-2: 
Dentro de la función 'encrypt', desplaza cada letra del `original_text` hacia adelante en el alfabeto por el `shift_amount` e imprime el texto cifrado.

Puedes usar la función incorporada de Python `index()` para averiguar la posición de un elemento en una lista. Ejemplo:
```
fruits = ["Apple", "Pear", "Orange"]
fruits.index("Pear") #1
```

Por ejemplo, si tenemos los siguientes valores:
```
plain_text = "hello"
shift_amount = 1
```
La salida cifrada final debería ser:

`Aquí está el resultado codificado: ifmmp`

Donde cada una de las letras de 'hello' ha sido desplazada una posición arriba.

<div class="hint">
Desglosemos el problema:

  1. Necesitas un bucle for para recorrer cada una de las letras en el plain_text.
  2. Encuentra la posición de cada letra en la lista del alfabeto.
3. Agrega el shift_amount deseado por el usuario a la posición para obtener la posición de la letra codificada.
4. Encuentra la letra correspondiente para esa posición.
5. Añade cada letra codificada a una nueva cadena e imprímela después de que termine el bucle.

</div>


### POR HACER-3: 
Llama a la función `encrypt()` y pasa las entradas del usuario. Deberías poder probar el código y cifrar un mensaje.


### POR HACER-4: 
¿Qué sucede si tratas de desplazar la letra 'z' hacia adelante por 9? ¿Puedes corregir el código?

<div class="hint">
  Hay muchas maneras de hacer esto.
1. Puedes agregar más de 1 conjunto del alfabeto a la lista de letras del alfabeto.
2. Puedes desplazar el shift_amount para que siempre esté dentro de 0 - 25 y encaje en la lista.
3. Puedes usar el módulo para obtener el resto.
</div>