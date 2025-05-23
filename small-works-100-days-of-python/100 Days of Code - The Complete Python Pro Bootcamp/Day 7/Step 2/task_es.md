### POR HACER-1
- Crea una cadena vacía llamada `placeholder`.
- Para cada letra en la palabra_elegida, añade un `_` a `placeholder`.
- Por lo tanto, si la `palabra_elegida` era "manzana", `placeholder` debería ser `_ _ _ _ _ _ _` con 7 `"_"` representando cada letra para adivinar.
- Imprime `hint`.

<div class="hint">
  Recuerda que puedes usar la función range() dentro de un bucle para llevar a cabo una acción un número particular de veces. 
</div>


### POR HACER-2
- Crea una cadena vacía llamada "display".
- Haz un bucle a través de cada letra en la `palabra_elegida`
- Si la letra en esa posición coincide con `guess`, entonces revela esa letra en el `display` en esa posición.
- p. ej. Si el usuario adivina "a" y la palabra elegida era "manzana", entonces `display` debería ser `_ a _ _ a _ a`.
- Imprime `display` y deberías ver la letra adivinada en la posición correcta.
- Pero cada letra que no coincide está representada con un "_".

<div class="hint">
  Recuerda que el bucle for recorrerá cada letra en la palabra_elegida en orden. Puedes usar ese hecho para crear una nueva cadena, añadiendo la letra o un "_".
</div>