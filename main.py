#Exercise 1 - Squaring Numbers

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
#
# #Write your 1 line code 👇 below:
#
#
# squared_numbers = [n * n for n in numbers]
#
#
# #Write your code 👆 above:
#
# print(squared_numbers)


#Exercise 2 - Filtering Even Numbers

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
#
# #Write your 1 line code 👇 below:
#
# result = [n for n in numbers if n % 2 == 0]
#
# #Write your code 👆 above:
#
# print(result)


# Exercise 3 - Data Overlap

with open("file1.txt") as file1:
    file_1_data = file1.readlines()

with open("file2.txt") as file2:
    file_2_data = file2.readlines()

result = [int(num) for num in file_1_data if num in file_2_data]

# Write your code above 👆

print(result)