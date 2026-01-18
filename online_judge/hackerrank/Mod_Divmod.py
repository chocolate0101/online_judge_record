# link of the question: https://www.hackerrank.com/challenges/python-mod-divmod/problem?isFullScreen=true

dividend = int(input())
divisor = int(input())

quotient_remainder = divmod(dividend, divisor)

print(quotient_remainder[0])
print(quotient_remainder[1])
print(quotient_remainder)