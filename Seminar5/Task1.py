def exponentiation(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * exponentiation(a, b - 1)

a = int(input("Введите число A: "))
b = int(input("Введите степень B: "))

result = exponentiation(a, b)

print(f"{a} в степени {b} = {result}")