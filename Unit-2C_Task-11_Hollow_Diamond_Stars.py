rows = ____  # e.g. 3

# Upper half
for ____ in ____:  # row_loop_var; range(1, rows + 1)
    for ____ in ____:  # leading spaces
        print(" ", end=" ")
    for ____ in ____:  # column_loop_var_dots; range(1, 2 * row_loop_var)
        if ____:  # first or last position in this row?
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Lower half (same idea with row_loop_var from rows-1 down to 1)
for ____ in ____:
    for ____ in ____:
        print(" ", end=" ")
    for ____ in ____:
        if ____:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()