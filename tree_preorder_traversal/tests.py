
import unittest

from .run import _pre_order

class Node(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class TestPreOrder(unittest.TestCase):

    
    def test_single_node(self):
        
        head = Node(1)
        expected_order = [ 1 ]

        order = _pre_order(head)
        self.assertSequenceEqual(expected_order, order)


    def test_left_branch(self):

        head = Node(1)
        head.left = Node(2)
        expected_order = [ 1, 2 ]

        order = _pre_order(head)
        self.assertSequenceEqual(expected_order, order)


    def test_right_branch(self):

        head = Node(1)
        head.right = Node(2)
        expected_order = [ 1, 2 ]
        
        order = _pre_order(head)
        self.assertSequenceEqual(expected_order, order)


    def test_both(self):

        head = Node(1)
        head.left = Node(2)
        head.right = Node(3)
        expected_order = [ 1, 2, 3 ]

        order = _pre_order(head)
        self.assertSequenceEqual(expected_order, order)


    def test_left_depth(self):
        
        head = Node(1)
        head.left = Node(2)
        head.left.left = Node(3)
        expected_order = [ 1, 2, 3 ]

        order = _pre_order(head)
        self.assertSequenceEqual(expected_order, order)


    def test_left_depth_then_right(self):
        
        head = Node(1)
        head.left = Node(2)
        head.left.left = Node(3)
        head.right = Node(4)
        expected_order = [ 1, 2, 3, 4 ]

        order = _pre_order(head)
        self.assertSequenceEqual(expected_order, order)

        
    def test_depth_with_right(self):
        
        head = Node(1)
        head.right = Node(2)
        head.right.left = Node(3)
        head.right.left.right = Node(4)
        expected_order = [ 1, 2, 3, 4 ]

        order = _pre_order(head)
        self.assertSequenceEqual(expected_order, order)



