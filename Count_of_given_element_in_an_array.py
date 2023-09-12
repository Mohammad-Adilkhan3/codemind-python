n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=0
for i in l:
    if i==k:
        c+=1
print(c)