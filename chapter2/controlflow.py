num1=-5
num2=12
num3=8

if (num1>=num2) and (num1>=num3):
    largest=num1
elif(num2>=num1) and (num2>=num3):
    largest=num2
else:
    largest=num3
print("largest number is:",largest)

my_range=range(1,5)
a=0
for val in my_range:
    a=a+1
print(a)