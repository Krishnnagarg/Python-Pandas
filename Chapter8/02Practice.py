
# 1. Find Max Num 

# def find_max(a,b,c):
#     return max(a,b,c)

# first_num = int(input("Enter Your First Num :- "))
# second_num = int(input("Enter Your second Num :- "))
# third_num = int(input("Enter Your third Num :- "))
# result = find_max(first_num,second_num,third_num)
# print(f"Max number in which is :- {result}")

# 2. sum of n number using recursion 

# def sumOfNumber(num):
#     if num == 0:
#         return 0
#     return num + sumOfNumber(num-1)

# first_num = int(input("Enter Your First Num :- "))
# result = sumOfNumber(first_num)
# print(f"Sum of {first_num} is :- {result}")

# 3. convert inches to cm

# def convertInCm(num):
#     return num * 2.54  # cm = inch * 2.54 this is formula 
    
# number = int(input("Enter Your inch :- "))
# result = convertInCm(number)
# print(f"{number} inch is equal to {result} cm")

# 4. Pattern Print

def printPattern(num):
    if num == 0: # base condition apply in recursion is mandatory
       return
    print("* " * num)
    printPattern(num - 1) # recurison apply 
    
number = int(input("Enter Your number :- "))
printPattern(number)