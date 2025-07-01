# def raise_to_power(base, exponent):
#     print(f"{base} ** {exponent} = {base**exponent}")

# raise_to_power(3, 3)

# def multiply_nums(num1, num2):
#     return num1 * num2


# print(multiply_nums(3, 5))

# def square_num(num):
#     return num * num
# print(square_num(3))

# def is_even(num):
#     if num % 2 != 0:
#         return False
#     return True
# print(is_even(5))

# def uppercase_all_names(*names):
#     return [name.upper() for name in names]

# print(uppercase_all_names("Omolola", "Molayo", "Lekan", "Awwal"))


# def filter_out_nums_less_than_50(*nums):
#     nums_greater_than_50 = [num for num in nums if num > 50]
#     return tuple(nums_greater_than_50)

# print(filter_out_nums_less_than_50(45, 89, 12, 43, 90))

# def is_alliteration(two_word_string):
#     # return [word for word in two_word_string if two_word_string.startswith() == two_word_string.startswith()]
#     # return False
# print(is_alliteration())

# def is_alliteration(two_word_string):
#     two_word = input("Enter a two-word string").split()
# print(is_alliteration())

################### ASSIGNMENT ###################
#1. Write a function sum_numbers(a, b) that returns the sum of two numbers.
# def sum_numbers(a, b):
#     print(f"{a} + {b} = {a+b}")

# sum_numbers(3, 3)

#2. Write a function is_even(n) that returns True if n is even and False if n is odd.
# def is_even(n):
#     return n % 2 == 0
# print(is_even(5))
#3. Write a function is_prime(n) that returns True if n is a prime number and False otherwise.
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# print(is_prime(6))
#4. Using the is_prime(n) function from number 3, write a function that asks a user for an input n and returns all 
# the prime numbers up to n.

#5. Write a function lesser_of_two_evens(a, b) that returns the lesser of two given numbers if both numbers are
#  even, but returns the greater if one or both numbers are odd.
# def lesser_of_two_evens(a, b):
#     if a % 2 == 0 and b % 2 == 0:

#6. Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if both
#  words begin with the same letter.
# is_alliteration(‘Levelheaded llama’) —> True
# is_alliteration(‘Crazy Kangaroo’) –> False

# def is_alliteration(two_word_string: str):
#     word1, word2 = two_word_string.lower().split()
#     first_letter_word_1 = word1[0]
#     second_letter_word_2 = word2[0]
#     return first_letter_word_1 == second_letter_word_2

# print(is_alliteration("Levelheaded llama"))
# print(is_alliteration("Silicon Valley"))

#7. Write a function old_macdonald(name) that capitalizes the first and fourth letters of a name
# old_macdonald(‘macdonald’) —> MacDonald

# def old_macdonald(name :str):
#     return name[0].upper() + name[1:3] + name[3].upper() + name[4:]
# print(old_macdonald("macdonald"))
# Note: ‘macdonald’.capitalize() returns Macdonald, not MacDonald.
#8. Write a function spy_game(list_of_ints) that takes in a list of integers and returns True if it contains 007 
# in order.
# spy_game([1, 2, 4, 0, 0, 7, 5]) —> True
# spy_game([1, 0, 2, 4, 0, 5, 7]) —> True
# spy_game([1, 7, 2, 0, 4, 5, 0]) —> False
#9. Write a function vol(radius) that computes the volume of a sphere given its radius.
# import math

# def vol(radius):
#     return
#10. Write a function range_check(num, low, high) that checks whether a number is in a given range 
# (inclusive of high and low).
#11. Write a function upper_lower(text) that accepts a string and calculates the number of uppercase letters and 
# lowercase letters.
#12. Write a function unique_list(list_items) that takes in a list and returns a new list with unique elements of 
# the first list. Do not use the set() constructor.
#  13.	Write a function multiply(list_items) to multiply all the numbers in a list.
# 	Sample List: [1, 2, 3, -4]
# 	Expected output: -24
#  14. 	Write a function is_pangram(text) to check whether a string is a pangram or not. 
# 	Note: A pangram is a word or sentence that contains every letter of the alphabet at  
# 	least once. For example: “The quick brown fox jumps over the lazy dog”.
# 	Hint: Import and use the string module.
#  15. 	Write a function are_anagrams(s1, s2) that checks if two strings are anagrams of each
# 	other. a word, phrase, or name formed by rearranging the letters of another, such as
# 	spar, formed from rasp.
#  16. 	Write a function calculate_bmi(weight, height) that calculates the Body Mass Index 
# 	(BMI) given weight in kilograms and height in meters.
#  17. 	Write a function calculate_simple_interest(principal, rate, time) that calculates the 
# 	simple interest given principal amount, interest rate, and time (in years).




############# CLASSWORK ################
def get_hex_code(color):
    if color == "red":
        return "The hex color is #FF0000"
    if color == "blue":
        return "The hex color is #0000FF"
    if color == "green":
        return "The hex color is #008000"
    if color == "white":
        return "The hex color is #FFFFFF"
    if color == "black":
        return "The hex color is #000000"
print(get_hex_code(input("Enter a color: ")))