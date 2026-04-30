
# def greet(): # no parameter
#     print("Hello Krishna")

# greet()


def greet(name): # parameter pass
    print(f"Hello {name}")

greet("Krishna")


def add(a,b): # with return 
    return a+b

result = add(2,3)
print(result)

 
def greetF(name="Ram"): #Default Parameter
    print(f"Hello {name}")
    
greetF("Krishna")
greetF()


def student(name, age): # keyword Arguments
    print(name, age)

student(age=20, name="Krishna")


# example
def check(num):
    return "Even" if num % 2 == 0 else "Odd"

number = int(input("Enter Your Number:- "))
print(f"{number} is {check(number)}")