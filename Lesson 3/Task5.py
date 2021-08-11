"""
Lesson3.Task5.
Программа запрашивает у пользователя строку чисел, разделенных
 пробелом. При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и
снова нажать Enter. Сумма вновь введенных чисел будет добавляться
к уже подсчитанной сумме. Но если вместо числа вводится специальный
символ, выполнение программы завершается. Если специальный символ
введен после нескольких чисел, то вначале нужно добавить сумму этих
чисел к полученной ранее сумме и после этого завершить программу.
"""


def my_sum():
    res = 0
    while True:
        numbers = input('Введите числа через пробел или q для выхода: ').split()
        for num in numbers:
            try:
                if num == 'q':
                    return res
                else:
                    res += int(num)
            except ValueError:
                print("Для выхода из программы нажмите 'q'")
        print(f'Сумма: {res}')


print(my_sum())
