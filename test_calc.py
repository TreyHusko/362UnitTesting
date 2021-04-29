import unittest
import calc

class testCaseAdd(unittest.TestCase):
    def test_sum(self):
        result = calc.sum(5,10.5)
        self.assertEqual(result, 15.5)
    def test_sum2(self):
        result = calc.sum(5,5)
        self.assertEqual(result, 11)
if __name__ == "__main__":
    unittest.main()
