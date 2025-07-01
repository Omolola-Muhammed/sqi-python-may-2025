# 1.Create a tuple called dimensions with values 10, 20, 30. Unpack the values into variables 
# length, width, and height, and print each variable.
dimensions = (10, 20, 30)
length, width, height = dimensions
print(dimensions)
# 2.Given the tuple coordinates:
# coordinates = (1.5, 2.5, 3.5)
# Unpack the tuple into variables x, y, and z, and print the value of y.
coordinates = (1.5, 2.5, 3.5)
x, y, z = coordinates
print(coordinates[1])
# 3.Create a tuple called person with values ("John", 25, "Engineer").
#  Unpack the values into variables name, age, and profession, and print the value of profession.
person = ("John", 25, "Engineer")
name, age, profession = person
# print(person[2])
print(profession)
# 4.Given the nested tuple data:
# data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
# Unpack the first element of data into variables student1 and student2, and print student2.
data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
(student1, *_) = data
print(data[0][1])
# 5.Create a tuple called colors with values ("red", "green", "blue", "yellow"). 
# Unpack the first two values into variables color1 and color2, and print both variables.
colors = ("red", "green", "blue", "yellow")
color1 = colors[0]
color2 = colors[1]
print(color1, color2)
# 6.Given the tuple record:
# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# Unpack the tuple to extract the name, the tuple containing age and position, and the list of departments.
#  Print the extracted age and the first department.
record = ("Jane", (32, "Manager"), ["HR", "Finance"])
name, age_position, departments = record
age, position = age_position
first_dept, second_dept = departments
print(age)
print(first_dept)
# 7.Create a tuple called triplet with values ("one", "two", "three"). 
# Unpack the tuple into variables and print the value of the second variable.
triplet = ("one", "two", "three")
first, second, third = triplet
print(triplet[1])
# 8.Given the tuple info:
# info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
# Unpack the tuple to get the product ID, category, price, and manufacture date. 
# Print the category and the manufacture year.
info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
productID, category_price, manufacture_date = info
category, price = category_price
print(category, manufacture_date)
# 9.Create a tuple called nested_tuple with values (("a", "b"), ("c", "d"), ("e", "f")). 
# Unpack the nested tuples into individual variables and print the second value of the third tuple.
nested_tuple = (("a", "b"), ("c", "d"), ("e", "f"))
a, b, c = nested_tuple
print(b)
# 10.Given the tuple inventory: inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
# Unpack the tuple to get each fruit and its corresponding quantity, then print the quantity of bananas.
inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
apple_quantity, banana_quantity, cherries_quantity = inventory
print(banana_quantity[1])


#1. Given the tuple student_info = ('John', 'Doe', 20, 'Computer Science'),
#  unpack it into four variables: first_name, last_name, age, and major. Then, print each variable on a new line.
student_info = ('John', 'Doe', 20, 'Computer Science')
first_name, last_name, age, major = student_info
print(student_info)
#2. Given the tuple numbers = (1, 2, 3, 4, 5, 6), use extended unpacking to assign the first element to first,
#  the last element to last, and the middle elements to middle. Print each variable.

