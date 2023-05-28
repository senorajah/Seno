import unittest

def divide_numbers(numerator, denominator):
    return numerator / denominator

class DivideNumbersTestCase(unittest.TestCase):
    def test_divide_numbers(self):
        self.assertEqual(divide_numbers(10, 2), 5.0)  # Test case where numerator is divisible by denominator
        self.assertEqual(divide_numbers(7, 3), 2.3333333333333335)  # Test case where numerator is not divisible by denominator
        self.assertEqual(divide_numbers(0, 5), 0.0)  # Test case where numerator is 0
        self.assertEqual(divide_numbers(10, 0), float('inf'))  # Test case where denominator is 0

if __name__ == '__main__':
    unittest.main()
