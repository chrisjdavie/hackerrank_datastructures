
import unittest

from tree_preorder_traversal.tests import Node

from .run import _post_order

class TestPostOrder(unittest.TestCase):

    def test_null(self):

        expected_output = []

        actual_output = _post_order(None, [])

        self.assertSequenceEqual(expected_output, actual_output)


    def test_single_node(self):

        expected_output = [ 1 ]

        head = Node(1)

        actual_output = _post_order(head, [])

        self.assertSequenceEqual(expected_output, actual_output)


    def test_left_depth(self):

        expected_output = [ 1, 2 ]

        head = Node(2)
        head.left = Node(1)

        actual_output = _post_order(head, [])

        self.assertSequenceEqual(expected_output, actual_output)


    def test_right(self):

        expected_output = [ 1, 2 ]

        head = Node(2)
        head.right = Node(1)

        actual_output = _post_order(head, [])

        self.assertSequenceEqual(expected_output, actual_output)


    def test_two_levels(self):

        expected_output = [ 1, 2, 3 ]

        head = Node(3)
        head.right = Node(2)
        head.right.left = Node(1)

        actual_output = _post_order(head, [])

        self.assertSequenceEqual(expected_output, actual_output)

