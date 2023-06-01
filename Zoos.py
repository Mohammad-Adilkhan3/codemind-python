a=input()
count=0
count1=0
for i  in a:
    if(i=='z'):
        count+=1
    if(i=='o'):
        count1+=1
if(count*2==count1):
    print("Yes")
else:
    print("No")