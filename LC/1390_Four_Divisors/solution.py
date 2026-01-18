# solution 1
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        sum_divisor = 0
        for num in nums:
            num_divisor = 0
            current_sum_divisor = 0
            for i in range(1, int(num ** 0.5)+1):
                if num == i * i:
                    current_sum_divisor += i
                    num_divisor += 1
                elif num % i == 0:
                    current_sum_divisor += i
                    current_sum_divisor += num // i
                    num_divisor += 2

                if num_divisor > 4:
                    break
                
            if num_divisor == 4:
                sum_divisor += current_sum_divisor

        return sum_divisor

# solution 2
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        large_num = max(nums)
        ans = 0
        count_divisor_list = [0 for _ in range(large_num+1)]
        sum_divisor_list = [0 for _ in range(large_num+1)]

        for i in range(1, large_num+1):
            for j in range(i, large_num+1, i):
                count_divisor_list[j] += 1
                sum_divisor_list[j] += i

        for num in nums:
            if count_divisor_list[num] == 4:
                ans += sum_divisor_list[num]

        return ans

# solution 3 (best solution)
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        
        for num in nums:
            if num < 6:
                continue

            limit = int(num ** 0.5)
            for i in range(2, limit + 1):
                if num % i == 0:
                    div1 = i
                    div2 = num // i
                    
                    if div1 == div2:
                        break

                    if div1 * div1 == div2:
                        ans += 1 + num + div1 + div2
                    else:
                        is_div2_prime = True
                        for k in range(2, int(div2 ** 0.5) + 1):
                            if div2 % k == 0:
                                is_div2_prime = False
                                break
                        
                        if is_div2_prime:
                            ans += 1 + num + div1 + div2
                    
                    break
                    
        return ans