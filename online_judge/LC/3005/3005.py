# link of the question：https://leetcode.com/problems/count-elements-with-maximum-frequency/description/

# my answer
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums.sort()
        unique_nums = ()
        frequency = 1
        frequency_list = []
        if len(nums_set) == len(nums):
            return len(nums_set)
        else:
            for i in range(len(nums)-1):
                if nums[i] == nums[i+1]:
                    frequency += 1
                else:
                    frequency_list.append(frequency)
                    frequency = 1
            frequency_list.append(frequency)
            max_frequency = max(frequency_list)
            total_frequency = 0
            for frequency in frequency_list:
                if max_frequency == frequency:
                    total_frequency += max_frequency
            
            return total_frequency

# better answer
from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequency_list = Counter(nums)
        max_frequency = max(frequency_list.values())
        
        total_frequency = 0
        for frequency in frequency_list:
            if frequency == max_frequency:
                total_frequency += max_frequency
        return total_frequency






