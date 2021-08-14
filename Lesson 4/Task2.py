'''
Lesson4.Task2.
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
'''

import random
generated_list = random.sample(range(1, 100), 10)
print(f'Исходный список: {generated_list}')
new_list = []
for el in range(len(generated_list) - 1):
    if generated_list[el] < generated_list [el+1]:
        new_list.append(generated_list[el+1])
print(f'Новый список: {new_list}')