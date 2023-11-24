n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input())) 
lst.sort()
for a in lst:
    print(a)