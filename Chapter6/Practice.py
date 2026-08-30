# example 1 :- WAP to Find the greatest of 4 numbers Entered by users

# a = int(input("Enter Your Number 1 :- "))
# b = int(input("Enter Your Number 2 :- "))
# c = int(input("Enter Your Number 3 :- "))
# d = int(input("Enter Your Number 4 :- "))

# # max_num = a if a>=b and a>=c and a>=d else b if b>=a and b>=c and b>=d else c if c>=b and c>=a and c>=d else d 
# # print(f"Greatest number is {max_num}")

# max_num = max(a,b,c,d)
# print(f"Greatest number is {max_num}")


# example 2 :- WAP to find out wheather a student pass or failed .
# if it require a total of 40% and at least 33% in each subject to pass

# sub1 = int(input("Enter Your Marks :- "))
# sub2 = int(input("Enter Your Marks :- "))
# sub3 = int(input("Enter Your Marks :- "))

# totalMarks = sub1 + sub2 + sub3
# percentage = totalMarks/3

# result = "Pass" if percentage >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33 else "Fail"
# print(f"Student will be {result} with {percentage}%")

# example 3

# username = input("Enter Your username :- ")

# if (len(username) < 10):
#     print("Your Username contains Less than 10 Character")
# else:
#     print("All is Well ")
    
    
# example 4

# l = ["Krishna","Rakhi","Yash"]
# name = input("Enter YOur Name :- ")

# if(name in l):
#     print("Your Name in list")
# else :
#     print("Your Name is not lies in List")
    
    
    
names = ["Krishna","Rakhi","Yash","Deepak","Vashu"]
name = input("Enter Your Name :- ")

if (name in names):
    print(f"{name} your name in List")
else :
    print(f"{name} your name not in list")