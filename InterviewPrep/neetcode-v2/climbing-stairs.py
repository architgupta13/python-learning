def climbStairs(n: int) -> int:
    ### Method 1: Native recursion ###
    # if n < 0:
    #     return 0

    # if n == 0 or n == 1:
    #     return 1

    # return climbStairs(n - 1) + climbStairs(n - 2)

    ### Method 2: Memoisation -> top-down ###
    # return recursivelyClimbStairs(n, [-1 for _ in range(n + 1)])

    ### Method 3: Bottom-up ###
    # if n < 0:
    #     return 0

    # dp = [0] * (n + 1)

    # dp[0] = 1
    # dp[1] = 1

    # for i in range(2, n + 1):
    #     dp[i] = dp[i - 1] + dp[i - 2]

    # return dp[n]

    ### Method 4: Two pointers ###
    if n < 0:
        return 0

    current_minus_1, current_minus_2 = 1, 1
    for _ in range(2, n + 1):
        current_minus_1, current_minus_2 = current_minus_1 + current_minus_2, current_minus_1
    return current_minus_1


def recursivelyClimbStairs(n: int, dp: list[int]) -> int:
    if dp[n] != -1:
        return dp[n]

    if n < 0:
        return 0

    if n <= 1:
        return 1

    dp[n] = recursivelyClimbStairs(n - 1, dp) + recursivelyClimbStairs(n - 2, dp)
    return dp[n]


if __name__ == "__main__":
    inputs = [
        dict(n=2),
        dict(n=3),
    ]
    for i, input in enumerate(inputs):
        print(f"\n***** Test #{i} *****")
        print("Input:", input)
        output = climbStairs(input["n"])
        print("Output:", output)
