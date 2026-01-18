# link of the question: https://cpe.mcu.edu.tw/cpe/problems/CPE250930/CPE250930-P3.uva673.pdf

num_test_case = int(input())
for _ in range(num_test_case):
	input_str = input()
	parentheses = []
	is_valid = 1
	for ch in input_str:
		if ch == "(" or ch == "[":
			parentheses.append(ch)
		else:
			if len(parentheses) == 0:
				is_valid = 0
				break
			if ch == ")":
				if parentheses.pop() != "(":
					is_valid = 0
					break
			elif ch == "]":
				if parentheses.pop() != "[":
					is_valid = 0
					break
					
	if len(parentheses) == 0 and is_valid == 1:
		print("Yes")
	else:
		print("No")
				