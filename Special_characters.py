n=input()
c=0
e=[]
o=[]
for i in n:
    if i in "!@#$%^&*(){}/|[].,<>+=-*":
        c+=1
    if i in "0123456789":
        if int(i)%2==0:
            e.append(i)
        else:
            o.append(i)
if c%2==0:
    for i in range(min(len(e),len(o))):
        print(e[i]+o[i],end="")
else:
    for i in range(min(len(e),len(o))):
        print(o[i]+e[i],end="")
if len(e)>len(o):
    for i in range(len(o),len(e)):
        print(e[i],end="")
else:
    for i in range(len(e),len(o)):
        print(o[i],end="")