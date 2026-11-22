rows = ____  # e.g. 5

for ____ in ____:  # row_loop_var; range(1, rows + 1)
    for ____ in ____:  # column_loop_var_spaces; range(1, rows - row_loop_var + 1)
        print(" ", end=" ")
    for ____ in ____:  # column_loop_var; range(1, 2 * row_loop_var)
        print(____, end=" ")  # print 1, 2, 3, ... with a space between
    print()