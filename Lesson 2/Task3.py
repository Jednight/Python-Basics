"""
Lesson2.Task3.
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.
"""
seasons_list = ['зима', 'весна', 'лето', 'осень']
seasons_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
month_number = int(input('Введите номер месяца: '))
if month_number == 12 or month_number == 1 or month_number == 2:
    print(f'Время года (решение через list): {seasons_list[0]}')
    print(f'Время года (решение через dict): {seasons_dict.get(1)}')
elif month_number == 3 or month_number == 4 or month_number == 5:
    print(f'Время года (решение через list): {seasons_list[1]}')
    print(f'Время года (решение через dict): {seasons_dict.get(2)}')

elif month_number == 6 or month_number == 7 or month_number == 8:
    print(f'Время года (решение через list): {seasons_list[2]}')
    print(f'Время года (решение через dict): {seasons_dict.get(3)}')
elif month_number == 9 or month_number == 10 or month_number == 11:
    print(f'Время года (решение через list): {seasons_list[3]}')
    print(f'Время года (решение через dict): {seasons_dict.get(4)}')
else:
    print('Ошибка! Число должно быть от 1 до 12!')
