El programa preguntará:
```
¿Cuántas letras te gustaría en tu contraseña?
¿Cuántos símbolos te gustaría?
¿Cuántos números te gustaría?
```
El objetivo es tomar las entradas del usuario a estas preguntas y luego generar una contraseña aleatoria. Usa tu conocimiento sobre las listas y los bucles de Python para completar el desafío.

### Demostración
https://appbrewery.github.io/python-day5-demo/

### Versión fácil
Genera la contraseña en secuencia. Letras, luego símbolos, luego números. Si el usuario quiere

4 letras
2 símbolos y
3 números
entonces la contraseña podría verse así:

`fgdx$*924`

Puedes ver que todas las letras están juntas. Todos los símbolos están juntos y todos los números siguen el mismo orden. Intenta resolver este problema primero.

<div class="hint">
  Recuerda que puedes usar la función random.choice() para obtener un elemento aleatorio de una lista. Pero debes importar el módulo random primero.
</div>

### Versión difícil
Cuando hayas completado la versión fácil, estarás listo para afrontar la versión difícil. En la versión avanzada de este proyecto, la contraseña final no sigue un patrón. Entonces el ejemplo anterior podría verse así:

`x$d24g*f9`

Y cada vez que generes una contraseña, las posiciones de los símbolos, los números y las letras son diferentes. Esto hará que la contraseña sea más difícil de descifrar para los hackers.

La habilidad esencial de un buen programador es usar Google para encontrar lo que necesitas. ¡Tu cerebro es para pensar, no para memorizar funciones! Necesitarás usar Google para resolver este proyecto en el nivel difícil. Si te quedas atascado, consulta la pista de abajo para qué buscar en Google.

<div class="hint">
  Intenta buscar en Google: "Cómo mezclar elementos en una lista en Python"
</div>