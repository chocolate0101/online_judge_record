# link of the problem: https://cpe.mcu.edu.tw/cpe/problems/CPE250930/CPE250930-P2.uva483.pdf
while True:
	try:
		input_str = list(input().split())
	except:
		break
	
	print(" ".join(s[::-1] for s in input_str))
	