# with open("oop.py", "r") as f:
#     contents = f.read()
# print(contents)

# with open("python-website.html", "a") as f:
#     f.write(f"We found ourselves here now")

# with open("new_file.txt", "r") as f:
#     # f.read()
#     contents = f.read()

# for line in enumerate(contents):
#     print(f"line + {contents}")

########### ASSIGNMENT ################
# 1. Define a custom exception called NegativeNumberError.
# Write a function check_positive(number) that raises 
# NegativeNumberError if the input number is negative.
# Catch the exception when calling the function.


# class NegativeNumberError(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)



# def check_positive(number):
#     while True:
#         try:
#             num = int(input("Enter a number: "))
#         except ValueError:
#             print("Enter a number")
#         else:
#             if num < 1:
#                 raise NegativeNumberError("Negative numbers are not allowed")
#             print("Enter a positive number")
#             break


# try:
#     check_positive("number")
# except NegativeNumberError as e:
#     print(f"Negative number entered: {e}")

# 2. Handle Multiple Exceptions:
# Write a function safe_divide(a, b) that performs division.
# Handle ZeroDivisionError if the divisor is zero.
# Handle TypeError if the inputs are not numbers.
# Handle ValueError if the inputs are not convertible to floats.


# def safe_divide(a, b):
#     while True:
#         try:
#             float(a) / float(b)
#         except ZeroDivisionError as e:
#             print(f"Cannot divide by zero: {e}")
#         except TypeError as e:
#             print(f"num1 and num2 must be numbers: {e}")
#         except ValueError as e:
#             print(f"num1 and num2 must be numbers: {e}")
    

# print(safe_divide(4, 2))
    

# with open("inputass.py", "r") as f:
#     contents = f.read()
# print(contents)

# with open("listass.py", "w") as f:
#     f.write("I am just annoyed this morning")
    


import string