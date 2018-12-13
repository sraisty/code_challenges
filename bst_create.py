
def create_bst(lst):

    # make that element our root node

    if not lst:
        return

    if len(lst) == 1:
        return BSTNode(lst[0])

    else:
        mid = len(lst) // 2
        n = BSTNode(lst[mid])
        n.left = create_bst(lst[0:mid])
        n.right = create_bst(lst[mid+1:])

    return n

class BSTNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return "<NODE: {}, left:{}, right:{}>".format(self.data, self.left, self.right)

