
numbers = {1,2,3,4,5,6}
numbers_2 = {5,6,7,8,9,10}
print(numbers)
print(len(numbers))

numbers.add(7)
print(numbers)

numbers.discard(8)
print(numbers)

for nums in numbers:
    print(nums)
    
print(numbers | numbers_2) #union 
print(numbers & numbers_2) #intersection
print(numbers - numbers_2) #difference

# example
marks = {90,26,38,28,28,38,20}
unique = set(marks)
print(unique)

# example 
emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com"]
unique_emails = set(emails)
print(unique_emails)

# example 
num_1 = [10,20,20,30,40]
num_11 = set(num_1)
num_11.add(50)
print(num_11)