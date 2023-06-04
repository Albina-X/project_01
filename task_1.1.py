# Дана строка с перечислением песен: 
# my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Вывести на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

# Решение 1 - посчитать индексы:
my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

print ('первый трек', my_favorite_songs [:14])
print ('последний трек', my_favorite_songs [-14:])
print ('второй трек', my_favorite_songs [15:30])
print ('второй трек с конца', my_favorite_songs [-27:-15])


# Решение 2 (!!!ЧТОБЫ ВОСПОЛЬЗОВАТЬСЯ РЕШЕНИЕМ 2 необходимо закомментировать 1 решение и убрать комментарий со второго!!!) - воспользуемся методом split и выведем треки в одну строку:  

# First_track = my_favorite_songs.split(', ')[0]

# Last_track = my_favorite_songs.split(', ')[-1]

# Second_track = my_favorite_songs.split(', ')[1]

# Second_Last_track = my_favorite_songs.split(', ')[-2]

# print (First_track, Last_track, Second_track, Second_Last_track)

