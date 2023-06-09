""" Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами. 
Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке """

ritm = input("Введите строчку стиха: ")
strRitm = tuple(ritm.split())

vowels = {'а'}

for i, word in enumerate(strRitm):
    count_vowels = word.lower().count('а')
    for k in range(i+1, len(strRitm)):
        if count_vowels == strRitm[k].lower().count('а'):
            print(f"Парам пам-пам")
        else:
            print(f"Пам парам")
