Anteriormente, hemos visto que las funciones nos permiten empaquetar código en un bloque con nombre que se puede utilizar repetidamente en un punto posterior.

### PAUSA 1 - Revisión
- Crea una función llamada `greet()`.
- Escribe 3 declaraciones `print` dentro de la función.
- Llama a la función `greet()` y ejecuta tu código.

### Entradas
Al agregar un nombre de variable dentro de los paréntesis cuando creamos (definimos) una nueva función, permite que esa función acepte entradas cuando se llama. 

Eso significa que podemos modificar cómo se comporta la función cada vez pasando diferentes entradas.

```
# Creando la función
def myFunction(input):
    print(f"¡Hola! {input}")
```
```
# Usando la función
myFunction("Tommy") 
# Dará como resultado "¡Hola! Tommy"
```

### Las Entradas son Variables
Cuando creas una función con entradas, estás definiendo un nombre de variable que se le dará a los datos que se pasen.

El nombre de la variable de entrada, por ejemplo, `name` en este código aquí: `def greet(name):` se llama parámetro.

El valor de la variable de entrada, por ejemplo, `Angela` cuando llamas a la función `greet` anterior: `greet("Angela")` se llama argumento.