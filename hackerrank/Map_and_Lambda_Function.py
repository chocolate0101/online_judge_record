# link of the question: https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true

cube = lambda x: pow(x, 3)

def fibonacci(n):
    fibonacci_list = []
    for i in range(n):
        if i == 0:
            fibonacci_list.append(0)
        elif i == 1:
            fibonacci_list.append(1)
        else:
            fibonacci_list.append(fibonacci_list[i-2] + fibonacci_list[i-1])
    return fibonacci_list

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))