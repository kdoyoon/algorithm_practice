import sys
from itertools import combinations
n = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

p = [i for i in range(n)]
answer =  int(1e9)

for sm in combinations(p, n//2):
    lm = list(set(p) - set(sm))
    s=l=0
    
    for i, j in list(combinations(sm,2)):
        s += lst[i][j]
        s += lst[j][i]
        
    for i, j in list(combinations(lm,2)):
        l += lst[i][j]
        l += lst[j][i]
        
    answer = min(answer, abs(s-l))
    
print(answer)