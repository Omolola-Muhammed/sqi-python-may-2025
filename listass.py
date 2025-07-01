# Create a list called fruits with items "apple", "banana", and "orange". Print the first item.
fruits = ["apple", "banana", "orange"]
print(fruits[0])
# Create a list called colors with items "red", "green", "blue". Print the last item using negative indexing.
colors = ["red", "green", "blue"]
print(colors[-1])
# Create a list called numbers with items from 1 to 10. Print items from index 3 to index 7.
numbers = ["1", "2", "3", "4", "5","6","7","8","9","10"]
print(numbers[3:7])
# Create a list called alphabets with items "a", "b", "c", ..., "z". Print a slice from index -3 to the end.
alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print(alphabets[-3:])
# Create a list called ages with items 20, 30, 40. Change the value of the second item to 35.
ages = ["20","30","40"]
ages[1] = 35
print(ages)
# Create a list called grades with items "A", "B", "C", "D". Change the values of items from index 1 to index 3 to "X".
grades = ["A","B","C","D"]
grades[1:3] = ["X"]
print(grades)
# Create a list called cities with items "New York", "London", "Paris". Insert "Tokyo" at the beginning of the list.
cities = ["New York", "London","Paris"]
cities.insert(0, "Tokyo")
print(cities)
# Create a list called fruits with items "apple", "banana", "cherry". Print the number of items in the list.
fruits_2 = [ "apple", "banana", "cherry"]
print(len(fruits_2))
# Create a list called prices with items 10.5, 20.0, 15.75. Print the data type of the list.
prices = [10.5, 20.0, 15.75]
print(type(prices))
# Create a list called mixed with items 10, "apple", True. Print the list.
mixed = [10, "apple", True]
print(mixed)
# Create a tuple called tuple_data with items "a", "b", "c". Convert the tuple into a list.
tuple_data = ("a", "b", "c")
print(list(tuple_data))
# Create a list called books with items "Python", "Java". Append "JavaScript" to the end of the list.
books = ["Python", "Java"]
books.append("Javascript")
print(books)
# Create a list called names with items "Alice", "Bob", "Eve". Insert "Charlie" at index 1.
names = ["Alice", "Bob", "Eve"]
names.insert(1, "Charlie")
print(names)
# Create two lists called list1 and list2 with items 1, 2, 3 and 4, 5, 6 respectively. Extend list1 with list2.
list1 = [1,2,3]
list2 = [4,5,6]
list1.extend(list2)
print(list1)
# Create a list called students with items "Alice", "Bob". Add items from a tuple ("Charlie", "David") to students.
students = ["Alice", "Bob"]
tuple_ = ("Charlie", "David")
students.extend(tuple_)
print(students)
# Create a list called colors with items "red", "green", "blue". Remove "green" from the list.
colors_2 = ["red", "green", "blue"]
colors_2.remove("green")
print(colors_2)
# Create a list called numbers with items 10, 20, 30, 40. Use the del keyword to remove the item at index 2.
numbers_2 = [10, 20, 30, 40]
del[2]
print(numbers_2)
# 18.	Create a list called fruits with items "apple", "banana", "cherry". Clear the list.
fruits_3 = ["apple", "banana", "cherry"]
print(fruits_3.clear())
#  19.	Create a list called names with items "Zoe", "Alice", "Bob". Sort the list alphabetically.
names_2 = ["Zoe", "Alice", "Bob"]
print(names_2.sort())
#  20. 	Create a list called ages with items 25, 35, 20. Sort the list in descending order.
ages_2 = [25, 35, 20]
#  21. 	Sorting lists is CASE-SENSITIVE by default. Create a list called words with items 
# "Apple", "banana", "Orange". Sort the list in CASE-INSENSITIVE alphabetical order.
#  22. 	Create a list called numbers with items 1, 2, 3, 4. Print the list in reverse order.
#  23.	Create a list called letters with items "a", "b", "c", "d". Print the list in reverse order using
# 	slicing.
#  24.	Create a list called original with items "one", "two", "three". Create a copy of the list.
#  25.	Create two lists called list1 with items "a", "b" and list2 with items "c", "d". Join list1 and 
# 	list2 together.
#  26.	Access and print the second subject of the first person in the list.
# 	data = [
#     ["Alice", 25, ["Math", "Physics"]],
#     ["Bob", 30, ["Chemistry", "Biology"]],
#     ["Charlie", 35, ["History", "Geography"]]
# ]
#  27.	Access and print the first value in the list of numbers associated with "San Francisco".
# 	records = [
#     ["New York", [10, 20, 30]],
#     ["San Francisco", [40, 50, 60]],
#     ["Austin", [70, 80, 90]]
# ]
# 28.	Get the first e in Ayo’s gender and Get Ben’s age.
#  	group = [
#     ["Ayo", ["Female", 12]],
#     ["Ben", ["Male", 9]]
# ]
#  29.	Get the l in Nina’s gender and Get Tobi’s age
# 	records = [
#     ["Tobi", ["Male", [6]]],
#     ["Nina", ["Female", [7]]]
# ]
#  30.	Get the two oo’s in X1’s 2nd mobility status (loose) together (slicing) and Get the battery percentage of R2
# robot_grid = [
#     ["R2", ["battery", [98]]],
#     ["R5", ["status", "active"]],
#     ["X1", [["joint", "loose"], "error"]]
# ]
#  31.	Get the Five in the Jazz song title and Get the duration of the Jazz song
# playlist = [
#     ["Jazz", ["Take Five", 5.24]],
#     ["Pop", ["Blinding Lights", 3.20]],
#     ["Rock", ["Bohemian Rhapsody", 5.55]]
# ]
#  32.	Get the letter v in Tiger’s category and Get the first letter of the Frog’s type
# animals = [
#     ["Elephant", ["Herbivore"]],
#     ["Tiger", ["Carnivore"]],
#     ["Frog", ["Amphibian"]]
# ]



