def minCostClimbingStairs(cost: list[int]) -> int:
    # ### Method 1: Bottom-up ###
    # num_stairs = len(cost) + 1

    # dp = [0] * num_stairs

    # for i in range(2, num_stairs):
    #     dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

    # return dp[num_stairs - 1]

    # ### Method 2: Native recursion ###
    # return recursiveMinCostClimbingStairs(cost)

    # ### Method 3: Top-down memoization ###
    # cache = [-1] * (len(cost) + 1)
    # return topDownMinCostClimbingStairs(cost, cache)

    ### Method 4: Two pointers ###
    last_step, last_to_last_step = 0, 0
    for i in range(2, len(cost) + 1):
        last_step, last_to_last_step = min(cost[i-1] + last_step, cost[i-2] + last_to_last_step), last_step
    return last_step


def topDownMinCostClimbingStairs(cost: list[int], dp: list[int]) -> int:
    num_stairs = len(cost)
    if dp[num_stairs] != -1:
        return dp[num_stairs]

    if num_stairs <= 1:
        return 0

    dp[num_stairs] = min(topDownMinCostClimbingStairs(cost[:-1], dp) + cost[-1], topDownMinCostClimbingStairs(cost[:-2], dp) + cost[-2])
    return dp[num_stairs]


def recursiveMinCostClimbingStairs(cost: list[int]) -> int:
    if len(cost) <= 1:
        return 0

    return min(
        recursiveMinCostClimbingStairs(cost[:-1]) + cost[-1],
        recursiveMinCostClimbingStairs(cost[:-2]) + cost[-2],
    )


if __name__ == "__main__":
    inputs = [
        dict(cost=[10, 15, 20]),
        dict(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]),
    ]
    for i, input in enumerate(inputs):
        print(f"\n***** Test #{i} *****")
        print("Input:", input)
        output = minCostClimbingStairs(input["cost"])
        print("Output:", output)
