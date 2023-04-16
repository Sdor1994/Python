# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

num = int (input ("Введите число N: "))

St = 2

stop = 0

for i in range(num):
    if stop !=1:
        St = St ** i 
        if St <= num:
            print (St , end=' ')
            St=2
        else:
            stop=1
    else :
        i=num
