# link of the question: https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/description/

class Solution:
    def maxOperations(self, s: str) -> int:
        max_operation = 0
        count_one = 0
        for i in range(len(s)):
            if s[i] == "1":
                count_one += 1
            else:
                if i+1 == len(s) or s[i+1] != "0":
                    max_operation += count_one
        
        return max_operation