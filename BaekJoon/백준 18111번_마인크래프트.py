import sys

n,m,b = map(int, input().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = 10000000000000000000

for i in range(257):
    max_ = 0
    min_ = 0
    
    for j in range(n):
        for k in range(m):
            if ground[j][k] < i:
                min_ += (i - ground[j][k])
            else:
                max_ += (ground[j][k]-i)
                
    inventory = max_ + b
    
    if inventory < min_:
        continue
    time = 2 * max_ + min_
    if time <= ans:
        ans = time
        height = i
        
print(ans, height)
                

