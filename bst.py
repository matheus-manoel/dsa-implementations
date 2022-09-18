class BSTNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if self.val is None:
            self.val = val
            return

        if val >= self.val:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BSTNode(val)
        else:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BSTNode(val)

    def search(self, val):
        if self.val == val:
            return self

        if val >= self.val:
            if self.right:
                return self.right.search(val)
            else:
                raise Exception
        else:
            if self.left:
                return self.left.search(val)
            else:
                raise Exception

    def printTree(self, level=0):
        if self.right:
            self.right.printTree(level + 1)
        print(' ' * 4 * level, '-> ', self.val)
        if self.left:
            self.left.printTree(level + 1)

    def _removal_search(self, val, parent=None):
        if self.val == val:
            return self, parent

        if val >= self.val:
            if self.right:
                return self.right._removal_search(val, self)
            else:
                raise Exception
        else:
            if self.left:
                return self.left._removal_search(val, self)
            else:
                raise Exception

    def remove(self, val):
        node_to_remove, parent = self._removal_search(val, None)

        if node_to_remove.left and node_to_remove.right:
            pass
        elif not (node_to_remove.left or node_to_remove.right):
            if parent and parent.left.val == node_to_remove.val:
                parent.left = None
            elif parent and parent.right.val == node_to_remove.val:
                parent.right = None
        else:
            if parent and parent.left.val == node_to_remove.val:
                parent.left = node_to_remove.left or node_to_remove.right
            elif parent and parent.right.val == node_to_remove.val:
                parent.right = node_to_remove.left or node_to_remove.right





bst = BSTNode()
bst.insert(10)
bst.insert(8)
bst.insert(11)
bst.insert(5)
bst.insert(9)
bst.insert(6)
bst.insert(14)
bst.printTree()
# print(bst.search(9).val)
# print(bst.search(20).val)
bst.remove(6)
bst.printTree()
bst.remove(14)
bst.printTree()
bst.remove(9)
bst.printTree()
