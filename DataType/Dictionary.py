#Dictionary is an unordered , indexed, changable array of elements
library = {
    'History':50,
    'Science':70,
    'General Knowledge':190,
    'Novel':502,
}
print(library)

print(library['Science'])
print(library.get('Novel')) #get method is used access any element from a dictionary
print(len(library))
# Change a value of a dictionary
library['Science']=87
print (library)

for i in library:
    print (i,library[i])

# Only print values
for i in library.values():
    print (i)


# print both keys and values
for i in library.items():
    print (i)
#membership operation
if 'Science' in library:
    print ("Science books are available")
else:
    print ("Sciene books are not there in our library")

#check if no of books are > 50
for i in library.values():
    if i >= 100:
        print(i)

# Add a new item to dictionary
library['Science Ficton']=20
print (library)
# Remove an item from a dictionary

library.pop('Science')
print (library)

library.popitem() # It will remove last inserted key
print (library)

#del library #It can delete the list completely or remove an item using a key name
#library.clear() #this will make the dictionary empty
print (library)

# Copy method will copy the whole list to a new one
newlibrary = library.copy()
print(newlibrary)

#Nested  Dictionary

Father = {
    "Name":"Trinath Pradhan",
    "Age" : 67,
    "Occupation" : "Farmer"
}

Mother = {
    "Name":"Nayana Pradhan",
    "Age" : 60,
    "Occupation" : "House Maker"
}

Wife = {
    "Name":"Sonali Pradhan",
    "Age" : 26,
    "Occupation" : "IT Engineer"
}

Self = {
    "Name":"Kulamani Pradhan",
    "Age" : 27,
    "Occupation" : "IT Engineer"
}

MyFamily = {
    "Self" : Self,
    "Wife" : Wife,
    "Father": Father,
    "Mother" : Mother
}

print (MyFamily)