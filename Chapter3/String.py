
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



names = "KrisHna garg"
print(names.lower())
print(names.upper())
print(names.capitalize())
print(names.title())

names1 = "python sql msexcel powerbi"
print(names1.split()) # convert Sting---->List
namess1 = "python,sql,msexcel,powerbi"
print(namess1.split(","))

names2 = ["Python" , "SQL" , "MsExcel" ,"Powerbi"]
print(",".join(names2)) # convert List---->String
names3 = ["Data" , "Analyst"]
print(" ".join(names3))

text = "banana"
print(text.count("a"))

email = "Krishna1705@gmail.com"
print(email.startswith("Krishna"))
print(email.endswith("@gmail.com"))

name = "Krishna"
age = 22
print(f"Hello {name} your age is {age}")