def climbStairs(n, i=0):
    if i > n:
        return 0
    if i == n:
        return 1
    ways = climbStairs(n, i+1) + climbStairs(n, i+2)
    return ways


# print(climbStairs(2))
# print(climbStairs(3))


def climbStairs2(n, i=0, memo={}):
    print(memo)
    if (i, n) in memo:
        return memo[(i, n)]
    if i > n:
        return 0
    if i == n:
        return 1
    memo[(i, n)] = climbStairs(n, i+1) + climbStairs(n, i+2)
    print(memo)
    return memo[(i, n)]


# print(climbStairs2(2))
# print(climbStairs2(3))

def climbStairs3(n, memo={}):
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in memo:
        return memo[n]
    memo[n] = climbStairs3(n - 1, memo) + climbStairs3(n - 2, memo)

    return memo[n]


print(climbStairs3(2)) # Answer = 2
print(climbStairs3(3)) # Answer = 3


# climbStairs2 and climbStairs3 have the same time complexity O(n) and climbStairs1 has a time complexity of O(2^n)