# link of the question: https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true

size_m = int(input())
m_set = set(map(int, input().split()))

size_n = int(input())
n_set = set(map(int, input().split()))

m_diff_n = m_set.difference(n_set)
n_diff_m = n_set.difference(m_set)
diff_list = list(m_diff_n.union(n_diff_m))
diff_list.sort()

for i in diff_list:
    print(i)
