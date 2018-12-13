def flip_horizontal_in_place(matrix):
    """
        >>> n = flip_horizontal_in_place([[0]])
        >>> print(n)
        [[0]]

        >>> b = [[2]]
        >>> flip_horizontal_in_place(b)
        [[2]]

        >>> flip_horizontal_in_place([[1,2,3],[4,5,6]])
        [[3, 2, 1], [6, 5, 4]]

        >>> flip_horizontal_in_place([[1,2],[4,5]])
        [[2, 1], [5, 4]]
    """

    col_hi = len(matrix[0]) - 1
    col_lo = 0
    while col_lo < col_hi:
        for row in matrix:
            row[col_lo], row[col_hi] = row[col_hi], row[col_lo]
        col_lo += 1
        col_hi -= 1
    return matrix


def flip_horizontal_in_place2(matrix):
    """
        >>> n = flip_horizontal_in_place2([[0]])
        >>> print(n)
        [[0]]

        >>> b = [[2]]
        >>> flip_horizontal_in_place2(b)
        [[2]]

        >>> flip_horizontal_in_place2([[1,2,3],[4,5,6]])
        [[3, 2, 1], [6, 5, 4]]

        >>> flip_horizontal_in_place2([[1,2],[4,5]])
        [[2, 1], [5, 4]]
    """
    for row in matrix:
        row.reverse()
    return matrix


def flip_horizontal_copy(matrix):
    """
        >>> n = flip_horizontal_copy([[0]])
        >>> print(n)
        [[0]]

        >>> b = [[2]]
        >>> flip_horizontal_copy(b)
        [[2]]

        >>> flip_horizontal_copy([[1,2,3],[4,5,6]])
        [[3, 2, 1], [6, 5, 4]]

        >>> flip_horizontal_copy([[1,2],[4,5]])
        [[2, 1], [5, 4]]
    """

    # THIS DOES NOT WORK:
    # for row in matrix:
    #     row = row[::-1]

    # THIS WORKS
    for r in range(len(matrix)):
        matrix[r] = matrix[r][::-1]
    return matrix


def flip_vertical_in_place(matrix):
    """
        >>> flip_vertical_in_place([[0]])
        [[0]]

        >>> flip_vertical_in_place([[1,2,3,4], [10,20,30,40]])
        [[10, 20, 30, 40], [1, 2, 3, 4]]

        >>> flip_vertical_in_place([[1,2],[3,4],[5,6]])
        [[5, 6], [3, 4], [1, 2]]
    """
    # METHOD #1: Simplest
    # matrix.reverse()
    # return matrix

    # METHOD #2 without using reverse
    r_lo = 0
    r_hi = len(matrix)-1
    while r_lo < r_hi:
        matrix[r_lo], matrix[r_hi] = matrix[r_hi], matrix[r_lo]
        r_lo += 1
        r_hi -= 1
    return matrix


def flip_vertical_copy(matrix):
    """
        >>> flip_vertical_copy([[0]])
        [[0]]

        >>> flip_vertical_copy([[1,2,3,4], [10,20,30,40]])
        [[10, 20, 30, 40], [1, 2, 3, 4]]

        >>> flip_vertical_copy([[1,2],[3,4],[5,6]])
        [[5, 6], [3, 4], [1, 2]]
    """
    return matrix[::-1]

def rotate_clockwise(matrix):
    """
        >>> rotate_clockwise([[1]])
        [[1]]

        >>> rotate_clockwise([[1, 2]])
        [[1], [2]]

        >>> rotate_clockwise([[1, 2],[3,4]])
        [[3, 1], [4, 2]]

        >>> rotate_clockwise([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
        [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]

        >>> rotate_clockwise([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
        [[9, 5, 1], [10, 6, 2], [11, 7, 3], [12, 8, 4]]

        [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]])

        [[13,9,5,1],
         [14,10,6,2],
         [15,11,7,3],
         [16,12,8,4]]

    """
    m_numrows = len(matrix)  # rows in the original matrix. This becomes cols in new matrix
    m_numcols = len(matrix[0])  # cols in original matrix & num rows in new matrix

    # This one doesn't work.  Any changes made to one row are made to ALL rows in
    # the resulting matrix
    # rot_matrix = [[0] * m_numrows] * m_numcols

    # the following works for initing an array of the right shape
    rot_matrix = [[None for _ in range(m_numrows)] for _ in range(m_numcols)]

    for m_row in range(m_numrows):
        for m_col in range(m_numcols):
            n_row = m_col
            n_col = m_numrows - m_row - 1

            # val = matrix[m_row][m_col]
            # rot_matrix[n_row][n_col] = val
            rot_matrix[n_row][n_col] = matrix[m_row][m_col]

    return rot_matrix


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")
