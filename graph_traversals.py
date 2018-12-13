class Node:

    def __init__(self, data, adjacent_set=None):
        self.data = data
        if adjacent_set is None:
            self.adjacent = set()
        else:
            self.adjacent = adjacent_set

    def connect_2way(self, other_node):
        self.adjacent.add(other_node)
        other_node.adjacent.add(self)

    def connect_from_to(self, other_node):
        self.adjacent.add(other_node)
        # no reciprocal connection from other_node to me

    # def is_connected(self, n2):
        


class Graph:

    def __init__(self):
        self.nodes = set()

    def add_node(self, n):
        self.nodes.add(n)

    def add_nodes(self, n_set):
        self.nodes = self.nodes | n_set

    def print_groups(self):
        nodes = self.nodes.copy()
        groups = []

        while nodes:

            this_group = set()

            current = nodes.pop()
            this_group.add(current)
            for adjacent_node in current:
                if adjacent_node not in this_group:

            g_to_visit.append(list(current.adjacent))




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB! ***\n")