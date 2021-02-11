n = int(input())
f = 1
cnt = 0
hdiv, tdiv = [], []
while f * f < n:
    if n % f == 0:
        hdiv.append(f)
        tdiv.append(n // f)
    f += 1
if f * f == n:
    hdiv.append(f)
div = hdiv + tdiv[::-1]
for i in div:
    print(i)