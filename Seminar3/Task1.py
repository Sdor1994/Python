# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


num = int(input ("Введите колличество элементов: "))
array = [1]*num
X = int (input ("Введите искомое значение: "))
count = 0

for i in range (num):
    import random
    array[i] = random.randint(1,10)
    if array[i] == X:
        count += 1

print (array)
print (count)
