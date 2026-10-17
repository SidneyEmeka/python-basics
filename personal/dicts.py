#just like seets but key value pair
#its mutable
theBonds = {"A": 23, "B": 33, "D": 5}
print(theBonds['B']) #or
print(theBonds.get("a", "Fool e no dey")) #the secoond argumnent is a fall back for keys that doesnt exist

#we can create a dict from a set
theSet = {23,33,4,33,43}
theKeys = ["w",'x','i','u','p']

theDict = dict(zip(theKeys,theSet))
print(theDict['x'])
