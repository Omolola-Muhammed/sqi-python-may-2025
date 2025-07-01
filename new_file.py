# Write a Python program named `sum_of_two_digits.py` that takes a string as input from the user. The string will consist of exactly two digits (e.g., "23", "98", "09"). Your program should calculate and output the sum of these two digits.

# Example:

# For input "23", the program should output 5 i.e. (2 + 3).
# For input "98", the program should output 17 i.e. (9 + 8).
# For input "09", the program should output 9 i.e. (0 + 9).

# Assume that the input will always be a string made up of
# exactly two digits.

digits = input("Enter a number made up of two digits in figures:")
digit_1 = digits[0]
digit_2 = digits[1]
sum_of_digits = int(digit_1) + int(digit_2)
print(f"The sum of {int(digit_1)} and {int(digit_2)} is {sum_of_digits}")