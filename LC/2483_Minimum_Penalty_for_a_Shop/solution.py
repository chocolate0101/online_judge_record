# solution 1 (1D Dynamic Programming)
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        best_score = [0]
        for customer in customers:
            if customer == "Y":
                best_score.append(best_score[-1] + 1)
            else:
                best_score.append(best_score[-1] - 1)

        return best_score.index(max(best_score))
    
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