# ###########assignment2##########
# Scenario: You are managing a guest list for a high-profile wedding. You have two lists: one for the 
# confirmed guests and another for the waitlisted guests. The couple wants a simple wedding with close friends and family in attendance so there is room for only 10 guests. Follow the instructions to manage the guest lists accordingly. Write the program in a file `wedding_guest_manager.py`.
#1. Currently, Alice, Charlie, Eve, Bob, Frank, Grace, David, Hannah, Liam and Mia have accepted invitations to the wedding and are on the confirmed_guests list. The confirmed_guests list is full. New guests who accept the invitation will be waitlisted.
#2. Three siblings Ken, Jack and Ivy accept the invitation but are put on the waitlist.
#3. Noah, the groom’s ex-classmate in the university and Oliver who lives next door to the bride have accepted the invitation. Put them on the waitlist.
# Alice has a family emergency and won’t be able to attend the wedding, She cancels her attendance. Remove Alice from the confirmed guest list and add the first person from the waitlist to the confirmed list. 
# Charlie is the godfather of the groom and he is the one funding the wedding. Therefore he is a VIP guest and the couple has asked you to make sure he is on the guestlist. Check whether or not Charlie is on the guestlist.
# David and Eve have decided they no longer want to attend the wedding and therefore cancel their attendance. Remove them from the confirmed_guests list. 
# Move the first 2 people on the waitlist into the guestlist to fill up the newly freed slots.
# Oliver just realized the day of the wedding is the same day he has to take his pet to see the vet and he cancels his attendance. Remove him from the waitlist.
# The event planner has asked you for the names of the last 3 guests on the guest list because she needs to make additional arrangements for them. Get her this information.
# 10. 	The bride and groom have decided that they want to allow room for 5 more people to attend their wedding. Move 
# 	waitlisted guest (Noah) into the confirmed_guests list.
# 11. 	The event planner wants a report on the number of people who will be attending the wedding. Give her this information.
# 12. 	The event planner has also requested that you give her a list of all the names of the confirmed_guests. 
# The guests would be seated alphabetically at the venue and so she wants the names in alphabetical order.
# 13. 	A new guest called Collins who is the son of Grace and Noah would be attending on their behalf, Replace Grace and Noah 
# 	on the confirmed_guests list with Collins. Make sure you re-sort the list.
# 14. 	The caterer has also requested for the confirmed_guests list so she can provide the guests with customized bags 
# 	containing their food with their names on it. Give her a copy of the confirmed_guests list titled 
# 	guests_list_for_caterer`.
# 15. 	The deadline for accepting the invitations sent has now passed. There is no more need for the waitlist. 	Clear the 
# 	waitlist.

# At every stage from numbers 1 to 15, print out the following like so:
# print(“\n\nStage X”)
# print(“Confirmed guests: ”, confirmed_guests)
# print(“Waitlist: ”, waitlist)
# X means the current stage i.e. 1, 2, etc. If the question requests for some particular info apart from the content of confirmed_guests and waitlist such as numbers 5, 9 and 11, print it under the three lines above.
