# Задача 1.2. Пункт A. 


# Приведен плейлист песен в виде списка списков, в котором список my_favorite_songs содержит список названий и длительности каждого трека
# Вывести общее время звучания трех случайных песен в формате "Три песни звучат ХХХ минут"

# Решение:
# Сначала сгенерируем список трех случайных песен:

import random
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
random_songs = random.sample(my_favorite_songs,3)

# Далее сложим длительность выбранных песен и выведем результат в терминал:

sum = 0
a = []
for i in random_songs:
    a.append (i[1])
    sum += i[1]

print('Три песни:', random_songs[0][0], ',', random_songs[1][0], ',', random_songs[2][0], 'звучат', round(sum, 3), 'минут.')
