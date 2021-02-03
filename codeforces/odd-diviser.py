# uncompleted

n = int(input())
nums = [ int(input()) for _ in range(n)]
lower_divisor = 2
upper_divisor = 2

for num in nums:
    flg = 0
    i = 1
    while(i * i <= num):
        if num % i == 0:
            lower_divisor = i
            if num != i * i: upper_divisor = num // i
        if (lower_divisor != 1 and lower_divisor % 2 == 1) or upper_divisor % 2 == 1:
            flg = 1
            break
        i += 1
    if flg == 1: print('YES')
    else: print('NO')