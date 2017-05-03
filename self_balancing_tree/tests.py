
import unittest

from tree_testing.node import Node

from .run import rebalance

class TestRebalance(self):


    def assert_trees_equal(self, node_a, node_b):
        if not node_a and not node_b:
            return        
        if (not node_a and node_b) or (not node_b and node_a):
            self.fail("node exists in one tree and not the other")
        
        self.assertEqual(node_a.data, node_b.data)
        self.assert_trees_equal(node_a.left, node_b.right)
        self.assert_trees_equal(node_a.right, node_b.right)


    def test_single_node(self):
        
        head = Node(5)
        expected_head = head.copy()

        rebalanced_head = rebalance(head)

        self.assert_trees_equal(expected_head, rebalanced_head)


    def test_left_node(self):

        head = Node(5)
        head.left = Node(4)

        expected_head = head.copy()

        rebalanced_head = rebalance(head)

        self.assert_trees_equal(expected_head, rebalanced_head)


    def test_right_node(self):

        head = Node(5)
        head.right = Node(6)

        expected_head = head.copy()

        rebalanced_head = rebalance(head)

        self.assert_trees_equal(expected_head, rebalanced_head)


    def test_balanced_left_right(self):

        head = Node(5)
        head.left = Node(4)
        head.right = Node(6)

        expected_head = head.copy()

        rebalanced_head = rebalance(head)

        self.assert_trees_equal(expected_head, rebalanced_head)


    def test_left_left(self):

        head = Node(5)
        head.left = Node(4)
        head.left.left = Node(3)

        expected_head = Node(4)
        expected_head.left = Node(3)
        expected_head.right = Node(5)

        self.assert_trees_equal(expected_head, rebalanced_head)


    def test_left_right(self):

        head = Node(5)
        head.left = Node(3)
        head.right = Node(4)

        expected_head = Node(4)
        expected_head.left = Node(3)
        expected_head.right = Node(5)

        self.assert_trees_equal(expected_head, rebalanced_head)


    def test_right_right(self):

        head = Node(3)
        head.right = Node(4)
        head.right.right = Node(5)

        expected_head = Node(4)
        expected_head.left = Node(3)
        expected_head.right = Node(5)

        self.assert_trees_equal(expected_head, rebalanced_head)


    def test_right_left(self):

        head = Node(3)
        head.right = Node(5)
        head.right.right = Node(4)

        expected_head = Node(4)
        expected_head.left = Node(3)
        expected_head.right = Node(4)

        self.assert_trees_equal(expected_head, rebalanced_head)

        
