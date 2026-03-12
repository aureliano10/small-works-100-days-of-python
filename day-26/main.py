students_score = {
    "Alex" : 89,
    "Beth": 1,
    "Caroline": 1,
    "Dave": 1,
    "Eeleanor": 1,
    "Freddie": 1,
}
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
import random
students_score = {student: random.randint(1, 100) for student in names}
print(students_score)
