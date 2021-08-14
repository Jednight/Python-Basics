'''
Lesson4.Task6.1.
Реализовать бесконечный итератор, генерирующий целые числа,
начиная с указанного.
'''
from itertools import count

for el in count(int(input('Введите стартовое число: '))):
    print(el)
