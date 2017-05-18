# 9x9 grid composed of 3 3x3 grids
"""
[[1,2,3],[4,5,6],[7,8,9]]
[[1,2,3],[4,5,6],[7,8,9]]
[[1,2,3],[4,5,6],[7,8,9]]

[[1,2,3],[4,5,6],[7,8,9]]
[[1,2,3],[4,5,6],[7,8,9]]
[[1,2,3],[4,5,6],[7,8,9]]

[[1,2,3],[4,5,6],[7,8,9]]
[[1,2,3],[4,5,6],[7,8,9]]
[[1,2,3],[4,5,6],[7,8,9]]

what is needed:
horizontal check function
vertical check function
square check function 

"""
numbers = range(1, 10)
empty = 'X' * 9
separator = '-' * 18
# print(empty)
# print(('{}|{}|{}|{}|{}|{}|{}|{}|{}\n').format(*numbers) * 9)
# print(('{}|' * 9 + '\n').format(*empty) * 9)

# board = ([('{} {} {}|' * 3).format(*empty)] * 3 +
#          [('{}' * 18).format(*separator)] +
#          [('{} {} {}|' * 3).format(*empty)] * 3 +
#          [('{}' * 18).format(*separator)] +
#          [('{} {} {}|' * 3).format(*empty)] * 3)


# # for line in board:
# #     print(line)
# # print(board)

# # print("Lines here")
# # print(board[0][:])
# # print(board[1][:])
# square1 = [board[0][0:5], board[1][6:11],  board[2][12:17]]
# square2 = [board[0][0:5], board[1][6:11],  board[2][12:17]]
# square3 = [board[0][0:5], board[1][6:11],  board[2][12:17]]
# square4 = [board[3][0:5], board[4][6:11],  board[5][12:17]]
# square5 = [board[3][0:5], board[4][6:11],  board[5][12:17]]
# square6 = [board[3][0:5], board[4][6:11],  board[5][12:17]]
# square7 = [board[6][0:5], board[8][6:11],  board[9][12:17]]
# square8 = [board[6][0:5], board[8][6:11],  board[9][12:17]]
# square9 = [board[6][0:5], board[8][6:11],  board[9][12:17]]

# for line in square8:
#     print(line)


def build_board(values):
    board = ([('{} {} {}|' * 3).format(*values)] * 3 +
             [('{}' * 18).format(*separator)] +
             [('{} {} {}|' * 3).format(*values)] * 3 +
             [('{}' * 18).format(*separator)] +
             [('{} {} {}|' * 3).format(*values)] * 3)
    for i in range(10):
        board[i][:].format(*values)
    for line in board:
        print(line)
    print(board[0:9][0][6])
    return [board]
build_board([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7,
             8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9,
             1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2,
             3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4,
             5, 6, 7, 8, 9])


# def check_squares(board):
#     """
#     check to see if the square has all numbers 1-9 and no repeats
#     """
#     board = build_board([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7,
#              8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9,
#              1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2,
#              3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4,
#              5, 6, 7, 8, 9])
#     square1 = [board[0][0:5], board[1][6:11],  board[2][12:17]]
#     square2 = [board[0][0:5], board[1][6:11],  board[2][12:17]]
#     square3 = [board[0][0:5], board[1][6:11],  board[2][12:17]]
#     square4 = [board[3][0:5], board[4][6:11],  board[5][12:17]]
#     square5 = [board[3][0:5], board[4][6:11],  board[5][12:17]]
#     square6 = [board[3][0:5], board[4][6:11],  board[5][12:17]]
#     square7 = [board[6][0:5], board[8][6:11],  board[9][12:17]]
#     square8 = [board[6][0:5], board[8][6:11],  board[9][12:17]]
#     square9 = [board[6][0:5], board[8][6:11],  board[9][12:17]]
#     all_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     for value in all_values:
#         if value in square1


# def check_horizontals(board):
#     board = build_board([1, 2, 3, 4, 5, 6, 7, 8, 9,
#                          1, 2, 3, 4, 5, 6, 7, 8, 9,
#                          1, 2, 3, 4, 5, 6, 7, 8, 9,
#                          1, 2, 3, 4, 5, 6, 7, 8, 9,
#                          1, 2, 3, 4, 5, 6, 7, 8, 9,
#                          1, 2, 3, 4, 5, 6, 7, 8, 9,
#                          1, 2, 3, 4, 5, 6, 7, 8, 9,
#                          1, 2, 3, 4, 5, 6, 7, 8, 9,
#                          1, 2, 3, 4, 5, 6, 7, 8, 9])
#     all_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     for i in range(11):
#         used = []
#         wrong = []
#         row = board[i][:]
#         for value in all_values:
#             if str(value) in str(row):
#                 if value not in used:
#                     used.append(value)
#                 else:
#                     wrong.append(value)
#                     print("This value is not correct {}" +
#                           ".format(value)")
#         if len(wrong) > 0:
#             print("This puzzle is not correct")
#     for line in board:
#         print(line)


# check_horizontals([1, 2, 3, 4, 5, 6, 7, 8, 9,
#                    1, 2, 3, 4, 5, 6, 7, 8, 9,
#                    1, 2, 3, 4, 5, 6, 7, 8, 9,
#                    1, 2, 3, 4, 5, 6, 7, 8, 9,
#                    1, 2, 3, 4, 5, 6, 7, 8, 9,
#                    1, 2, 3, 4, 5, 6, 7, 8, 9,
#                    1, 2, 3, 4, 5, 6, 7, 8, 9,
#                    1, 2, 3, 4, 5, 6, 7, 8, 9,
#                    1, 2, 3, 4, 5, 6, 7, 8, 9])


# def check_verticals(board):
#     board = build_board([1, 2, 3, 4, 5, 6, 7, 8, 9,
#                          1, 2, 3, 4, 5, 6, 7, 8, 9,
#                          1, 2, 3, 4, 5, 6, 7, 8, 9,
#                          1, 2, 3, 4, 5, 6, 7, 8, 9,
#                          1, 2, 3, 4, 5, 6, 7, 8, 9,
#                          1, 2, 3, 4, 5, 6, 7, 8, 9,
#                          1, 2, 3, 4, 5, 6, 7, 8, 9,
#                          1, 2, 3, 4, 5, 6, 7, 8, 9,
#                          1, 2, 3, 4, 5, 6, 7, 8, 9])

#     vert1 = board[0][0] + board[1][0] + board[2][0]
#     all_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     for j in range(19):
#         column = []
#         for i in range(11):
#             if str(board[i][j]).isnumeric():
#                 column.append(board[i][j])
#             for value in all_values:
#                 wrong = []
#                 used = []
#                 if str(value) in all_values and value not in used:
#                     used.append(value)
#                 else:
#                     wrong.append(value)
#                     print("this value is not correct {}".format(value))
#         print(column)
#     if len(wrong) > 0:
#         print("This puzzle is not correct")
#     for line in board:
#         print(line)

# check_verticals([[1, 2, 3, 4, 5, 6, 7, 8, 9],
#                  [1, 2, 3, 4, 5, 6, 7, 8, 9],
#                  [1, 2, 3, 4, 5, 6, 7, 8, 9],
#                  [1, 2, 3, 4, 5, 6, 7, 8, 9],
#                  [1, 2, 3, 4, 5, 6, 7, 8, 9],
#                  [1, 2, 3, 4, 5, 6, 7, 8, 9],
#                  [1, 2, 3, 4, 5, 6, 7, 8, 9],
#                  [1, 2, 3, 4, 5, 6, 7, 8, 9],
#                  [1, 2, 3, 4, 5, 6, 7, 8, 9]])





