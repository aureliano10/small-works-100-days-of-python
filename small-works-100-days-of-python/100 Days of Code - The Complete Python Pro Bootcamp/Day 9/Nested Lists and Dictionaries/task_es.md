Puedes mezclar y combinar varios tipos de datos para lograr la estructura deseada.

### Anidando una Lista dentro de un Diccionario
En lugar de un valor String asignado a una clave, podemos reemplazarlo con una Lista. Puedes anidar una Lista en un Diccionario de esta manera:

```
my_dictionary = {
    key1: [List],
    key2: Value,
}
```

### PAUSA 1
Ve si puedes descubrir cómo imprimir "Lille" de la Lista anidada llamada `travel_log`.
```
travel_log = {
    "Francia": ["París", "Lille", "Dijon"],
    "Alemania": ["Stuttgart", "Berlín"],
}
```
<div class="hint">
  Para obtener esta parte: <code>["París", "Lille", "Dijon"]</code>
Necesitarías: <code>travel_log["Francia"]</code>

Por lo tanto, para obtener Lille, necesitas:
<code>travel_log["Francia"][1]</code>
</div>

### Anidando Listas dentro de otras Listas

Hemos visto previamente Listas Anidadas:

```
nested_list = ["A", "B", ["C", "D"]]
```

### PAUSA 2
¿Recuerdas cómo obtener los ítems que están profundamente anidados en una lista? Intenta imprimir "D" de la lista `nested_list`.

<div class="hint">
  Para obtener esta lista: ["C", "D"] necesitamos el código:

<code>nested_list[2]</code>

Por lo tanto, para obtener "D" necesitamos:

<code>nested_list[2][1]</code>
</div>


### Anidando un Diccionario dentro de un Diccionario
También puedes anidar un diccionario en un diccionario:

```
my_dictionary = {
    key1: Value,
    key2: {Key: Value, Key: Value},
}
```

### PAUSA 3
Descubre cómo imprimir "Stuttgart" de la siguiente lista:
```
travel_log = {
  "Francia": {
    "ciudades_visitadas": ["París", "Lille", "Dijon"], 
    "total_visitas": 12
   },
  "Alemania": {
    "ciudades_visitadas": ["Berlín", "Hamburgo", "Stuttgart"], 
    "total_visitas": 5
   },
}
```