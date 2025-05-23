Las funciones terminan en la palabra clave `return`. Si escribes código debajo de la declaración return, ese código no se ejecutará.

Sin embargo, puedes tener múltiples declaraciones de return en una función. ¿Entonces cómo funciona eso?

### Retornos condicionales

Cuando tenemos control de flujo, como que el código se comportará de manera diferente (seguirá diferentes rutas de ejecución) dependiendo de ciertas verificaciones condicionales, podemos terminar con múltiples finales (returns).

por ejemplo:
```
def puedeComprarAlcohol(edad):
    if edad >= 18:
        return True
    else:
        return False
```

### Retornos vacíos
También puedes escribir return sin nada después, y esto simplemente le dice a la función que salga.

por ejemplo:
```
def puedeComprarAlcohol(edad):
    # Si el tipo de datos de la entrada de edad no es un entero, entonces salga.
    if type(edad) != int:
        return

    if edad >= 18:
        return True
    else:
        return False
```