while True:
	try:
		num_int = int(input())
	except EOFError:
		break
	nums = list(map(int, input().split()))
	count = 0
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			count += (nums[i] > nums[j])
			
	print(f"Minimum exchange operations : {count}")