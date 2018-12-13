# Given list of sorted lists of integers
# return one sorted merged list containing all 

def merge_sorted_lists(list_of_lists):
    """
    >>> merge_sorted_lists([[1],[2]])
    [1, 2]

    >>> merge_sorted_lists([[1, 3],[2, 4]])
    [1, 2, 3, 4]

    >>> merge_sorted_lists([[-1, 1, 3],[-8, 4, 6, 12], [1], [23, 46]])
    [-8, -1, 1, 1, 3, 4, 6, 12, 23, 46 ]
    """

    num_lists = len(list_of_lists)
    merged = []

    # look at the first element of all lists and find the min value
    # pop that min off its list and append it to the new_list
    lists_copy = list_of_lists.copy()

    while lists_copy:
        min_val = None
        list_with_min = None

        # find the list with the lowest value at the first position
        for list_num in range(len(lists_copy)):
            if min_val is None or lists_copy[list_num][0] < min_val:
                min_val = lists_copy[list_num][0]
                list_with_min = list_num

        # push that min value onto the result list
        merged.append(min_val)

        # remove the min item from its list so it isn't double counted
        lists_copy[list_with_min].pop(0)
        # if an entire list in the lists_copy is now empty, 
        # remove it
        if lists_copy[list_with_min] == []:
            lists_copy.pop(list_with_min)

    return merged


def merge_sorted_lists_better(lists):
    """
    >>> merge_sorted_lists_better([[1],[2]])
    [1, 2]

    >>> merge_sorted_lists_better([[1, 3],[1, 2, 4]])
    [1, 1, 2, 3, 4]

    >>> merge_sorted_lists_better([[-1, 1, 3],[-8, 4, 6, 12], [1], [23, 46]])
    [-8, -1, 1, 1, 3, 4, 6, 12, 23, 46 ]
    """


def merge_sorted_lists(list1, list2):
    i1 = 0
    i2 = 0
    while i1 < len(list1) or i2 < len(list2):
        if




if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.")