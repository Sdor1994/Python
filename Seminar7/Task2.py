""" Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, 
вычисляющую элемент по номеру строки и столбца.
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения. """

def print_operation_table(operation, num_rows, num_columns):
    for row in range(1, num_rows + 1):
        for col in range(1, num_columns + 1):
            result = operation(row, col)
            print(f"{result}\t", end="")
        print()

# Пример использования функции с операцией умножения
num_rows = int(input("Введите количество столбцов: "))
num_columns = int(input("Введите количество строк: "))

print_operation_table(lambda row , col: row*col, num_rows , num_columns)
