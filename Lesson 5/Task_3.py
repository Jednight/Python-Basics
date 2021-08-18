"""
Lesson5.Task3.
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""


def employee_salary():
    salaries = {}
    try:
        with open('Task_3.txt', 'r', encoding='utf-8') as file:
            for line in file:
                salaries[line.split()[0]] = float(line.split()[1])
            print('Меньше 20000 получают:')
            for name, salary in salaries.items():
                if salary < 20000:
                    print(name)
            print(f'Средний оклад: {sum(salaries.values()) / len(salaries):.2f}')
    except:
        print('Что-то поломалось')


my_file = open('Task_3.txt', 'r', encoding='utf-8')
print(f'Содержимое файла: \n {my_file.read()}')

employee_salary()
