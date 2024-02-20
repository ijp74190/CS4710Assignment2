"""
Ian Pope (700717419)
Assignment 2
"""

#Part 1 Star Pattern
for i in range(1,6):    #Double loop for the first 5 rows
    for j in range(i):
        print('*', end=" ")
    print()

for i in range(4):  #Double loop for last 4 rows
    for j in range(4-i):
        print('*', end=" ")
    print()
print()


#Part 2
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#Checks the index of the item and displays if odd
print("my_list's odd indexes elements are: ", end="")
for i in range(len(my_list)):
    if i % 2 == 1:
        print(my_list[i], end=" ")
print("\n")


#Part 3
x = [23, 'Python', 23.98]
y = []

for item in x:  #Appends the type of each element in x to y
    y.append(type(item))
print(y)
print()


#Part 4
def getUniqueItems(lst):    #Function declaration
    uniqueItems = []        #Appends item to empty list if item is not in list
    for item in lst:
        if item not in uniqueItems:
            uniqueItems.append(item)
    return uniqueItems  #Returns list of items

sampleList = [1,2,3,3,3,3,4,5]
uniqueList = getUniqueItems(sampleList) #Fuction call to get unique items
print(uniqueList, "\n")


#Part 5
upper = 0
lower = 0
user = input("Enter a string: ")    #Gets string from user

for char in user:
    if char.islower():  #Checks if char is lower-case
        lower += 1
    if char.isupper():  #Checks if char is upper-case
        upper += 1

print("No. of Upper-case characters: ", upper)
print("No. of Lower-case characters: ", lower)
