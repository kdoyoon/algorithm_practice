from itertools import permutations

import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
cal = list(map(int, sys.stdin.readline().split()))

operator = '+' * cal[0] + '-' * cal[1] + '*' * cal[2] + '/' * cal[3]
operator_perm = permutations(operator, n-1)

max_result = -int(1e9)
min_result = int(1e9)

for perm in operator_perm:
    result = num[0]
    
    for i in range(1, n):
        if perm[i-1] == '+':
            result += num[i]
        elif perm[i-1] == '-':
            result -= num[i]
        elif perm[i-1] == '*':
            result *= num[i]
        else:
            if result < 0 and num[i] > 0:
                result = -1 *(result*(-1) // num[i])
            else:
                result //=num[i]
                
    max_result = max(max_result, result)
    min_result = min(min_result, result)
    
print(max_result)
print(min_result)