# link of the question: https://leetcode.com/problems/increment-submatrices-by-one/description/

# solution 1
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [ [0 for i in range(n)] for i in range(n) ]
        for i in range(len(queries)):
            for j in range(queries[i][0], queries[i][2]+1):
                for k in range(queries[i][1], queries[i][3]+1):
                    matrix[j][k] += 1

        return matrix
    
# solution 2
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [ [0 for i in range(n+1)] for j in range(n+1)]
        for query in queries:
            matrix[query[0]][query[1]] += 1
            matrix[query[2]+1][query[1]] -= 1
            matrix[query[0]][query[3]+1] -= 1
            matrix[query[2]+1][query[3]+1] += 1
        
        for i in range(len(matrix)):
            cur = 0
            for j in range(len(matrix[0])):
                cur += matrix[i][j]
                matrix[i][j] = cur

        for i in range(len(matrix)):
            cur = 0
            for j in range(len(matrix[0])):
                cur += matrix[j][i]
                matrix[j][i] = cur

        return [row[:n] for row in matrix[:n]]