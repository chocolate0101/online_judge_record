# link of the question: https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true

# better approach
set_a = set(map(int, input().split()))
num_set = int(input())
is_superset = 1

for i in range(num_set):
    tmp_set = set(map(int, input().split()))
    if not tmp_set < set_a:
        print("False")
        is_superset = 0
        break
        
if is_superset:
    print("True")

# myself
set_a = set(map(int, input().split()))
num_set = int(input())
is_superset = 1

for i in range(num_set):
    tmp_set = set(map(int, input().split()))
    if tmp_set <= set_a:
        unique_element = set_a.difference(tmp_set)
        if len(unique_element) == 0:
            is_superset = 0
            print("False")
            break
    else:
        print("False")
        is_superset = 0
        break
        
if is_superset:
    print("True")