def calculate_average(scores):
    return (sum(scores))/len(scores)

theScores = [33,44,24,45,33,22,45,55,5]

avg = calculate_average(theScores)
print(avg)

def studResult(name,score):
    return f'Your name is {name.upper()}, you got {score}'

report = studResult(score=40,name="Sidney")
print(report)