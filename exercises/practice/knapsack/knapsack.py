def maximum_value(maximum_weight, items):
    n = len(items)
    dp = [[0 for _ in range(maximum_weight + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight, value = items[i - 1]["weight"], items[i - 1]["value"]
        for j in range(1, maximum_weight + 1):
            if weight <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][maximum_weight]