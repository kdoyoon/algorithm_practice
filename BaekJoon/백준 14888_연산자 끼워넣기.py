#백트래킹

from itertools import permutations
import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
cal = list(map(int, sys.stdin.readline().split()))

maxi = -int(1e9)
mini = int(1e9)

def dfs(depth, total, plus, minus, mul, div):
    global maxi, mini
    if depth == n:
        maxi = max(total, maxi)
        mini = min(total, mini)
        
    if plus:
        dfs(depth+1, total + num[depth], plus - 1, minus, mul, div)
    if minus:
        dfs(depth+1, total - num[depth],plus, minus-1, mul, div)
    if mul:
        dfs(depth+1, total * num[depth],plus, minus, mul-1, div)
    if div:
        dfs(depth+1, int(total / num[depth]),plus, minus, mul, div-1)
        
dfs(1, num[0], cal[0], cal[1], cal[2], cal[3])

print(maxi)
print(mini)