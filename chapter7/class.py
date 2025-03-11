class Number:
    def add(self,a,b):
        return a+b
    def multiply(self,a,b):
        return a*b

#instantiate an object

n1=Number()

sum=n1.add(5,6)
print(sum)

product=n1.multiply(3,4)
print(product)