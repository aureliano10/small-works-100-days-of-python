Una función en su forma más simple es solo un nombre envoltorio para un bloque de código. Le das un nombre y luego, cuando llamas a la función por ese nombre, todo el código dentro del bloque de la función se ejecutará. Puede ayudarnos a ahorrar tiempo y reducir el código repetido.

### Definir una nueva función
```
def <nombre_de_la_función>():
    print("Hola")
    # Hacer algo más
    # Hacer algo más ...
```

### Llamar a una función
Llamar a una función simplemente significa activar la función. Podemos llamar a una función en cualquier punto de nuestro código en Python.

```
<nombre_de_la_función>()
```

Poniendo todo junto, por ejemplo:
```
#Creando la función
def obtener_nombre_usuario():
    nombre = input("¿Cuál es tu nombre? ")
    print("Hola, " + nombre)
    # Dentro de la función

#Fuera de la función
print("Hola")
obtener_nombre_usuario() # Llamando a la función
```

Este código producirá la siguiente secuencia de salida:
```
Hola
¿Cuál es tu nombre? #Escribo Angela
Hola
Angela