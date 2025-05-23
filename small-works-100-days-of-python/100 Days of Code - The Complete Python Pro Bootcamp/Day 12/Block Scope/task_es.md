Python es un poco diferente de otros lenguajes de programación en que no tiene alcance de bloque.

Esto significa que las variables creadas anidadas en otros bloques de código, por ejemplo, bucles for, declaraciones if, bucles while, etc., no obtienen un ámbito local. Se les otorga un alcance de función si están dentro de una función o un alcance global si no lo están.

p.ej.

```
# Accesible en cualquier lugar
my_global_var = 1

def my_function():
    # Solo accesible dentro de my_function()
    my_local_var = 2
    
for _ in range(10):
    # Accesible en cualquier lugar
    my_block_var = 3

```