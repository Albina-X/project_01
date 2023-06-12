# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

# Решение:
def remove_exclamation_marks(s):
    '''Функция убирает любой символ в заданной строке 
    с помощью метода .replace '''

    i=s.replace('!', '')
    return i

print(remove_exclamation_marks('I live! in Russia.')) # выводит: I live in Russia