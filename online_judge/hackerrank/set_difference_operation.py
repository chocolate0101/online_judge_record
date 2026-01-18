# link of the question: https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true

num_subscribe_english = int(input())
subscribe_english_set = set(map(int, input().split()))

num_subscribe_french = int(input())
subscribe_french_set = set(map(int, input().split()))

print(len(subscribe_english_set - subscribe_french_set))