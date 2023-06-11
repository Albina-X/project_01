# Задача 2.4.

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"


# Решение_1:
def remove_last_em(s):
    '''Функция убирает последний символ в строке
    '''
    result_string = ""
    index = len(s)
    for i in range(index-1):
       result_string += s[i]
    return result_string

print(remove_last_em('!Hello, my name is Max.!')) # выводит: !Hello, my name is Max.


# Решение_2:
# def remove_last_em(s):
#     '''Функция убирает последний символ в строке
#       с помощью метода .rstrip'''
    
#     s1 = s.rstrip('!')
#     return s1

# print(remove_last_em('!Hello, my name is Max.!')) # выводит: !Hello, my name is Max.