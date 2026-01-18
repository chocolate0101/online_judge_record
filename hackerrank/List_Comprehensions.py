# link of question：https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ans = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if not (i + j + k == n):
                    ans.append([i,j,k])
                    
    print(ans)