"""Задача 5. Модуль для проверки ферзей
Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него
напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно
расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8
ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 -
координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют
- ложь.
"""


# 1 заданы позиции 8 ферзей
def check_queen(str: list) -> bool:
    n = 8
    x = []
    y = []
    for s in str:
        x.append(s[0])
        y.append(s[1])

    correct = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                correct = False
    return correct


str = [(1, 7), (2, 4), (3, 2), (4, 8), (5, 6), (6, 1), (7, 3), (8, 5)]  # не бьют
# print(check_queen(str))
if check_queen(str):
    print(f"{check_queen(str)} - не бьют")
else:
    print(f"{check_queen(str)} - бьют")


#######################################################################
# 2 расставить 8 ферзей на поле 8 на 8


# def is_valid(row, col, board):
#     # проверка, бьются ли ферзи в той же строке или диагоналях
#     for i in range(row):
#         if board[i] == col or \
#             board[i] - i == col - row or \
#             board[i] + i == col + row:
#             return False
#     return True
# def solve(size, row, board, results):
#     # если все столбцы заполнены, добавляем расстановку ферзей в результаты
#     if row == size:
#         results.append(board[:])
#         return
#     # пытаемся поставить ферзя в каждую строку текущего столбца
#     for col in range(size):
#         if is_valid(row, col, board):
#             board[row] = col
#             solve(size, row+1, board, results)
#             board[row] = -1
# def find_all_solutions(size):
#     results = []
#     board = [-1] * size
#     solve(size, 0, board, results)
#     return results

# #Вызов функции

# all_solutions = find_all_solutions(8) # найдем все расстановки ферзей на 8х8 доске
# for solution in all_solutions:
#     print(solution)
# # for i in range(1,n+1):
# #     #str += [(i, (randint(i, n+1))]
# #     str =[(i, randint(1, n+1)) for i in range(1, n+1)]
