a,b=map(int,input().split())
if(b-a==1 or a-b==1):
    print("Yes")
elif(b-a==9 or a-b==9):
    print("Yes")
else:
    print("No")