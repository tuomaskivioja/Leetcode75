
# Climbing Stairs
def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    first, second = 1, 2
    for i in range(3, n + 1):
        third = first + second
        first, second = second, third
    return second

# Coin Change
def coinChange(coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# Longest Increasing Subsequence
def lengthOfLIS(nums: List[int]) -> int:
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# Word Break Problem
def wordBreak(s: str, wordDict: List[str]) -> bool:
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for word in wordDict:
            if i >= len(word) and s[i - len(word):i] == word:
                dp[i] = dp[i] or dp[i - len(word)]
    return dp[n]

# Combination Sum IV
def combinationSum4(nums: List[int], target: int) -> int:
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if i >= num:
                dp[i] += dp[i - num]
    return dp[target]

# House Robber
def rob(nums: List[int]) -> int:
    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    if len(nums) == 2:
        return max(nums[0], nums[1])

    # Initialize the dynamic programming array
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        # Calculate the maximum amount for the current house by choosing between:
        # 1. Robbing the current house and the maximum amount for (i-2) houses
        # 2. The maximum amount for (i-1) houses
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

    return dp[-1]
