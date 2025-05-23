### Alcance Local
Las variables (o funciones) declaradas dentro de las funciones tienen un alcance local (también llamado alcance de función). Solo son visibles por otro código dentro del mismo bloque de código.

p.ej.
```
def mi_funcion():
    mi_var_local = 2
    
# Esto causará un NameError
print(mi_var_local) 
```

### Alcance Global
Las variables o funciones declaradas en el nivel superior (sin indentar) de un archivo de código tienen un alcance global. Es accesible en cualquier lugar del archivo de código.

p.ej.

```
mi_var_global = 3

def mi_funcion():
    # Esto funciona sin problemas
    print(mi_var_global)
```