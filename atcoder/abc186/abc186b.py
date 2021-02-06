H, W = map(int, input().split())
s = 0
A_min = 101
for _ in range(H):
	nums = list(map(int, input().split()))
	s += sum(nums)
	A_min = min(A_min, min(nums))
print(s - (A_min * H * W))