def solution(s):
    s = [int(a) for a in s.split()]
    min_, max_ = min(s), max(s)
    return f"{min_} {max_}"