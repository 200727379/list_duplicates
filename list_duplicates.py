#Author: Mothapo Rampedi Lesley
#Email: rampedilesley@gmail.com
#Date: 29 April 2021

"""
Use a list to solve the following problem: Read in 20 numbers. As each number is read, print
it only if it is not a duplicate of a number already read.
	
"""
item = input("Enter list item:")
my_list = list(())
i = 0
while i < 5:
    if item not in my_list:
        my_list.append(item)
        item = input("Enter list item:")
        i = i + 1
    else:
        print("Duplicate")
        item = input("Enter list item:")
print(my_list)