x = input()
m = int(input())
d = 0
if len(x) == 1:
    if int(x) <= m: print(1)
    else: print(0)
    exit()
for c in x:
    num = int(c)
    if(d < num): d = num
left = d
right = m + 1
while right - left > 1:
    mid = (left + right) // 2
    k = 0
    s = 0
    for c in x[::-1]:
        c = int(c)
        s += c * (mid ** k)
        k += 1
    if s <= m: left = mid
    else: right = mid
print(left - d)