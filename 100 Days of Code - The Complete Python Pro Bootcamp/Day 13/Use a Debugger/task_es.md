La mayoría de los IDE (Entornos de Desarrollo Inteligentes) como PyCharm tendrán herramientas integradas para la depuración. Esto se conoce normalmente como el depurador. En muchos aspectos, son como las instrucciones de impresión con esteroides.

Los depuradores nos permiten echar un vistazo a nuestro código durante la ejecución y hacer una pausa en las líneas seleccionadas para averiguar cuál es el mecanismo interno y dónde está fallando.

Hay un par de cosas que son las mismas en la mayoría de los IDEs con las que deberías estar familiarizado:

1. **Punto de Interrupción** - Puedes establecer un punto de interrupción haciendo clic en una línea en el margen del código (donde están los números de línea). Esta línea será donde el programa hace una pausa durante el ejecución de la depuración.

2. **Paso por Encima** - Este botón pasará a través de la ejecución de tu código línea por línea y te permitirá ver los valores intermedios de tus variables.
3. **Entrar en** - Esto entrará en cualquier otro módulo que tu código haga referencia. p. ej. si usas una función del módulo random, te mostrará el código original de esa función para que puedas entender mejor su funcionalidad y cómo se relaciona con tus problemas.
4. **Entrar en Mi Código** - Esto hace lo mismo que Entrar en, pero limita el alcance a tu propio código de proyecto e ignora el código de la biblioteca como random.

### PAUSA 1
Utiliza el depurador de PyCharm para averiguar cuál es el problema en el código inicial y corrígelo.