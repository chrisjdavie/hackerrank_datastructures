
import unittest

from linked_list_testing.node_handling import Node

from .run import FindMergeNode


class TestFindMergeNode(unittest.TestCase):

    def test_symmetric(self):

        points_AB = [ 1 ]
        points_merged = [ 2 ]

        headA = Node.build_from_list(points_AB)
        headB = Node.build_from_list(points_AB)
        tail = Node.build_from_list(points_merged)
        
        headA.next = tail
        headB.next = tail

        merge_value = FindMergeNode(headA, headB)

        self.assertEqual(merge_value, points_merged[0])


    def test_asymmetric(self):

        points_A = [ 1, 2 ]
        points_B = [ 1 ]
        points_merged = [ 3 ]

        headA = Node.build_from_list(points_A)
        headB = Node.build_from_list(points_B)
        tail = Node.build_from_list(points_merged)

        headA.next.next = tail
        headB.next = tail

        merge_value = FindMergeNode(headA, headB)

        self.assertEqual(merge_value, points_merged[0])

