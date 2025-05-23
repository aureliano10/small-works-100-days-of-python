### Elige tu dificultad
- **Normal** 😎: Usa todas las pistas a continuación para completar el proyecto.
- **Difícil** 🤔: Usa solo las Pistas 1, 2, 3 para completar el proyecto.
- **Extra Difícil** 😭: Usa solo las Pistas 1 y 2 para completar el proyecto.
- **Experto** 🤯: Usa solo la Pista 1 para completar el proyecto.

### Nuestras reglas de la casa para el juego de Blackjack

- La baraja es ilimitada en tamaño.
- No hay comodines.
- El Sota/Reina/Rey cuentan todos como 10.
- El As puede contar como 11 o 1.
- Utiliza la siguiente lista como la baraja de cartas:

`cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`
- Las cartas en la lista tienen la misma probabilidad de ser sacadas.
- Las cartas no se retiran de la baraja al ser sacadas.
- El ordenador es el crupier.


<div class="hint" title="Hint 1">
  Ve a este sitio web y prueba el juego de Blackjack: 

https://games.washingtonpost.com/games/blackjack/

Luego prueba el proyecto completado de Blackjack aquí: 

https://appbrewery.github.io/python-day11-demo/
</div>

<div class="hint" title="Hint 2">
Lee esta desglosación de los requisitos del programa: 

http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF

Luego intenta crear tu propio diagrama de flujo para el programa.

</div>

<div class="hint" title="Hint 3">
  Descarga y lee este diagrama de flujo que he creado:

https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

</div>


<div class="hint" title="Hint 4">
  Crea una función <code>deal_card()</code> que use la Lista de abajo para retornar una carta aleatoria.

<code>cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]</code>

Recuerda que el 11 es el As.
</div>

<div class="hint" title="Hint 5">
  Reparte al usuario y al ordenador 2 cartas cada uno usando <code>deal_card()</code> y <code>append()</code>.

<code>user_cards = []</code>

<code>computer_cards = []</code>
</div>

<div class="hint" title="Hint 6">
  Crea una función llamada <code>calculate_score()</code> que tome una Lista de cartas como entrada 
y retornar la suma de todas las cartas en la Lista como la puntuación.
Googlea la función <code>sum()</code> para que te ayude a hacer esto.
</div>


<div class="hint" title="Hint 7">
Dentro de <code>calculate_score()</code> comprueba si hay un blackjack (una mano con solo 2 cartas: as + 10) y retorna <code>0</code> en lugar de la puntuación real. <code>0</code> representará un blackjack en nuestro juego.
</div>


<div class="hint" title="Hint 8">
  Dentro de <code>calculate_score()</code> verifica si hay un 11 (as). Si la puntuación ya es mayor de 21, elimina el 11 y reemplázalo con un 1. Es posible que necesites Googlear para encontrar la documentación sobre las funciones integradas de Python <code>append()</code> y <code>remove()</code>.

https://developers.google.com/edu/python/lists#list-methods
</div>

<div class="hint" title="Hint 9">
  Llama a la función <code>calculate_score()</code>. Si el ordenador o el usuario tiene un blackjack (0) o si la puntuación del usuario es mayor de 21, entonces el juego termina.
</div>

<div class="hint" title="Hint 10">
  Si el juego no ha terminado, pregúntale al usuario si quiere sacar otra carta. Si la respuesta es afirmativa, entonces usa la función <code>deal_card()</code> para agregar otra carta a la Lista <code>user_cards</code>. Si no, entonces el juego ha terminado.
</div>

<div class="hint" title="Hint 11">
  La puntuación necesitará ser comprobada con cada nueva carta sacada y las comprobaciones en la Pista 9 necesitarán ser repetidas hasta que el juego termine.
</div>

<div class="hint" title="Hint 12">
  Una vez que el usuario haya terminado, es el momento de dejar que el ordenador juegue. El ordenador debería seguir sacando cartas mientras tenga una puntuación inferior a 17.
</div>

<div class="hint" title="Hint 13">
  Crea una función llamada <code>compare()</code> y pasa el <code>user_score</code> y el <code>computer_score</code>. 

- Si el ordenador y el usuario tienen la misma puntuación, entonces es un empate.
- Si el ordenador tiene un blackjack (0), entonces el usuario pierde. 
- Si el usuario tiene un blackjack (0), entonces el usuario gana. 
- Si el <code>user_score</code> es mayor de 21, entonces el usuario pierde. 
- Si el <code>computer_score</code> es mayor de 21, entonces el ordenador pierde. 
- Si ninguna de las anteriores, entonces el jugador con la puntuación más alta gana.
</div>

<div class="hint" title="Hint 14">
  Pregunta al usuario si quiere reiniciar el juego. Si responden que sí, limpia la consola y comienza un nuevo juego de blackjack y muestra el logo de art.py.
</div>
