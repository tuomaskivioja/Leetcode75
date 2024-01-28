# Sum of Two Integers
def getSum(a: int, b: int) -> int:
    mask = 0xffffffff
    while b & mask:
        a, b = a ^ b, (a & b) << 1
    return a & mask if b > mask else a | b

# Number of 1 Bits
def hammingWeight(n: int) -> int:
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# Counting Bits
def countBits(n: int) -> List[int]:
    res = [0] * (n + 1)
    for i in range(1, n + 1):
        res[i] = res[i & (i - 1)] + 1
    return res

# Missing Number
def missingNumber(nums: List[int]) -> int:
    expected_sum = len(nums) * (len(nums) + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Reverse Bits
def reverseBits(n: int) -> int:
    res = 0
    for i in range(32):
        res <<= 1
        res |= (n & 1)
        n >>= 1
    return res
