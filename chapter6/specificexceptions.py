#here we handle specific exceptions
def findReciprocal(value):
    try:
        print("Value:", value)
        r=1/value
        print("The Reciprocal of ",value,"is", r)
    except ValueError:
        print("you got value error")
    except ZeroDivisionError:
        print("You got zero division error")
    except:
        print("handling all other errors")
findReciprocal(0)