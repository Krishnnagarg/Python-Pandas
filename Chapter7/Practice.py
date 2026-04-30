# 1. Try this:

# 1–10 print karo
# Even numbers print karo
# List ke elements print karo
# While loop se countdown

for i in range(11):
    print(i)
    
for i in range(2,11,2):
    print(i)

names = ["Krishna","Rakhi","Yash","Deepak"]
for index,name in enumerate(names):
    print(f"{index}->{name}") # f-string apply for formatted output
    
i=5
while i>=0:
    print(i)
    i-=1
    
    