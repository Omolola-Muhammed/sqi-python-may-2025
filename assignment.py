# 1. Format the following sentence using f-string, .format(), and concatenation:
# "Welcome to Mars! This planet is 237 million years old. It is True that it is friendly to visitors. Gravity here is 3.721 m/s²."
planet = "Mars"
age = 237
is_friendly = True
gravity = 3.721

print("Welcome to {}! This planet is {} million years old. It is {} that It is friendly to visitors. Gravity here is {}m/s²."
.format(planet, age, is_friendly, gravity))
print(f"Welcome to {planet}! This planet is {age} million years old. It is {is_friendly} that it is friendly to visitors. Gravity here is {3.721}m/s².")
print("Welcome to " + planet + "! This planet is " + str(age) + " million years old. It is " + str(is_friendly) + " that It is friendly to visitors. Gravity here is " + str(gravity) + "m/s².")


# 2. Format the following sentence using all three styles:
# "You are watching Inception. Your seat number is 45. It is false that this is a premium seat. The ticket costs $12.99."
movie = "Inception"
ticket_price = 12.99
seat_number = 45
is_premium = False

print("You are watching {}. Your seat number is {}. It is {} that this is a premium seat. The ticket costs ${}."
.format(movie, seat_number, is_premium, ticket_price))
print(f"You are watching {movie}. Your seat number is {seat_number}. It is {is_premium} that this is a premium seat. The ticket costs {ticket_price}.")
print("You are watching " + movie + ".Your seat number is " + str(seat_number) + ". It is" + str(is_premium) + "that is " + str(is_friendly) + " that It is friendly to visitors. Gravity here is " + str(gravity) + "m/s².")


# 3. Compose this sentence using all three formatting styles:
# "Sweet Crumbs is located in Downtown. We have 150 cakes today, each priced at $5.75 on average. It is True that we sell chocolate cakes."
bakery_name = "Sweet Crumbs"
num_cakes = 150
average_price = 5.75
has_chocolate = True
location = "Downtown"

print("Welcome to {}! This planet is {} million years old. It is {} that It is friendly to visitors. Gravity here is {}m/s²."
.format(planet, age, is_friendly, gravity))
print(f"Welcome to {planet}! This planet is {age} million years old. It is {is_friendly} that it is friendly to visitors. Gravity here is {3.721}m/s².")
print("Welcome to " + planet + "! This planet is " + str(age) + " million years old. It is " + str(is_friendly) + " that It is friendly to visitors. Gravity here is " + str(gravity) + "m/s².")



# 4. Create this sentence using all three formatting methods:
# "Last night at Moonlight Arena, Aria Blaze performed 18 songs over 2.5 hours. It is True that the concert was live."
# artist = "Aria Blaze"
# duration = 2.5
# num_songs = 18
# was_live = True
# venue = "Moonlight Arena"

# print("Welcome to {}! This planet is {} million years old. It is {} that It is friendly to visitors. Gravity here is {}m/s²."
# .format(planet, age, is_friendly, gravity))
# print(f"Welcome to {planet}! This planet is {age} million years old. It is {is_friendly} that it is friendly to visitors. Gravity here is {3.721}m/s².")
# print("Welcome to " + planet + "! This planet is " + str(age) + " million years old. It is " + str(is_friendly) + " that It is friendly to visitors. Gravity here is " + str(gravity) + "m/s².")



# 5. Format the following sentence using f-string, .format(), and concatenation:
# "Meet Whiskers, a 2-year-old cat weighing 3.9 kg. It is True that Whiskers is vaccinated."
# pet_name = "Whiskers"
# pet_type = "cat"
# weight = 3.9
# age = 2
# vaccinated = True

# print("Welcome to {}! This planet is {} million years old. It is {} that It is friendly to visitors. Gravity here is {}m/s²."
# .format(planet, age, is_friendly, gravity))
# print(f"Welcome to {planet}! This planet is {age} million years old. It is {is_friendly} that it is friendly to visitors. Gravity here is {3.721}m/s².")
# print("Welcome to " + planet + "! This planet is " + str(age) + " million years old. It is " + str(is_friendly) + " that It is friendly to visitors. Gravity here is " + str(gravity) + "m/s².")

# 11. Assign values "Orange", "Banana", "Cherry" to multiple variables x, y and z in one line respectively.
values = "Orange", "Banana", "Cherry"
x, y, z = values
print(values)
# 12.	Assign the values 10, "John", and True to the variables age, name, and is_student in a 
# single line.
age, name, is_student = 10, "John", True
# age = "10"
# name = " John "
# is_student = "True"
# print(age + name + is_student)

#  13. 	Swap the values of x and y, where x = 5 and y = 10, without using a temporary variable.
x,y = 5,10
y,x = x,y


#  14. 	Create a list of numbers with values 1, 2, and 3. Unpack the list into separate 
# variables a, b, and c.
nums = ["1", "2", "3"]
a, b, c = nums
print(a)
print(b)
print(c)
#  15. 	Convert a string variable called height from “1.35” to a float.
height = "1.35"
height = float(height)
#  16.	Predict the output of the following statements:
# a) bool("") --- true-
# b) bool(123)---- true
# c) bool(["apple", "cherry", "banana"]) ---true
# d) bool(False) ----false
# e) bool(None) ---false
# f) bool(0) ---false
# g) bool("abc") ---false
# h) bool(()) ----true
# i) bool([]) ---true
# j) bool({}) ----true


# 1.Write a program that asks the user for their name and then greets them with their 
# name: Print a greeting message that includes the user's name in the format "Hello, {name}!".

name = input("What is your name?")
print(f"Hello, {name}!")
# 2.Ask the user for their birth year and calculate their age. Print the user's age in the 
# format “You are {age} years old.”.

age = int(input("What year were you born?"))
print(f"You are {2025 - age} years old.")
# 3.Ask the user for their favourite color. Print a statement that includes the color in the format 
# “Your favorite color is {favourite_color}.”.

fav_color = input("What is your favorite color?")
print(f"Your favorite color is {fav_color}")
# 4.Ask the user to input some text and check if it is a palindrome. A palindrome is a word, phrase,
#  or sequence that reads the same backwards as forwards, e.g. `madam` or `nurses run` or `121`.
# Print a statement in the format “It is {is_palindrome} that {text} is a palindrome.”. `is_palindrome` is either `True` or `False`.
# 5.Create a program that asks the user to input a password and checks if it meets certain criteria (at least 8 characters and not more than 30 characters).
# Print a statement in the format “It is {is_valid} that the password fulfils the criteria.”. `is_valid` is either `True` or `False`.
# Bonus point if you can hide the password input from displaying on the screen as clear text.
# 6.Write a program that asks the user for their weight (in kilograms) and height (in meters) and calculates their Body Mass Index (BMI). Calculate the BMI using the formula BMI = weight / (height ** 2). Round the BMI to 2 decimal places. Print a statement in the format “Your BMI is {BMI}”.
