import itertools
n = int(input())
dots = []
for _ in range(n):
    x, y = map(int, input().split())
    dots.append([x, y])
for dot in itertools.combinations(dots, 3):
    dot = list(dot)
    dot[1] = [ dot[1][0] - dot[0][0], dot[1][1] - dot[0][1] ]
    dot[2] = [ dot[2][0] - dot[0][0], dot[2][1] - dot[0][1] ]
    if(dot[1][0] * dot[2][1] == dot[1][1] * dot[2][0]):
        print('Yes')
        exit()
print('No')