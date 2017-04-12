
from .run import has_cycle

from linked_list_testing.node_handling import Node
import unittest

class TestHasCycle(unittest.TestCase):

    def test_null(self):

        output = has_cycle(None)

        self.assertFalse(output)


    def test_no_cycle(self):

        points = [ 1 ]
        head = Node.build_from_list(points)

        output = has_cycle(head)


    def test_cycle(self):

        points = [ 1, 2, 3 ]
        head = Node.build_from_list(points)

        node1 = head.next
        node2 = node1.next
        
        node2.next = node1

        output = has_cycle(head)

        self.assertTrue(output)

