def greet(name):
    print("Hello",name)
    print("Whats going on")
greet("mbani")


def add_numbers(n1,n2):
    sum=n1+n2
    print("sum =",sum)
num1=45
num2=15
add_numbers(num1,num2)

def sub_numbers(x,y):
    sub=x-y
    return sub
result=sub_numbers(9,5)
print("sub=",result)

def get_absolute(num):
    if num>=0:
        return num
    
    else:   
        return -num
print(get_absolute(-6))