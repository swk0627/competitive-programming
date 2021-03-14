a, b, w = map(int, input().split())
w *= 1000
flg = True
mi = w // b
ma = w // a + 1
max_ans = 0
min_ans = 0
for num in range(mi, ma + 1):
    r = w // num
    ad = w % num
    if ad == 0:
        if a <= r <= b:
            min_ans = num
            if flg:
                max_ans = num
                flg = False
    if ad != 0:
        if a <= r and r + 1 <= b:
            min_ans = num
            if flg:
                max_ans = num
                flg = False
if max_ans == 0 and min_ans == 0: print('UNSATISFIABLE')
else: print(max_ans, min_ans)