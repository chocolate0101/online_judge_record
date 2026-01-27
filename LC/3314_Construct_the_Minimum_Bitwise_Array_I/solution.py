# solution 1
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        is_find = 0
        for num in nums:
            is_find = 0
            for x in range(num):
                if (x | (x+1)) == num:
                    is_find = 1
                    ans.append(x)
                    break

            if not is_find:
                ans.append(-1)
        
        return ans

# solution 2 (best solution)
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num % 2 == 0:
                ans.append(-1)
            else:
                diff = ( (num+1) & -(num+1) ) >> 1
                ans.append(num - diff)
        return ans