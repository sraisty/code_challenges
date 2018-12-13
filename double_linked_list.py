class Node:
    
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return "({}, {})".format(self.key, self.value)


class DoubleLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def __repr__(self):
        current_node = self.head
        ret_str = "HEAD--->"
        while current_node:
            ret_str += (f"{current_node}, ")
            current_node = current_node.next
        ret_str += "<----TAIL"
        return ret_str

    def extend(self, lst):
        """
        lst is a list of (k,v) tuples, that will each be added to the end
        of the doublelinkedlist
        """
        last_node = self.tail.prev
        for (k, v) in lst:
            node = Node(key=k, value=v)
            node.prev = last_node
            last_node.next = node
            last_node = last_node.next

        self.tail.prev = last_node


    def unlink(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def delete(self, node):
        self.unlink(node)
        del(node)

    def add_to_front(self, node):
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head

    def find(self, x):
        current_node = self
        ret_list = []
        count = 0

        while current_node:
            if current_node.data == x:
                current_node.delete()
                count += 1
                ret_list.append(current_node)
                current_node = current_node.next()


class LRUCache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.current_size = 0
        self.key_to_node_dict = {}
        self.double_list = DoubleLinkedList()

    def get(self, key):
        self.


    def put(self, key, value):

