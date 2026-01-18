while True:
	input_num = list(map(int, input().split()))
	if input_num == [0, 0]:
		break
	
	count = 0
	for i in range(input_num[1]):
		if input_num[0] <= i * i <= input_num[1]:
			count += 1
	
	print(count)