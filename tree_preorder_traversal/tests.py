
import unittest

from .run import _pre_order

from tree_testing.node import Node

class TestPreOrder(unittest.TestCase):

    def test_null(self):
        order = _pre_order(None)
        self.assertSequenceEqual([], order)

    
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



