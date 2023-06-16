# Задача 4.1.

# (Подробные условия задачи по ссылке: https://github.com/pyshkovni/homeworks/blob/main/lvl_4/task_4.1.py)
# В базе данных teacher создайте таблицу Students...наполните данными...и написать программу
# с помощью которой по ID студента можно получать информацию о школе и студенте. Формат вывода:
# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

#1. Подключимся к БД и создадим таблицу Students: 
import sqlite3

# def get_connection():
#     connection = sqlite3.connect('teachers.db')
#     return connection

# def close_connection(connection):
#     if connection:
#         connection.close()

# connection = sqlite3.connect('teachers.db')
# cursor = connection.cursor()
# query = """CREATE TABLE Students (
# Student_Id INTEGER NOT NULL,
# Student_Name TEXT NOT NULL,
# School_Id INTEGER NOT NULL PRIMARY KEY);"""
# cursor.execute(query)
# connection.commit()
# connection.close()

# 2. Наполним созданную таблицу данными:
# connection = sqlite3.connect('teachers.db')
# cursor = connection.cursor()
# query = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
# VALUES
# (201, 'Иван', '1'),
# (202, 'Петр', '2'),
# (203, 'Анастасия', '3'),
# (204, 'Игорь', '4');"""
# cursor.execute(query)
# connection.commit()
# connection.close()

# Вывод данных:
# def get_connection():
#     connection = sqlite3.connect('teachers.db')
#     return connection

# def close_connection(connection):
#     if connection:
#         connection.close()

# def get_school_name(school_id):
#     try:
#         connection = get_connection()
#         cursor = connection.cursor()
#         query = "SELECT * FROM School WHERE School_Id = ?;"
#         cursor.execute(query, (school_id,))
#         record = cursor.fetchone()
#         close_connection(connection)
#         return record[1]
#     except(Exception, sqlite3.Error) as error:
#         print('Ошибка в получении данных ', error)

# def get_student_info(student_id):
#     try:
#         connection = get_connection()
#         cursor = connection.cursor()
#         query = "SELECT * FROM Students WHERE Student_Id = ?;"
#         cursor.execute(query, (student_id,))
#         records = cursor.fetchall()
#         for row in records: 
#             print('ID Студента:', row [0])
#             print('Имя студента:', row [1])
#             print('ID школы:', row [2])
#             print('Название школы:', get_school_name(row[2]), '\n')
#         close_connection(connection)
#     except(Exception, sqlite3.Error) as error:
#         print('Ошибка в получении данных ', error)

# get_student_info(204)

# Решение с помощью метода join:
def get_connection():
    connection = sqlite3.connect('teachers.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def get_student_info(student_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT Students.*, School.School_Name FROM Students JOIN School ON Students.School_Id = School.School_Id WHERE Student_Id = ?;"
        cursor.execute(query, (student_id,))
        records = cursor.fetchall()
        for row in records:
            print('ID Студента:', row[0])
            print('Имя студента:', row[1])
            print('ID школы:', row[2])
            print('Название школы:', row[3], '\n')
        close_connection(connection)
    except sqlite3.Error as error:
        print('Ошибка в получении данных', error)

get_student_info(203)