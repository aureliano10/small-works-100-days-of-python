Puedes forzar al código a permitirte modificar algo con global si usas la palabra clave global antes de usarla.

Por ejemplo, esto te dará un error

```
a = 1
def my_function():
    a += 1
    print(a)
```

Pero esto funcionará
```
a = 1
def my_function():
    global a
    a += 1
    print(a)
```