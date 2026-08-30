
for i in range(2,21,2):
    print(i)
    
    
i=2
while i<=20:
    print(i)
    i += 2


for i in range(10):
    if i==5:
        break
    print(i)

    
for i in range(10):
    if i==5:
        continue
    print(i)
    
for i in range(3):
    for j in range(2):
        print(i, j)
 
names = ["Krishna", "Rahul"] #enumerate
for index, name in enumerate(names):
    print(index, name)

names = ["Krishna", "Rakhi"]
marks = [90, 85]
for n, m in zip(names, marks):
    print(n, m)

# names = "Krishna"
# for char in names :
#     print(char)

# for i in range(len(names)):
#     print(f"{i+1} {names[i]}")