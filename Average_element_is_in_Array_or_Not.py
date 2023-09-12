n=int(input())
l=list(map(int,input().split()))
s=sum(l)
a=s//n
if a in l:
    print("True")
else:
    print("False")