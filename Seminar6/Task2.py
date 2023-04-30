def find_indexes(arr, min_val, max_val):
    indexes = []
    for i in range(len(arr)):
        if min_val <= arr[i] <= max_val:
            indexes.append(i)
    return indexes

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
min_val = 5
max_val = 15
indexes = find_indexes(arr, min_val, max_val)
print(f"Элементы массива {arr}, значения которых принадлежат диапазону от {min_val} до {max_val}, имеют индексы: {indexes}")
