# link of the question: https://leetcode.com/problems/make-array-elements-equal-to-zero/description/

# solution 1
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        index_of_zero = []
        if nums.count(0) == 0:
            return 0
        else:
            for index, item in enumerate(nums):
                if item == 0:
                    index_of_zero.append(index)
        
        valid_selection = 0
        for index in index_of_zero:
            direction = -1 # -1: left, 1: right
            tmp_nums = nums[:]
            tmp_index = index
            while True:
                if not (0 <= tmp_index <= len(nums) - 1):
                    break
                if tmp_nums[tmp_index] == 0:
                    tmp_index += direction
                else:
                    tmp_nums[tmp_index] -= 1
                    direction *= -1
                    tmp_index += direction

            if tmp_nums.count(0) == len(tmp_nums):
                valid_selection += 1

            direction = 1 # -1: left, 1: right
            tmp_nums = nums[:]
            tmp_index = index
            while True:
                if not (0 <= tmp_index <= len(nums) - 1):
                    break
                if tmp_nums[tmp_index] == 0:
                    tmp_index += direction
                else:
                    tmp_nums[tmp_index] -= 1
                    direction *= -1
                    tmp_index += direction

            if tmp_nums.count(0) == len(tmp_nums):
                valid_selection += 1

        return valid_selection

# solution 2
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        index_of_zero = [index for index, item in enumerate(nums) if item == 0]
        valid_selection = 0
        direction_list = [-1, 1]
        for index in index_of_zero:
            for direction in direction_list:
                tmp_direction = direction # -1: left, 1: right
                tmp_nums = nums[:]
                tmp_index = index
                while True:
                    if not (0 <= tmp_index <= len(nums) - 1):
                        break
                    if tmp_nums[tmp_index] == 0:
                        tmp_index += tmp_direction
                    else:
                        tmp_nums[tmp_index] -= 1
                        tmp_direction *= -1
                        tmp_index += tmp_direction

                if all(item == 0 for item in tmp_nums):
                    valid_selection += 1

        return valid_selection
    
# link of the question: https://leetcode.com/problems/make-array-elements-equal-to-zero/description/

# solution 3
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        valid_selection = 0
        for i in range(len(nums)):
            left_sum = sum(nums[0:i])
            right_sum = sum(nums[i+1:])
            if nums[i] == 0:
                if left_sum == right_sum:
                    valid_selection += 2
                elif abs(left_sum - right_sum) == 1:
                    valid_selection += 1
        return valid_selection
    
# solution 4
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        valid_selection = 0
        left_sum = 0
        right_sum = sum(nums)
        for i in range(len(nums)):
            left_sum += nums[i]
            right_sum -= nums[i]
            if nums[i] == 0:
                if left_sum == right_sum:
                    valid_selection += 2
                elif abs(left_sum - right_sum) == 1:
                    valid_selection += 1
        return valid_selection