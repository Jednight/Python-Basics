"""
Lesson5.Task2.
Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
"""


def count_info():
    try:
        with open('Task_2.txt', 'r', encoding='utf-8') as f:
            my_list = file.readlines()
            for i in range(len(my_list)):
                new_l = my_list[i].split()
                print(f'Количество строк в файле: {len(my_list)}. В {i + 1}-ой строке: {len(new_l)} слов.')
    except FileNotFoundError:
        return 'Файл отсутствует.'


my_file = open('Task_2.txt', 'r', encoding='utf-8')
print(f'Содержимое файла: \n {my_file.read()}')

count_info()
