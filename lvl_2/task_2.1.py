# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# функции sorted, max и min использовать нельзя!

# Решение:

# Вариант 1, , если список чисел будет задан переменной:

def maximum(arr):
    
    '''Функция для расчета максимального значения из списка'''

    if not arr:
        return None
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

def minimum(arr):
    
    '''Функция для расчета минимального значения из списка'''

    if not arr:
        return None
    min_num = arr[0]
    for num in arr:
        if num < min_num:
            min_num = num
    return min_num

list = [0, -98, 987, 7, 8657, 76, 1, -56, 3456, -318, 14]

print('Max -->', maximum(list),'\nMin -->', minimum(list))

# Вариант 2: 
# Чтобы не использовать заготовленный список,
# воспользуемся импортом из модуля ast функции literal_eval
# которая позволит ввести пользователю список чисел

# from ast import literal_eval
 
# list = literal_eval(input('Введите список целых чисел: '))

# print('Max -->', maximum(list),'\nMin -->', minimum(list))