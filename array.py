
# Two Sum
def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums_dict = {}
    for i, num in enumerate(nums):
        if target - num in nums_dict:
            return [nums_dict[target - num], i]
        nums_dict[num] = i

# Best Time to Buy and Sell Stock
def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0
    min_price = float('inf')
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

# Contains Duplicate
def containsDuplicate(self, nums: List[int]) -> bool:
    return len(nums) > len(set(nums))

# Product of Array Except Self
def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    left_products = [1 for _ in nums]
    right_products = [1 for _ in nums]
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]
    return [left_products[i] * right_products[i] for i in range(n)]

# Maximum Subarray
def maxSubArray(self, nums: List[int]) -> int:
    max_sum = nums[0]
    curr_sum = nums[0]
    for i in range(1, len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(max_sum, curr_sum)
    return max_sum

# Maximum Product Subarray
def maxProduct(self, nums: List[int]) -> int:
    max_product = nums[0]
    curr_max = nums[0]
    curr_min = nums[0]
    for i in range(1, len(nums)):
        temp_max = curr_max * nums[i]
        temp_min = curr_min * nums[i]
        curr_max = max(nums[i], temp_max, temp_min)
        curr_min = min(nums[i], temp_max, temp_min)
        max_product = max(max_product, curr_max)
    return max_product

# Find Minimum in Rotated Sorted Array
def findMin(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    if nums[0] < nums[-1]:
        return nums[0]
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        if nums[mid] < nums[mid - 1]:
            return nums[mid]
        if nums[mid] > nums[0]:
            left = mid + 1
        else:
            right = mid - 1

# Search in Rotated Sorted Array
def search(self, nums: List[int], target: int) -> int:
    if not nums:
        return -1
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if nums[start] <= nums[mid]:
            if nums[start] <= target <= nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] <= target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1

# 3 Sum
def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return res

# Container With Most Water
def maxArea(self, height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        curr_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, curr_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area