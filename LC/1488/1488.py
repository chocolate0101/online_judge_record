# link of the question: https://leetcode.com/problems/avoid-flood-in-the-city/?envType=daily-question&envId=2025-10-07

# better approach (still TLE)
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        look_ahead = rains
        ans = []
        is_choose = 0

        current_situation = {}
        for i in range(len(rains)):
            if len(current_situation) == 0:
                if rains[i] != 0:
                    current_situation[rains[i]] = 1
                    ans.append(-1)
                else:
                    ans.append(1)
            else:
                if rains[i] != 0:
                    current_day = rains[i]
                    tmp = current_situation.get(current_day, -1)
                    if tmp != -1:
                        # current_day is in dict
                        if tmp == 0:
                            current_situation[current_day] = 1
                            ans.append(-1)
                        else:
                            ans = []
                            return ans
                    else:
                        current_situation[rains[i]] = 1
                        ans.append(-1)
                else:
                    if len(look_ahead) != 0:
                        for j in range(i+1, len(look_ahead)):
                            next_rain = look_ahead[j]
                            tmp = current_situation.get(next_rain, -1)
                            if tmp != -1 and current_situation[next_rain] == 1:
                                # next_rain is in dict
                                is_choose = 1
                                current_situation[next_rain] = 0
                                ans.append(next_rain)
                                break
                        if is_choose:
                            is_choose = 0
                        else:
                            ans.append(1)
                    else:
                        ans.append(1)

        return ans
    
# brute force
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        except_no_rain = []
        ans = []
        is_find = 0
        is_choose = 0
        for i in rains:
            if i != 0:
                except_no_rain.append(i)

        current_situation = []
        for i in range(len(rains)):
            if len(current_situation) == 0:
                if rains[i] != 0:
                    current_situation.append([rains[i], 1])
                    ans.append(-1)
                    del except_no_rain[0]
                else:
                    ans.append(1)
            else:
                if rains[i] != 0:
                    for j in range(len(current_situation)):
                        if current_situation[j][0] == rains[i]:
                            if current_situation[j][1] == 0:
                                is_find = 1
                                current_situation[j][1] = 1
                                ans.append(-1)
                            else:
                                ans = []
                                return ans
                    if not is_find:
                        current_situation.append([rains[i], 1])
                        ans.append(-1)
                    else:
                        is_find = 0
                    del except_no_rain[0]
                else:
                    if len(except_no_rain) != 0:
                        for j in range(len(except_no_rain)):
                            next_rain = except_no_rain[j]
                            for k in range(len(current_situation)):
                                if current_situation[k][0] == next_rain and current_situation[k][1] == 1:
                                    is_choose = 1
                                    current_situation[k][1] = 0
                                    ans.append(next_rain)
                                    break
                            if is_choose:
                                break
                        if is_choose:
                            is_choose = 0
                        else:
                            ans.append(1)
                    else:
                        ans.append(1)

        return ans