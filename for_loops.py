# for num in range(12, 22, 2):
#     print(num)

# story = "Once upon a time"
# for char in story:
#     print(char)
    
     #################### ASSIGNMENT ###################
# 1. Write a program that takes an integer input from the user and uses a loop to calculate 
# the sum of its digits. Print the sum. Example:
# Input: 1234
# Output: 10 (1+2+3+4)
# digits = (input("Enter some numbers: ")).strip()
# total = 0
# for digit in digits:
#     total += int(digit)
# print(total)
# 2.Collect a string from the user and use loops to count the number of vowels and consonants in the string. Print
#  the counts. Example:
# Input: "hello world"
# Output: Vowels: 3, Consonants: 7
# text = input("Enter a string: ").strip().lower()
# vowels = 0
# consonants = 0
# for char in text:
#     if char.isalpha():
#      if char in "aeiou":
#         vowels += 1
#     else:
#         consonants += 1
# print(f"Vowels: {vowels}, Consonants: {consonants}")
# 3.Write a program that takes an integer input from the user and prints the multiplication table for that number
#  up to 12. Example:
# Input: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 12 = 60
# multiplication_table = int(input("Enter a number: "))
# for num in range(1,13):
#     print(f"{multiplication_table} * {num} = {multiplication_table * num}")
# 4.Collect a string from the user and use a loop to reverse the string. Print the reversed string. Do not reverse
#  the string using [::-1] or reversed().
# Example:
# Input: "python"
# Output: "nohtyp"

# text = input("Enter a text: ")
# index = len(text) - 1
# for char in text:
#     if index >= 0:
#      char = text[index]
#      print(char)
#      index -= 1
        
    
# 5.Write a program that takes a list of numbers (entered as comma-separated values) from the user and removes any
#  duplicate values. Print the new list. Do not use the set() constructor. Use a loop. Example:
# Input: "1, 2, 3, 2, 4, 3"
# Output: [1, 2, 3, 4]
# 6.	Write a program that takes an integer input n from the user and prints the first 
# 	n numbers in the Fibonacci sequence. Example:
# 	Input: 10
# 	Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
#  7. 	Collect a list of numbers from the user (entered as comma-separated values) and use a 
# 	loop to find and print the largest number in the list. Don’t use the built-in max 
# 	function or anything similar.
# 	Input: "10, 20, 5, 15"
# 	Output: 20
# numbers = tuple(input("Enter comma-separated numbers: ").split(","))

# maximum = int(numbers[0])
# index = 1
# numbers = numbers[1:]
# for number in numbers:
#   number = int(number)
#   if number > maximum:
#         maximum = number
#         index += 1

# print(maximum)
#  8. 	Write a program that takes an integer n from the user and calculates the sum of all 
# 	even numbers from 1 to n. Print the sum.
# 	Input: 10
# 	Output: 30 (2 + 4 + 6 + 8 + 10)
# n = int(input("Enter a number: "))
# sum = 0
# total = ""
# for i in range(2, n + 1, 2):
#  sum += i
#  total += str(i) + "+"
#  print(total + "=" + str(sum))
#  9. 	Collect a string from the user and use a loop to count the frequency of each character 
# 	in the string. Print each character along with its frequency. Example:
# 	Input: "hello"
# 	Output:
# h: 1
# e: 1
# l: 2
# o: 1
# text = input("Enter some text: ")
# frequency = {}
# index = 0
# for char in text:
#     if index < len(text):
#      char = text[index]
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1
#     index += 1

# print(frequency)
# 10.	Write a program that takes an integer n from the user and calculates the sum of 
# 	squares of all numbers from 1 to n. Print the sum. Example:
# 	Input: 3
# 	Output: 14 (1^2 + 2^2 + 3^2)
# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1, n + 1):
#  sum += i ** 2
# print(sum)
#  11. 	Collect a phrase from the user and use a loop to generate an acronym by taking the first
# 	letter of each word. Print the acronym. Example:
# 	Input: "Portable Network Graphics"
# 	Output: "PNG"
# text = input("Enter an acronym in full: ")
# acronym = ""
# for word in text.split():
#     acronym += word[0].upper()
# print(acronym)
#  12. 	Collect a string from the user and use a loop to count the number of words in the string. 
# 	Print the count. Example:
# 	Input: "Hello world from Python"
# 	Output: 4
# sentence = input("Enter a sentence: ").strip(" ")
# word_count = 0
# words = sentence.split()
# for word in words:
#     word_count += 1
# print(word_count)
#  13. 	Collect a string from the user and only print put the words that start with the letter 
# 	‘S’. Example:
# 	Input: “Print only the words that start with s in this sentence”
# 	Output: 
# 	start
# 	s
# 	Sentence
#  14. 	Print all the even numbers from 1 to 20 using the range function and a loop.
# for num in range(2, 21, 2):
#     print(num)
#  15. 	Use a list comprehension to create a list of numbers between 1 and 50 that are divisible
# 	by 3.
# list_of_numbers = range(1,50)
# for numbers in list_of_numbers:
#     if numbers % 3 == 0:
#         print(numbers)
#  16.	Go through the string below and if the length of a word is even, print that word.
# 	st = ‘Print every word in this sentence that has an even number of letters’
# 	Output: 
# 	word
# 	in
# 	this
# 	sentence
# 	that
# 	an
# 	even
# 	number
# 	of
# st = "Print every word in this sentence that has an even number of letters"
# words = st.split()
# print(words)
# for word in words:
#     if len(word) % 2 == 0:
#         print(word)
#  17. 	Write a program that prints the integers from 1 to 100. But for multiples of three, print 
# 	“Fizz” instead of the number, and for multiples of five, print “Buzz”. For numbers which 
# 	are multiples of both three and five, print “FizzBuzz”.
# list_of_numbers = range(1,100)
# for number in list_of_numbers:
#     if number % 15 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)



############### Classwork ############
sports = ["Basketball", "Volleyball", "Tennis", "Swimming"]
for index, sports in enumerate(sports):
    print(f"Sports# {index +1} -> {sports}")