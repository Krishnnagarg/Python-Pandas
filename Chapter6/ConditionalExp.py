
age = 22 
result  = "Adult" if age >= 18 else "Minor"
print(result)

a = 10
b = 20
max_num = a if a>b else b
print(f"Greater number is {max_num}")

# Multiple Conditions
num = 0
result = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
print(result)

# practice 

number = int(input("Enter Your Number :- "))
result = "Even" if number % 2 == 0 else "Odd"
print(f"{number} is {result}") # f-string used for formating output


num1 = int(input("Enter Your Number :- "))
result = "Positive" if num1 > 0 else "Negative" if num1 < 0 else "Zero"
print(f"Your {num1} number is :- {result}")