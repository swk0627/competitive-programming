# uncompleted

n = int(input())
nums = [ int(input()) for _ in range(n)]

for num in nums:
    cnt = 0
    s = 0
    flg = 0
    while(s <= num):
        s += 2020
        cnt += 1
    s -= 2020
    cnt -= 1
    for i in range(cnt):
        if(s + i + 1 == num):
           flg = 1
           break
    if flg == 1: print('YES')
    else: print('NO')