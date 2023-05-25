n=int(input())
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end="")
    for k in range(0,i):
        print(chr(k+65),end="")
    for l in range(i-1,0,-1):
        print(chr(l+64),end="")
    print( )