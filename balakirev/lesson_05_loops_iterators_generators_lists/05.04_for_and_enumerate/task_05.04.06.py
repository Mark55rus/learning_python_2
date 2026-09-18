#  Подвиг 3. В программе выполняется чтение двумерного списка чисел размером n x m элементов:
# s = sys.stdin.readlines()
# lst2D = [list(map(int, x.strip().split())) for x in s]
# Формат списка lst2D следующий (пример):
# lst2D = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# Необходимо перебрать элементы этого списка змейкой, т.е. в порядке, показанном на рисунке
# (https://ucarecdn.stepik.net/9773b6a5-2052-4733-832f-6a9569578bba/) и
# последовательно вывести их на экран в одну строчку через пробел:
# Например, вывод приведенного списка lst2D должен быть таким:
# 1 2 3 6 5 4 7 8 9

import sys

s = sys.stdin.readlines()
lst2D = [list(map(int, x.strip().split())) for x in s]

new_st = []

for i, v in enumerate(lst2D):
    if i % 2 == 0:
        for i in range(len(v)):
            new_st += ' ' + str(v[i])
    else:
        for i in range(len(v) - 1, -1, -1):
            new_st += ' ' + str(v[i])

print(new_st.lstrip())

