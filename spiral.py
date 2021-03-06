def spiral(num, offset=0):
    """Print points in matrix, going in a spiral.

    Give a square matrix, like this 4 x 4 matrix, it's composed
    of points that are x, y points (top-left is 0, 0):

        0,0  1,0  2,0  3,0
        0,1  1,1  2,1  3,1
        0,2  1,2  2,2  3,2
        0,3  1,3  2,3  3,3

    Starting at the top left, print the x and y coordinates of each
    point, continuing in a spiral.

    (Since we provide 3 different versions, you can change this to
    the routine you want to test:

       #spiral = spiral_by_nested_boxes

    Here are different sizes:

        >>> spiral(1)
        (0, 0)

        >>> spiral(2)
        (0, 0)
        (1, 0)
        (1, 1)
        (0, 1)

        >>> spiral(3)
        (0, 0)
        (1, 0)
        (2, 0)
        (2, 1)
        (2, 2)
        (1, 2)
        (0, 2)
        (0, 1)
        (1, 1)

        >>> spiral(4)
        (0, 0)
        (1, 0)
        (2, 0)
        (3, 0)
        (3, 1)
        (3, 2)
        (3, 3)
        (2, 3)
        (1, 3)
        (0, 3)
        (0, 2)
        (0, 1)
        (1, 1)
        (2, 1)
        (2, 2)
        (1, 2)
    """

    if num == 1:
        x = offset
        y = offset
        print("({}, {})".format(x, y))

    else:
        y = 0

        for x in range(0, num):
            print((offset + x, offset))

        for y in range(1, num):
            print((offset + num - 1, offset + y))

        for x in range(num - 2, -1, -1):
            print((offset + x, offset + num - 1))

        for y in range(num - 2, 0, -1):
            print((offset, offset + y))

        if num > 2:
            spiral(num - 2, offset=offset+1)


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU MUST BE DIZZY WITH PRIDE!\n")
