n=int(input())
l=[]
for i in range(1,n):
    if n%i==0:
        l.append(i)
s=sum(l)
if n==s:
    print("True")
else:
    print("False")