# solution 1 (1D Dynamic Programming)
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = []
        penalty.append(customers.count('Y'))
        min_penalty = penalty[0]
        min_index = 0
        n = len(customers)
        for i in range(1, n):
            if customers[i-1] == 'Y':
                penalty.append(penalty[i-1] - 1)
            else:
                penalty.append(penalty[i-1] + 1)

            if penalty[i] < min_penalty:
                min_penalty = penalty[i]
                min_index = i

        no_close = penalty[n-1] + (1 if customers[n-1] == 'N' else -1)
        return n if no_close < min_penalty else min_index
    
# solution 2 (Prefix Sum)
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        current_score = 0
        best_score = 0
        best_hour = 0
        for i, customer in enumerate(customers):
            if customer == "Y":
                current_score += 1
            else:
                current_score -= 1

            if current_score > best_score:
                best_hour = i+1
                best_score = current_score

        return best_hour