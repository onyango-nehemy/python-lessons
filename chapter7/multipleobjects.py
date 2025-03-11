class MyClass:
    a=20
    def func(self):
        return 'Hello'
#create objects from it now

ob1=MyClass()
ob2=MyClass()

print(ob1.func())
print(ob2.a)

ob1.a=100
ob2.a=300

print(ob1.a)
print(ob2.a)