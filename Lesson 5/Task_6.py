"""
Lesson5.Task6.
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
"""


def subjects():
    try:
        mydict = {}
        with open("Task_6.txt", 'r', encoding='utf-8') as file_object:
            for line in file_object:
                name, stats = line.split(':')
                name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split()))
                mydict[name] = name_sum
            print(f'{mydict}')
    except FileNotFoundError:
        return 'Файл не найден.'

my_file = open('Task_6.txt', 'r', encoding='utf-8')
print(f'Содержимое файла: \n {my_file.read()}')

subjects()
