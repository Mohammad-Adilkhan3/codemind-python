n=input()
n=n.split(",")
l=[]
for i in n:
    i=i.split(":")
    for j in i:
        l.append(j)
for i in range(0,len(l),2):
    maxi=0
    p=[]
    u=len(l[i])
    y=l[i]
    for k in l[i+1]:
        if int(k)<=u:
            o=int(k)-1
            p.append(o)
    for i in p:
        if maxi<=i:
            maxi=i
    if maxi==0:
        print("X",end="")
    else:
        print(y[maxi],end="")