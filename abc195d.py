import copy
n, m, q = map(int, input().split())
wvs = []
for _ in range(n):
    w, v = map(int, input().split())
    wvs.append([w, v])
x = list(map(int, input().split()))
qs = []
for _ in range(q):
    qs.append(list(map(int, input().split())))
tmp = copy.deepcopy(wvs)
for q in qs:
    wvs = copy.deepcopy(tmp)
    ans = 0
    left = q[0] - 1
    right = q[1]
    nx = x[:left] + x[right:]
    nx.sort()
    for box in nx:
        mav = 0
        for wv in wvs:
            if wv[0] <= box and mav <= wv[1]:
                mai = wv[0]
                mav = wv[1]
        if mav != 0: wvs.remove([mai, mav])
        ans += mav
    print(ans)