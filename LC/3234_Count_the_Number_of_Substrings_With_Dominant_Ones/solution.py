# link of the question:

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            is_dominant = 0
            count_zero, count_one = 0, 0
            for j in range(i, len(s)):
                if s[j] == "0":
                    count_zero += 1
                    if is_dominant:
                        if count_one >= count_zero ** 2:
                            ans += 1
                        else:
                            is_dominant = 0
                else:
                    count_one += 1
                    if is_dominant:
                        ans += 1
                    else:
                        if count_one >= count_zero ** 2:
                            ans += 1
                            is_dominant = 1

        return ans
    
# solution 2
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            is_dominant = 0
            count_zero, count_one = 0, 0
            for j in range(i, len(s)):
                if s[j] == "0":
                    count_zero += 1
                    if count_zero >= sqrt(len(s)):
                        break
                    if is_dominant:
                        if count_one >= count_zero ** 2:
                            ans += 1
                        else:
                            is_dominant = 0
                else:
                    count_one += 1
                    if count_one >= len(s) - (count_zero ** 2):
                        ans += len(s) - count_zero
                        break
                    if is_dominant:
                        ans += 1
                    else:
                        if count_one >= count_zero ** 2:
                            ans += 1
                            is_dominant = 1

        return ans