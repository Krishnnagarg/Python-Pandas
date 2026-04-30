
# name = "Krishna"
# a = len(name)
# print(a)

# b = name[1:4] # start index include but last index not include
# print(b) # ris 


name = "hello world"
print(len(name))
print(name.endswith("hna"))
print(name.startswith("Kri"))
print(name.capitalize()) 
print(name.upper())
print(name.lower())
print(name.replace("hello" , "hi"))
print(name.find("world"))

text = "hello bhai kaise ho"
print(text.split())

first = "Hello"
second = "Bhai"

result = first + " " + second
print(result)

name = input("Enter your name: ")

print("Welcome " + name) # + is only used for concat string 
print("Welcome " , name) # always used , 


word = "  hello WORLD"
print(word.strip().lower().replace("world","Krishna").title())

a = "Krishna is a \'good\' boy "
print(a)