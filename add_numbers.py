from typing import Union

def add_two_numbers(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    """
    Adds two numbers and returns their sum.

    This function is designed to be flexible, accepting both integers and
    floating-point numbers as input and returning their sum.

    Args:
        num1 (Union[int, float]): The first number to be added.
        num2 (Union[int, float]): The second number to be added.

    Returns:
        Union[int, float]: The sum of the two input numbers.
                          The return type will match the type of the inputs
                          or be a float if one input is a float.
    """
    return num1 + num2

if __name__ == "__main__":
    # Example usage of the add_two_numbers function

    # Case 1: Adding two integers
    number1_int = 5
    number2_int = 10
    sum_int = add_two_numbers(number1_int, number2_int)
    print(f"The sum of {number1_int} and {number2_int} is: {sum_int}") # Expected: 15

    # Case 2: Adding two floating-point numbers
    number1_float = 3.5
    number2_float = 2.7
    sum_float = add_two_numbers(number1_float, number2_float)
    print(f"The sum of {number1_float} and {number2_float} is: {sum_float}") # Expected: 6.2

    # Case 3: Adding an integer and a floating-point number
    number1_mixed_int = 7
    number2_mixed_float = 2.5
    sum_mixed = add_two_numbers(number1_mixed_int, number2_mixed_float)
    print(f"The sum of {number1_mixed_int} and {number2_mixed_float} is: {sum_mixed}") # Expected: 9.5

    # Case 4: Adding negative numbers
    number1_negative = -8
    number2_negative = -3
    sum_negative = add_two_numbers(number1_negative, number2_negative)
    print(f"The sum of {number1_negative} and {number2_negative} is: {sum_negative}") # Expected: -11

    # Case 5: Adding zero
    number1_zero = 0
    number2_positive = 15
    sum_zero = add_two_numbers(number1_zero, number2_positive)
    print(f"The sum of {number1_zero} and {number2_positive} is: {sum_zero}") # Expected: 15
<ctrl63>