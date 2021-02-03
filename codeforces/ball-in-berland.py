# uncompleted

n = int(input())
line2s = []
line3s = []
for _ in range(n):
    line1 = list(map(int, input().split()))
    line2 = list(map(int, input().split()))
    line3 = list(map(int, input().split()))
    line2s.append(line2)
    line3s.append(line3)
for line2, line3 in zip(line2s, line3s):
    cnt = 0
    for i in range(len(line2)-1):
        for j in range(i+1, len(line2)):
            if line2[i] != line2[j] and line3[i] != line3[j]:
                cnt += 1
    print(cnt)