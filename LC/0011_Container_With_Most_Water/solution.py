# link of the question: https://leetcode.com/problems/container-with-most-water/?envType=daily-question&envId=2025-10-04

"""
思考邏輯：
一開始先假設最大面積是最外圍的兩個高度所形成的面積
接著移動較矮的，去尋找更高的高度，因為面積是由較矮的高度所決定的

time complexity: O(n^2) -> O(n)
space complexity: O(1)
"""

# brute force
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                current_area = min(height[i], height[j]) * (j-i)
                if current_area > max_area:
                    max_area = current_area

        return max_area
    
# two pointer approach
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0
        for i in range(len(height)-1):
            current_area = min(height[left], height[right]) * (right-left)
            if current_area > max_area:
                max_area = current_area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area