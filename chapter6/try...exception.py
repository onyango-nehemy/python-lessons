def findReciprocal(value):
    try:
        print("Value",value)
        r=1/value
        print("The reciprocal of ", value, "is",r,"\n")
    except:
        print("You cannot find reciprocal of ",value,"\n")
findReciprocal(2)
findReciprocal("Hello")