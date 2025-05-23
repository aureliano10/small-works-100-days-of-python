Corrija cualquier error (subrayados en rojo) que aparezca en el editor antes de ejecutar su código. Las advertencias (en amarillo) son correcciones opcionales, a veces pueden causar un problema más adelante, otras veces está bien y el editor simplemente no entiende lo que está tratando de hacer.

### Capturando Excepciones
Puede usar un bloque try/except en Python para capturar cualquier excepción que pueda ocurrir. Por ejemplo, si imagina que podría haber un error del usuario. Puede evitar que se produzca un bloqueo en su código al anticiparlo. Atrapa el código peligroso dentro de un bloque try y utiliza un bloque except para capturar cualquier error potencial. Luego define lo que debe suceder cuando ese error ocurre en lugar de simplemente bloquearse y detener el código.

p.ej.

```
try:
    print(6 > "cinco")
except TypeError:
    print("No puedes mezclar enteros y cadenas en una comparación")
```

### PAUSA 1 
Corrige el error para que la instrucción print muestre el valor correcto de la edad en el área de salida.