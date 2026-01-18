# link of the question: https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/description/

# solution 1
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        answer = []
        for i in range(len(nums)-k+1):
            sub_array_count = Counter(nums[i:i+k])
            keep_array = [ [0, 0] for j in range(x) ]   # [ [value, key], [value, key], ... ]
            for key, value in sub_array_count.items():
                for j in range(x):
                    if value > keep_array[j][0]:
                        keep_array.append([value, key])
                        min_element = min(keep_array)
                        min_index = keep_array.index(min_element)
                        del keep_array[min_index]
                        break
                    elif value == keep_array[j][0] and [value, key] > min(keep_array):
                        keep_array.append([value, key])
                        min_element = min(keep_array)
                        min_index = keep_array.index(min_element)
                        del keep_array[min_index]
                        break
            sum = 0
            for j in range(x):
                sum += keep_array[j][0] * keep_array[j][1]
            answer.append(sum)
        
        return answer



# solution 2
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        answer = []
        sub_array_count = Counter(nums[:k-1])
        for i in range(len(nums)-k+1):
            sub_array_count[nums[i+k-1]] += 1
            keep_array = []
            for key, value in sub_array_count.items():
                keep_array.append([value, key])
            sort_keep_array = sorted(keep_array, reverse=True)
            sum = 0
            for j in range(min(len(sort_keep_array), x)):
                sum += sort_keep_array[j][0] * sort_keep_array[j][1]
            answer.append(sum)
            sub_array_count[nums[i]] -= 1
            
        return answer
