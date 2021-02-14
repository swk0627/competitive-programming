t = int(input())
LR = []
for _ in range(t):
    l, r = map(int, input().split())
    LR.append([l, r])
for lr in LR:
    if lr[1] % 2 == 0:
        num = lr[1] // 2 - lr[0]
        if num < 0:
            print(0)
            continue
        print((num+1)*(2*num+1))
    if lr[1] % 2 == 1:
        num = lr[1] // 2 - lr[0]
        if num < 0:
            print(0)
            continue
        print((num+1)*(2*num+3))