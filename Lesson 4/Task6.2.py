'''
Lesson4.Task6.2.
Реализовать бесконечный итератор, повторяющий элементы
некоторого списка, определенного заранее.
'''

from itertools import cycle

list = [10, -8, 'List', True, None, 108]
for el in cycle(list):
    print(el)