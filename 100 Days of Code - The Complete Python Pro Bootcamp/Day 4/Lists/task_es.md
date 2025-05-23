Puedes crear una colección sencilla de elementos ordenados utilizando una lista en Python. Por ejemplo:

`fruits = ["Cherry", "Apple", "Pear"]`

o

`states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]`

### acceder a elementos en listas

Puedes proporcionar el nombre de la lista, seguido de corchetes y el índice del elemento que quieres. Por ejemplo:

`states_of_america[0]`

te dará "Delaware".

Recuerda que en todo lo relacionado con computación, el primer número con el que contamos es 0 y nunca 1. 0, 1, 2, 3 en lugar de 1, 2, 3, 4.

### índices negativos

Puedes acceder a los elementos de la lista contando desde el final utilizando números enteros negativos. Por ejemplo:
```
fruits = ["Cherry", "Apple", "Pear"]
fruits[-1] #esto será "Pear"
```

### modificar elementos

Puedes usar la misma sintaxis para obtener elementos de una Lista y modificarlos. Por ejemplo:
```
fruits = ["Cherry", "Apple", "Pear"]
fruits[0] = "Orange"
# fruits ahora será ["Orange", "Apple", "Pear"]
```

### agregar elementos

Puedes agregar elementos al final de una Lista utilizando la función `append()`. Por ejemplo:
```
fruits = ["Cherry", "Apple", "Pear"]
fruits.append("Orange")
# fruits ahora será ["Cherry", "Apple", "Pear", "Orange"]
```

### documentación sobre listas

Puedes encontrar la documentación sobre las listas en Python y otras funciones relacionadas con listas aquí: https://docs.python.org/3/tutorial/datastructures.html