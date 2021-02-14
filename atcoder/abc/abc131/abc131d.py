n = int(input())
works = []
time = 0
for _ in range(n):
    a, b = map(int, input().split())
    works.append([b, a])
works.sort()
for work in works:
    time += work[1]
    if(work[0] < time):
        print('No')
        exit()
print('Yes')