
# 1. Create Table 

n = int(input("Enter Your number :- "))

for i in range(1,11):
    print(f"{n}*{i} = {n*i}")

# 2. Select in list whose name start with K 

names = ["Krishna","Rakhi","Yash","Kashmir","Kiran"]

for name in names:
    if (name.startswith("K")): 
        print(f"Hello {name}")

    