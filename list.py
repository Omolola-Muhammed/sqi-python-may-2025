# sports = ["Basketball", "Volleyball", "Tennis", "Golf"]
# print(len(sports))
# sports.append("Baseball")
# print(sports)
# sports.remove("Volleyball")
# print(sports)
# print(sports[0][6:])
# sports.insert(2, "Hockey")
# print(sports)
# print("Rugby" in sports)
# print(sports[1])

# class2
# Exercise 1: Student Grades Average
# Description:
# Write a program that:
# Asks the user to input grades (as numbers) for 5 subjects.
# Stores them in a list.
# Calculates and prints the average grade.
# Prints "Pass" if the average is 50 or above, else prints "Fail".

# subject_1 = int(input("Enter your grade as numbers"))
# subject_2 = int(input("Enter your grade as numbers"))
# subject_3 = int(input("Enter your grade as numbers"))
# subject_4 = int(input("Enter your grade as numbers"))
# subject_5 = int(input("Enter your grade as numbers"))

# totalgrade = [subject_1, subject_2, subject_3, subject_4, subject_5] 
# print(sum(totalgrade)/len(totalgrade))
# Exercise 2: Swap First and Last
# Description:
# Create a program that:
# Takes 4 names as comma-separated input and stores them in a list where each item in the list is one name.
# Swaps the first and last names in the list.
# Prints the updated list.

# names = input("Enter your 4 names seperated by comma").split(",")
# names[0],names[3] = names[3],names[0]
# print(names)

# Exercise 3: 
# Ask the user to input an odd number of comma-separated numbers.
# Store them in a list.
# Print the median number.
# odd_numbers = input("Enter several odd numbers seperated by comma: ").split(",")
# odd_numbers.sort()
# print(len(odd_numbers) // 2)
# print(odd_numbers[2])


# Exercise 4:
# Repeat This Word
# Description:
# Ask the user for a word and a number.
# Print the word repeated that many times.
word = input("Enter a word: ")
number =int(input("Enter a number: "))
print(word * number)