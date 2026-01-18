# link of question：https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list_arr = list(set(arr))
    list_arr.sort()
    print(list_arr[-2])