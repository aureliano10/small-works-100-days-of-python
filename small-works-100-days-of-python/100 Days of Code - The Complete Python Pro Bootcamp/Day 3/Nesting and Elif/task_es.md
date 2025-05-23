### Condicionales anidados
Puedes colocar declaraciones if/else dentro de otras declaraciones if/else. A esto se le conoce como anidamiento.
p.ej.
```
if nota_matematicas >= 90:
    if nota_ingles >= 90:
        print("Eres bueno en todo")
    else:
        print("Eres bueno en matemáticas")
if nota_ingles >= 90:
    print("Eres bueno en inglés)
```

En este caso, solo cuando un estudiante tiene más de 90 en matemáticas e inglés, recibe "Eres bueno en todo".

Nota: También puedes tener declaraciones if que no tienen una declaración else emparejada.