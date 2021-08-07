"""
Lesson2.Task5.
Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который
не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге
существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
должен разместиться после них.
"""
my_list = [9, 5, 5, 3, 2]
number = int(input("Введите число: "))
i = None
for el, num in enumerate(my_list):
    if number > num:
        i = el
        break

if i is None:
    my_list.append(number)
else:
    my_list.insert(i, number)

print(my_list)
