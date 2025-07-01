# num = int(input("Enter an even number"))
# if num % 2 == 0: 
#     print(True)
# else:
#     print(False)

# today = input("Enter the day of the week")
# if today == "Wednesday" :
#     print("you are correct")
# else:
#     print(f"Today is Wednesday not {today}")

# number = int(input("Enter a number in multiple of 5: "))
# if number % 5 == 0: 
#     print("It is a multiple of 5")
# else:
#     print("It is not a multiple of 5")

# number = int(input("Enter a number: "))
# if number % 5 == 0 and number % 3 == 0: 
#     print("It is a multiple of 3 and 5")
# else:
#     print("It is not a multiple of 3 and 5")


# has_umbrella = True
# has_raincoat = False

# if has_raincoat and has_umbrella != True:
#     print("You are not protected")
# elif has_umbrella:
#     print("You are protected from the rain")
# elif has_raincoat:
#     print("You are protected from the rain")
# elif has_umbrella and has_raincoat:
#     print("You are well protected from the rain")
    


##################### ASSIGNMENT #####################
#1. Collect two numbers as input from the user and assign as variables, a and b, write an if 
# statement that prints "a and b are both positive" if both a and b are positive, prints 
# "Only one is positive" if one of them is positive, and prints "Neither is positive" if 
# neither is positive.
# a = int(input("Enter a number:"))
# b = int(input("Enter a number:"))
# if a > 0 and b > 0:
#     print("a and b are both positive")
# elif a > 0 or b > 0:
#     print("Only one is positive")
# else:
#     print("Neither is positive")
#2. Collect three numbers x, y and z as a comma separated string input from the user and print "Increasing order"
#  if they are in STRICTLY increasing order, "Decreasing order" if they are in STRICTLY decreasing order, and
#  "Neither" otherwise.
# x = int(input("Enter a number:"))
# y = int(input("Enter a number:"))
# z = int(input("Enter a number:"))
# if x < y < z:
#     print("Increasing order")
# elif x > y > z:
#     print("Decreasing order")
# else:
#     print("Neither")
#3. Write a program that reads a string called `palindrome` supplied through user input and checks if it is a 
# palindrome. Print "Is a palindrome" if it is, otherwise print "Not a palindrome".
# palindrome = input("Enter a palindrome: ")
# if palindrome.lower().replace(" ", "") == palindrome[::-1].lower().replace(" ", ""):
#     print("Is a palindrome")
# else:
#     print("Not a palindrome")
#4. You have three variables: x, y, and z collected as 3 separate inputs from the user. Write an if statement 
# that checks if exactly two out of the three variables are equal and prints "Two are equal" if this is true. 
# Otherwise, print "All different" or "All same" accordingly.
# x = int(input("Enter a number:"))
# y = int(input("Enter a number:"))
# z = int(input("Enter a number:"))
# if x == y or x == z:
#     print("Two are equal")
# elif x == y == z:
#     print("All same")
# else:
#     print("All different")
#5. Given three angles angle1, angle2, and angle3 collected as 3 separate inputs from the user, use if statements 
# to check if they can form a valid triangle. Print "Valid triangle" if the sum of the angles is 180 degrees and
#  all angles are greater than 0. Otherwise, print "Invalid triangle".
# angle1 = int(input("Enter a number to form a triangle:"))
# angle2 = int(input("Enter a number to form a triangle:"))
# angle3 = int(input("Enter a number to form a triangle:"))
# if angle1 + angle2 + angle3 == 180:
#     print("Valid triangle")
# elif angle1 and angle2 and angle3 > 0:
#     print("Valid triangle")
# else:
#     print("Ivalid triangle")
#6. You have a single character variable `ch` supplied through user input. Write an if statement that prints
#  "Vowel" if ch is a vowel (a, e, i, o, u, both uppercase and lowercase), and "Consonant" otherwise. Assume that 
# the input is a single alphabet character.
# char = input("Enter a letter")
# if char == ("a, e, i, o, u"):
#     print("Vowel")
# else:
#     print("Consonant")
#7. Given a comma separated string input from the user of three colors color1, color2, and color3, write an if
#  statement to check if all three colors are primary colors (red, blue, yellow). Print "All primary colors" if
#  they are, otherwise print "Not all primary colors".
# color1 = input("Enter a color:")
# color2 = input("Enter a color:")
# color3 = input("Enter a color:")
# if color1 and color2 and color3 == ("red, blue, yellow"):
#     print("All primary colors")
# else:
#     print("Not all primary colors")
#8. You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". Write an if 
# statement that prints "Manual mode activated" if mode is "manual", "Automatic mode activated" if mode is 
# "automatic", and "System is off" if mode is "off".
# mode = input("Enter a mode")
# if mode == "manual":
#     print("Manual mode activated")
# elif mode == "automatic":
#     print("Automatic mode activated")
# elif mode == "off":
#     print("System is off")
#9. Given a string `message` entered by the user, use if statements to check if the message contains any of the
#  words
#  "urgent", "important", or "immediate". If it contains any of these words, print "High priority message".
#  Otherwise, print "Normal message".
# message = input("Enter a message").lower()
# if "urgent" in message or "important" in message or "immediate":
#     print("High Priority")
# else:
#     print("Normal message")
# 10.	You have two variables, status1 and status2, provided through user input, each of 
# 	which can be "active", “inactive", or "pending". Write an if statement to print 
# 	"Both active" if both statuses are "active", "One active" if exactly one is "active",
# 	and "None active" if neither is "active".
# status1 = input("Enter a status:")
# status2 = input("Enter a status:")
# if status1 == "active" and status2 == "active":
#     print("Both active")
# elif status1 == "active" or status2 == "active":
#     print("Only one active")
# else:
#     print("None active")
#  11. 	Given a string `filename` supplied by the user, write an if statement to check if the
# 	filename ends with “.jpg", ".png", or ".gif". Print "Image file" if it does, otherwise
# 	print "Not an image file".
# filename = input("Enter a file:").strip().lower()
# if filename.endswith("jpg") or filename.endswith("png") or filename.endswith("gif"):
#     print("image file")
# else:
#     print("Not an image file")
#  12. 	You have a variable `access_level` provided through user input which can be "admin",
# 	"user", or "guest". Write an if statement that prints "Full access" if access_level is
# 	"admin", "Limited access" if it is "user", and "No access" if it is "guest".
# access_level = input("Enter your level:").strip().lower()
# if access_level == "admin":
#     print("Full access")
# elif access_level == "user":
#     print("Limited access")
# elif access_level == "guest":
#     print("No access")
# else:
#     print("invalid")
#  13. 	Given a string `email` collected from the user, write an if statement to check if the
# 	email contains both "@" and 	"." characters. Print "Valid email" if it does, otherwise
# 	print "Invalid email".
# email = input("Enter your email")
# if email.__contains__("@") and email.__contains__("."):
#     print("Valid email")
# else:
#     print("Invalid email")
#  14. 	You have a variable `day` provided by user input which can be any day of the week 
# 	(e.g., "Monday", "Tuesday", 	etc.). Write an if statement that prints "Weekend" if the
# 	day is "Saturday" or "Sunday", and "Weekday" if it is any other day.
# day = input("Enter what day it is: ")
# if day == "saturday" or day == "sunday":
#     print("weekend")
# else:
#     print("weekday")
#  15. 	Write a program that takes three numbers (num1, num2, num3) as a comma-separated string 
# 	input from the user and prints the greatest number. Use conditional statements
# 	to determine which number is the greatest. Bonus point if you can do it without `else` 
# 	statements.
# num1 = input("Enter a number: ")
# num2 = input("Enter a number: ")
# num3 = input("Enter a number: ")
# if num1 > num2 > num3:
#     print(max(num1, num2, num3))
# elif num1 < num2 < num3:
#     print("none")