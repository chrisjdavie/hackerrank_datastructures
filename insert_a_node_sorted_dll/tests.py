
import unittest

from linked_list_testing.node_handling import TestLinkedLists
from .run import SortedInsert, Node


class TestSortedInsert(TestLinkedLists):

    def test_null(self):
        
        head_in = None
        data_insert = 2

        expected_points = [ 2 ]
        expected_out = Node.build_from_list(expected_points)
        
        actual_out = SortedInsert(head_in, data_insert)

        self.compare_lists(expected_out, actual_out)

    
    def compare_results(self, data_in, list_in, expected_points):

        head_in = Node.build_from_list(list_in)

        expected_out = Node.build_from_list(expected_points)

        actual_out = SortedInsert(head_in, data_in)

        self.compare_lists(expected_out, actual_out)
         

    def test_insert_last(self):

        data_in = 2
        list_in = [ 1 ]
        expected_points = [ 1, 2 ]

        self.compare_results(data_in, list_in, expected_points)


    def test_insert_first(self):

        data_in = 1
        list_in = [ 2 ]
        expected_points = [ 1, 2 ]

        self.compare_results(data_in, list_in, expected_points)


    def test_insert_middle(self):

        data_in = 2
        list_in = [ 1, 3 ]
        expected_points = [ 1, 2, 3 ]

        self.compare_results(data_in, list_in, expected_points)


    def test_duplicate_insert(self):

        data_in = 1
        list_in = [ 1 ]
        expected_points = [ 1, 1 ]

        self.compare_results(data_in, list_in, expected_points)

