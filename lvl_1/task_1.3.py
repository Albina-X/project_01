# Задача 1.3.:

# Напишите скрипт, который принимает от пользователя номер месяца, а возвращает количество дней в нем. 
# Результат проверки вывести на консоль. Допущение: в феврале 28 дней. Если номер месяца некорректен - сообщить об этом

amount_of_days = int(input('Введите номер месяца: '))

if amount_of_days == 1:
    print('Вы ввели январь. 31 день')
elif amount_of_days == 3:
    print('Вы ввели март. 31 день')
elif amount_of_days == 2:
    print('Вы ввели февраль. 28 дней')
elif amount_of_days == 4:
    print('Вы ввели апрель. 30 дней')
elif amount_of_days == 5:
    print('Вы ввели май. 31 день')
elif amount_of_days == 6:
    print('Вы ввели июнь. 30 дней')
elif amount_of_days == 7: 
    print('Вы ввели июль. 31 день')
elif amount_of_days == 8:  
    print('Вы ввели август. 31 день')
elif amount_of_days == 9:
    print('Вы ввели сентябрь. 30 дней')
elif amount_of_days == 10:
    print('Вы ввели октябрь. 31 день')
elif amount_of_days == 11:
    print('Вы ввели ноябрь. 30 дней')
elif amount_of_days == 12:
    print('Вы ввели декабрь. 31 день')

else:    print('Номер месяца введен некорректно: такого месяца не существует!')
