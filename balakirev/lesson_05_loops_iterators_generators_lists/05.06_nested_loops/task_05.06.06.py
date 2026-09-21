# Подвиг 4. На вход программе подается двумерный список размерностью 5 х 5 элементов, 
# состоящий из нулей и в некоторых позициях единицы (см. пример ниже). 
# В программе уже реализовано их чтение и сохранение в списке:
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]    
# Список lst_in имеет следующий формат (пример):
# lst_in=[[0, 0, 0, 1, 0],
#         [0, 0, 1, 0, 1],
#         [0, 0, 1, 0, 0],
#         [0, 0, 1, 1, 0],
#         [1, 0, 0, 0, 0]]                  
# Требуется проверить, не касаются ли единицы друг друга по горизонтали, вертикали и диагонали. 
# То есть, вокруг каждой единицы должны быть нули. Если проверка проходит вывести на экран "ДА", иначе "НЕТ".

import sys

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

flg = True
n = len(lst_in)

for i in range(n):
    for j in range(n):
        if lst_in[i][j] == 1:
            # horizontal
            if j > 0 and lst_in[i][j - 1] == 1:
                flg = False
            if j < n - 1 and lst_in[i][j + 1] == 1:
                 flg = False
            # vertical
            if i > 0 and lst_in[i - 1][j] == 1:
                flg = False
            if i < n - 1 and lst_in[i + 1][j] == 1:
                flg = False
            # diagonal
            if i > 0 and j > 0 and lst_in[i - 1][j - 1] == 1:
                flg = False
            if i > 0 and j < n - 1 and lst_in[i - 1][j + 1] == 1:
                flg = False
            if i < n - 1 and j > 0 and lst_in[i + 1][j - 1] == 1:
                flg = False
            if i < n - 1 and j < n - 1 and lst_in[i + 1][j + 1] == 1:
                flg = False

print('ДА' if flg else 'НЕТ')

# Проверять матрицу квадратами
# n = len(lst_in) - 1
# flg = True

# import sys

# # считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]

# # здесь продолжайте программу (используйте список lst_in)
# flag = "ДА"
# for i in range(len(lst_in) - 1):
#     for j in range(len(lst_in) - 1):
#         if lst_in[i][j] + lst_in[i][j + 1] + lst_in[i + 1][j] + lst_in[i + 1][
#         j + 1] > 1:
#             flag = "НЕТ"
#             break
# print(flag)