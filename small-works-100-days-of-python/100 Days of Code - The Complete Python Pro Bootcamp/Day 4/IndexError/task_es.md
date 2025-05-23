### Longitud de una Lista
Puedes obtener la longitud de una lista (número de elementos en la lista) o la longitud de una cadena (número de caracteres en la cadena) usando la función `len()`. https://docs.python.org/3/library/functions.html#len

### IndexError
Cuando intentas acceder a un elemento que no está dentro del rango de la Lista, obtendrás un IndexError. Por ejemplo:

```
fruits = ["Cherry", "Apple", "Pear"]
print(fruits[3]) #Este será un IndexError
```

### Listas Anidadas
Puedes colocar Listas dentro de otras Listas, esto se convierte en algo llamado una "Lista Anidada" o una "Lista 2D". Por ejemplo:

```
fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
fruits_and_veg = [fruits, veg]
#La lista se vería así: [["Cherry", "Apple", "Pear"], ["Cucumber", "Kale", "Spinnach"]]
```
También podrías representar la lista en formato 2D de esta manera:
```
["Cherry", "Apple", "Pear"]
["Cucumber", "Kale", "Spinnach"]