# uncompleted

t = int(input())
line1s = []
line2s = []
line3s = []
for _ in range(t):
    line1 = list(map(int, input().split()))
    line2 = list(map(int, input().split()))
    line3 = list(map(int, input().split()))
    line1s.append(line1)
    line2s.append(line2)
    line3s.append(line3)

for line2, line3 in zip(line2s, line3s):
    cnt = 0
    flg = 0
    min_conv_point = 2 * line1s[cnt][0] + 1
    for i in range(len(line2)-1):
        for j in range(i+1, len(line2)):
            if line1s[cnt][1] <= line2[i] + line2[j]:
                print('aaa')
                print(line2[i])
                flg = 1
                if min_conv_point > line3[i] + line3[j]:
                    min_conv_point = line3[i] + line3[j]
    cnt += 1

    if flg == 0: print(-1)
    else: print(min_conv_point)