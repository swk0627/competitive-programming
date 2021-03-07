n = int(input())
a = []
b = []
for _ in range(n):
    ab = list(map(int, input().split()))
    a.append(ab[0])
    b.append(ab[1])
tmp = 1000000
for i in range(len(a)):
    for j in range(len(b)):
        if i != j:
            mab = max(a[i], b[j])
            tmp = min(tmp, mab)
        else:
            tmp = min(tmp, a[i] + b[j])
print(tmp)