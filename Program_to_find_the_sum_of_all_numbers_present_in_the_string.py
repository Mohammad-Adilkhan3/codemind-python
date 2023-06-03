a=input()
sum=0
for i in range  (len(a)):
    if a[i] in '123456789':
        sum=sum+int(a[i])
print(sum)