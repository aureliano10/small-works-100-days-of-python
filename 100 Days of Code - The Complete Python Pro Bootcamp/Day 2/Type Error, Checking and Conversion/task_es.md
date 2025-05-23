### TypeError
Estos errores ocurren cuando estás utilizando el tipo de datos incorrecto.
p.ej. `len(12345)`

Debido a que solo puedes darle Strings a la función `len()`, se negará a funcionar y te dará un TypeError si le das un número (Integer).

#### PAUSA 1. Corrige la función `len()` para que no tenga más advertencias o errores.

### Comprobación de Tipos
Puedes comprobar el tipo de datos de cualquier valor o variable en python usando la función `type()`.

`print(type("abc")) #te dará <class 'str'>`

#### PAUSA 2. Escribe 4 chequeos de tipo para imprimir los 4 tipos de datos
Utilizando las funciones `type()` y `print()` para imprimir 4 líneas en el área de salida para obtener la colección completa de tipos de datos que aprendimos. `<class 'str'> <class 'int'> <class 'float'> y <class 'bool'>`

### Conversión de Tipos
Puedes convertir datos a diferentes tipos de datos utilizando funciones especiales.
p.ej.

`float()` 

`int()`

`str()`

#### PAUSA 3. Haz que esta línea de código se ejecute sin errores
`print("Número de letras en tu nombre: " + len(input("Ingresa tu nombre")))`