n1=float(input("enter number1:"))
operator=input("enter the operator:")
n2=float(input("enter number2:"))


if operator=='+':
    print(n1,operator,n2,"=",n1+n2)
elif operator =='-':
    print(n1,operator,n2,"=",n1-n2)
elif operator=='/':
    print(n1,operator,n2,"=",n1/n2)
elif operator=='*':
    print(n1,operator,n2,"=",n1*n2)
else:
    print("invalid input")
