# ==============================================EXERCISES==============================================
# 🛒 1. Grocery Store – Find Common Items in Carts
# Exercise:
# You have two shopping carts. Each contains a list of items. Use sets to find:

# Items both people are buying # eggs, butter

# Items only one of them is buying   # milk, bread, cheese, yoghurt

# All items either of them is buying # milk, bread, eggs, butter, cheese, yoghurt

# cart1 = ["milk", "bread", "eggs", "butter"]
# cart2 = ["eggs", "butter", "cheese", "yogurt"]

# same_item = set(cart1).intersection(set(cart2))
# print(same_item)

# one_of_them = set(cart1.)

# 🎟 2. Movie Club – Count Unique Movies Watched
# Exercise:
# Three friends watched movies over the weekend. Each of them lists the movies they saw. Use sets to find out:

# How many unique movies were watched in total.

# alice = {"Inception", "Titanic", "Joker"}
# bob = {"Joker", "Interstellar", "Inception"}
# carol = {"Avatar", "Titanic", "Joker"}

# unique = alice.union(bob).union(carol)
# print(unique)

# Answer: "Inception", "Titanic", "Joker", "Interstellar", "Avatar"

# 🧑‍🤝‍🧑 3. Party Invite List – Avoid Duplicates
# Exercise:
# You’re creating a guest list. Some names were added twice by mistake. Use a set to fix this.

# guest_list = ["Alice", "Bob", "Charlie", "Alice", "Bob", "Diana"]
# print(set(guest_list))

# 🏫 4. Students in Clubs – Who’s in Both?
# Exercise:
# In a school, some students are in the science club, and some are in the music club. Find students who are in both.

# science_club = {"John", "Mia", "Liam", "Olivia"}
# music_club = {"Emma", "Liam", "Noah", "Olivia"}

# science_music = science_club.intersection(music_club)
# ==============================================EXERCISES==============================================


############################ ASSIGNMENT ##################
# Create a set called fruits with values {"air", "water", "food"}. Check if "food" is in 
# the set and print the result.
fruits = {"air", "water", "food"}
print("food" in fruits)
# Create a set called colors with values {"red", "green", "blue"}. Add the color "yellow" 
# to the set and print the updated set.
colors = {"red", "green", "blue"}
colors.add("yellow")
print(colors)
# Given the set animals = {"cat", "dog", "rabbit"}, add multiple items ["horse", "sheep"] to the set 
# and print the updated set.
animals = {"cat", "dog", "rabbit"}
more_animals = ("horse", "sheep")
animals.update(more_animals)
print(animals)
# Create a set called countries with values {"USA", "Canada", "Mexico"}. Remove "Canada" from the set and
#  print the updated set.
countries = {"USA", "Canada", "Mexico"}
countries.remove("Canada")
print(countries)
# Given the set cities = {"New York", "Los Angeles", "Chicago"}, remove "Houston" which is not in the set
#  without raising an error.
cities = {"New York", "Los Angeles", "Chicago"}
cities.discard("Houston")
print(cities)
# Given the list seasons = ["Spring", "Summer", "Fall", "Winter", “Spring”], convert the list to a set to get rid
#  of the duplicate `Spring`.
seasons = ["Spring", "Summer", "Fall", "Winter", "Spring"]
print(set(seasons))
# Create two sets, set1 = {1, 2, 3} and set2 = {3, 4, 5}. Use the union method to join the sets and print the result.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)
# Given two sets, setA = {"a", "b", "c"} and setB = {"c", "d", "e"}, find the intersection of the sets and print the result.
setA = {"a", "b", "c"}
setB = {"c", "d", "e"}
setA.intersection(setB)
print(setA)
# Create a set called prime_numbers with values {2, 3, 5, 7}. Add the number 11 to the set and print the updated set.
prime_numbers = {2, 3, 5, 7}
prime_numbers.add(11)
print(prime_numbers)
# Given the set odd_numbers = {1, 3, 5, 7, 9}, remove a random item from the set and print the updated set.
odd_numbers = {1, 3, 5, 7, 9}
odd_numbers.pop()
print(odd_numbers)
# Create a set called vowels with values {"a", "e", "i", "o", "u"}. Empty the set and print the result.
vowels = {"a", "e", "i", "o", "u"}
vowels.clear()
print(vowels)
# Given the set letters = {"a", "b", "c"}, find the difference between `letters` and another set {"b", "c", "d"}. 
# Print the result. Afterwards, find the symmetric difference and print the result.
letters = {"a", "b", "c"}
another_set = {"b", "c", "d"}
symm_diff = letters.symmetric_difference(another_set)
print(symm_diff)
#  13.	Create a set called tech_brands with values {"Apple", "Google", "Microsoft"}. 
# 	Add the items from another set {"Amazon", "Facebook"} and print the updated set 
# 	tech_brands without creating a new set.
tech_brands = {"Apple", "Google", "Microsoft"}
brand_2 = {"Amazon", "Facebook"}
tech_brands.update(brand_2)
print(tech_brands)
#  14. 	Create a set called students with values {"Alice", "Bob", "Charlie", "David"}. Use the 
# 	remove method to remove "Charlie" from the set and print the updated set. Then try to 
# 	remove "Eve" from the set and observe the behavior.
students = {"Alice", "Bob", "Charlie", "David"}
students.remove("Charlie")
print(students)
# students.remove("Eve")
# print(students)
#  15. 	Given a list numbers_list = [1, 2, 3, 4, 4, 5, 5], convert this list to a set to remove 
# 	duplicates and print the resulting set.
numbers_list = [1, 2, 3, 4, 4, 5, 5]
print(set(list(numbers_list)))
#  16. 	Given a string text = "hello", convert this string to a set to find the unique 
# 	characters and print the resulting set.
text = "hello"
print(set(text))
#  17. 	Create a set called vehicles with values {"car", "bike", "bus", "train"}. Find out how 
# 	many items are in the set and print the result.
vehicles = {"car", "bike", "bus", "train"}
print(len(vehicles))
#  18. 	Given the set gadgets = {"laptop", "smartphone", "tablet", "smartwatch"}, print the 
# 	number of items in the set.
gadgets = {"laptop", "smartphone", "tablet", "smartwatch"}
print(len(gadgets))