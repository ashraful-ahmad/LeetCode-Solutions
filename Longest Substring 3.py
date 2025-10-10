"In this problem, we need to find the length of the longest substring without repeating characters."

def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        current = []

        for i in range(len(s)):
            if s[i] in current:
                # Remove characters up to and including the duplicate
                dup_index = current.index(s[i])
                current = current[dup_index + 1:]
            current.append(s[i])
            maxLen = max(maxLen, len(current))
        return maxLen

string = "abcabcbb"
print(lengthOfLongestSubstring(string))  # Output: 3
