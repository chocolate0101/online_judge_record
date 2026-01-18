# link of the question:https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true

n = int(input())
s = set(map(int, input().split()))
num_command = int(input())

for i in range(num_command):
    cur_command = input().split()
    if cur_command[0] == 'pop':
        s.pop()
    elif cur_command[0] == 'remove':
        s.remove(int(cur_command[1]))
    elif cur_command[0] == 'discard':
        s.discard(int(cur_command[1]))

print(sum(s))