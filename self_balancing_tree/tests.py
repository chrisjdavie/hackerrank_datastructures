
import unittest

from .run import rebalance
from .run import SelfBalanceNode as Node


class Test_BalanceFactor(unittest.TestCase):
    # the tree is self balancing - in principle, the balance factor should
    # never be greater than |2|. If it is, then I'm not sure what the 
    # algorithm will do

    def test_single_node(self):

        head = Node(1)
        bf = head._balance_factor()

        self.assertEqual(bf, 0) 


    def test_left(self):

        head = Node(1)
        head.left = Node(0)
        bf = head._balance_factor()

        self.assertEqual(bf, 1)


    def test_right(self):

        head = Node(1)
        head.right = Node(2)
        bf = head._balance_factor()

        self.assertEqual(bf, -1)


    def test_right_left(self):
        
        head = Node(2)
        head.left = Node(1)
        head.right = Node(3)
        bf = head._balance_factor()

        self.assertEqual(bf, 0)


    def test_two_levels(self):

        head = Node(1)
        head.right = Node(3)
        head.right.left = Node(2)

        bf = head._balance_factor()

        self.assertEqual(bf, -2)


class Test_MaxHeight(unittest.TestCase):

    def test_single_node(self):

        head = Node(1)
        max_height = head._max_height(-1)

        self.assertEqual(max_height, 0) 


    def test_left(self):

        head = Node(1)
        head.left = Node(0)
        max_height = head._max_height(-1)

        self.assertEqual(max_height, 1)


    def test_right(self):

        head = Node(1)
        head.right = Node(2)
        max_height = head._max_height(-1)

        self.assertEqual(max_height, 1)


    def test_two_levels(self):

        head = Node(1)
        head.left = Node(-1)
        head.left.right = Node(0)
        max_height = head._max_height(-1)

        self.assertEqual(max_height, 2)


class TreeTesting(unittest.TestCase):


    def assert_trees_equal(self, node_a, node_b):
        if not node_a and not node_b:
            return        
        node_exists_msg = "node exists in one tree and not the other"
        if (not node_a and node_b):
            self.fail( node_exists_msg + ". RHS node data: " + str(node_b.data) )
        if (not node_b and node_a):
            self.fail( node_exists_msg + ". LHS node data: " + str(node_a.data) )
        
        self.assertEqual(node_a.data, node_b.data)
        self.assert_trees_equal(node_a.left, node_b.left)
        self.assert_trees_equal(node_a.right, node_b.right)


class Test_Insert(TreeTesting):

    def test_left(self):
        
        head = Node(5)
        new_node = Node(3)
        head._insert(new_node)

        expected_head = Node(5)
        expected_head.left = Node(3)

        self.assert_trees_equal(head, expected_head)


    def test_right(self):

        head = Node(5)
        new_node = Node(7)
        head._insert(new_node)

        expected_head = Node(5)
        expected_head.right = Node(7)

        self.assert_trees_equal(head, expected_head)


    def test_left_right(self):

        head = Node(5)
        head._insert(Node(3))
        head._insert(Node(4))

        expected_head = Node(5)
        expected_head.left = Node(3)
        expected_head.left.right = Node(4)

        self.assert_trees_equal(head, expected_head)


    def test_right_left(self):

        head = Node(5)
        head._insert(Node(7))
        head._insert(Node(6))

        expected_head = Node(5)
        expected_head.right = Node(7)
        expected_head.right.left = Node(6)

        self.assert_trees_equal(head, expected_head)
        
        


class TestRebalance(TreeTesting):

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

        rebalanced_head = rebalance(head)

        self.assert_trees_equal(expected_head, rebalanced_head)


    def test_left_right(self):

        head = Node(5)
        head.left = Node(3)
        head.right = Node(4)

        expected_head = Node(4)
        expected_head.left = Node(3)
        expected_head.right = Node(5)

        rebalanced_head = rebalance(head)

        self.assert_trees_equal(expected_head, rebalanced_head)


    def test_right_right(self):

        head = Node(3)
        head.right = Node(4)
        head.right.right = Node(5)

        expected_head = Node(4)
        expected_head.left = Node(3)
        expected_head.right = Node(5)

        rebalanced_head = rebalance(head)

        self.assert_trees_equal(expected_head, rebalanced_head)


    def test_right_left(self):

        head = Node(3)
        head.right = Node(5)
        head.right.right = Node(4)

        expected_head = Node(4)
        expected_head.left = Node(3)
        expected_head.right = Node(4)

        rebalanced_head = rebalance(head)

        self.assert_trees_equal(expected_head, rebalanced_head)

        
