# Define a function to calculate the power of a number with user input
def power_with_user_input():
    """
    Prompt the user to enter the base number and the exponent, 
    then calculate and print the result using the power function.
    """
    base = int(input("Enter the base number: "))  # Prompt the user to enter the base number and convert it to an integer
    exponent = int(input("Enter the exponent: "))  # Prompt the user to enter the exponent and convert it to an integer
    result = 1  # Initialize the result variable with 1
    if exponent > 0:  # Check if the exponent is greater than 0
        result = power(base, exponent)  # If true, calculate the power using the power function
    print("The result is:", result)  # Print the result

# Define a function to calculate the power of a number using recursion
def power(base, exponent):
    """
    Calculate the power of a number using recursion.
    
    Args:
    base: The base number
    exponent: The exponent
    
    Returns:
    The result of the power calculation
    """
    # If the exponent is negative, recursively call the function with the positive exponent
    if exponent < 0:
        return 1 / power(base, -exponent)
    # If the exponent is 0, return 1
    elif exponent == 0:
        return 1
    # Otherwise, calculate the power using recursion
    else:
        return base * power(base, exponent - 1)

# Call the power function with user input
power_with_user_input()
    
# The time complexity of the given power function is O(n), 
# where n is the value of the exponent. 
# This is because the function makes n recursive calls, 
# each reducing the exponent by 1, until the base case is reached (exponent == 0). 
# Therefore, the time it takes to calculate the result is linearly proportional to the value of the exponent.

# step-by-step flow of the power function for power(3, 4) is as follows:

# power(3, 4)
# 3 * power(3, 3)
# 3 * (3 * power(3, 2))
# 3 * (3 * (3 * power(3, 1)))
# 3 * (3 * (3 * (3 * power(3, 0))))
# 3 * (3 * (3 * (3 * 1)))
# 3 * (3 * (3 * 3))
# 3 * (3 * 9)
# 3 * 27
# 81