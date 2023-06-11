# Задача 1.2. Пункт B.

# Есть словарь песен. Необходимо распечатать общее время звучания трех случайных песен и вывести: Три песни звучат ХХХ минут.

# Решение:

import random

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
# Сначала сгенерируем список трех случайных песен:

random_songs = random.sample(list(my_favorite_songs_dict.keys()), 3)

# Далее сложим длительность выбранных песен и выведем результат в терминал:

total_time = sum(my_favorite_songs_dict[song] for song in random_songs)

print('Три песни:', random_songs, 'звучат',  round(total_time, 3), 'минут.')
