examScore = [75,73,35,55,88]

print(examScore[-5])
print(examScore[-1])

examScore[-4] = 40
examScore.append(99) #adds to end of list
examScore.remove(75) #removes first occurence of the object
print(examScore)
print(len(examScore))

examScore.insert(-4,20) #inserts at index,the object
examScore.pop(-3) #removes object at the index, default is -1
print(examScore)