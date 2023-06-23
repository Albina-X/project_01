# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступны следующие методы матрицы: * принимать новые значения, * заменять существующие значения, * выводить число строк и колонок.

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!

### Решение:

class Matrix:
    def __init__(self, data):
        self.data = data
        self.num_rows = len(data)
        self.num_columns = len(data[0]) if self.num_rows > 0 else 0

    def set_value(self, row, column, value):
        if 1 <= row <= self.num_rows and 1 <= column <= self.num_columns:
            column_key = list(self.data[row - 1].keys())[column - 1]
            self.data[row - 1][column_key] = value
        else:
            print("Недопустимые значения строки или столбца.")

    def add_row(self, values):
        if len(values) == self.num_columns:
            new_row = {}
            for i, column_key in enumerate(self.data[0].keys()):
                new_row[column_key] = values[i]
            self.data.append(new_row)
            self.num_rows += 1
        else:
            print("Недопустимая длина строки.")

    def get_num_rows(self):
        return self.num_rows

    def get_num_columns(self):
        return self.num_columns

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            for row in self.data:
                line = "\t".join(str(value) for value in row.values())
                file.write(line + "\n")

data = [
    {"A": 1, "B": 2, "C": 3},
    {"A": 4, "B": 5, "C": 6},
    {"A": 7, "B": 8, "C": 9}
]

table = Matrix(data)

# Вывод числа строк и столбцов
num_rows = table.get_num_rows()
num_columns = table.get_num_columns()
print(f'Число строк: {num_rows}')
print(f'Число столбцов: {num_columns}')

# Замена значения в ячейке (2, 'B')
table.set_value(2, 2, 14)

# Добавление новой строки
new_row_values = [10, 11, 12]
table.add_row(new_row_values)

# Сохранение обновленной матрицы в файле

table.save_to_file("matrix.xls")