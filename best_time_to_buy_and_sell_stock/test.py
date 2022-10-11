import unittest

import code

class Test(unittest.TestCase):
    def test_return_type(self):
        result = code.maxProfit([1, 2, 3, 1])
        self.assertEquals(result, 2)

    def test_two(self):
        result = code.maxProfit([7,1,5,3,6,4])
        self.assertEquals(result, 5)


if __name__ == '__main__':
    unittest.main()