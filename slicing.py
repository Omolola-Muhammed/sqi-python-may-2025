# Slicing
# institution = "SQI College of ICT"
# print(institution[0 : 5])
# print(institution[0: 10: 2])--step

# negative slicing
# print(institution[-3:])
# print(institution[-3::])

# Reverse a string
# print(institution[::-1])--negative reversal

# method--variable name with a fullstop to bring methods
# company = "ICT Hub"
# print(company.capitalize())
# print(company.lower())
# print(company.upper())
# print(company.title())

# # with argument
# print(company.endswith("b"))
# print(company.startswith("R"))

# # to get all methods availableon anything string
# print(dir(""))

# print(company.isupper())
# print(company.islower())
# print(company.isdigit())


# Classwork
# Create a string variable sentence with the vale "the quick brown fox jumps over the lazy dog".
#  Capitalize the first letter of the string and print the result
sentence = "the quick brown fox jumps over the lazy dog"
print(sentence.capitalize())

# 2
book_title = "to kill a mockingbird"
print(book_title.title())

# 3
url = "https://www.example.com"
print(url.endswith(".com"))