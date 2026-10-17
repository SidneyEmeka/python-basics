###unordered in that it stores them as hashes not face value so if you print it does'nt come out as u arranged them
###unique values in that any repeated vaalue wount be stoored cos its hashed so hash == haash will skip

myset = {1,45,67,544,200,'b','u', 2,1,2}
print(myset)

#you can cast
myName = set('Ebuka') #it splits them individually into a set unordered and uniquely
print(myName)

#you can perform maths like uniion, intersecction, minus, add etc
print(myset-myName)
print(myset | myName) #or
print(myset & myName) #and
print(myset ^ myName) #diff =>prints the ones not common