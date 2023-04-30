a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов прогрессии: "))


progression = []

for i in range(n):
    a = a1 + i * d
    progression.append(a)

print("Элементы прогрессии:")
for a in progression:
    print(a)
