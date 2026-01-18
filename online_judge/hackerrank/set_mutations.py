# link of the question: https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true

set_size = int(input())
set_a = set(map(int, input().split()))

num_set = int(input())
for i in range(num_set):
    command = input().split()
    tmp_set = set(map(int, input().split()))
    
    if command[0] == 'intersection_update':
        set_a &= tmp_set
    elif command[0] == 'update':
        set_a |= tmp_set
    elif command[0] == 'symmetric_difference_update':
        set_a ^= tmp_set
    elif command[0] == 'difference_update':
        set_a -= tmp_set
    
print(sum(set_a))