# link of the question：https://leetcode.com/problems/two-sum/

# slow solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return 

# fast solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for idx, num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num], idx]
            dic[num] = idx

# python 的 dict，因為是透過 hash table 的方式實作的，所以查詢複雜度為 O(1)
# 而當發生 hash collision 時，dict 是透過 open addressing 中的 probing 來解決
# 使用 bitwise masking