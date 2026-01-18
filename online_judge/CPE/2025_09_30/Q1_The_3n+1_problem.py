# link of the problem: https://cpe.mcu.edu.tw/cpe/problems/CPE250930/CPE250930-P1.uva100.pdf

while True:
	try:
		num1, num2 = map(int, input().split())
	except:
		break
	
	max_cycle = 0
	for num in range(min(num1, num2), max(num1, num2)+1):
		tmp = num
		cycle = 1
		while tmp != 1:
			if tmp % 2 == 0:
				tmp //= 2
			else:
				tmp = tmp * 3 + 1
			
			cycle += 1
			
		if cycle > max_cycle:
			max_cycle = cycle
			max_cycle_num = num
			
	print(f"{num1} {num2} {max_cycle}")