a=int(input("Enter a positive integer: "))
try:
    if a<=0:
        raise ValueError("Not a positive number")
    print("you entered:", a)
except:
    print("invalid")