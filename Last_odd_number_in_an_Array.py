n=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    if i%2!=0:
        s.append(i)
print(s[-1])