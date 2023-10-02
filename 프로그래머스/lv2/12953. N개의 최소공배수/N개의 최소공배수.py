from math import gcd

def solution(arr):
    answer = min(arr)
    for n in arr:
        answer = answer*n // gcd(answer, n)
    return answer
        
        