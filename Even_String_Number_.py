n=input()
v=[]
c=[]
d=0
for i in n:
    if i in "0123456789":
        v.append(int(i))
for i in v:
    if i%2==1:
        d+=1
if(d==len(v)):
    print("-1")
else:
    for i in v:
        if i not in c:
            c.append(i)
    c.sort()
    c=c[::-1]
    if c[-1]%2==0:
        for i in c:
            print(i,end="")
    else:
        for i in range(len(c)-1,0,-1):
            if c[i]%2==0:
                temp=c[i]
                c[i]=-1
                break
        for i in c:
            if i>0:
                print(i,end="")
        print(temp)