# link of the question: https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = {}
        last = {}
        ans = 0
        for i in range(len(s)):
            if s[i] in first:
                last[s[i]] = i
            else:
                first[s[i]] = i
        
        for key in first:
            if key in last:
                ans += len(set(s[first[key]+1:last[key]]))

        return ans