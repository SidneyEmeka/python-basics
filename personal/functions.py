def isEven(n):
    return n % 2==0

def recArea(width, height = 1):  #defaut parammeteers always come last
    """
    Calculates the area of a rectangle using its Height and Width
    """
    print( (width + height) * 2)

recArea(20,10)
recArea(10,height=20) #named argumments commees last too
recArea(20)
