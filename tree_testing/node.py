
class Node(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def copy(self):
        node_copy = Node(self.data)
        if self.left:
            node_copy.left = self.left.copy()
        if self.right:
            node_copy.right = self.right.copy()
        return node_copy
