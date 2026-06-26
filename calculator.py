#!/usr/bin/env python
"""Calculator module for basic mathematical operations."""


class Calculator:
    """A simple calculator class for performing basic operations."""
    
    @staticmethod
    def add(a, b):
        """Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """Subtract two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Difference of a and b
        """
        return a - b
    
    @staticmethod
    def multiply(a, b):
        """Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Product of a and b
        """
        return a * b
    
    @staticmethod
    def divide(a, b):
        """Divide two numbers.
        
        Args:
            a: Dividend
            b: Divisor
            
        Returns:
            Result of a divided by b
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
