str = input("Enter a string:::")
count=0
for i in str:
    if(i=='e'):
        count+=1
if(count==2):
    print("True")
else:
    print("False")