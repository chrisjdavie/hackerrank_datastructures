
from .run import GetNode

import unittest
from linked_list_testing.node_handling import Node

class TestRun(unittest.TestCase):

    
    def compare_output(self, data_points, position, expected_value):

        head = Node.build_from_list(data_points)

        value = GetNode(head, position)
        
        self.assertEqual(value, expected_value)

        
    def test_single_value(self):
        
        self.compare_output([ 1 ], 0, 1)


    def test_two_values_0(self):
        
        self.compare_output([ 1, 2 ], 0, 2)


    def test_two_values_1(self):

        self.compare_output([ 1, 2 ], 1, 1)


    def test_hackerrank_0(self):

        self.compare_output([ 1, 3, 5, 6 ], 0, 6)


    def test_hackerrank_1(self):

        self.compare_output([ 1, 3, 5, 6 ], 2, 3)

