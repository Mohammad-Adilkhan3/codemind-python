n=int(input())
lst=[]
for i in range(n):
    l=n%10
    lst.append(l)
    n=n//10
print(max(lst))