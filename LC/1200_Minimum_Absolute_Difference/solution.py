# solution 1
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_abs_diff = inf
        min_abs_diff_list = []

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                tmp = abs(arr[i] - arr[j])
                if tmp < min_abs_diff:
                    min_abs_diff = tmp
                    min_abs_diff_list = []
                    if arr[i] < arr[j]:
                        min_abs_diff_list.append([arr[i], arr[j]])
                    else:
                        min_abs_diff_list.append([arr[j], arr[i]])
                elif tmp == min_abs_diff:
                    if arr[i] < arr[j]:
                        min_abs_diff_list.append([arr[i], arr[j]])
                    else:
                        min_abs_diff_list.append([arr[j], arr[i]])

        min_abs_diff_list.sort()
        return min_abs_diff_list

# solution 2
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