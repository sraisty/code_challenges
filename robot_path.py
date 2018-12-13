# Robot starts

def robot_path_possible(matrix):
    """
    # robot can move right or down (from my frame of reference)
    # Returns True is there is a path for robot to move from from upper_left 
    # corner of matrix to bottom right corner, False otherwise.

    >>> robot_path_possible([[True]])
    True

    >>> robot_path_possible([[True, True]])
    True

    >>> robot_path_possible([[True, False], [False, True]])
    False

    >>> robot_path_possible([[True, True], [False, True]])
    True

    >>> robot_path_possible([[True, False], [True, True]])
    True

    >>> robot_path_possible([[True, False, False], [True, True, False], [False, True, True]])
    True

    >>> robot_path_possible([[True, False, False], [True, False, False], [False, True, True]])
    False

    >>> robot_path_possible([[True, False, False, True, False, True],[True, True, False, True, True, True],[True, False, False, True, True, True],[True, False, True, True, True, True],[True, False, True, True, True, True]])
    False


    >>> robot_path_possible([[True, False, False, True, True, True],[True, True, True, False, True, True],[True, False, True, False, True, True], [True, False, True, True, False, True],[False, False, False, True, True, True]])
    True

    """

    rows = len(matrix)
    cols = len(matrix[0])
    end_point = (cols-1, rows-1)
    path = []

    points_to_visit = [(0, 0)]

    while points_to_visit:

        # depth first traversal
        c, r = points_to_visit.pop()

        if matrix[r][c]:

            # is this point the lower_right corner, and the end?
            if end_point == (c, r):
                return True

            # not the end square, but in future pass see if there
            # is a path using this square's right neighbor
            # and down_neighbor
            if r + 1 < rows:
                # we can move down
                points_to_visit.append((c, r+1))
            if c + 1 < cols:
                # we can move right from this square
                points_to_visit.append((c+1, r))

    return False


def robot_path(maze, row=0, col=0):
        """
    # robot can move right or down (from my frame of reference)
    # Returns True is there is a path for robot to move from from upper_left 
    # corner of matrix to bottom right corner, False otherwise.

    >>> robot_path([[True]])
    [(0,0)]

    >>> robot_path([[True, True]])
    [(0,0), (0,1)]

    >>> robot_path([[True, False], [False, True]])
    False

    >>> robot_path([[True, True], [False, True]])
    [(0, 0), (0, 1), (1, 1)]

    >>> robot_path([[True, False], [True, True]])
    [(0, 0), (1,0), (1, 1)]

    >>> robot_path([[True, False, False], [True, True, False], [False, True, True]])
    True

    >>> robot_path([[True, False, False], [True, False, False], [False, True, True]])
    False

    >>> robot_path([[True, False, False, True, False, True],[True, True, False, True, True, True],[True, False, False, True, True, True],[True, False, True, True, True, True],[True, False, True, True, True, True]])
    False


    >>> robot_path([[True, False, False, True, True, True],[True, True, True, False, True, True],[True, False, True, False, True, True], [True, False, True, True, False, True],[False, False, False, True, True, True]])
    True

    """
    rows = len(maze)
    cols = len(maze[0])
    end_point = (rows-1, cols-1)
    path = [(row, col)]

    if row == rows-1 and col == cols-1:
        # found the end of the maze
        return path

    if r+1 < rows:
        down_path = robot_path(maze, r+1, c)
    if c+1 < cols:
        right_path = robot_path(maze, r, c+1)

    if down_path()


def robot_path(maze, row=0, col=0, already_failed=None):
    # TODO
    if already_failed is None:
        already_failed = set()



if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.")
