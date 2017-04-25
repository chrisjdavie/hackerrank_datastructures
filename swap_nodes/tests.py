
import unittest

from .run import Node, swap_node


class TestNode(unittest.TestCase):

    def test_init_only_data(self):

        data = 1
        a_node = Node(data)

        self.assertIsNone(a_node.left)
        self.assertIsNone(a_node.right)


    def test_init_left_right(self):

        data = 1
        left = "left"
        right = "right"
        a_node = Node(data, left, right)

        self.assertEqual(a_node.left, left)
        self.assertEqual(a_node.right, right)


class TestSwapNode(unittest.TestCase):

    def compare_trees(self, expected_node, actual_node):

        if not expected_node:
            self.assertIsNone(expected_node)
            self.assertIsNone(actual_node)
        else:
            self.assertEqual(expected_node.data, actual_node.data)
            self.compare_trees(expected_node.left, actual_node.left)
            self.compare_trees(expected_node.right, actual_node.right)


    def test_no_change(self):

        head = Node(1)
        head.left = Node(2)
        head.right = Node(3)

        expected_head = Node(1)
        expected_head.left = Node(2)
        expected_head.right = Node(3)

        swap_node(head, 2, 0)

        self.compare_trees(expected_head, head)


    def test_one_level_swap(self):

        head = Node(1)
        head.left = Node(2)
        head.right = Node(3)

        expected_head = Node(1)
        expected_head.left = Node(3)
        expected_head.right = Node(2)

        swap_node(head, 1, 0)

        self.compare_trees(expected_head, head)


    def test_multiple_level_swap(self):

        head = Node(1)
        head.left = Node(2)
        head.left.left = Node(3)
        head.left.left.left = Node(4)
        head.left.left.left.left = Node(5)

        expected_head = Node(1)
        expected_head.left = Node(2)
        expected_head.left.right = Node(3)
        expected_head.left.right.left = Node(4)
        expected_head.left.right.left.right = Node(5)

        swap_node(head, 2, 0)

        self.compare_trees(expected_head, head)

        


