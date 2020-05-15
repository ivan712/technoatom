from run import *
import unittest
from unittest.mock import patch

class testfoo(unittest.TestCase):
    def test_block(self):
        self.assertEqual(block([1,2,3]),6)
        self.assertEqual(block([1,3]),3)
        self.assertEqual(block([2,3]),6)
        self.assertEqual(block([1,2,3,4]),24)
        self.assertEqual(block([1,2,3,3,2,1,1,1,1]),36)
        self.assertEqual(block([1,2,3,1,2,33,0]),0)


    def test_foo(self):
        self.assertEqual(foo([1,2,3]),[6,3,2])
        self.assertEqual(foo([0,1,2,0]),[0,0,0,0])
        self.assertEqual(foo([0,1,2,0]),[0,0,0,0])

    @patch('run.foo', return_value=[9,1,1])
    def test_mock_foo(self,foo):
        self.assertEqual(foo([1,2,3]),[9,1,1,])

    @patch('run.foo', return_value=[])
    def test_mock_foo(self,foo):
        self.assertEqual(foo([1,2,3]),[])


if __name__ == '__main__':
    unittest.main()
