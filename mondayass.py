#  14. 	Create a list of numbers with values 1, 2, and 3. Unpack the list into separate 
# variables a, b, and c.
values = [1, 2, 3]
a, b, c = values
print(a, b , c)
#  15. 	Convert a string variable called height from “1.35” to a float.
height = "1.35"
height2float = 1.35
print(type(height2float))
#  16.	Predict the output of the following statements:
# 	a) bool("")
False
# b) bool(123)
True
# c) bool(["apple", "cherry", "banana"])
True
# d) bool(False)
False
# e) bool(None)
False
# f) bool(0)
False
# g) bool("abc")
True
# h) bool(())
False
# i) bool([])
False
# j) bool({})
False
# 17.	Convert a string “James John Kennedy” called “names” to a list using the string 
# .split() method. Store the result in a list called “names_list”
# 18.	You have a list of cities called cities_list containing ['New York', 'Los Angeles', 
# 'Chicago']. Convert this list into a single string where each city is separated by a 
# semicolon and a space. Store the result in a string called cities_string.
# 19.	Create a string variable sentence with the value "the quick brown fox jumps over the 
# lazy dog". Capitalize the first letter of the string and 
# print the result.
sentence = ("the quick brown fox jumps over the lazy dog")
print(sentence.capitalize())
# 20. 	Create a string variable book_title with the value "to kill a mockingbird". Capitalize 
# the first letter of each word and print the result.
book_title = ("to kill a mockingbird")
print(book_title.title())
# 21. 	Create a string variable text with the value "hello world". Count the number of 
# occurrences of the letter 'o' and print the result.
text = "hello world"
print(text.count("o"))
# 22. 	Create a string variable filename with the value "document.txt". Check if the string 
# starts with "doc" and print the result.
filename = "document.txt"
print(filename.startswith("doc"))
# 23.	Create a string variable url with the value "https://www.example.com". Check if the 
# string ends with ".com" and print the result.
url = "https://www.example.com"
print(url.endswith(".com"))
# 24.	Create a string variable phrase with the value "find the needle in the haystack". Find 
# the position of the word "needle" and print the result.
phrase = "find the needle in the haystack"
print(phrase.find("needle"))
# 25.	Create a string variable template with the value "Hello, {}. Welcome to {}.". Use the 
# format() method to replace the placeholders with "Alice" and "Wonderland" and print the 
# Result. Bonus point if you can do it with the f-string and concatenation methods also.
# 26.	Create a string variable `quote` with the value "To be or not to be". Find the position 
# of the word "not" and print the result.
quote = "To be or not to be"
print(find("not"))
# 27.	Create a string variable word with the value "hello". Check if all characters in the 
# string are lowercase and print the result.
value = "hello"
print(value.islower())
# 28.	Create a string variable shout with the value "HELLO". Check if all characters in the 
# string are uppercase and print the result.
value = "HELLO"
print(value.isupper())
# 29.	Create a string variable mixed_case with the value "PyThOn". Convert all characters to 
# lowercase and print the result.
value = PyThon
print(value.lower())
# 30. 	Create a string variable mixed_case with the value "PyThOn". Convert all characters to 
# uppercase and print the result.
# 31. 	Create a string variable padded_text with the value " hello ". Remove leading whitespace and 
# print the result.
# 32. 	Create a string variable padded_text with the value " hello ". Remove trailing whitespace and 
# print the result.
# 33.	Create a string variable padded_text with the value " hello ". Remove both leading and trailing 
# whitespace and print the result.
# 34.	Create a string variable greeting with the value "Hello, World!". Replace "World" with "Alice" 
# and print the result.
# 35.	Given the string course_name = "Introduction to Python", use slicing to print:
# 	The word "Introduction".
# The word "Python".
# 36.	Given the string quote = "To be or not to be, that is the question.", use slicing to print:
# The substring "To be or not to be".
# The substring "that is the question".
# 37.	Given the string phrase = "A journey of a thousand miles begins with a single step", use 
# slicing to print:
# The last 5 characters.
# All characters except the last 7.
# 38.	Given the string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", use slicing to print:
# Every second letter (A, C, E, ...).
# Every third letter starting from the first letter (A, D, G, ...).
# 39. 	Given the string word = "tenet", use slicing to:
# Reverse the string and print the result.
# 40. 	Given the string sentence = "Learning Python is fun and rewarding!", use slicing to print:
# Characters from index 9 to 19. (Python is f)
# Every second character from index 0 to 10. (Lann y)
# Every third character from the beginning to the end. (LrnPh  nnrai!)
# 41. 	Given the string programming_language = "JavaScript", use slicing to:
# Print the first character.
# Print the last character.
# 42.	Given the string data = "DataScience", use slicing to:
# Print the substring "Science".
# 43.	Given the string greeting = "Good Morning!", use slicing to:
# Print every second character.
# 44.	Given the string name = "Alexander", use slicing to:
# Print the first three characters concatenated with the last three characters.
