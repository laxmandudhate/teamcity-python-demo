"""
Main Application Module
This is the main entry point for the TeamCity CI demo project.
It demonstrates how to use all the functions from the calculator module.
"""

# Import all functions from the calculator module
from calculator import add, subtract, multiply, divide


def main():
    """
    Main function that demonstrates all calculator operations.
    This function calls each operation with sample values and prints results.
    """
    
    # Print a welcome message
    print("=" * 50)
    print("Welcome to the TeamCity Python Demo Calculator!")
    print("=" * 50)
    print()
    
    # Define sample values for our calculations
    num1 = 20
    num2 = 5
    
    print(f"Using sample values: num1 = {num1}, num2 = {num2}")
    print()
    
    # Test Addition
    print("--- Addition Operation ---")
    result_add = add(num1, num2)
    print(f"add({num1}, {num2}) = {result_add}")
    print()
    
    # Test Subtraction
    print("--- Subtraction Operation ---")
    result_subtract = subtract(num1, num2)
    print(f"subtract({num1}, {num2}) = {result_subtract}")
    print()
    
    # Test Multiplication
    print("--- Multiplication Operation ---")
    result_multiply = multiply(num1, num2)
    print(f"multiply({num1}, {num2}) = {result_multiply}")
    print()
    
    # Test Division
    print("--- Division Operation ---")
    result_divide = divide(num1, num2)
    print(f"divide({num1}, {num2}) = {result_divide}")
    print()
    
    # Summary of results
    print("=" * 50)
    print("Summary of Results:")
    print("=" * 50)
    print(f"Addition:       {num1} + {num2} = {result_add}")
    print(f"Subtraction:    {num1} - {num2} = {result_subtract}")
    print(f"Multiplication: {num1} × {num2} = {result_multiply}")
    print(f"Division:       {num1} ÷ {num2} = {result_divide}")
    print("=" * 50)
    print()
    
    # Additional test case - Division by zero error handling
    print("--- Error Handling Example ---")
    print("Attempting to divide by zero...")
    try:
        invalid_result = divide(10, 0)
    except ValueError as e:
        print(f"Error caught: {e}")
    
    print()
    print("Application completed successfully!")


# This ensures the main function only runs when the script is executed directly
# and not when it's imported as a module in another script
if __name__ == "__main__":
    main()