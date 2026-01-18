# link of the question: https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true

# using python api
num_case = int(input())

for i in range(num_case):
    size_set_a = int(input())
    set_a = set(map(int, input().split()))
    
    size_set_b = int(input())
    set_b = set(map(int, input().split()))
    
    same_element_set = set_b.intersection(set_a)

    if set_a <= set_b: # or set_a.issubset(set_b)
        print("True")
    else:
        print("False")

# evaluate by myself
num_case = int(input())

for i in range(num_case):
    size_set_a = int(input())
    set_a = set(map(int, input().split()))
    
    size_set_b = int(input())
    set_b = set(map(int, input().split()))
    
    same_element_set = set_b.intersection(set_a)
    
    if same_element_set == set_a:
        print("True")
    else:
        print("False")