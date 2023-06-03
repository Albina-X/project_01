# Дана строка с перечислением песен: 
# my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Вывести на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

# Решение 1 - посчитать индексы:
my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# W a s t e  a  M o m  e  n  t  ,    S  t  a  y  i  n   g \  '     A  l  i  v  e  ,     A     S  o  r  t  a
# 0 1 2 3 4 567 8 9 10 11 12 13 1415 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 

# F  a  i  r  y  t  a  l  e  ,     S  t  a  r  t     M  e     U  p  ,     N  e  w     S  a  l  v  a  t  i  o  n  '
# 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77

print ('первый трек', my_favorite_songs [:14])
print ('последний трек', my_favorite_songs [-14:])
print ('второй трек', my_favorite_songs [15:30])
print ('второй трек с конца', my_favorite_songs [-27:-15])



# Решение 2 - воспользуемся методом split и выведем треки в одну строку:

First_track = my_favorite_songs.split(', ')[0]

Last_track = my_favorite_songs.split(', ')[-1]

Second_track = my_favorite_songs.split(', ')[1]

Second_Last_track = my_favorite_songs.split(', ')[-2]

print (First_track, Last_track, Second_track, Second_Last_track)
