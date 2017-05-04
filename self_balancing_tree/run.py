
from tree_testing.node import Node

class SelfBalanceNode(Node):

    def __init__(self, data):
        
        super().__init__(data)


    def insert(self, new_node):

        self._insert(new_node)
        return self.rebalance()


    def rebalance(self):

        return self._rebalance()[1]


    def _rebalance(self):
        
        replace_current = self
        bf = self._balance_factor() 

        if bf == 2:
            left_bf, replace_left = self.left._rebalance()
            if left_bf == -1:
                self.left_right_case()

            if abs(left_bf) == 1:
                replace_current = self.left_left_case()
            else:
                self.left = replace_left

        if bf == -2:
            right_bf, replace_right = self.right._rebalance()            

            if right_bf == 1:
                self.right_left_case()

            if abs(right_bf) == 1:
                replace_current = self.right_right_case()
            else:
                self.right = replace_right

        return bf, replace_current


    def right_left_case(self):
        # moves the configuration from right left to right right
        # this is then dealt with by right_right_case()

        # preserving the subtrees
        subtree_C = self.right.left.right

        # swapping the nodes
        new_right = self.right.left
        new_right_right = self.right
        self.right = new_right
        self.right.right = new_right_right

        # putting the subtrees back in
        self.right.right.left = subtree_C
        
    
    def right_right_case(self):

        # preserving the subtrees
        subtree_B = self.right.left

        # swapping the nodes
        replace_current = self.right
        replace_current.left = self

        # putting the subtrees back in
        replace_current.left.right = subtree_B

        return replace_current


    def left_right_case(self):
        # moves the configuration from left right to left left
        # this is then dealt with by left_left_case()

        # preserving the subtrees
        subtree_B = self.left.right.left

        # swapping the nodes
        new_left = self.left.right
        new_left_left = self.left
        self.left = new_left
        self.left.left = new_left_left

        # putting the subtrees back in
        self.left.left.right = subtree_B


    def left_left_case(self):

        # preserving the subtrees
        subtree_C = self.left.right

        # swapping the nodes
        replace_current = self.left
        replace_current.right = self

        # putting the subtrees back in
        replace_current.right.left = subtree_C

        return replace_current


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

