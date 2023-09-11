n=int(input())
l=list(map(int,input().split()))
so=0
for i in range(0,n,2):
    so+=l[i]
print(so)
    