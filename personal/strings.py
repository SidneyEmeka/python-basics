#Strings are imutable so we can't add remove with indexes

name = 'gering'

print(name[1:3]) #like a range, from index 1 to 2{excludes 3}
print(name[:3]) #like a range, from index 0 to 2{excludes 3}
print(name[0:]) #like a range, from index 0 to the last
print(name[-1]) #Prints the last letter now counting from the last, -1 to -6{no 0 this time}