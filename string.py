
# Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s: str) -> int:
    char_map = {}
    start = max_length = 0
    for end in range(len(s)):
        if s[end] in char_map:
            start = max(start, char_map[s[end]] + 1)
        char_map[s[end]] = end
        max_length = max(max_length, end - start + 1)
    return max_length

# Longest Repeating Character Replacement
def characterReplacement(s: str, k: int) -> int:
    count = {}
    max_count = start = max_length = 0
    for end in range(len(s)):
        count[s[end]] = count.get(s[end], 0) + 1
        max_count = max(max_count, count[s[end]])
        if end - start + 1 - max_count > k:
            count[s[start]] -= 1
            start += 1
        max_length = max(max_length, end - start + 1)
    return max_length

# Minimum Window Substring
def minWindow(s: str, t: str) -> str:
    if not t or not s:
        return ""
    dict_t = Counter(t)
    required = len(dict_t)
    l, r = 0, 0
    formed = 0
    window_counts = {}
    ans = float("inf"), None, None
    while r < len(s):
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1
        while l <= r and formed == required:
            character = s[l]
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1
            l += 1
        r += 1
    return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

# Valid Anagram
def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

# Group Anagrams
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    ans = defaultdict(list)
    for s in strs:
        ans[tuple(sorted(s))].append(s)
    return list(ans.values())

# Valid Parentheses
def isValid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

# Valid Palindrome
def isPalindrome(s: str) -> bool:
    newStr = [char.lower() for char in s if char.isalnum()]
    return newStr == newStr[::-1]

# Longest Palindromic Substring
def longestPalindrome(s: str) -> str:
    def expandAroundCenter(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    if len(s) < 2 or s == s[::-1]:
        return s
    max_palindrome = ''
    for i in range(len(s) - 1):
        palindrome1 = expandAroundCenter(i, i)
        palindrome2 = expandAroundCenter(i, i + 1)
        max_palindrome = max(palindrome1, palindrome2, max_palindrome, key=len)
    return max_palindrome

# Palindromic Substrings
def countSubstrings(s: str) -> int:
    def expandAroundCenter(left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            count += 1
        return count

    total = 0
    for i in range(len(s)):
        total += expandAroundCenter(i, i)
        total += expandAroundCenter(i, i + 1)
    return total

# Encode and Decode Strings (Leetcode Premium)
class Codec:
    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        strs, i = [], 0
        while i < len(s):
            j = s.find('#', i)
            i = j + 1 + int(s[i:j])
            strs.append(s[j + 1:i])
        return strs
