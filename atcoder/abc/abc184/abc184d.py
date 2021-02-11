a, b, c = map(int, input().split())
memo = {}
def calc_mean(x, y, z):
    if x == 100 or y == 100 or z == 100:
        return 0
    key = x * 1000000 + y * 1000 + z
    if key in memo.keys():
        return memo[key]
    memo[key] = x / (x + y + z) * (calc_mean(x+1, y, z) + 1) \
        + y / (x + y + z) * (calc_mean(x, y+1, z,) + 1) \
            + z / (x + y + z) * (calc_mean(x, y, z+1) + 1)
    return memo[key]
print(calc_mean(a, b, c))