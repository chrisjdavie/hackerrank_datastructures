
import unittest

from tree_preorder_traversal.tests import Node

from .run import _in_order

class TestInOrder(unittest.TestCase):

    def test_null(self):

        expected_output = []

        actual_output = _in_order(None, [])

        self.assertSequenceEqual(expected_output, actual_output)


    def test_single_node(self):

        expected_output = [ 1 ]

        head = Node(1)

        actual_output = _in_order(head, [])

        self.assertSequenceEqual(expected_output, actual_output)


    def test_left_node(self):

        expected_output = [ 1, 2 ]

        head = Node(2)
        head.left = Node(1)

        actual_output = _in_order(head, [])

        self.assertSequenceEqual(expected_output, actual_output)


    def test_right_node(self):

        expected_output = [ 1, 2 ]

        head = Node(1)
        head.right = Node(2)

        actual_output = _in_order(head, [])

        self.assertSequenceEqual(expected_output, actual_output)


    def test_three_levels(self):

        expected_output = [ 1, 2, 3 ]

        head = Node(1)
        head.right = Node(3)
        head.right.left = Node(2)

        actual_output = _in_order(head, [])

        self.assertSequenceEqual(expected_output, actual_output)


