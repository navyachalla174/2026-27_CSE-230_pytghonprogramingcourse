rows = ____  # e.g. 3

for ____ in ____:  # row_loop_var; range(1, rows + 1)
    for ____ in ____:  # column_loop_var_spaces; range(1, rows - row_loop_var + 1)
        print(" ", end=" ")
    for ____ in ____:  # column_loop_var_dots; range(1, 2 * row_loop_var)
        print(____, end=" ")  # print one star
    print()