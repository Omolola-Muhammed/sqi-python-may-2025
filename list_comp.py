# result = []
# my_list = ["drink", "food", "sleep", "read"]
# for word in my_list:
#     result.append(word.upper())
# print(result)

# animals = ["Hyena", "Zebra", "Ape", "Lion", "Elephant", "Cheetah", "Tiger"]
# numbers_of_letterE = [str(char.count("e")) for char in animals]
# print(numbers_of_letterE)

# states = ["Oyo", "Ogun", "Lagos", "Osun", "Anambra"]
# states_starting_with_o = [state.lower() for state in states if state.lower().startswith("o")]
# print(states_starting_with_o)

# states = ["Oyo", "Ogun", "Lagos", "Osun", "Anambra"]
# states_starting_with_o = [state for state in states if state.startswith("O") or state.startswith("A")]
# print(states_starting_with_o)

# nums = [32, 30, 45, 15, 12, 43]
# num_not_multiples_of_5 = [num for num in nums if num % 5 != 0]
# print(num_not_multiples_of_5)

# states = ["Oyo", "Ogun", "Lagos", "Osun", "Anambra"]
# states_starting_with_o = [state for state in states if state[0] != "L"]
# print(states_starting_with_o)

# numbers = [3, 23, 45, 67, 23, 1]
# all_odd = all(num % 2 != 0 for num in numbers)
# print(all_odd)


######################## ASSIGNMENT #####################
#  15. 	Use a list comprehension to create a list of numbers between 1 and 50 that are divisible
# 	by 3.

# numbers_divisible_by3 = [num for num in range(1, 51) if num % 3 == 0]
# print(numbers_divisible_by3)

# Scenario: You need to check if a user's password is strong enough.

# Task: Write a program in a file named `password_strength_checker.py` that takes a string called `password` and prints `True` if the password is strong and `False` otherwise. A strong password:

# Is at least 8 characters long.
# Contains both uppercase and lowercase characters.
# Contains at least one digit.
# Contains at least one special character (e.g., !@#$%^&*()).

# Tip: Check for True or False for each condition of a strong password and chain the boolean results of each of them. If they are all True, the boolean chaining will result to True and result to False if there is at least one False.

# DO NOT USE REGEX.


password = "p@sswoRd2"
at_least_8_chars = len(password) >= 8

has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isnumeric() for char in password)
has_special_char = any(char for char in password if char in "!@#$%^&*()")

print(all([at_least_8_chars, has_upper, has_lower, has_digit, has_special_char]))
print(at_least_8_chars and has_upper and has_lower and has_digit and has_special_char)