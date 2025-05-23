Los bucles nos permiten indicarle a la computadora que repita acciones sin tener que escribir código repetitivo. Si quisiéramos que la computadora imprima del 1 al 100, sería muy tedioso escribir una declaración `print` para cada número, o incluso escribir todos los números del 1 al 100. Los bucles nos permiten crear una regla que la computadora puede seguir para realizar una acción repetitiva.

### Sintaxis

```
for <nombre de la variable de cada elemento> in <una lista>:
    <hacer algo>
    <hacer otra cosa> 
```

### PAUSA 1 - Sé una computadora
Predice qué se imprimirá desde el siguiente código:

```
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
```

### Indentación
La indentación es muy importante en la programación de Python. Cada vez que veas el símbolo `:`, debes prestar atención a la indentación que viene después.

Por ejemplo, este código se comportará de manera muy diferente:

```
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print("Hello")
```

de este otro código:

```
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
print("Hello")