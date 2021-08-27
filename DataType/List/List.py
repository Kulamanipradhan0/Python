# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
######################################


fruits = ["Apple","Orange","Grapes","Pears"]
for i in fruits:
    print(i)
print(fruits)

# Elements are indexed starting from 0

print("0th Indexed value is : "+fruits[0])

# Last element of the list

print("Last element of the list fruits is :"+fruits[len(fruits)-1])

# Calculate the length of the List

print("Length of list fruits  is : "+str(len(fruits)))

# We can insert new elements to a list

fruits.append('Cherry') # append() method will add the element to the end
print(fruits)

fruits.insert(3,'Melon') # Insert() method will insert the element into a specified indexed position
print(fruits)

# We can also remove elements from a list

fruits.remove('Cherry') # Remove() method will remove a particular valued element from a list
print(fruits)

fruits.pop(3) # pop() method will remove an element from a list using an index value
              # If index is not specified it will remove the last element
print(fruits)

del fruits[2] #del keyword can also be used to delete an specified indexed element
print(fruits)

home_fruits = fruits
print(home_fruits)  # one way of doing it but in this case any change to old list will reflect to new one

home_fruits.insert(3,'Melon')
print("#############################")
print(fruits)
print(home_fruits)


# We can sort a list usin sort() method

fruits.sort()
print(home_fruits)

# Join two strings

fruits_extened = fruits + home_fruits
print(fruits_extened)   # See it can contain duplicates

# Create a new list by extending the current one

fruits.extend(fruits_extened)
print(fruits)
# We can copy one complete list to another using copy() method