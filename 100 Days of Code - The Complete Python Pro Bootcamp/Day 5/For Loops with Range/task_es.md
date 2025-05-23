La combinación de la función `range()` con el Bucle For de Python nos permite ejecutar un bucle tantas veces como queramos. En lugar de recorrer cada elemento de una Lista, podemos recorrer un rango de números.

### Función Range

`range(1, 10)`

Este código por sí solo no hace nada. Por ejemplo, si intentases imprimirlo, no te daría números individuales.

Pero se puede usar en conjunto con Bucles For. e.g.

```
for numero in range(1, 10):
    print(numero)
```

Esto imprimirá cada uno de los números del 1 al 9. Por lo tanto, el rango también se puede expresar así:

`a <= range(a, b) < b`

Donde el rango de números incluye el límite inferior pero no incluye el límite superior.

### PAUSA 1 - El desafío de Gauss
Calcula la suma de los números entre 1 y 100, inclusive el 1 y el 100.
