
# def print_num(n):
#     if n==0:
#         return
#     print(n)
#     print_num(n-1)
    
# print_num(6)


# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)

# num = int(input("Enter Your Number :- "))
# result = factorial(num)
# print(f"Factorial of {num} is :- {result}")


# def print_num(n):
#     if n == 0:
#         return 
#     print_num(n-1)
#     print(n)


# num = int(input("Enter Your Number :- "))
# print_num(num)


def print_num(n):
    if n==0:
        return
    print_num(n-1)
    if n % 2 == 0:
        print(n)
    

num = int(input("Enter Your Number :- "))
print_num(num)
