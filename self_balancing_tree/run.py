
from tree_testing.node import Node

class SelfBalanceNode(Node):

    def __init__(self, data):
        
        super().__init__(data)


    def _insert(self, new_node):
        
        if new_node.data < self.data:
            if self.left:
                self.left._insert(new_node)
            else:
                self.left = new_node

        if new_node.data > self.data:
            if self.right:
                self.right._insert(new_node)
            else:
                self.right = new_node


    def _max_height(self, prev_height):
        # potential optimization: memoize if nothing new is inserted

        height = prev_height + 1
        left_height = height
        right_height = height

        if self.left:
            left_height = self.left._max_height(height)
        if self.right:
            right_height = self.right._max_height(height)

        return max([height, left_height, right_height])


    def _balance_factor(self):

        left_height = 0
        right_height = 0

        if self.left:
            left_height = self.left._max_height(0)
        if self.right:
            right_height = self.right._max_height(0)

        return left_height - right_height


def rebalance(head):
    return -1
