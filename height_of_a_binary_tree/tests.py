
import unittest

from .run import height

class Node:

    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


class TestHeight(unittest.TestCase):

    def test_zero_height(self):
        
        expected_height = 0
        
        root = Node(1)

        actual_height = height(root)

        self.assertEqual(expected_height, actual_height)


    def test_left_height_one(self):

        expected_height = 1

        root = Node(2)
        root.left = Node(1)

        actual_height = height(root)

        self.assertEqual(expected_height, actual_height)


    def test_right_height_one(self):

        expected_height = 1

        root = Node(1)
        root.right = Node(2)

        actual_height = height(root)

        self.assertEqual(expected_height, actual_height)


    def test_height_two_mixed(self):

        expected_height = 2

        root = Node(2)
        root.left = Node(1)
        root.right = Node(4)
        root.right.left = Node(3)

        actual_height = height(root)

        self.assertEqual(expected_height, actual_height)


