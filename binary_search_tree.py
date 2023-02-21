class BSTNode(object):
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val == None or self.val == val:
            self.val = val
        if val < self.val:
            if self.left == None:
                self.left = BSTNode(val)
            else:
                self.left.insert(val)
        elif val > self.val:
            if self.right == None:
                self.right = BSTNode(val)
            else:
                self.right.insert(val)

    def get_min(self):
        current = self
        while current.left:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right:
            current = current.right
        return current.val

    def delete(self, val):
        if self == None:
            return None

        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.val:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.right == None:
                return self.left
            elif self.left == None:
                return self.right
            else:
                min_larger_node_val = self.right.get_min()
                self.val = min_larger_node_val
                self.right = self.right.delete(min_larger_node_val)
        return self

    def preorder(self, visited):
        if self.val:
            visited.append(self.val)
            if self.left:
                self.left.preorder(visited)
            if self.right:
                self.right.preorder(visited)
        return visited

    def postorder(self, visited):
        if self.val:
            if self.left:
                self.left.postorder(visited)
            if self.right:
                self.right.postorder(visited)
            visited.append(self.val)
        return visited

    def inorder(self, visited):
        if self.val:
            if self.left:
                self.left.inorder(visited)
            visited.append(self.val)
            if self.right:
                self.right.inorder(visited)
        return visited

    def exists(self, val):
        if val < self.val:
            if self.left:
                return self.left.exists(val)
        elif val > self.val:
            if self.right:
                return self.right.exists(val)
        else:
            return True
        return False

    def __repr__(self):
        lines = []
        print_tree(self, lines)
        return "\n".join(lines)
