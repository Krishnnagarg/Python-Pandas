# Try this:

# 1. Function banao: 2 numbers ka sum
# 2. Function: Even/Odd check
# 3. Function: max of 3 numbers

# 1.
def add(a,b):
    return a+b

first_num = int(input("Enter Your First Number :- "))
second_num = int(input("Enter Your Second Number :- "))
result = add(first_num,second_num)
print(f"Sum is {first_num} + {second_num} is {result}")

# 2.
def checkNum(num):
    return "Even" if num % 2 == 0 else "Odd"

number = int(input("Enter Your Number:- "))
result = checkNum(number)
print(f"{number} is {result}")

# 3.
def maxNum(a,b,c):
    # return a if a>=b and a>=c else b if b>=a and b>=c else c
    return max(a,b,c)

first_num = int(input("Enter Your First Number :- "))
second_num = int(input("Enter Your Second Number :- "))
third_num = int(input("Enter Your Third Number :- "))

print(f"Max Number in which is {maxNum(first_num,second_num,third_num)}")
