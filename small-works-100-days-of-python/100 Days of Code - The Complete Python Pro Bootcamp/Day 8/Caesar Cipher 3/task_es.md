### TODO-1: 
Importa e imprime el logo desde art.py cuando el programa comienza.

### TODO-2: 
¿Qué sucede si el usuario ingresa un número/símbolo/espacio que no está en la Lista `alphabet`?

¿Puedes corregir el código para mantener el número/símbolo/espacio cuando el texto se codifica/decodifica?

p.ej. 
```
texto_original = "encuéntrame a las 3!"
texto_cifrado = "XXXX XXXXXX X XXX 3!"
```

<div class="hint">
  Si no es una letra en la Lista alphabet, ¿quizás puedes simplemente agregarlo al final de texto_cifrado como el carácter sin modificar?
</div>


### TODO-3: 

¿Puedes encontrar una manera de reiniciar el programa de cifrado?

p.ej. 

`Escribe 'sí' si quieres intentarlo de nuevo. De lo contrario, escribe 'no'.`

Si escriben 'sí', entonces pregúntales nuevamente la dirección/texto/desplazamiento y llama a la función `caesar()` otra vez.

<div class="hint">
  Intenta crear un bucle while que continúe ejecutando el programa si el usuario escribe 'sí'.
</div>