# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

num = int(input ("Введите колличество элементов: "))
array = [1]*num
X = int (input ("Введите искомое значение: "))

for i in range (num):
    import random
    array[i] = random.randint(1,50)

print (array)

index = 0
min = abs(X - array[0])
for i in range(1, num):
    buffer = abs(X -array[i])
    if buffer < min:
        min = buffer
        index = i
print (f"{array[index]}")
