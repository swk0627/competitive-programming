def memo_fib(n):
    if n == 0 or n == 1:
        return 1
    if n in memo.keys():
        return memo[n]
    else:
        memo[n] = memo_fib(n-1) + memo_fib(n-2)
        return memo[n]

if __name__ == '__main__':
    num = int(input())
    memo = {}
    for i in range(num+1):
        print('{:4d}: {:<4d}'.format(i, memo_fib(i)))
    # print('{:4d}: {:<4d}'.format(num, memo_fib(num))