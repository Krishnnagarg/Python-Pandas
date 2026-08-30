
# student={
#     "name":"Krishna",
#     "age":21,
#     "marks":90
# }

# print(student)
# print(student.get("name"))
# print(student.get("home"))

# student["city"] = "Safidon"
# print(student)

# student.pop("marks")
# print(student)


# print(student.keys())
# print(student.values())
# print(student.items())



# student = {
#     "name" :"Krishna",
#     "age" :21,
#     "marks":85
# }

# print(student["name"])

# student["city"] = "safidon"
# student["age"] = 22
# print(student.keys())
# print(student.values())
# print(student.items())

# print(f"student name is {student.get("name")}")

# for key,value in student.items():
#     print(key,value)

# student.update({"name":"Rakhi"})
# print(student.get("name"))


# students ={
#     "name":"Krishna",
#     "age":21,
#     "marks":85
# }

# students["city"] = "safidon"  #add new key value pair
# students["marks"] = 90   #update marks 

# for key,value in students.items():  #print using loop
#     print(key,value)
    
# x = [1,2,3,4,5]

# for i in x:
#     if i == 3:
#         x.remove(i)
    
# print(x)


students = {
    "name":"Krishna",
    "age":22,
    "city":"safidon"
}

print(students)

students["age"] = 23 # value update if key exists 
print(students)

for key in students:
    print(key)
    
for value in students.values():
    print(value)

for key , value in students.items():
    print(key ,"---->", value)

print(students["name"])
print(students["age"])
# print(students["state"]) # show error

print(students.get("name"))
print(students.get("age"))
print(students.get("state"))

students.pop("age")
print(students)
print(students.get("age"))

print(len(students))

print("name" in students)
print("name" not in students)

print(students.keys())
print(students.values())
print(students.items())

