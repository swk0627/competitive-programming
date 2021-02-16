n, k = map(int, input().split())
s = input()
u = []
for i in range(k):
    s *= 2
    for j in range(0, len(s) - 1, 2):
        if s[j] == 'R' and (s[j+1] == 'S' or s[j+1] == 'R'):
            u.append('R')
        if s[j] == 'R' and s[j+1] == 'P':
            u.append('P')
        if s[j] == 'S' and (s[j+1] == 'P' or s[j+1] == 'S'):
            u.append('S')
        if s[j] == 'S' and s[j+1] == 'R':
            u.append('R')
        if s[j] == 'P' and (s[j+1] == 'R' or s[j+1] == 'P'):
            u.append('P')
        if s[j] == 'P' and s[j+1] == 'S':
            u.append('S')
    s = ''.join(u)
    u.clear()
print(s[0])