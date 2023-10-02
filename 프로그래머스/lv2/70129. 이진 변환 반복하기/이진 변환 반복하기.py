def solution(s):
    cnt_0 = 0
    cnt = 0
    while True:
        if s == '1':
            break
        else:
            cnt_0 += s.count('0')
            temp = sum([int(a) for a in s])
            cnt += 1
            s = bin(temp)[2:]
    return [cnt, cnt_0]
    