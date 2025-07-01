# i = 6
# while i <= 50:
#     print(i)
#     i += 2

# i = 7
# while i <= 50:
#     print(i + 1)
#     i += 1


######################### PRACTICE ###########################
# i = 5
# while i <= 50:
#     print(i + 5)
#     i += 5


# i = 50
# while i >= 5:
#     print(i - 5)
#     i -= 5



########################### CLASSWORK #######################
# i = 0
# while i <= 200:
#     print(i)
#     i += 5

# i = 69
# while i <= 203:
#     if i % 15 == 0:
#         print(i)
#     i += 1

# 2.
# numbers = []
# i = 1
# while i <= 50:
#     numbers.append(i)
#     i += 1

# print(numbers)

# i = 1
# while i <= 10:
#     if i != 5:
#         print(i)
#     i += 1

# length = int(input("Enter the length of the rectangle: "))
# breadth = int(input("Enter a breadth of the rectangle: "))
# i = 1
# while i <= breadth:
#     print("*" * length)
#     i += 1

# series = ["Wednesday", "Umbrealla Academy", "Vampire Diaries", "Stranger Things", "Blindspot", "Prison Break"]
# i = 0
# while i < len(series):
#     the_series = series[i]
#     print(f"Series {i + 1}: {the_series}")
#     i += 1

# series = ["Wednesday", "Umbrealla Academy", "Vampire Diaries", "Stranger Things", "Blindspot", "Prison Break"]
# i = 0
# while i < len(series):
#     the_series = series[i]
#     print(f"The Series at index {i}: {the_series}")
#     i += 1

# i = 0
# while True: 
#     if i == 5 % 10:
#         break
#     print(i)
#     i += 5


################# ASSIGNMENT ###############
#1. Print numbers from 1 to 5
# Expected Output:
# 1
# 2
# 3
# 4
# 5

# i = 1
# while i <=5:
#     print(i)
#     i += 1
#2. Print "Hello" 3 times
# Expected Output:
# Hello
# Hello
# Hello

# i = 1
# while i <= 3:
#     print("Hello")
#     i += 1
#3. Print only even numbers from 2 to 10 (do not use += 2)
# Expected Output:
# 2
# 4
# 6
# 8
# 10
i = 1
# while i <= 10:
#     if i % 2 == 0:
#         print(i)
#     i += 1
# Print numbers in reverse from 5 to 1 using a while loop.
# Expected Output:
# 5
# 4
# 3
# 2
# 1
# i = 5
# while i >= 1:
#     print(i)
#     i -= 1
#  7.	Print a right triangle of stars
# Ask the user to enter a number
# Example:
# Input: 4

# Output:
# *
# **
# ***
# ****

# number = int(input("Enter a number"))
# i = 1
# while i <= number:
#     print("*" * i)
#     i += 1
#  8. 	Print a countdown
# Ask the user to enter a number where they want to start the countdown from.
# Example:
# Input: 5

# Output:
# 5
# 4
# 3
# 2
# 1
# Go!

# number = int(input("Enter a number: "))
# i = 0
# while i <= number:
#     print(number - i)
#     i += 1
########### 2nd ###########
#2. Write a program that simulates a grocery store checkout. The user should enter the prices of items until they 
# decide to stop. The program should calculate and display the total cost.
# Sample Input and Output:
# Enter item price: 2.99
# Enter another item? (yes/no): yes
# Enter item price: 5.49
# Enter another item? (yes/no): no
# Total cost: 8.48

# price = float(input("Enter item price: "))
# price_2 = input("Enter another item? (yes/no) : ").strip().lower()
# while True:
#     if price_2 == "yes":
#         continue
#     if price_2 == "no":
#         price_2 +=  price
#         print("Total cost:" [price])
#         break

#3. Write a program that continuously prompts the user to enter a password until they enter a valid one. A valid 
# password must be at least 8 characters long and have a maximum of 25 characters.
# Sample Input and Output:
# Enter password: hello
# Password must be at least 8 characters long and have a maximum of 25 characters.
# Enter password: mysecretpasswordisasecret
# Password accepted.
#  5. 	Write a program that tracks the inventory of items in a store. The user should be able 
# 	to add or remove items and the program should display the current inventory after each
# 	operation. The program stops when the user decides to exit.
# 	The current store inventory is {‘eggs’: 40, ‘fish’: 200, ‘bread’: 343, ‘yam’:2}
# 	Sample Input and Output:
# 	Enter operation (add/remove/exit): add
# Enter item: eggs
# Enter quantity: 10
# Current inventory: {'eggs': 50, 'fish': 200, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): remove
# Enter item: fish
# Enter quantity: 50
# Current inventory: {'eggs': 50, 'fish': 150, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): exit


########## 3rd ##############
# Write a program that uses a while loop to print numbers from 1 to 10.
# i = 0
# while i <= 10:
#     print(i)
#     i += 1
# Write a program that takes an integer n from the user and calculates the sum of all 
# natural numbers up to n using a while loop.

# n = int(input("Enter a number: "))
# i = 1
# sum = 0
# while i <= n:
#     sum += i
#     i += 1

# Write a program that generates a random secret number between 1 and 50. Use a while loop to allow 
# the user to guess the number with a maximum of 5 attempts. Provide hints if the guess is too high or too low. 
# E.g. if the secret num is 35, and the user guesses 42, their guess is too high. If they guess lower than 35, 
# their guess is too low.
# num = int(input("Guess a number: "))
# i = 1
# while i <= 50:
#     if num == 42:
#         print("Your guess is too high")
#         i += 1
#     elif num < 35:
#         print("Your guess is too low")
#         i += 1
#     else:
#         print("Try again")
#         i += 1
# Write a program that keeps asking the user for a password until they enter the correct one. The correct password
#  is `secret`.
# password = input("Enter your password: ").strip().lower()
# if password != "secret":
#     print("Incorrect password")

# Write a program that takes an integer input from the user and uses a while loop to print a countdown from that
#  number to zero.
num = int(input("Enter a number: "))
while i < num:
    print(num)
    num -= 1
    i += 1
# Write a program that takes an integer n from the user and uses a while loop to print all even numbers from 1 to n.
# num = int(input("Enter a number"))
# i = 1
# while i <= num:
#     if num
# Write a program that takes two integers, base and exponent, from the user and uses a while loop to calculate base
#  raised to the power of exponent.
# Sample Input:
# Enter the base: 2
# Enter the exponent: 3
# Output:
# 2 raised to the power of 3 is 8
# Sample Input:
# Enter the base: 5
# Enter the exponent: 4
# Output:
# 5 raised to the power of 4 is 625
# Write a program that takes a string input from the user and uses a while loop to count the number of vowels (a, e, i, o, u) in the string.
# Write a program that takes a string input from the user and uses a while loop to reverse the string.
