
import unittest
from linked_list_testing.node_handling import Node, TestLinkedLists

from .run import RemoveDuplicates

class TestRemoveDuplicates(TestLinkedLists):


    def test_null(self):
        
        nodes_input = None
        nodes_output = RemoveDuplicates(nodes_input)

        self.assertIsNone(nodes_output)


    def run_from_data_points(self, points_in, points_expected):

        nodes_in = Node.build_from_list(points_in)
        nodes_expected = Node.build_from_list(points_expected)

        nodes_out = RemoveDuplicates(nodes_in)
        
        self.compare_lists(nodes_out, nodes_expected)        


    def test_no_change(self):

        data_points = [ 1, 2, 3 ]
        
        self.run_from_data_points(data_points, data_points)


    def test_single_value_duplicated(self):

        points = [ 1, 1 ]
        points_expected = [ 1 ]

        self.run_from_data_points(points, points_expected)


    def test_single_value_not_first(self):

        points = [ 1, 2, 2 ]
        points_expected = [ 1, 2 ]

        self.run_from_data_points(points, points_expected)


    def test_multiple_duplicates(self):

        points = [ 1, 1, 2, 2 ]
        points_expected = [ 1, 2 ]

        self.run_from_data_points(points, points_expected)


    def test_hackerrank_0(self):

        points = [ 1, 1, 3, 3, 5, 6 ]
        points_expected = [ 1, 3, 5, 6 ]

        self.run_from_data_points(points, points_expected)

