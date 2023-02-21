# Queue implementation with linked list
# We can perform O(1) add, remove functionality
class Queue:
    def remove_from_head(self):
        if self.head != None:
            removed_node = self.head
            self.head = self.head.next
            return removed_node

    def add_to_tail(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def __init__(self):
        self.tail = None
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val
