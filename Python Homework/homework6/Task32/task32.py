#  Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)


min_number = int(input('Введите минимальное значение массива '))
max_number = int(input('Введите максимальное значение массива '))
import random 
list_1 = [random.randint(1,10) for _ in range(10)]
print (list_1)

for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i, end=' ')