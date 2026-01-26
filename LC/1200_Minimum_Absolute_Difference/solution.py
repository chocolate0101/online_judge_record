class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_abs_diff = inf
        min_abs_diff_list = []
        arr.sort()

        for i in range(len(arr)-1):
            tmp = arr[i+1] - arr[i]
            if tmp < min_abs_diff:
                min_abs_diff = tmp
                min_abs_diff_list = []
                min_abs_diff_list.append([arr[i], arr[i+1]])
            elif tmp == min_abs_diff:
                min_abs_diff_list.append([arr[i], arr[i+1]])

        return min_abs_diff_list