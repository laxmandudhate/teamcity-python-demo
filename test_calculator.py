#!/usr/bin/env python
"""Unit tests for the calculator module."""

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition operation."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-5, 3), -2)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)
    
    def test_subtract(self):
        """Test subtraction operation."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(10.5, 2.5), 8.0)
    
    def test_multiply(self):
        """Test multiplication operation."""
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(-5, 3), -15)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
    
    def test_divide(self):
        """Test division operation."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(15, 3), 5)
        self.assertEqual(self.calc.divide(10, 4), 2.5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
