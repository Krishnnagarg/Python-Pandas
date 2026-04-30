
l = [10,2,3,4,5,6,7,8,9]

for i in l:
    print(i)

i=0
while i<len(l):
    print(l[i])
    i += 1
    
    
for i in range(2,21,2):
    print(i)

i = 1
while i <= 5 :
    print(i)
    i += 1
    
# break
for i in range(10):
    if i == 5:
        break
    print(i)
    
# continue    
for i in range(10):
    if i == 2:
        continue
    print(i)

# Nested loop

for i in range(3):
    for j in range(2):
        print(i, j)

# Loop With String

name = "Krishna"
for ch in name:
    print(ch)