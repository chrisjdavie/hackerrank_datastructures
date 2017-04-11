
import unittest
from .run import MergeLists

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    @classmethod
    def build_from_list(obj, data):
        
        head = obj(data[0])
        prev_node = head        
        
        for value in data[1:]:
            new_node = obj(value)
            prev_node.next = new_node
            prev_node = new_node

        return head


class TestNulls(unittest.TestCase):

    def test_nulls(self):
        
        headA = None
        headB = None

        head_out = MergeLists(headA, headB)

        self.assertIsNone(head_out)


    def run_from_data_points(self, points_A, points_B, points_expected):

        if points_A is None:
            headA = None
        else:
            headA = Node.build_from_list(points_A)

        if points_B is None:
            headB = None
        else:
            headB = Node.build_from_list(points_B)            

        head_expected = Node.build_from_list(points_expected)

        head_out = MergeLists(headA, headB)

        self.compare_lists(head_out, head_expected)


    def compare_lists(self, head_out, head_expected):

        next_out = head_out
        next_expected = head_expected
        while(next_out and next_expected):
            self.assertEqual(next_out.data, next_expected.data)
            next_out = next_out.next
            next_expected = next_expected.next
        
        self.assertIsNone(next_out)
        self.assertIsNone(next_expected)        


    def test_A_sided(self):

        data_points = [1, 2, 3]
        
        self.run_from_data_points(data_points, None, data_points)


    def test_B_sided(self):

        data_points = [1, 2, 3]
        
        self.run_from_data_points(None, data_points, data_points)


    def test_both_sided(self):

        data_points = [1, 2]
        data_points_expected = [1, 1, 2, 2]
        
        self.run_from_data_points(data_points, data_points, data_points_expected)


    def test_hackerrank_0(self):
        
        points_A = [ 1, 3, 5, 6 ]
        points_B = [ 2, 4, 7 ]

        points_expected = [ 1, 2, 3, 4, 5, 6, 7 ]

        self.run_from_data_points(points_A, points_B, points_expected)        


    def test_hackerrank_1(self):

        points_A = [ 15 ]
        points_B = [ 12 ]

        points_expected = [ 12, 15 ]

        self.run_from_data_points(points_A, points_B, points_expected)        


    def test_hackerrank_2(self):

        points_A = None
        points_B = [ 1, 2 ]

        points_expected = points_B

        self.run_from_data_points(points_A, points_B, points_expected)        

        
        
