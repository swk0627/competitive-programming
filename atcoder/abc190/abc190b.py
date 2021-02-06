n, s, d = map(int, input().split())
magics = []
for _ in range(n):
    magics.append(list(map(int, input().split())))

for i in range(n):
    if not(magics[i][0] >= s or magics[i][1] <= d):
        print('Yes')
        exit()

print('No')