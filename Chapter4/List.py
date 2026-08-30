
numbers = [1,2,3]
print(numbers)

numbers.append(4)
print(numbers)

numbers.insert(1,100)
print(numbers)

numbers.remove(2)
print(numbers)

numbers.pop(0)
print(numbers)

number = [5,2,1,4,3]
number.sort()
print(number)

numbers.reverse()
print(numbers)

print(len(numbers)) 

num = [17,12,21,30,20]
num.append(31)
num.sort()
print(num)

names = ["Krishna" , "Rakhi" , "Yash" , "Shubham"]
for name in names:
    print(name)
    
numbers = [22,32,13,16,19,17,30]
total = 0
for num in numbers:
    total += num
    print("total :" , total)
    
print("total :" , total)

# fruits = ["apple" , "banana" , "mango" , "grapes"]
# fruits.append("Orange")
# print(fruits)