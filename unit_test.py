import unittest

class TestPowerFunctions(unittest.TestCase):
    """Test case class for testing power functions"""

    def test_power_positive_exponent(self):
        """Test case for calculating power with positive exponents"""
        print("Testing power function with base 2 and exponent 3")
        self.assertEqual(power(2, 3), 8)  # Test power function with base 2 and exponent 3
        print("Testing power function with base 5 and exponent 2")
        self.assertEqual(power(5, 2), 25)  # Test power function with base 5 and exponent 2
    
    def test_power_negative_exponent(self):
        """Test case for calculating power with negative exponents"""
        print("Testing power function with base 3 and exponent -2")
        self.assertEqual(power(3, -2), 1/9)  # Test power function with base 3 and exponent -2
        print("Testing power function with base 4 and exponent -3")
        self.assertEqual(power(4, -3), 1/64)  # Test power function with base 4 and exponent -3
    
    def test_power_zero_exponent(self):
        """Test case for calculating power with zero exponents"""
        print("Testing power function with base 10 and exponent 0")
        self.assertEqual(power(10, 0), 1)  # Test power function with base 10 and exponent 0
        print("Testing power function with base 7 and exponent 0")
        self.assertEqual(power(7, 0), 1)  # Test power function with base 7 and exponent 0

if __name__ == '__main__':
    unittest.main()