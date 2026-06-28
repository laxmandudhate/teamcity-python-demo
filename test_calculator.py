"""
Unit Tests for Calculator Module
This module contains comprehensive test cases for all calculator functions.
Uses pytest framework for testing.
Tests include both valid and invalid test cases.
"""

import pytest
from calculator import add, subtract, multiply, divide


class TestAddition:
    """Test cases for the add function."""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(5, 3) == 8
    
    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        assert add(-5, -3) == -8
    
    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        assert add(10, -4) == 6
    
    def test_add_with_zero(self):
        """Test adding zero to a number."""
        assert add(5, 0) == 5
    
    def test_add_floats(self):
        """Test adding floating point numbers."""
        assert add(2.5, 3.7) == pytest.approx(6.2)


class TestSubtraction:
    """Test cases for the subtract function."""
    
    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers."""
        assert subtract(10, 4) == 6
    
    def test_subtract_negative_numbers(self):
        """Test subtracting two negative numbers."""
        assert subtract(-5, -3) == -2
    
    def test_subtract_mixed_numbers(self):
        """Test subtracting positive and negative numbers."""
        assert subtract(10, -5) == 15
    
    def test_subtract_with_zero(self):
        """Test subtracting zero from a number."""
        assert subtract(5, 0) == 5
    
    def test_subtract_floats(self):
        """Test subtracting floating point numbers."""
        assert subtract(10.5, 3.2) == pytest.approx(7.3)


class TestMultiplication:
    """Test cases for the multiply function."""
    
    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        assert multiply(6, 7) == 42
    
    def test_multiply_negative_numbers(self):
        """Test multiplying two negative numbers."""
        assert multiply(-5, -4) == 20
    
    def test_multiply_mixed_numbers(self):
        """Test multiplying positive and negative numbers."""
        assert multiply(5, -3) == -15
    
    def test_multiply_with_zero(self):
        """Test multiplying any number by zero."""
        assert multiply(10, 0) == 0
    
    def test_multiply_with_one(self):
        """Test multiplying any number by one."""
        assert multiply(7, 1) == 7
    
    def test_multiply_floats(self):
        """Test multiplying floating point numbers."""
        assert multiply(2.5, 4.0) == 10.0


class TestDivision:
    """Test cases for the divide function."""
    
    def test_divide_positive_numbers(self):
        """Test dividing two positive numbers."""
        assert divide(20, 4) == 5.0
    
    def test_divide_negative_numbers(self):
        """Test dividing two negative numbers."""
        assert divide(-20, -4) == 5.0
    
    def test_divide_mixed_numbers(self):
        """Test dividing positive and negative numbers."""
        assert divide(20, -4) == -5.0
    
    def test_divide_with_one(self):
        """Test dividing a number by one."""
        assert divide(10, 1) == 10.0
    
    def test_divide_floats(self):
        """Test dividing floating point numbers."""
        assert divide(10.0, 2.5) == pytest.approx(4.0)
    
    def test_divide_by_zero(self):
        """Test that dividing by zero raises a ValueError."""
        with pytest.raises(ValueError):
            divide(10, 0)
    
    def test_divide_by_zero_error_message(self):
        """Test that the error message is correct for division by zero."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)
    
    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        assert divide(0, 5) == 0.0


# Additional edge case tests
class TestEdgeCases:
    """Test edge cases and boundary conditions."""
    
    def test_large_numbers(self):
        """Test operations with large numbers."""
        assert add(1000000, 2000000) == 3000000
    
    def test_very_small_floats(self):
        """Test operations with very small floating point numbers."""
        result = add(0.0001, 0.0002)
        assert result == pytest.approx(0.0003)
    
    def test_division_result_is_float(self):
        """Ensure division always returns a float."""
        result = divide(10, 2)
        assert isinstance(result, float)
        assert result == 5.0