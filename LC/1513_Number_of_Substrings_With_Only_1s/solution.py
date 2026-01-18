# link of the question: https://leetcode.com/problems/number-of-substrings-with-only-1s/description/

def numSub(s: str) -> int:
        count_one, ans = 0, 0
        for ch in s:
            if ch == "1":
                count_one += 1
            else:
                ans = ans + (count_one + 1) * count_one // 2
                count_one = 0
        
        ans = ans + (count_one + 1) * count_one // 2
        return ans