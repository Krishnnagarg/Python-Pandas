
# write a program store 7 fruits in a list enter by user

# fruits = []

# for i in range(7):
#     fruit = input("Enter your Fruit Name: ")
#     fruits.append(fruit)
    
# print("Fruits List : " , fruits)
    

# f1 = input("Enter Your Fruit Name: ")
# fruits.append(f1)
# f2 = input("Enter Your Fruit Name: ")
# fruits.append(f2)
# f3 = input("Enter Your Fruit Name: ")
# fruits.append(f3)
# f4 = input("Enter Your Fruit Name: ")
# fruits.append(f4)
# f5 = input("Enter Your Fruit Name: ")
# fruits.append(f5)
# f6 = input("Enter Your Fruit Name: ")
# fruits.append(f6)
# f7 = input("Enter Your Fruit Name: ")
# fruits.append(f7)

# print(fruits)


#2 WAP to accept 6 students marks and display them in sorted manner

# studs_marks = []
# for i in range(6):
#     marks = int(input("Enter YOur Marks : "))
#     studs_marks.append(marks)
    
# studs_marks.sort()

# print("Sorted Marks : " ,studs_marks)


#3 check that tuple type cannot be changed in python 

# a = (34,234,"Krishna")

# a[2] = "Rakhi"


# 4
numbers = [10,30,20,40]
# sum = 0
# for num in numbers:
#     sum += num
    
# print("Sum of list is : " , sum)
    
print("Sum of list is :" , sum(numbers)) # sum is also built-in function in python


# 5
a = (7,0,8,0,0,9)
print("Number of 0 in which :-", a.count(0))
