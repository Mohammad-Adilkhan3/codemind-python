a=input()
s=0
for i in a:
    b=a.count(i)
    if(b==1):
        print(a.index(i))
        s=1
        break
if(s==0):
    print("-1")