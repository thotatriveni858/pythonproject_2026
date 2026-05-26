# Task 1:
# Reverse List:
# Write Python code to reverse the order of elements in the given list 
# Print the reversed list.
# my_list = [10, 20, 30, 40, 50, 11]
# # Your code here
# my_list . 
# # Output should be: [11,50,40,30,20,10]

# my_list = [10, 20, 30, 40, 50, 11]
# my_list.reverse()
# print(my_list)
# print(my_list)

# my_list = [10, 20, 30, 40, 50, 11]

# reversed_list = my_list[::-1]
# print(reversed_list)

# Task 2:
# Common Elements:
# Given two lists 
# them.
# list1 and 
# list2 , find and print the common elements between 
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]


# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# result = list(set(list1) & set(list2))
# print(result)

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# common = []

# for i in list1:
#     if i in list2:
#         common.append(i)

# print("Common elements:", common)

# Unique Elements:
# Create a new list 
# unique_list containing only the unique elements from the 
# given list 
# original_list . Print the unique list.
# original_list = [1, 2, 2, 3, 4, 4, 5]
# # Your code here
# # Output should be: [1, 2, 3, 4, 5]


#original_list = [1, 2, 2, 3, 4, 4, 5]
# original_list = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]
# result = list(set(original_list))
# print(result)

# original_list = [1, 2, 2, 3, 4, 4, 5]
# unique_list = []
# for i in original_list:
#     if i not in unique_list:
#         unique_list.append(i)
# print(unique_list)

# Task 4:
# Remove Duplicates:
# Remove duplicate elements from the given list 
# without duplicates while preserving the order.
# duplicated_list and print the list 
# duplicated_list = [1, 2, 2, 3, 4, 4, 5]
# # Your code here
# # Output should be: [1, 2, 3, 4, 5]

# duplicated_list = [1, 2, 2, 3, 4, 4, 5]
# unique_list = []
# for i in duplicated_list:
#     if i not in unique_list:
#         unique_list.append(i)
# print(unique_list)

# Exercise 1: List Concatenation
# Write a Python script that concatenates two lists and prints the result

#1. Used Operator:
# list_values = [9,8,7,6,5,4]
# list_values2 = [1,2,3,4,5]
# # print(list_values + list_values2)
# # print(list_values2 + list_values)
# result = list_values + list_values2
# print(result)

# 2. Used extend() method: [extend method is nothing but modifies the list]
# list_custval = [5,6,7]
# list_custval2 = [0,9,8]
# list_custval.extend(list_custval2)
# print(list_custval)

#3. used for for loop

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# result = list1.copy()
# for item in list2:
#     result.append(item)
# print(result)

# Exercise 2: List Repetition
# Write a Python script that repeats a list three times and prints the result

# Used the * operator
# list_value = [1,3,5,7,8,9,1,3]
# result = list_value * 5
# print(result)

#used the for :
#extend() → adds multiple elements to a list
# my_list = [1, 2, 3]
# result = []
# for i in range(3):
#     result.extend(my_list)
# print(f"Repeated List is:", result)

# Exercise 3: List Removal
# Write a Python script that removes the elements at even indices from a list.

# my_list = [10, 20, 30, 40, 50, 60] # Here, The index of 10 is 0, 20 is 1, 30 is 2,....
# result = [my_list[i] for i in range(len(my_list)) if i % 2 != 0]
# print(result)

# my_list = [10, 20, 30, 40, 50, 60]
# result = my_list[1::2]
# print(result)

# Exercise 4 List Insertion
# Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of 
# a list

# my_list = [1,1,1]
# my_list.insert(0,12)
# my_list.insert(0,11)
# my_list.insert(0,10)
# my_list.insert(6,4)
# print(my_list)

# List comprehensions
#  Square Numbers Create a list of squares of numbers from 1 to 10.
#  Even Numbers   Generate a list of even numbers from 1 to 20.
# Words Lengths Given a list of words, create a list containing the lengths of 
# each word.
# words = ["apple", "banana", "cherry", "date"]

#Square Numbers Create a list of squares of numbers from 1 to 10.
# for i in list:
#     result = i ** 2
#     print(result)

#syntax[expression for item in iterable if condition]
# squares = [i**2 for i in range(1, 11)]
# print(squares)

# Even Numbers Generate a list of even numbers from 1 to 20.
# list = [1,2,3,4,5,6,7,8,9,10,11,12]
# for i in list:
#     if i % 2 == 0:
#         print(i)

# list = [1,2,3,4,5,6,7,8,9,10,11,12]
# even_num = [i for i in list if i % 2 == 0] 
# print(even_num)

# even_numbers = [i for i in range(1, 21) if i % 2 == 0]
# print(even_numbers)

# Words Lengths Given a list of words, create a list containing the lengths of 
# each word.

# Words Lengths Given a list of words, create a list containing the lengths of 
# each word.

words = ["apple", "banana", "cherry", "date"]

lengths = [len(word) for word in words]
print(lengths)