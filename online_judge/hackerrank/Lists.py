# link of the question：https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    ans_list = []
    for i in range(N):
        instruction = input().split()
        if instruction[0] == 'insert':
            index = int(instruction[1])
            element = int(instruction[2])
            ans_list.insert(index, element)
        elif instruction[0] == 'print':
            print(ans_list)
        elif instruction[0] == 'remove':
            element = int(instruction[1])
            ans_list.remove(element)
        elif instruction[0] == 'append':
            element = int(instruction[1])
            ans_list.append(element)
        elif instruction[0] == 'sort':
            ans_list.sort()
        elif instruction[0] == 'pop':
            del ans_list[-1]
        elif instruction[0] == 'reverse':
            ans_list.reverse()