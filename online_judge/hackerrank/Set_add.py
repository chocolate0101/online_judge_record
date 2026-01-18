# link of the question: https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true

num_stamp = int(input())
country_set = set()
for i in range(num_stamp):
    country_set.add(input())
    
print(len(country_set))