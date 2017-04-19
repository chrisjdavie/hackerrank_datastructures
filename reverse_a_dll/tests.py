
from linked_list_testing.node_handling import TestLinkedLists
from linked_list_testing.double_node import Node

from .run import Reverse

class TestReverse(TestLinkedLists):

    def test_null(self):

        head_in = None
        
        head_out = Reverse(head_in)

        self.assertIsNone(head_out)


    def test_symmetric(self):

        data_points = [ 1 ]
        head_in = Node.build_from_list(data_points)

        head_out = Reverse(head_in)

        self.compare_lists(head_in, head_out)


    def test_reversed(self):

        data_points = [ 1, 2 ]
        head_in = Node.build_from_list(data_points)

        expected_out = Node.build_from_list(data_points[::-1])
        head_out = Reverse(head_in)

        self.compare_lists(expected_out, head_out)


    def test_duplicates(self):
        
        data_points = [ 1, 1 ]
        head_in = Node.build_from_list(data_points)

        expected_out = Node.build_from_list(data_points)
        head_out = Reverse(head_in)

        self.compare_lists(expected_out, head_out)

