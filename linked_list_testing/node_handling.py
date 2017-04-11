
import unittest

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


class TestLinkedLists(unittest.TestCase):

    def compare_lists(self, head_out, head_expected):

        next_out = head_out
        next_expected = head_expected
        while(next_out and next_expected):
            self.assertEqual(next_out.data, next_expected.data)
            next_out = next_out.next
            next_expected = next_expected.next
        
        self.assertIsNone(next_out)
        self.assertIsNone(next_expected)        

