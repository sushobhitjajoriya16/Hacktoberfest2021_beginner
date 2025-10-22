# Hacktoberfest 2025 - LeetCode #3 Longest Substring Without Repeating Characters
# Sliding window, O(n)

def lengthOfLongestSubstring(s: str) -> int:
    seen = {}
    start = max_len = 0

    for i, ch in enumerate(s):
        if ch in seen and seen[ch] >= start:
            start = seen[ch] + 1
        seen[ch] = i
        max_len = max(max_len, i - start + 1)

    return max_len
