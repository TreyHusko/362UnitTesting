import unittest
import calc

class testCaseAdd(unittest.TestCase):
    def test_sum(self):
        result = calc.sum(5,10.5)
        self.assertEqual(result, 15.5)
    def test_sum2(self):
        result = calc.sum(5,5)
        self.assertEqual(result, 11)

class testCaseSub(unittest.TestCase):
    def test_diff(self):
        result = calc.diff(5,10)
        self.assertEqual(result, -5)
    def test_diff2(self):
        result = calc.diff(10, 5)
        self.assertEqual(result, 6)

class testCaseMult(unittest.TestCase):
    def test_multiply(self):
        result = calc.diff(5,10)
        self.assertEqual(result, -5)
    def test_multiply2(self):
        self.assertRaises(TypeError, calc.multiply, 1, 'two')

class testCaseDiv(unittest.TestCase):
    def test_divide(self):
        result = calc.diff(5,10)
        self.assertEqual(result, -5)
    def test_divide2(self):
        self.assertRaises(ZeroDivisionError, calc.divide, 5, 0)
        
if __name__ == "__main__":
    unittest.main()
