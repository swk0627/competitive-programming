k = int(input())
s = input()[:4]
t = input()[:4]
cnt = [ k for _ in range(10)]
for x in s:
    cnt[int(x)] -= 1
for x in t:
    cnt[int(x)] -= 1

def score(s):
    cnt = [ 0 for _ in range(10)]
    for c in s:
        cnt[int(c)] += 1
    ans = 0
    for i in range(1, 10):
        ans += i * 10 ** cnt[i]
    return ans

ans = 0

for i in range(1, 10):
    if cnt[i] == 0:
        continue
    for j in range(1, 10):
        if i == j or cnt[j] == 0:
            continue
        if score(s + str(i)) > score(t + str(j)):
            ans += cnt[i] * cnt[j]

for i in range(1, 10):
    if cnt[i] < 2:
        continue
    if score(s + str(i)) > score(t + str(i)):
        ans += cnt[i] * (cnt[i] - 1)
n = 9 * k - 8
print(ans / n / (n - 1))