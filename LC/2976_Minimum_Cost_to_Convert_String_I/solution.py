class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        cost_graph = [[inf for _ in range(26)] for _ in range(26)]

        for ori, chg, c in zip(original, changed, cost):
            u = ord(ori) - ord('a')
            v = ord(chg) - ord('a')
            cost_graph[u][v] = min(cost_graph[u][v], c)

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    cost_graph[i][j] = min(cost_graph[i][j], cost_graph[i][k] + cost_graph[k][j])

        total_cost = 0
        for i in range(len(source)):
            if source[i] == target[i]:
                continue

            r = ord(source[i]) - ord('a')
            c = ord(target[i]) - ord('a')
            
            if cost_graph[r][c] == inf:
                return -1
            
            total_cost += cost_graph[r][c]

        return total_cost