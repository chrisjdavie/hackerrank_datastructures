import unittest
from .run import left_rotation

class TestRotation(unittest.TestCase):

    def test_singular_list(self):
        
        input = [ 1 ]
        d = 1
        expected_output = [ 1 ]

        output = left_rotation(input, d)

        self.assertSequenceEqual(expected_output, output)


    def test_triple_no_change(self):
        # not technically within specification

        input = [ 1, 2, 3 ]
        d = 0
        expected_output = [ 1, 2, 3 ]

        output = left_rotation(input, d)

        self.assertSequenceEqual(expected_output, output)


    def test_triple_full_rotation(self):

        input = [ 1, 2, 3 ]
        d = 3
        expected_output = [ 1, 2, 3 ]

        output = left_rotation(input, d)

        self.assertSequenceEqual(expected_output, output)


    def test_triple_d_one(self):

        input = [ 1, 2, 3 ]
        d = 1
        expected_output = [ 2, 3, 1 ]

        output = left_rotation(input, d)

        self.assertSequenceEqual(expected_output, output)


    def test_triple_d_four(self):

        input = [ 1, 2, 3 ]
        d = 4
        expected_output = [ 2, 3, 1 ]

        output = left_rotation(input, d)

        self.assertSequenceEqual(expected_output, output)

