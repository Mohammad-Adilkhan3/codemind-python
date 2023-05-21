from itertools import permutations
n=input()
l=list(permutations(range(0,len(n))))
for i in l:
    for j in i:
        print(n[j],end="")
    print()