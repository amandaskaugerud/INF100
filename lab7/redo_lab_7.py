# from uib_inf100_graphics import *
# oppg 1
# def draw_grid(canvas, x1, y1, x2, y2, color_grid):
    # width_cell = abs(x1-x2)/len(color_grid[0])
    # heigth_cell = abs(y1-y2)/len(color_grid)
    # for row in range(len(color_grid)):
    #     for col in range(len(color_grid[0])):
    #         x1_coord = x1 + (width_cell * col)
    #         y1_coord = y1 + (heigth_cell * row)
    #         canvas.create_rectangle(x1_coord,y1_coord,x1_coord+width_cell,y1_coord+heigth_cell, fill=color_grid[row][col], outline="black")

# oppg 2
# del A
# def remove_row(grid: list, row: int)-> list:
#     grid.remove(grid[row])

# del B
import copy
# def row_removed(grid: list,row:int) -> list:
#     new_grid = copy.deepcopy(grid)
#     new_grid = new_grid[:row] + new_grid[row+1:]
#     return new_grid

# del C
# def remove_col(grid: list, col: int):
    # for row in grid:
    #     row.remove(row[col])


# del D
# def col_removed(grid:list, col: int) -> list:
    # new_grid = copy.deepcopy(grid)
    # result_grid = []
    # for row in new_grid:
    #     new_row = row[:col]+row[col+1:]
    #     result_grid.append(new_row)
    # return result_grid

# oppg 3
# def all_rows_and_cols_equal_sum(grid:list)->bool:
    # row_sum = list()
    # for row in range(len(grid)):
    #     row_sum.append(sum(grid[row]))

    # col_sum_list = list()
    # for col in range(len(grid[0])):
    #     col_sum = int()
    #     for row in range(len(grid)):
    #         col_sum += grid[row][col]
    #     col_sum_list.append(col_sum)

    # if row_sum.count(row_sum[0]) == len(row_sum) and col_sum_list.count(col_sum_list[0]) == len(col_sum_list):
    #     return True
    # return False



# oppg 4
# def check_in_cols(word:str, grid:list) -> bool:
#     for col in range(len(grid[0])):
#         col_word = str()
#         for row in range(len(grid)):
#             col_word += grid[row][col]
#         if word in col_word:
#             return True
#     return False

# def check_in_rows(word:str,grid:list) -> bool:
#     for row in range(len(grid)):
#         row_str = "".join(grid[row])
#         if word in row_str:
#             return True
#     return False

# def find_words_in_character_grid(char_grid, words) -> list:
#     words_in_char_grid = list()
#     for word in words:
#         if check_in_rows(word, char_grid):
#             words_in_char_grid.append(word)
#         elif check_in_cols(word, char_grid):
#             words_in_char_grid.append(word)
#     return words_in_char_grid

