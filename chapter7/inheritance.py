class polygon:
    def __init__(self,no_of_sides):
        self.n=no_of_sides
        self.sides=[]
        for i in range(no_of_sides):
            self.sides.append(0)
    def input_sides(self):
        for i in range(self.n):
            self.sides[i]=float(input("enter the sides " + str(i+1 )+":"))

#inheriting triangle from the polygon class
class Triangle(polygon):
    def __init__(self):
        polygon.__init__(self,3)
    def find_area(self):
        a,b,c=self.sides
        #calculate the semi-perimeter
        s=(a+b+c)/2
        area=(s*(s-a)*(s-b)*(s-c))**0.5
        print("the area of the  triangle is ",area)

t=Triangle()
t.input_sides()
t.find_area()
