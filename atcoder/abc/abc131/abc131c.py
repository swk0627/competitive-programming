import math
lcm = lambda x, y: int(x * y / math.gcd(x, y))
a, b, c, d = map(int, input().split())
q_c = b // c - (a - 1) // c
q_d = b // d - (a - 1) // d
q_cd = b // lcm(c, d) - (a - 1) // lcm(c, d)
print((b - (a - 1)) - (q_c + q_d - q_cd))