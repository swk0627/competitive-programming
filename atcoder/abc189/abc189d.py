n = int(input())
s = [ input() for _ in range(n)]
cnt = 1
for i in reversed(range(len(s))):
    if s[i] == 'OR': cnt += 2**(i+1)
print(cnt)