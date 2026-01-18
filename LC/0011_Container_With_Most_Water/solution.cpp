// link of the question: https://leetcode.com/problems/container-with-most-water/?envType=daily-question&envId=2025-10-04

"""
思考邏輯：
一開始先假設最大面積是最外圍的兩個高度所形成的面積
接著移動較矮的，去尋找更高的高度，因為面積是由較矮的高度所決定的

time complexity: O(n^2) -> O(n)
space complexity: O(1)
"""

class Solution {
public:
    int maxArea(vector<int>& height) {
        int max_area = 0;
        int left = 0;
        int right = height.size()-1;

        for (int i = 0; i < height.size()-1; i++) {
            int current_area = min(height[left], height[right]) * (right - left);
            if (current_area > max_area) {
                max_area = current_area;
            }

            if (height[left] > height[right]) {
                right--;
            } else {
                left++;
            }
        }
        return max_area;
    }
};