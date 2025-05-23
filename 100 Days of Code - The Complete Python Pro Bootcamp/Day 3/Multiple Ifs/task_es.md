Puedes escribir tantas declaraciones if como necesites para verificar diferentes condiciones que no estén relacionadas entre sí.
Compara los bloques de código a continuación:
```
# If/elif/else
if <la condición 1 es verdadera>
    <haz A>
elif <la condición 2 es verdadera>
    <haz B>
else
    <haz C>
```
```
# Declaraciones if anidadas
if <la condición 1 es verdadera>
    <haz A>
    if <la condición 2 es verdadera>
        <haz B>
        if <la condición 3 es verdadera>
            <haz C>
```

```
# Múltiples declaraciones if
if <la condición 1 es verdadera>
    <haz A>
if <la condición 2 es verdadera>
    <haz B>
if <la condición 3 es verdadera>
    <haz C>
```

En el bloque if/elif/else, solo puede suceder uno de A, B o C, porque if/elif/else son mutuamente excluyentes. La primera condición debe fallar para entrar en el elif y el elif (o múltiples elif) debe fallar para entrar en el else. La condición 2 solo se verifica si la condición 1 es falsa.

En las declaraciones if anidadas, pueden suceder A, B y C, pero las condiciones 1, 2 y 3 deben ser todas verdaderas. La computadora solo verificará la condición 2 si la condición 1 es verdadera.

En las múltiples declaraciones if, pueden suceder A, B y C. Pero son completamente independientes entre sí. C puede suceder incluso si A y B no suceden. Se verifica cada condición, independientemente del resultado de las demás.