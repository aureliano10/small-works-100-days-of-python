Puede usar docstrings para escribir comentarios de varias líneas que documentan su código.

### Sintaxis
Simplemente encierre su texto dentro de un par de tres comillas dobles.

p.ej.
```
"""
Mi
Comentario
Multilínea
"""

```

### Documentación de funciones
Una característica útil de los docstrings es que puede usarlo justo debajo de la definición de una función y ese texto se mostrará cuando pase el cursor sobre una llamada a la función. Es una buena manera de recordarte lo que realiza una función que has creado tú mismo.

p.ej.
```
def mi_función(num):
    """Multiplica un número por sí mismo."""
    return num * num
```