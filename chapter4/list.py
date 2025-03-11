numbers=[1,44,10,100,3.33]
#accessing list elements
print(numbers[0])
print(numbers[4])
print(numbers[3])

#also we can talk about negative indexing

my_list=['p','y','t','h','o','n']

print(my_list[-1])
print(my_list[-6])

print(my_list[2:5])

#changing the items of the list

odd=[2,4,6,8]
odd[0]=1
print(odd)

odd[1:4]=[3,5,7]
print(odd)

odd1=[1,3,5]
odd1.append(7)
print(odd1)
odd1.extend([7,9,11])
print(odd1)

#looping through the lists
fruits=['apple','banana','mango']

for fruit in fruits:
    print("i love",fruit)