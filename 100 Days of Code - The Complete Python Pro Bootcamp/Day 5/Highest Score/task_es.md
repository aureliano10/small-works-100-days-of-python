### Suma
Python tiene muchas funciones integradas para ayudarnos a trabajar con números. Una de ellas nos ayuda a calcular la suma (el total).
p.ej.
```
student_scores = [180, 124, 165, 173, 189, 169, 146]
total_score = sum(student_scores)
```
Pero, ¿cómo funciona `sum()` detrás de escena? El código está escrito por las personas que desarrollaron Python y podría verse algo así:

```
student_scores = [180, 124, 165]

sum = 0
for score in student_scores:
    sum += score
    
print(sum)
```



### PAUSA 1 - Máximo
También existen métodos incorporados en Python llamados `max()` y `min()`, que te permiten pasar una lista de números, y te darán el número más alto o el número más bajo.

Tu tarea es descubrir cómo los programadores de Python podrían haber construido esta funcionalidad usando bucles y condicionales.

## COMPLETA ESTE DESAFÍO SIN USAR max()

Se te entrega una lista de notas de exámenes, y tienes que imprimir la nota más alta de la lista.
Necesitarás utilizar lo que has aprendido sobre listas, bucles for y condicionales para imprimir la nota más alta de la lista de student_scores.
Por ejemplo, si las notas fueron:
```
8 65 89 86 55 91 64 89
```
Tu código debería imprimir
```
91
```