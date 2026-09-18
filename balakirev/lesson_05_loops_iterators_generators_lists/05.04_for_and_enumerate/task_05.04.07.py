# Подвиг 4 (классический). Необходимо написать программу формирования квадратной двумерной таблицы чисел 
# matrix размером N x N, где N - целое число (больше нуля), читаемое из входного потока командой:
# N = int(input())                 
# Таблица matrix должна описываться двумерным вложенным списком и содержать целые числа от 1 и далее по порядку,
# записанных "змейкой" согласно следующему рисунку:
# https://ucarecdn.stepik.net/592a40a6-4ad4-4a14-81ac-5b806ac5a9b9/
# Например, для таблицы matrix размером N=5, должны получить следующий вложенный список:
# matrix = [
#     [1, 2, 3, 4, 5],
#     [16, 17, 18, 19, 6],
#     [15, 24, 25, 20, 7],
#     [14, 23, 22, 21, 8],
#     [13, 12, 11, 10, 9]
# ]
# Выведите полученный список matrix на экран командой:
# for row in matrix:
#     print(' '.join(str(num) for num in row))

N = int(input())
matrix = [[0] * N for _ in range(N)]
num = 1
top = 0
bottom = N - 1
left = 0
right = N - 1


while num <= N ** 2:
    # to the right
    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1

    top += 1

    #to the down
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1

    right -= 1

    #to the left
    for i in range(right, left - 1, -1):
        matrix[bottom][i] = num
        num += 1

    bottom -= 1

    #to the top
    for i in range(bottom, top - 1, - 1):
        matrix[i][left] = num
        num += 1

    left += 1

for row in matrix:
    print(' '.join(str(num) for num in row))
