
import unittest

from .run import check_binary_search_tree_

from tree_testing.node import Node

class TestCheckBinarySearchTree(unittest.TestCase):

    def test_singe_node(self):
        
        head = Node(1)
        eval = check_binary_search_tree_(head)
        self.assertIs(True, eval)


    def test_valid_LHS(self):

        head = Node(2)
        head.left = Node(1)
        eval = check_binary_search_tree_(head)
        self.assertIs(True, eval)


    def test_invalid_LHS(self):

        head = Node(1)
        head.left = Node(2)
        eval = check_binary_search_tree_(head)
        self.assertIs(False, eval)


    def test_valid_RHS(self):

        head = Node(1)
        head.right = Node(2)
        eval = check_binary_search_tree_(head)
        self.assertIs(True, eval)


    def test_invalid_RHS(self):

        head = Node(2)
        head.right = Node(1)
        eval = check_binary_search_tree_(head)
        self.assertIs(False, eval)


    def test_left_and_right_valid(self):

        head = Node(2)
        head.left = Node(1)
        head.right = Node(3)
        eval = check_binary_search_tree_(head)
        self.assertIs(True, eval)


    def test_left_and_right_not_valid(self):

        head = Node(3)
        head.left = Node(1)
        head.right = Node(2)
        eval = check_binary_search_tree_(head)
        self.assertIs(False, eval)


    def test_one_level_down_valid(self):

        head = Node(2)
        head.right = Node(4)
        head.right.left = Node(3)
        eval = check_binary_search_tree_(head)
        self.assertIs(True, eval)
        

    def test_one_level_down_invalid_lower_bound(self):
        
        # is invalid due to the head, not due to the parent

        head = Node(2)
        head.right = Node(4)
        head.right.left = Node(1)
        eval = check_binary_search_tree_(head)
        self.assertIs(False, eval)


    def test_one_level_down_invalid_upper_bound(self):

        # is invalid due to the head, not due to the parent

        head = Node(3)
        head.left = Node(1)
        head.left.right = Node(4)
        eval = check_binary_search_tree_(head)
        self.assertIs(False, eval)

