import sys

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
parent = [0] * (n+1)
edges = []
for i in range(n+1):
    parent[i] = i

for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    edges.append((c,a,b))

edges.sort()
answer = 0
for e in edges:
    c,a,b = e
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a,b)
        answer += c
        
print(answer)