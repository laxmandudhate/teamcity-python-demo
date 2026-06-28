"""
Calculator Module
This module provides basic arithmetic operations for the TeamCity CI demo project.
Each function demonstrates a simple operation that can be tested with pytest.
"""


def add(a, b):
    """
    Add two numbers together.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
    
    Returns:
        The sum of a and b
    
    Example:
        >>> add(5, 3)
        8
    """
    return a + b


def subtract(a, b):
    """
    Subtract the second number from the first number.
    
    Args:
        a: First number (int or float)
        b: Second number to subtract (int or float)
    
    Returns:
        The difference of a minus b
    
    Example:
        >>> subtract(10, 4)
        6
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers together.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
    
    Returns:
        The product of a and b
    
    Example:
        >>> multiply(6, 7)
        42
    """
    return a * b


def divide(a, b):
    """
    Divide the first number by the second number.
    
    Args:
        a: Dividend (int or float)
        b: Divisor (int or float) - cannot be zero
    
    Returns:
        The quotient of a divided by b
    
    Raises:
        ValueError: If the divisor (b) is zero
    
    Example:
        >>> divide(20, 4)
        5.0
    """
    if b == 0:
        raise ValueError("Cannot divide by zero! The divisor must not be zero.")
    return a / b