from math import inf
num_case = int(input())
for _ in range(num_case):
	pool_max_capacity, target_temperature = map(int, input().split())
	num_jars = int(input())
	jar_info = []
	for i in range(num_jars):
		jar_info.append(list(map(int, input().split())))
	
	min_diff = inf
	target_index = []
	for i in range(num_jars):
		total_volume = 0
		total_temperature = 0
		for j in range(i, num_jars):
			total_volume += jar_info[j][0]
			total_temperature += jar_info[j][0] * jar_info[j][1]
			if total_volume > pool_max_capacity:
				break
			elif total_volume >= pool_max_capacity / 2:
				avg_temperature = total_temperature / total_volume
				diff_temperature = abs(avg_temperature - target_temperature)
				if diff_temperature <= 5 and diff_temperature < min_diff:
					min_diff = diff_temperature
					target_index = [i, j]
				
	if target_index == []:
		print("Not possible")
	else:
		print(f"{target_index[0]} {target_index[1]}")