list=[1,1,1,3,4,2,44,22,21,33,22]
print("Original list::", list)

temp=[]

for i in list:
    if i not in temp:
        temp.append(i)
print("After removing duplicates:::",temp)
