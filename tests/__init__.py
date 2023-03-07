#!/usr/bin/python3
import unittest



class Test(unittest.TestCase):
    def test_sum(self):
        sum = lambda n1,n2:n1+n2
        self.assertEqual(sum(2,2), 4, "2+2=4")

if __name__ == '__main__':
    unittest.main()
