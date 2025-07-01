# class Book:
#     def __init__(self, title, author, no_of_pages, genre, is_published):
#         self.title = title
#         self.author = author
#         self.no_of_pages = no_of_pages
#         self.genre = genre
#         self.is_published = is_published


#     def print_info(self):
#         return f"It is {self.is_published} that {self.title} by {self.author} with {self.no_of_pages} pages is interesting"

# sweet_dreams = Book("Sweet Dreams", "Forgotten", 115, "Literature", True)
# laws_of_power = Book("48 laws of power", "lola", 125, "fiction", False)

# print(sweet_dreams.print_info())
# print(laws_of_power.print_info())
# print(sweet_dreams.title)
# print(sweet_dreams.author)
# print(laws_of_power.title)
# print(laws_of_power.author)

# class CartItem:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def total_price(self):
#         return f"{self.price * self.quantity}"

# class Cart:
#     def __init__(self, cart_items):
#         self.cart_items = cart_items

#     def total(self):
#         # cart_item = [str(item) for item in self.cart_items]
#         return 
    
# cart_item1 = CartItem("eggs", 250, 4)
# cart_item1 = CartItem("bread", 1200, 6)
# print(cart_item1.total_price())

#################### ASSIGNMENT ####################
# 1. Fill in the Line class methods to accept coordinates as a pair of tuples and 
# return the slope and distance of the line. Look up the formulas for finding the distance and slope of a line.


# class Line:
#     def __init__(self, coor1, coor2): 
#         self.coor1 = coor1
#         self.coor2 = coor2

#     def distance(self):
#         x1, y1 = self.coor1
#         x2, y2 = self.coor2
#         return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

#     def slope(self):
#         x1, y1 = self.coor1
#         x2, y2 = self.coor2
#         if x2 - x1 == 0:
#             return "slope is undefined"
#         else:
#             return (y2 - y1) / (x2 - x1)

# # # EXAMPLE EXECUTION

# coordinatel = (3,2)
# coordinate2 = (8,10)

# line_1 = Line(coordinatel, coordinate2)

# print(line_1.distance())  # 9.433981132056603
# print(line_1.slope())  # 1.6
# # 2.	Fill in the class

# class Cylinder:
#     def __init__(self, height=1, radius=1):
#         self.height = height
#         self.radius = radius 

#     def volume (self):
#         return 3.14159 * (self.radius ** 2) * self.height

#     def surface_area(self):
#         return 2 * 3.14159 * self.radius * (self.radius + self.height)

# # # EXAMPLE EXECUTION

# cylinder = Cylinder(2,3)
# print(cylinder.volume())  # 56.52
# print(cylinder.surface_area())  # 94.2


############ ACCOUNT ASSIGNMENT ############
# 
# from datetime import datetime
# age = int(input("Enter your age: "))
# current_year = datetime.now().year
# while True:
#     if age < 1:
#         print("Negative ages are not allowed")
#         break
#         continue
#     print(f"{current_year - age}")
#     break
    

