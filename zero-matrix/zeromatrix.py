"""Given an NxM matrix, if a cell is zero, set entire row and column to zeroes.

A matrix without zeroes doesn't change:

    >>> zero_matrix([[1, 2 ,3], [4, 5, 6], [7, 8, 9]])
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

But if there's a zero, zero both that row and column:

    >>> zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
    [[0, 0, 0], [4, 0, 6], [7, 0, 9]]

Make sure it works with non-square matrices:

    >>> zero_matrix([[1, 0, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [[0, 0, 0, 0], [5, 0, 7, 8], [9, 0, 11, 12]]
"""


def zero_matrix(matrix):
    """Given an NxM matrix, for cells=0, set their row and column to zeroes."""

    zero_rows = set()
    zero_cols = set()
    total_rows = len(matrix)
    total_cols = len(matrix[0])

    # go through all the elements in the matrix and when we find a 0, add its
    # row# and col# to the list of rows and columns to be zeroed out later
    for row_idx in range(total_rows):
        for col_idx in range(total_cols):
            if matrix[row_idx][col_idx] == 0:
                zero_rows.add(row_idx)
                zero_cols.add(col_idx)

    #  Zero out all the rows where a 0 was found
    for r_idx in zero_rows:
        # zero all columns in the row out
        for c in range(total_cols):
            matrix[r_idx][c] = 0

    # zero out all the columns where a 0 was found
    for c_idx in zero_cols:
        for row in matrix:
            row[c_idx] = 0

    return matrix


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** TESTS PASSED! YOU'RE DOING GREAT!\n")
