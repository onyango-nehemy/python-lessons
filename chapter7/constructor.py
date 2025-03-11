class MyClass:
    def __init__(self,p1=0,p2=0):
        self.a=p1
        self.b=p2
o1=MyClass(2,3)
print((o1.a,o1.b))

o2=MyClass()
print((o2.a,o2.b))
         