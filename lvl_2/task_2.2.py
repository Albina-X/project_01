# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

# Решение_1(если заданы словари): 

def quarter_of(month):
    '''Функция ищет номер квартала по номеру месяца'''
    list_of_quarters = {
        1: (1, 2, 3),
        2: (4, 5, 6),
        3: (7, 8, 9),
        4: (10, 11, 12)
    }
    
    for quarter, months in list_of_quarters.items():
        if month in months:
            return quarter
    
    return None

list_of_months = {1: 'Январь',   2: 'Февраль', 3: 'Март',
          4: 'Апрель',   5: 'Май',     6: 'Июнь',
          7: 'Июль',     8: 'Август',  9: 'Сентябрь',
          10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'
}

month = int(input('Введите номер месяца: '))
quarter = quarter_of(month)

if quarter is not None:
    print(f"Месяц {list_of_months[month]} является частью {quarter}-го квартала.")
else:
    print(f"Неверный номер месяца.")

# Решение_2:
# def quarter_of(month):
#     if month in range(1, 4):
#         return 1
#     elif month in range(4, 7):
#         return 2
#     elif month in range(7, 10):
#         return 3
#     elif month in range(10, 13):
#         return 4
#     else:
#         return None
# month = int(input('Введите номер месяца: '))
# quarter = quarter_of(month)
# print(f"Месяц {month} является частью {quarter}-го квартала.")