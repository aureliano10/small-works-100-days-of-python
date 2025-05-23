### POR HACER-1: 
Crea una función llamada `decrypt()` que toma `original_text` y `shift_amount` como 2 entradas.

### POR HACER-2: 
Dentro de la función `decrypt()`, desplaza cada letra del `original_text` hacia delante en el abecedario *hacia atrás* por el `shift_amount` e imprime el texto descifrado.

<div class="hint">
  Puedes multiplicar cualquier número por -1 para convertirlo en un número negativo.
</div>


### POR HACER-3: 
- Combina las funciones `encrypt()` y `decrypt()` en una sola función llamada `caesar()`. 
- Usa el valor de la variable seleccionada por el usuario `direction` para determinar qué funcionalidad utilizar. 
- llama a la función caesar en lugar de encrypt/decrypt y pasa las tres variables `direction`/`text`/`shift`.

<div class="hint">
  Recuerda que cuando multiplicas un número por -1 se invierte su signo.
p.ej. <code>3 + ( 5 * -1) </code> es lo mismo que <code>3 - 5</code>.
</div>


<div class="hint">
Debería decir:  

<code>Aquí está el resultado codificado: XXX</code>

o

<code>Aquí está el resultado decodificado: XXX</code> 

</div>