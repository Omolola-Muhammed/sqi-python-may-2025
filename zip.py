# ===================================ASSIGNMENT===================================
# Use only for loops for the problems below:

# 1. You are given two lists, names and grades. Print them together
# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']

# Expected Output:
# Ken got grade A
# Mia got grade E
# Rose got grade F
# Henry got grade C
# Suzan got grade B

# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']
# for name, grade in zip(names, grades):
#     print(f"{name} got grade {grade}")
     

# 2. Print only the items at even indexes
# items = ['zero', 'one', 'two', 'three']

# Expected Output:
# 0: zero
# 2: two
# items = ['zero', 'one', 'two', 'three']
# for index, items in enumerate(items):
#     if index % 2 == 0:
#         print(f"{index}: {items}")

# 3 Given two lists of numbers of the same length, print the indices and values of where they differ in a list.
# list1 = [5, 8, 6, 7, 12, 4]
# list2 = [5, 3, 6, 9, 12, 0]

# Expected output:
# [
#   'Index 1: 8 != 3',
#   'Index 3: 7 != 9',
#   'Index 5: 4 != 0',
# ]
# list1 = [5, 8, 6, 7, 12, 4]
# list2 = [5, 3, 6, 9, 12, 0]

# for index in range(len(list1)):
#     if list1[index] != list2[index]:
#         print(f"index {index}: {list1[index]} != {list2[index]}")
# ===================================ASSIGNMENT===================================