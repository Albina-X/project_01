# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Использовать условный оператор if-elif-else нельзя!

# Решение_1:

def switch_it_up(number):
    '''Функция длс возврата числового значения прописью, 
    с использованием конструкции try/except'''

    numbers = {
           1: 'One',   2: 'Two', 
           3: 'Three', 4: 'Four', 
           5: 'Five',  6: 'Six', 
           7: 'Seven', 8: 'Eigth', 
           9: 'Nine',  0: 'Zero'
}
    try:
        return numbers[number]
    except KeyError:
        return None

print(switch_it_up(1))
print(switch_it_up(2))
print(switch_it_up(3))
print(switch_it_up(4))
print(switch_it_up(5))
print(switch_it_up(6))
print(switch_it_up(7))
print(switch_it_up(8))
print(switch_it_up(9))
print(switch_it_up(0))
print(switch_it_up(1738390))

# Решение_2
# def switch_it_up(number):
#     '''Функция для возврата числового значения прописью, 
#     с использованием метода .get'''

#     numbers = {
#            1: 'One',   2: 'Two', 
#            3: 'Three', 4: 'Four', 
#            5: 'Five',  6: 'Six', 
#            7: 'Seven', 8: 'Eigth', 
#            9: 'Nine',  0: 'Zero'
#     }
    
#     return numbers.get(number)

# print(switch_it_up(1))
# print(switch_it_up(2))
# print(switch_it_up(3))
# print(switch_it_up(4))
# print(switch_it_up(5))
# print(switch_it_up(6))
# print(switch_it_up(7))
# print(switch_it_up(8))
# print(switch_it_up(9))
# print(switch_it_up(10))
# print(switch_it_up(0))