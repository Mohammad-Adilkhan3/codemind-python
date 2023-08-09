import math
p,r,t=map(int,input().split())
i=(p*pow((1+(r/100)),t))
print("%.2f"%i)