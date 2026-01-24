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